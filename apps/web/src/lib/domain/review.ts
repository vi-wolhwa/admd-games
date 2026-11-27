/**
 * 리뷰(읽기) — 설계: docs/design/research/04-reviews.md, ADR 0009 · 0011.
 * 찬반 판정 없음(쓴 사람이 추천했으면 '추천함'), 도움이 됐어요 = 긍정 하나, 플레이 시간을 그대로 보여 준다.
 */
import { type Cursor, decodeCursorOf } from './cursor';

/** 정렬 — '도움이 됐어요'는 없앴다(사용자 결정 2026-11-28) */
export type ReviewSort = 'recent' | 'played';
export const REVIEW_SORTS: readonly ReviewSort[] = ['recent', 'played'];
export const REVIEW_SORT_LABEL: Record<ReviewSort, string> = {
	recent: '최신',
	played: '오래 한 사람'
};

/**
 * 리뷰 키워드 — 쓸 때 이 목록에서 1개 이상 고른다(네이버 방식, 사용자 결정 2026-11-28).
 * 좋은 점만 — 아쉬운 점은 리뷰 글로(싫어요 없음 원칙, ADR 0009).
 */
export const REVIEW_KEYWORDS = [
	'짧고 굵음',
	'오래 붙잡게 돼요',
	'같이 하면 더 좋아요',
	'이야기가 좋아요',
	'음악이 좋아요',
	'그림이 예뻐요',
	'조작이 편해요',
	'힌트가 친절해요',
	'한 손으로'
] as const;
/** 리뷰 · 답글 글자 수 한도(사용자 결정 2026-11-28) */
export const REVIEW_BODY_MAX = 500;
export const REPLY_BODY_MAX = 500;
export const REVIEW_PAGE_SIZE = 10;

/** 글쓴이(리뷰 · 답글). makerSlug = 메이커스 프로필 주소 — 없으면 눌러도 이동하지 않음 */
export interface Person {
	name: string;
	/** 자모 얼굴 글자 · 색 이름(tokens.css --color-face-*) */
	faceChar: string;
	faceColor: string;
	makerSlug: string | null;
}

export interface ReviewAuthor extends Person {
	reviewCount: number;
}

/**
 * 답글 — 누구나 단다(로그인 뒤), 한 단계만(답글에 답할 때는 @닉네임). 리뷰에서는 멘션 불가(사용자 결정 2026-11-28).
 * mentions = 이 글에 나온 아는 닉네임 → 메이커스 프로필 주소(없으면 null: 파란 글씨지만 이동 없음)
 */
export interface ReplyData {
	id: string;
	author: Person;
	/** 이 게임의 메이커가 단 답글 */
	byGameMaker: boolean;
	body: string;
	createdAt: number;
	updatedAt: number | null;
	mentions: Record<string, string | null>;
}

export interface ReviewData {
	id: string;
	author: ReviewAuthor;
	/** 글쓴이가 이 게임을 추천했나 */
	recommended: boolean;
	/** 쓸 때까지 플레이한 시간(분) — 기록이 없으면 null('플레이 기록 없음') */
	playMinutes: number | null;
	/** 쓸 때 버전 */
	version: string | null;
	createdAt: number;
	/** 고쳐 쓴 시각 — 있으면 '수정'으로 표시 */
	updatedAt: number | null;
	/** 글쓴이가 고른 키워드 */
	phrases: string[];
	body: string;
	/** 오래된 순 */
	replies: ReplyData[];
}

export interface ReviewQuery {
	sort: ReviewSort;
	/** 고른 말로 거르기 */
	phrase: string | null;
}

export const DEFAULT_REVIEW_QUERY: ReviewQuery = { sort: 'recent', phrase: null };

export function parseReviewQuery(params: URLSearchParams): ReviewQuery {
	const sort = REVIEW_SORTS.find((s) => s === params.get('rsort')) ?? DEFAULT_REVIEW_QUERY.sort;
	const phrase = params.get('rphrase')?.trim().slice(0, 20) ?? '';
	return { sort, phrase: phrase || null };
}

export function reviewSearchParams(q: ReviewQuery, into = new URLSearchParams()): URLSearchParams {
	into.delete('rsort');
	into.delete('rphrase');
	if (q.sort !== DEFAULT_REVIEW_QUERY.sort) into.set('rsort', q.sort);
	if (q.phrase) into.set('rphrase', q.phrase);
	return into;
}

/** 커서 값: recent [쓴 시각] · played [플레이 분(없으면 -1), 쓴 시각] */
const ARITY: Record<ReviewSort, number> = { recent: 1, played: 2 };

export function decodeReviewCursor(raw: string, sort: ReviewSort): Cursor<ReviewSort> | null {
	return decodeCursorOf(raw, sort, ARITY[sort]);
}
