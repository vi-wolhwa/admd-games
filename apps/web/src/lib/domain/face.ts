/**
 * 기본 고양이 얼굴 — 얼굴을 고르지 않은 사람(건너뛰기 · 메이커)에게 이름으로 정해 주는 얼굴(늘 같음).
 * 눈 = 이름 첫 글자의 초성(한글이 아니면 그 글자), 입 = 'ㅅ', 색 = 이름으로 정해지는 12색 중 하나.
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

export const DEFAULT_MOUTH = 'ㅅ';

export function faceOf(name: string): { char: string; mouth: string; color: string } {
	const first = name.trim().charAt(0);
	const code = first.charCodeAt(0) - 0xac00;
	const char =
		code >= 0 && code < 11172 ? (CHOSEONG[Math.floor(code / 588)] ?? first) : first.toUpperCase();
	let h = 0;
	for (const ch of name) h = (h * 31 + (ch.codePointAt(0) ?? 0)) >>> 0;
	return {
		char: char || '?',
		mouth: DEFAULT_MOUTH,
		color: FACE_COLORS[h % FACE_COLORS.length] ?? 'jjok'
	};
}
