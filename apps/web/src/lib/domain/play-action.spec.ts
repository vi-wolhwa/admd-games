import { describe, expect, it } from 'vitest';

import { deviceFromUserAgent, playAction, type PlayRecord } from './play-action';

const web = { launch: 'web' as const, devices: ['pc' as const, 'phone' as const] };
const record: PlayRecord = { lastPlayedAt: 1, totalMinutes: 72, progress: null };

describe('playAction', () => {
	it('기록이 없으면 처음, 있으면 플레이, 진행도를 알면 이어하기', () => {
		expect(playAction(web, null, 'pc')).toEqual({ kind: 'first' });
		expect(playAction(web, record, 'pc')).toEqual({ kind: 'played', record });
		expect(playAction(web, { ...record, progress: 0.45 }, 'pc')).toMatchObject({
			kind: 'resume',
			progress: 0.45
		});
	});

	it('설치형은 다운로드, 이 기기에서 못 하면 그것이 먼저', () => {
		expect(playAction({ launch: 'download', devices: ['pc'] }, record, 'pc')).toEqual({
			kind: 'download'
		});
		expect(playAction({ launch: 'download', devices: ['pc'] }, null, 'phone')).toEqual({
			kind: 'unsupported',
			devices: ['pc']
		});
		expect(playAction({ launch: 'web', devices: ['phone', 'pad'] }, null, 'pc')).toMatchObject({
			kind: 'unsupported'
		});
	});
});

describe('deviceFromUserAgent', () => {
	it('휴대폰 · 패드 · PC 를 가늠한다', () => {
		expect(
			deviceFromUserAgent('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) Mobile')
		).toBe('phone');
		expect(deviceFromUserAgent('Mozilla/5.0 (Linux; Android 14; SM-S918N) Mobile Safari')).toBe(
			'phone'
		);
		expect(deviceFromUserAgent('Mozilla/5.0 (Linux; Android 14; SM-X710) Safari')).toBe('pad');
		expect(deviceFromUserAgent('Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X)')).toBe('pad');
		expect(deviceFromUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/140')).toBe('pc');
		expect(deviceFromUserAgent(null)).toBe('pc');
	});
});
