/** 화면에 쓰는 숫자 · 날짜 표기(한국어, Intl). 서버 · 화면 공용 */

/** 플레이 시간 — 1시간 미만은 분, 그 이상은 시간(소수 한 자리, .0 은 뺌) */
export function formatPlayTime(minutes: number): string {
	if (minutes < 60) return `${String(Math.max(1, Math.round(minutes)))}분`;
	const hours = Math.round((minutes / 60) * 10) / 10;
	return `${hours.toLocaleString('ko-KR')}시간`;
}

const SAME_YEAR = new Intl.DateTimeFormat('ko-KR', {
	month: 'long',
	day: 'numeric',
	timeZone: 'Asia/Seoul'
});
const FULL = new Intl.DateTimeFormat('ko-KR', {
	year: 'numeric',
	month: 'long',
	day: 'numeric',
	timeZone: 'Asia/Seoul'
});

/** 날짜 — 올해면 '11월 21일', 아니면 '2025년 11월 21일' */
export function formatDate(at: number, now: number): string {
	const y = (t: number) => new Date(t + 9 * 3_600_000).getUTCFullYear();
	return (y(at) === y(now) ? SAME_YEAR : FULL).format(at);
}

/** 날짜 — 늘 연도까지('2026년 10월 2일'). 공개일처럼 기준이 되는 날짜에 */
export function formatFullDate(at: number): string {
	return FULL.format(at);
}
