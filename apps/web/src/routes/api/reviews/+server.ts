import { error } from '@sveltejs/kit';

import { parseReviewQuery, REVIEW_PAGE_SIZE } from '#lib/domain/review.ts';

import type { RequestHandler } from './$types';

/** 리뷰 이어 불러오기(게임 상세 리뷰 탭의 '더 보기') — 첫 묶음은 페이지 load 가, 그다음 10개씩은 여기서 */
export const GET: RequestHandler = async ({ url, locals }) => {
	const game = url.searchParams.get('game');
	const cursor = url.searchParams.get('cursor');
	if (!game || !cursor) error(400, '게임(game)과 이어 불러올 위치(cursor)가 필요해요.');
	const page = await locals.services.reviews.listReviews(game, parseReviewQuery(url.searchParams), {
		cursor,
		limit: REVIEW_PAGE_SIZE
	});
	return Response.json({ items: page.items, nextCursor: page.nextCursor });
};
