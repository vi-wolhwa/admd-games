import { parseTheme, THEME_COOKIE } from '#lib/domain/appearance.ts';

import type { LayoutServerLoad } from './$types';

/** 헤더의 테마 버튼이 첫 화면부터 맞는 아이콘을 그리도록(html 의 data-theme 은 hooks 가 넣음) */
export const load: LayoutServerLoad = ({ cookies }) => ({
	theme: parseTheme(cookies.get(THEME_COOKIE))
});
