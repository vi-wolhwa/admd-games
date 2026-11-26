import { describe, expect, it } from 'vitest';

import { hoverMedia, isNewGame } from './game';

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
	it('영상이 있으면 영상 하나만, 없으면 이미지 전부', () => {
		const img = (n: number) => ({ kind: 'image' as const, url: `i${String(n)}` });
		const video = { kind: 'video' as const, url: 'v' };
		expect(hoverMedia([img(1), video, img(2)])).toEqual([video]);
		expect(hoverMedia([img(1), img(2)])).toEqual([img(1), img(2)]);
	});
});
