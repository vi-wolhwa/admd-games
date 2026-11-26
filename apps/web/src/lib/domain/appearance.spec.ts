import { describe, expect, it } from 'vitest';

import { groundOf, parseTheme } from './appearance';

describe('테마', () => {
	it('쿠키가 dark 일 때만 다크, 그 밖의 값 · 없음은 라이트', () => {
		expect(parseTheme('dark')).toBe('dark');
		expect(parseTheme('light')).toBe('light');
		expect(parseTheme('nonsense')).toBe('light');
		expect(parseTheme(undefined)).toBe('light');
	});
});

describe('그라운드', () => {
	it('/makers 와 그 아래는 MakersGround, 나머지는 PlayGround', () => {
		expect(groundOf('/makers')).toBe('make');
		expect(groundOf('/makers/games')).toBe('make');
		expect(groundOf('/makersville')).toBe('play');
		expect(groundOf('/play')).toBe('play');
		expect(groundOf('/')).toBe('play');
	});
});
