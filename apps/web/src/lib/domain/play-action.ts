/**
 * 게임 상세의 주 버튼 — 플랫폼이 실제로 아는 것만으로 정한다(ADR 0011 §1).
 *   처음 → '지금 플레이' / 해 본 적 있음 → '플레이' + 마지막 · 모두 시간 / 진행도를 SDK 가 알려 줌 → '이어하기'
 *   설치형 → '다운로드' / 이 기기에서 못 함 → 휴대폰 · 패드로 안내
 * '다시 하기' · '완료' 는 없다(엔딩은 게임 안의 일).
 */
import type { Device, GameDetail } from './game';

/** 이 사람의 플레이 기록(PG06 에서 생김). 게스트 · 기록 없음 = null */
export interface PlayRecord {
	lastPlayedAt: number;
	totalMinutes: number;
	/** SDK 가 알려 준 진행도 0~1 — 없으면 null */
	progress: number | null;
}

export type PlayAction =
	| { kind: 'first' }
	| { kind: 'played'; record: PlayRecord }
	| { kind: 'resume'; record: PlayRecord; progress: number }
	| { kind: 'download' }
	| { kind: 'unsupported'; devices: Device[] };

export function playAction(
	game: Pick<GameDetail, 'launch' | 'devices'>,
	record: PlayRecord | null,
	device: Device
): PlayAction {
	if (!game.devices.includes(device)) return { kind: 'unsupported', devices: game.devices };
	if (game.launch === 'download') return { kind: 'download' };
	if (record?.progress != null) return { kind: 'resume', record, progress: record.progress };
	if (record) return { kind: 'played', record };
	return { kind: 'first' };
}

/** 요청의 User-Agent 로 기기를 가늠한다(첫 화면부터 맞는 버튼을 그리려고 — 틀려도 기능은 막지 않음) */
export function deviceFromUserAgent(ua: string | null): Device {
	if (!ua) return 'pc';
	if (/iPad|Tablet/i.test(ua) || (/Android/i.test(ua) && !/Mobile/i.test(ua))) return 'pad';
	if (/iPhone|iPod|Android|Mobile/i.test(ua)) return 'phone';
	return 'pc';
}
