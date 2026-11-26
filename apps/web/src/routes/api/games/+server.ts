import { error } from '@sveltejs/kit';

import { PAGE_SIZE, parseCatalogQuery } from '#lib/domain/catalog.ts';

import type { RequestHandler } from './$types';

/** 전체 게임 이어 불러오기(무한 스크롤) — 첫 묶음은 페이지 load 가, 그다음 12개씩은 여기서 */
export const GET: RequestHandler = async ({ url, locals }) => {
	const cursor = url.searchParams.get('cursor');
	if (!cursor) error(400, '이어 불러올 위치(cursor)가 없어요.');
	const page = await locals.services.catalog.listGames(parseCatalogQuery(url.searchParams), {
		cursor,
		limit: PAGE_SIZE
	});
	return Response.json({ items: page.items, nextCursor: page.nextCursor });
};
