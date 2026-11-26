/**
 * 구조화 로그 — Cloudflare Workers Logs 에서 필드로 검색할 수 있게 JSON 한 줄로 남긴다(setup-agenda 7-3).
 * 사용자에게는 친절한 문구와 오류 번호(requestId)만 보이고, 자세한 내용은 여기에만 남는다.
 */
type Level = 'info' | 'warn' | 'error';

export function log(level: Level, event: string, fields: Record<string, unknown> = {}): void {
	const line = JSON.stringify({ level, event, at: new Date().toISOString(), ...fields });
	if (level === 'error') console.error(line);
	else if (level === 'warn') console.warn(line);
	else console.log(line);
}
