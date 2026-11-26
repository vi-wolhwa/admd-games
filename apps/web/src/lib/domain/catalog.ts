/**
 * 전체 게임(PG03) 목록 질의 — 필터 · 정렬 · 이어 불러오기 커서.
 * 상태는 모두 주소에 남긴다(새로 고침 · 공유 · 뒤로 가기에 그대로 — ADR 0010).
 */
import type { Launch, LengthBucket } from './game';

export type CatalogSort = 'played' | 'recommended' | 'reviews' | 'new';
export type Players = 'solo' | 'group';

export interface CatalogQuery {
	/** 검색어 — 제목 · 메이커 이름에 들어 있으면 해당(빈 문자열 = 검색 안 함) */
	q: string;
	/** 태그 slug — 여러 개면 '하나라도 해당' */
	tags: string[];
	/** 이 구간 이하(5 = 1시간 넘게만) */
	length: LengthBucket | null;
	launch: Launch | null;
	players: Players | null;
	sort: CatalogSort;
}

export const DEFAULT_QUERY: CatalogQuery = {
	q: '',
	tags: [],
	length: null,
	launch: null,
	players: null,
	sort: 'played'
};

/**
 * 정렬(사용자 결정 2026-11-28). '많이 플레이한'은 게임별 플레이 수 캐시(games.play_count) —
 * PG06 플레이 기록이 생기기 전에는 모두 0이라 추천 수로 순서가 정해진다.
 */
export const SORT_LABEL: Record<CatalogSort, string> = {
	played: '많이 플레이한',
	recommended: '추천 많은',
	reviews: '리뷰 많은',
	new: '새로 나온'
};

export const PLAYERS_LABEL: Record<Players, string> = { solo: '혼자', group: '같이' };

export const PAGE_SIZE = 12;
export const MAX_LOADED = 96;
const MAX_TAGS = 10;
export const MAX_SEARCH = 40;

/** 주소에 쓰는 한 판 길이 값 */
const LENGTH_PARAM: Record<LengthBucket, string> = {
	1: '5m',
	2: '15m',
	3: '30m',
	4: '1h',
	5: 'long'
};
const LENGTH_FROM_PARAM = new Map(
	Object.entries(LENGTH_PARAM).map(([k, v]) => [v, Number(k) as LengthBucket])
);
const LAUNCHES: readonly Launch[] = ['web', 'download'];
const PLAYERS: readonly Players[] = ['solo', 'group'];
export const SORTS: readonly CatalogSort[] = ['played', 'recommended', 'reviews', 'new'];

function oneOf<T extends string>(list: readonly T[], value: string | null): T | null {
	return list.find((v) => v === value) ?? null;
}

export function parseCatalogQuery(params: URLSearchParams): CatalogQuery {
	const tags = [...new Set(params.getAll('tag').map((t) => t.trim()))]
		.filter(Boolean)
		.slice(0, MAX_TAGS);
	return {
		q: (params.get('q') ?? '').trim().slice(0, MAX_SEARCH),
		tags,
		length: LENGTH_FROM_PARAM.get(params.get('len') ?? '') ?? null,
		launch: oneOf(LAUNCHES, params.get('run')),
		players: oneOf(PLAYERS, params.get('ppl')),
		sort: oneOf(SORTS, params.get('sort')) ?? DEFAULT_QUERY.sort
	};
}

/** 질의를 주소로. 기본값은 남기지 않는다. `loaded` 는 지금까지 불러온 개수 */
export function catalogSearchParams(query: CatalogQuery, loaded = PAGE_SIZE): URLSearchParams {
	const p = new URLSearchParams();
	if (query.q) p.set('q', query.q);
	for (const t of query.tags) p.append('tag', t);
	if (query.length) p.set('len', LENGTH_PARAM[query.length]);
	if (query.launch) p.set('run', query.launch);
	if (query.players) p.set('ppl', query.players);
	if (query.sort !== DEFAULT_QUERY.sort) p.set('sort', query.sort);
	if (loaded > PAGE_SIZE) p.set('n', String(loaded));
	return p;
}

/**
 * 검색 비교용 검색어(사용자 결정 2026-11-28):
 * - 공백을 모두 무시 — 'A BC' 로 'ABC' · 'A B C' 를 찾는다(저장소 쪽도 공백을 빼고 비교)
 * - 끝에 조합되지 않은 한글 자모(ㄱ · ㅏ …)는 빼고 찾는다 — 입력 중인 글자 때문에 결과가 비지 않게
 * 남는 것이 없으면 빈 문자열(= 검색 안 함)
 */
export function searchKey(q: string): string {
	// U+3131–U+318E = 한글 호환 자모(ㄱ … ㅣ)
	return q.replace(/\s+/g, '').replace(/[ㄱ-ㆎ]+$/, '');
}

/** 주소의 불러온 개수 — 12개 단위로 올림, 12~96 */
export function parseLoaded(params: URLSearchParams): number {
	const n = Number(params.get('n'));
	if (!Number.isFinite(n) || n <= PAGE_SIZE) return PAGE_SIZE;
	return Math.min(MAX_LOADED, Math.ceil(n / PAGE_SIZE) * PAGE_SIZE);
}

/**
 * 커서 = 마지막 항목의 정렬 값 + id (OFFSET 을 쓰지 않는다 — D1 읽기 절약, ADR 0010).
 *   played: [플레이 수, 추천 수]   recommended: [추천 수]   reviews: [리뷰 수]   new: [공개 시각]
 */
export interface Cursor {
	sort: CatalogSort;
	values: readonly number[];
	id: string;
}

const CURSOR_ARITY: Record<CatalogSort, number> = { played: 2, recommended: 1, reviews: 1, new: 1 };

export function encodeCursor(cursor: Cursor): string {
	const json = JSON.stringify([cursor.sort, cursor.values, cursor.id]);
	return btoa(json).replaceAll('+', '-').replaceAll('/', '_').replace(/=+$/, '');
}

export function decodeCursor(raw: string, sort: CatalogSort): Cursor | null {
	try {
		const parsed: unknown = JSON.parse(atob(raw.replaceAll('-', '+').replaceAll('_', '/')));
		if (!Array.isArray(parsed) || parsed.length !== 3) return null;
		const [s, values, id] = parsed as unknown[];
		if (s !== sort || typeof id !== 'string' || !Array.isArray(values)) return null;
		if (values.length !== CURSOR_ARITY[sort]) return null;
		if (!values.every((v): v is number => typeof v === 'number' && Number.isFinite(v))) return null;
		return { sort, values, id };
	} catch {
		return null;
	}
}
