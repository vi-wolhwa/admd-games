/**
 * 게임 정보 — 화면 · 서버 공용 타입과 규칙. 필드 정의 원본: docs/product/game-metadata.md
 */

/**
 * 한 판에 걸리는 시간 구간(메이커가 고름). 분 단위 정확한 값은 업데이트마다 틀어져서 구간만 둔다.
 * 구간은 겹치지 않는다(사용자 결정 2026-11-28 — 5구간 누적 → 3구간).
 */
export type LengthBucket = 1 | 2 | 3;

export const LENGTH_BUCKETS: readonly LengthBucket[] = [1, 2, 3];

export const LENGTH_LABEL: Record<LengthBucket, string> = {
	1: '10분 안쪽',
	2: '10~30분',
	3: '30분 이상'
};

/** 매일 이어서 — 진행이 저장돼 날마다 들러 이어 하는 게임(메이커가 체크, 한 판 시간과 별개) */
export const DAILY_LABEL = '매일 이어서';

/** 실행 방식 — 올린 빌드 종류로 플랫폼이 안다. 이름은 둘 다 '어디서 하나'(사용자 결정 2026-11-28) */
export type Launch = 'web' | 'download';

export const LAUNCH_LABEL: Record<Launch, string> = {
	web: '브라우저',
	download: '다운로드'
};

/** 실행 방식 풀이(카드 칩 설명) */
export const LAUNCH_HINT: Record<Launch, string> = {
	web: '브라우저에서 바로 실행',
	download: '다운로드해서 설치'
};

export interface GameMedia {
	kind: 'image' | 'video';
	url: string;
}

/** 카드 한 장을 그리는 데 필요한 것만. */
export interface GameCardData {
	id: string;
	slug: string;
	title: string;
	makerName: string;
	/** 태그 이름, 메이커가 적은 순서 */
	tags: string[];
	length: LengthBucket;
	/** 매일 이어서 하는 게임 */
	daily: boolean;
	launch: Launch;
	/** 휴대폰에서도 됨(브라우저 게임만 고를 수 있음) */
	phone: boolean;
	playersMax: number;
	/** 설치형 보안 검사 통과 */
	scanPassed: boolean;
	cover: string;
	/** 호버 미리보기 — 영상을 끝까지 튼 뒤 이미지를 순환 (ADR 0009 #6, 보강 #11) */
	media: GameMedia[];
	recommendCount: number;
	reviewCount: number;
	/** 공개 시각(epoch ms) */
	publishedAt: number;
}

/** 태그 주소 이름 — 메이커가 적은 이름을 다듬은 것(대소문자 · 띄어쓰기만 맞춤, 한글 그대로) */
export function tagSlug(name: string): string {
	return name.trim().toLowerCase().replace(/\s+/g, '-');
}

const DAY = 24 * 60 * 60 * 1000;
/** '신작' 배지 기간 — 공개 후 14일 */
export const NEW_GAME_DAYS = 14;

export function isNewGame(publishedAt: number, now: number): boolean {
	const age = now - publishedAt;
	return age >= 0 && age < NEW_GAME_DAYS * DAY;
}

/**
 * 호버 때 보여 줄 차례: 영상 먼저(끝까지 재생) → 이미지 순환 → 다시 처음.
 * 영상이 사진보다 게임을 잘 보여 주므로 맨 앞(사용자 결정 2026-11-28, ADR 0009 보강 #11)
 */
export function hoverMedia(media: GameMedia[]): GameMedia[] {
	return [...media.filter((m) => m.kind === 'video'), ...media.filter((m) => m.kind === 'image')];
}

/** 기기 — 메이커가 고름(브라우저 게임만 휴대폰 · 패드 가능) */
export type Device = 'pc' | 'phone' | 'pad';
export const DEVICE_LABEL: Record<Device, string> = { pc: 'PC', phone: '휴대폰', pad: '패드' };

/** 게임 안 글자의 언어(코드 → 이름) */
export const LANGUAGE_LABEL: Record<string, string> = {
	ko: '한국어',
	en: '영어',
	ja: '일본어',
	zh: '중국어'
};

/** 상세(PG05)에 필요한 것 — 카드 정보 + 소개 · 플레이 정보. 정의: docs/product/game-metadata.md */
export interface GameDetail extends GameCardData {
	summary: string;
	/** 소개 · 특징 — 빈 줄로 문단, '- ' 로 시작하는 줄은 특징 목록 */
	description: string;
	makerSlug: string;
	/** 이 메이커의 공개 게임 수 */
	makerGameCount: number;
	devices: Device[];
	/**
	 * 온라인 — 인터넷으로 다른 사람과 같이 플레이(사용자 결정 2026-11-28 — 순위만 있는 게임은 해당 없음).
	 * 같은 기기에서 함께하는 인원은 playersMin ~ playersMax.
	 */
	online: boolean;
	languages: string[];
	/** 최소 사양(설치형만) */
	minSpec: string | null;
	/** 지금 버전(예: v1.3) — 리뷰는 버전마다 한 사람 하나 */
	version: string | null;
	playersMin: number;
}

/** 소개 글을 문단과 특징 목록으로 나눈다 */
export function splitDescription(text: string): { paragraphs: string[]; features: string[] } {
	const paragraphs: string[] = [];
	const features: string[] = [];
	for (const block of text.split(/\n\s*\n/)) {
		const lines = block
			.split('\n')
			.map((l) => l.trim())
			.filter(Boolean);
		const prose = lines.filter((l) => !l.startsWith('- '));
		features.push(...lines.filter((l) => l.startsWith('- ')).map((l) => l.slice(2).trim()));
		if (prose.length > 0) paragraphs.push(prose.join(' '));
	}
	return { paragraphs, features };
}

/**
 * 인원 표기 — 같은 기기 인원(혼자서 · 2명 · 2~4명) + 온라인.
 * 필터(혼자서 · 둘이서 · 온라인)와 같은 말을 쓴다.
 */
export function playersLabel(min: number, max: number, online = false): string {
	const local =
		max <= 1 ? '혼자서' : min === max ? `${String(max)}명` : `${String(min)}~${String(max)}명`;
	return online ? `${local} · 온라인` : local;
}

/** 한 판에 칸 표기 — '10분 안쪽', 매일 이어서 하면 뒤에 붙인다 */
export function lengthLabel(game: Pick<GameCardData, 'length' | 'daily'>): string {
	return game.daily ? `${LENGTH_LABEL[game.length]} · ${DAILY_LABEL}` : LENGTH_LABEL[game.length];
}
