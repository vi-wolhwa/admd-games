import { describe, expect, it } from 'vitest';

import { encodeCursor } from './cursor';
import {
	decodeReviewCursor,
	DEFAULT_REVIEW_QUERY,
	parseReviewQuery,
	reviewSearchParams
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
		const c = encodeCursor({ sort: 'helpful', values: [41, 1700], id: 'r1' });
		expect(decodeReviewCursor(c, 'helpful')).toEqual({
			sort: 'helpful',
			values: [41, 1700],
			id: 'r1'
		});
		expect(decodeReviewCursor(c, 'recent')).toBeNull();
	});
});
