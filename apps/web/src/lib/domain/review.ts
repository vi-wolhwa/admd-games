/**
 * 리뷰(읽기) — 설계: docs/design/research/04-reviews.md, ADR 0009 · 0011.
 * 찬반 판정 없음(쓴 사람이 추천했으면 '추천함'), 도움이 됐어요 = 긍정 하나, 플레이 시간을 그대로 보여 준다.
 */
import { type Cursor, decodeCursorOf } from './cursor';

export type ReviewSort = 'helpful' | 'recent' | 'played';
export const REVIEW_SORTS: readonly ReviewSort[] = ['helpful', 'recent', 'played'];
export const REVIEW_SORT_LABEL: Record<ReviewSort, string> = {
	helpful: '도움 많은',
	recent: '최신',
	played: '오래 한 사람'
};
export const REVIEW_PAGE_SIZE = 10;

export interface ReviewAuthor {
	name: string;
	/** 자모 얼굴 글자 · 색 이름(tokens.css --color-face-*) */
	faceChar: string;
	faceColor: string;
	reviewCount: number;
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
	/** 글쓴이가 고른 말 */
	phrases: string[];
	body: string;
	helpfulCount: number;
	reply: { body: string; createdAt: number; note: string | null } | null;
}

export interface ReviewQuery {
	sort: ReviewSort;
	/** 고른 말로 거르기 */
	phrase: string | null;
}

export const DEFAULT_REVIEW_QUERY: ReviewQuery = { sort: 'helpful', phrase: null };

export function parseReviewQuery(params: URLSearchParams): ReviewQuery {
	const sort = REVIEW_SORTS.find((s) => s === params.get('rsort')) ?? 'helpful';
	const phrase = params.get('rphrase')?.trim().slice(0, 20) ?? '';
	return { sort, phrase: phrase || null };
}

export function reviewSearchParams(q: ReviewQuery, into = new URLSearchParams()): URLSearchParams {
	into.delete('rsort');
	into.delete('rphrase');
	if (q.sort !== 'helpful') into.set('rsort', q.sort);
	if (q.phrase) into.set('rphrase', q.phrase);
	return into;
}

/** 커서 값: helpful [도움 수, 쓴 시각] · recent [쓴 시각] · played [플레이 분(없으면 -1), 쓴 시각] */
const ARITY: Record<ReviewSort, number> = { helpful: 2, recent: 1, played: 2 };

export function decodeReviewCursor(raw: string, sort: ReviewSort): Cursor<ReviewSort> | null {
	return decodeCursorOf(raw, sort, ARITY[sort]);
}
