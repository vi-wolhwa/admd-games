/**
 * 이어 불러오기 커서 = 마지막 항목의 정렬 값 + id (OFFSET 을 쓰지 않는다 — D1 읽기 절약, ADR 0010).
 * 게임 목록 · 리뷰 목록이 같이 쓴다. 정렬마다 값의 개수(arity)가 정해져 있고, 다른 정렬의 커서는 무시한다.
 */
export interface Cursor<S extends string = string> {
	sort: S;
	values: readonly number[];
	id: string;
}

export function encodeCursor(cursor: Cursor): string {
	const json = JSON.stringify([cursor.sort, cursor.values, cursor.id]);
	return btoa(json).replaceAll('+', '-').replaceAll('/', '_').replace(/=+$/, '');
}

export function decodeCursorOf<S extends string>(
	raw: string,
	sort: S,
	arity: number
): Cursor<S> | null {
	try {
		const parsed: unknown = JSON.parse(atob(raw.replaceAll('-', '+').replaceAll('_', '/')));
		if (!Array.isArray(parsed) || parsed.length !== 3) return null;
		const [s, values, id] = parsed as unknown[];
		if (s !== sort || typeof id !== 'string' || !Array.isArray(values)) return null;
		if (values.length !== arity) return null;
		if (!values.every((v): v is number => typeof v === 'number' && Number.isFinite(v))) return null;
		return { sort, values, id };
	} catch {
		return null;
	}
}
