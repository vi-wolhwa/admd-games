import { describe, expect, it } from 'vitest';

import { formatDate, formatPlayTime } from './format';

describe('formatPlayTime', () => {
	it('1시간 미만은 분, 넘으면 소수 한 자리 시간', () => {
		expect(formatPlayTime(48)).toBe('48분');
		expect(formatPlayTime(66)).toBe('1.1시간');
		expect(formatPlayTime(300)).toBe('5시간');
	});
});

describe('formatDate', () => {
	it('올해면 월 · 일만, 아니면 연도까지(한국 시간)', () => {
		const now = Date.UTC(2026, 10, 28);
		expect(formatDate(Date.UTC(2026, 10, 21), now)).toBe('11월 21일');
		// UTC 12월 31일 16시 = 한국 1월 1일(올해)
		expect(formatDate(Date.UTC(2025, 11, 31, 16), now)).toBe('1월 1일');
		expect(formatDate(Date.UTC(2025, 5, 2), now)).toBe('2025년 6월 2일');
	});
});
