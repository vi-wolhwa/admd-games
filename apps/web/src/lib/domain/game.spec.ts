import { describe, expect, it } from 'vitest';

import { hoverMedia, isNewGame, playersLabel, splitDescription } from './game';

const DAY = 86_400_000;

describe('isNewGame', () => {
	it('공개 후 14일 안쪽만 신작', () => {
		const now = 100 * DAY;
		expect(isNewGame(now - 13 * DAY, now)).toBe(true);
		expect(isNewGame(now - 14 * DAY, now)).toBe(false);
		expect(isNewGame(now + DAY, now)).toBe(false);
	});
});

describe('hoverMedia', () => {
	it('영상을 앞에, 그다음 이미지 — 올린 순서는 그대로', () => {
		const img = (n: number) => ({ kind: 'image' as const, url: `i${String(n)}` });
		const video = { kind: 'video' as const, url: 'v' };
		expect(hoverMedia([img(1), video, img(2)])).toEqual([video, img(1), img(2)]);
		expect(hoverMedia([img(1), img(2)])).toEqual([img(1), img(2)]);
	});
});

describe('splitDescription', () => {
	it("빈 줄로 문단, '- ' 줄은 특징", () => {
		expect(splitDescription('첫 문단\n이어짐\n\n- 하나\n- 둘\n\n끝')).toEqual({
			paragraphs: ['첫 문단 이어짐', '끝'],
			features: ['하나', '둘']
		});
	});
});

describe('playersLabel', () => {
	it('혼자서 · n명 · 범위, 온라인이면 뒤에 붙인다', () => {
		expect(playersLabel(1, 1)).toBe('혼자서');
		expect(playersLabel(2, 2)).toBe('2명');
		expect(playersLabel(1, 4)).toBe('1~4명');
		expect(playersLabel(2, 4, true)).toBe('2~4명 · 온라인');
	});
});
