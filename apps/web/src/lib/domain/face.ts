/**
 * 자모 얼굴 정하기 — 프로필 얼굴을 아직 고르지 않은 이름(예: 메이커)에 쓰는 기본 얼굴.
 * 글자 = 이름 첫 글자의 초성(한글이 아니면 그 글자), 색 = 이름으로 정해지는 12색 중 하나(늘 같음).
 */
const CHOSEONG = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ';
export const FACE_COLORS = [
	'hong',
	'ju',
	'gyul',
	'hwang',
	'olive',
	'pul',
	'bichwi',
	'cheongnok',
	'haneul',
	'jjok',
	'bora',
	'jadu'
] as const;

export function faceOf(name: string): { char: string; color: string } {
	const first = name.trim().charAt(0);
	const code = first.charCodeAt(0) - 0xac00;
	const char =
		code >= 0 && code < 11172 ? (CHOSEONG[Math.floor(code / 588)] ?? first) : first.toUpperCase();
	let h = 0;
	for (const ch of name) h = (h * 31 + (ch.codePointAt(0) ?? 0)) >>> 0;
	return { char: char || '?', color: FACE_COLORS[h % FACE_COLORS.length] ?? 'jjok' };
}
