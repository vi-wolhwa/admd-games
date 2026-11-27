import { describe, expect, it } from 'vitest';

import { encodeCursor } from './cursor';
import {
	decodeReviewCursor,
	DEFAULT_REVIEW_QUERY,
	parseReviewQuery,
	REVIEW_KEYWORDS,
	REVIEW_KEYWORDS_MAX,
	reviewHint,
	reviewSearchParams,
	toggleKeyword
} from './review';

describe('리뷰 질의', () => {
	it('모르는 정렬은 도움 많은 순, 읽은 것을 다시 쓰면 같고 다른 주소 값은 그대로', () => {
		expect(parseReviewQuery(new URLSearchParams('rsort=worst'))).toEqual(DEFAULT_REVIEW_QUERY);
		const q = { sort: 'played' as const, phrase: '짧고 굵음' };
		const p = reviewSearchParams(q, new URLSearchParams('tab=reviews'));
		expect(p.get('tab')).toBe('reviews');
		expect(parseReviewQuery(p)).toEqual(q);
	});

	it('커서는 정렬마다 값 개수가 맞아야 한다', () => {
		const c = encodeCursor({ sort: 'played', values: [66, 1700], id: 'r1' });
		expect(decodeReviewCursor(c, 'played')).toEqual({
			sort: 'played',
			values: [66, 1700],
			id: 'r1'
		});
		expect(decodeReviewCursor(c, 'recent')).toBeNull();
	});
});

describe('리뷰 쓰기', () => {
	it('키워드는 최대 5개까지 — 더 누르면 그대로, 고른 것을 누르면 빠진다', () => {
		const five = REVIEW_KEYWORDS.slice(0, REVIEW_KEYWORDS_MAX);
		const sixth = REVIEW_KEYWORDS[REVIEW_KEYWORDS_MAX] ?? '';
		expect(toggleKeyword(five, sixth)).toEqual(five);
		expect(toggleKeyword(five, five[0] ?? '')).toEqual(five.slice(1));
	});

	it('안내는 키워드 → 글 차례, 공백만 있는 글은 빈 글', () => {
		expect(reviewHint([], '좋아요')).toBe('키워드를 1개 이상 골라 주세요');
		expect(reviewHint(['짧고 굵음'], '  ')).toBe('리뷰를 작성해 주세요');
		expect(reviewHint(['짧고 굵음'], '좋아요')).toBeNull();
	});
});
