import { redirect } from '@sveltejs/kit';

import type { PageServerLoad } from './$types';

// 주소 구조(setup-agenda 1-1): / 는 PlayGround(/play)로. 나중에 / 를 소개 페이지로 쓸 수 있게 임시 이동(307).
export const load: PageServerLoad = () => {
	redirect(307, '/play');
};
