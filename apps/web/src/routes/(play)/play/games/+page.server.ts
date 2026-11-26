import { parseCatalogQuery, parseLoaded } from '#lib/domain/catalog.ts';

import type { PageServerLoad } from './$types';

/**
 * 전체 게임(PG03). 주소의 필터 · 정렬 · 불러온 개수(n)를 그대로 읽는다 —
 * 상세에서 뒤로 오면 같은 개수를 다시 그려서 브라우저가 스크롤 위치를 되살린다(ADR 0010).
 */
export const load: PageServerLoad = async ({ url, locals }) => {
	const query = parseCatalogQuery(url.searchParams);
	const { catalog } = locals.services;
	const [tags, first] = await Promise.all([
		catalog.listTags(),
		catalog.listGames(query, { cursor: null, limit: parseLoaded(url.searchParams) })
	]);
	return {
		query,
		tags,
		games: first.items,
		nextCursor: first.nextCursor,
		total: first.total ?? first.items.length,
		now: Date.now()
	};
};
