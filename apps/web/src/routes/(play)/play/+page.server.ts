import { redirect } from '@sveltejs/kit';

import type { PageServerLoad } from './$types';

// 홈(PG01)은 마지막에 만든다(page-order.md). 그 전까지 PlayGround 첫 화면 = 전체 게임(임시 이동 307)
export const load: PageServerLoad = () => {
	redirect(307, '/play/games');
};
