import { describe, expect, it } from 'vitest';

import { formatAgo, formatFullDate, formatPlayTime } from './format';

describe('formatPlayTime', () => {
	it('1시간 미만은 분, 넘으면 소수 한 자리 시간', () => {
		expect(formatPlayTime(48)).toBe('48분');
		expect(formatPlayTime(66)).toBe('1.1시간');
		expect(formatPlayTime(300)).toBe('5시간');
	});
});

describe('formatFullDate', () => {
	it('늘 연도까지, 한국 시간 기준', () => {
		// UTC 12월 31일 16시 = 한국 1월 1일
		expect(formatFullDate(Date.UTC(2025, 11, 31, 16))).toBe('2026년 1월 1일');
		expect(formatFullDate(Date.UTC(2025, 5, 2))).toBe('2025년 6월 2일');
	});
});

describe('formatAgo', () => {
	it('분 · 시간 · 일 · 개월 · 년으로 줄여 쓴다', () => {
		const now = Date.UTC(2026, 10, 28);
		const ago = (ms: number) => formatAgo(now - ms, now);
		expect(ago(10_000)).toBe('1분');
		expect(ago(59 * 60_000)).toBe('59분');
		expect(ago(5 * 3_600_000)).toBe('5시간');
		expect(ago(12 * 86_400_000)).toBe('12일');
		expect(ago(65 * 86_400_000)).toBe('2개월');
		expect(ago(400 * 86_400_000)).toBe('1년');
	});
});
