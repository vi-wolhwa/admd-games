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
	it('영상을 앞에, 그다음 이미지 — 올린 순서는 그대로', () => {
		const img = (n: number) => ({ kind: 'image' as const, url: `i${String(n)}` });
		const video = { kind: 'video' as const, url: 'v' };
		expect(hoverMedia([img(1), video, img(2)])).toEqual([video, img(1), img(2)]);
		expect(hoverMedia([img(1), img(2)])).toEqual([img(1), img(2)]);
	});
});
