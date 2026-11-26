/** 화면에 쓰는 숫자 · 날짜 표기(한국어, Intl). 서버 · 화면 공용 */

/** 플레이 시간 — 1시간 미만은 분, 그 이상은 시간(소수 한 자리, .0 은 뺌) */
export function formatPlayTime(minutes: number): string {
	if (minutes < 60) return `${String(Math.max(1, Math.round(minutes)))}분`;
	const hours = Math.round((minutes / 60) * 10) / 10;
	return `${hours.toLocaleString('ko-KR')}시간`;
}

const FULL = new Intl.DateTimeFormat('ko-KR', {
	year: 'numeric',
	month: 'long',
	day: 'numeric',
	timeZone: 'Asia/Seoul'
});

/** 날짜 — 올해면 '11월 21일', 아니면 '2025년 11월 21일' */

/** 날짜 — 늘 연도까지('2026년 10월 2일'). 공개일처럼 기준이 되는 날짜에 */
export function formatFullDate(at: number): string {
	return FULL.format(at);
}

const MINUTE = 60_000;
const HOUR = 60 * MINUTE;
const DAY = 24 * HOUR;

/**
 * 지난 시간 — '3분' · '5시간' · '12일' · '2개월' · '1년'(뒤에 '전'은 부르는 쪽이 붙인다).
 * 1분 안쪽은 '1분'. 달은 30일, 해는 365일로 센다(대략이면 충분 — 정확한 날짜는 함께 보이는 전체 날짜로).
 */
export function formatAgo(at: number, now: number): string {
	const d = Math.max(0, now - at);
	if (d < HOUR) return `${String(Math.max(1, Math.floor(d / MINUTE)))}분`;
	if (d < DAY) return `${String(Math.floor(d / HOUR))}시간`;
	if (d < 30 * DAY) return `${String(Math.floor(d / DAY))}일`;
	if (d < 365 * DAY) return `${String(Math.floor(d / (30 * DAY)))}개월`;
	return `${String(Math.floor(d / (365 * DAY)))}년`;
}
