import { error } from '@sveltejs/kit';

import type { PageServerLoad } from './$types';

/**
 * 메이커스 프로필(최소 — 사용자 결정 2026-11-28). 얼굴 · 이름 · 공개한 게임만.
 * 소개 · 팔로워 · 개발일지는 MakersGround(3묶음)에서 붙인다.
 */
export const load: PageServerLoad = async ({ params, locals }) => {
	const profile = await locals.services.gameDetails.makerProfile(params.slug);
	if (!profile) error(404, '메이커를 찾을 수 없어요.');
	return { profile, now: Date.now() };
};
