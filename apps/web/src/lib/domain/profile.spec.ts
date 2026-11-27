import { describe, expect, it } from 'vitest';

import { isValidNickname, mentionCandidates, splitMentions } from './profile';

describe('isValidNickname', () => {
	it('한글 · 영문만, 15자까지', () => {
		expect(isValidNickname('새벽배송')).toBe(true);
		expect(isValidNickname('PixelShop')).toBe(true);
		expect(isValidNickname('가'.repeat(15))).toBe(true);
		expect(isValidNickname('가'.repeat(16))).toBe(false);
		expect(isValidNickname('새벽 배송')).toBe(false);
		expect(isValidNickname('player1')).toBe(false);
		expect(isValidNickname('ㅋㅋ')).toBe(false);
		expect(isValidNickname('')).toBe(false);
	});
});

describe('splitMentions', () => {
	const known = new Set(['새벽배송', '청록', 'Pixel']);
	const isKnown = (n: string) => known.has(n);

	it('아는 닉네임만 멘션으로, 조사가 붙어도 닉네임까지만', () => {
		expect(splitMentions('@새벽배송님 저도요! @청록 고마워요', isKnown)).toEqual([
			{ mention: '새벽배송' },
			{ text: '님 저도요! ' },
			{ mention: '청록' },
			{ text: ' 고마워요' }
		]);
	});

	it('모르는 이름 · 이메일 같은 글은 그대로 글', () => {
		expect(splitMentions('@없는사람 a@b', isKnown)).toEqual([{ text: '@없는사람 a@b' }]);
	});

	it('후보는 각 @단어의 모든 앞부분', () => {
		expect(mentionCandidates('@청록님 @Pi')).toEqual(['청', '청록', '청록님', 'P', 'Pi']);
	});
});
