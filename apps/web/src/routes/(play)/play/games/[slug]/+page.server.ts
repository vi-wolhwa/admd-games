import { error } from '@sveltejs/kit';

import { deviceFromUserAgent } from '#lib/domain/play-action.ts';
import { parseReviewQuery, REVIEW_PAGE_SIZE, type ReviewData } from '#lib/domain/review.ts';

import type { PageServerLoad } from './$types';

/** 비슷한 게임 레일에 싣는 수 */
const SIMILAR = 8;
/** 리뷰 탭의 '자주 고른 말' 수 */
const PHRASES = 8;

/**
 * 게임 상세(PG05). 탭(소개 · 리뷰)은 주소의 tab 으로 — 리뷰는 리뷰 탭을 열 때만 읽는다(D1 읽기 절약).
 * 기기는 User-Agent 로 가늠해 첫 화면부터 맞는 버튼(이 기기 불가 등)을 그린다.
 */
export const load: PageServerLoad = async ({ params, url, locals, request }) => {
	const { gameDetails, reviews } = locals.services;
	const game = await gameDetails.getGame(params.slug);
	if (!game) error(404, '게임을 찾을 수 없어요.');

	const tab = url.searchParams.get('tab') === 'reviews' ? 'reviews' : 'about';
	const reviewQuery = parseReviewQuery(url.searchParams);
	const [similar, reviewPage, phrases] = await Promise.all([
		gameDetails.similarGames(game.id, SIMILAR),
		tab === 'reviews'
			? reviews.listReviews(game.id, reviewQuery, { cursor: null, limit: REVIEW_PAGE_SIZE })
			: null,
		tab === 'reviews' ? reviews.topPhrases(game.id, PHRASES) : null
	]);

	return {
		game,
		similar,
		tab,
		reviewQuery,
		reviewPage,
		phrases,
		// 내가 쓴 리뷰(버전마다 하나 — 지금 버전 것이 있으면 쓰기 대신 맨 위에). 로그인(SH01) 전에는 없음
		mine: [] as ReviewData[],
		device: deviceFromUserAgent(request.headers.get('user-agent')),
		now: Date.now()
	};
};
