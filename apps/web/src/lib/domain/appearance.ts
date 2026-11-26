/**
 * 화면 모양 규칙 — 테마(라이트 · 다크)와 그라운드(PlayGround · MakersGround).
 * ADR 0008: 처음은 라이트, 헤더의 버튼으로 바꾸고 쿠키에 기억한다. 주소 구조: /play · /makers (setup-agenda 1-1).
 */
export type Theme = 'light' | 'dark';
export type Ground = 'play' | 'make';

export const THEME_COOKIE = 'theme';

export function parseTheme(value: string | undefined): Theme {
	return value === 'dark' ? 'dark' : 'light';
}

export function groundOf(pathname: string): Ground {
	return pathname === '/makers' || pathname.startsWith('/makers/') ? 'make' : 'play';
}
