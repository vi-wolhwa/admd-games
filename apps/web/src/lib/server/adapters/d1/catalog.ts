import {
	and,
	asc,
	count,
	desc,
	eq,
	exists,
	gt,
	gte,
	inArray,
	isNull,
	lt,
	or,
	type SQL,
	sql
} from 'drizzle-orm';

import {
	type CatalogQuery,
	type Cursor,
	decodeCursor,
	encodeCursor,
	searchKey
} from '#lib/domain/catalog.ts';

import type { Catalog, CatalogPage } from '../../ports/catalog';
import { cardColumns, toCards } from './cards';
import type { D1Client } from './client';
import { games, gameTags, makers, tags } from './schema';

/**
 * D1 게임 목록. 읽기 비용(무료 5백만 행/일)을 아끼는 규칙:
 * - OFFSET 대신 커서(정렬 값 + id), 정렬마다 (status, 정렬 열…, id) 색인
 * - 개수는 첫 묶음에서만 센다, 태그 개수는 캐시 열(game_count)
 * - 카드의 태그 · 미디어는 그 묶음의 id 로 한 번에(batch)
 */
export function createD1Catalog(db: D1Client): Catalog {
	return {
		async listGames(query, page): Promise<CatalogPage> {
			const cursor = page.cursor ? decodeCursor(page.cursor, query.sort) : null;
			if (page.cursor && !cursor) return { items: [], nextCursor: null, total: null };

			const filter = filters(db, query);
			const where = cursor ? and(filter, after(cursor)) : filter;
			const list = db
				.select({ ...cardColumns, playCount: games.playCount })
				.from(games)
				.innerJoin(makers, eq(makers.id, games.makerId))
				.where(where)
				.orderBy(...ORDER[query.sort])
				.limit(page.limit + 1);

			let rows;
			let total: number | null = null;
			if (cursor) {
				rows = await list;
			} else {
				const [r, c] = await db.batch([list, db.select({ n: count() }).from(games).where(filter)]);
				rows = r;
				total = c[0]?.n ?? 0;
			}

			const hasMore = rows.length > page.limit;
			const pageRows = hasMore ? rows.slice(0, page.limit) : rows;
			const items = await toCards(db, pageRows);
			const last = pageRows.at(-1);
			return {
				items,
				nextCursor: hasMore && last ? encodeCursor(cursorOf(query, last)) : null,
				total
			};
		},

		async listTags() {
			const rows = await db
				.select({ slug: tags.slug, name: tags.name, count: tags.gameCount })
				.from(tags)
				.where(and(isNull(tags.aliasOf), gt(tags.gameCount, 0)))
				.orderBy(desc(tags.gameCount), asc(tags.name));
			return rows;
		}
	};
}

function filters(db: D1Client, q: CatalogQuery): SQL | undefined {
	const parts: (SQL | undefined)[] = [eq(games.status, 'published')];
	const key = searchKey(q.q);
	if (key) {
		// 제목 · 메이커 이름에 들어 있으면 — 양쪽 공백을 빼고 비교(searchKey). LIKE 의 % _ 는 글자 그대로(ESCAPE '!').
		// 공개 게임 행을 다 훑는다(게임 수가 적은 지금은 충분) — 수천 개가 되면 FTS5 색인으로(PG04 검색 때)
		const pattern = `%${key.replace(/[!%_]/g, (c) => `!${c}`)}%`;
		parts.push(
			or(
				sql`REPLACE(${games.title}, ' ', '') LIKE ${pattern} ESCAPE '!'`,
				exists(
					db
						.select({ one: sql`1` })
						.from(makers)
						.where(
							and(
								eq(makers.id, games.makerId),
								sql`REPLACE(${makers.name}, ' ', '') LIKE ${pattern} ESCAPE '!'`
							)
						)
				)
			)
		);
	}
	if (q.tags.length > 0) {
		parts.push(
			exists(
				db
					.select({ one: sql`1` })
					.from(gameTags)
					.innerJoin(tags, eq(tags.id, gameTags.tagId))
					.where(and(eq(gameTags.gameId, games.id), inArray(tags.slug, q.tags)))
			)
		);
	}
	if (q.length === 'daily') parts.push(eq(games.daily, true));
	else if (q.length) parts.push(eq(games.length, q.length));
	if (q.launch) parts.push(eq(games.launch, q.launch));
	if (q.players === 'solo') parts.push(eq(games.playersMin, 1));
	if (q.players === 'duo') parts.push(gte(games.playersMax, 2));
	if (q.players === 'online') parts.push(eq(games.online, true));
	return and(...parts);
}

const ORDER = {
	played: [desc(games.playCount), desc(games.recommendCount), desc(games.id)],
	recommended: [desc(games.recommendCount), desc(games.id)],
	reviews: [desc(games.reviewCount), desc(games.id)],
	new: [desc(games.publishedAt), desc(games.id)]
} satisfies Record<CatalogQuery['sort'], SQL[]>;

/** 커서 다음 항목들 — ORDER 와 같은 방향의 사전순 비교 */
function after(c: Cursor): SQL | undefined {
	const [a = 0, b = 0] = c.values;
	switch (c.sort) {
		case 'played':
			return or(
				lt(games.playCount, a),
				and(eq(games.playCount, a), lt(games.recommendCount, b)),
				and(eq(games.playCount, a), eq(games.recommendCount, b), lt(games.id, c.id))
			);
		case 'recommended':
			return or(lt(games.recommendCount, a), and(eq(games.recommendCount, a), lt(games.id, c.id)));
		case 'reviews':
			return or(lt(games.reviewCount, a), and(eq(games.reviewCount, a), lt(games.id, c.id)));
		case 'new':
			return or(lt(games.publishedAt, a), and(eq(games.publishedAt, a), lt(games.id, c.id)));
	}
}

function cursorOf(
	q: CatalogQuery,
	r: {
		id: string;
		playCount: number;
		recommendCount: number;
		reviewCount: number;
		publishedAt: number | null;
	}
): Cursor {
	switch (q.sort) {
		case 'played':
			return { sort: q.sort, values: [r.playCount, r.recommendCount], id: r.id };
		case 'recommended':
			return { sort: q.sort, values: [r.recommendCount], id: r.id };
		case 'reviews':
			return { sort: q.sort, values: [r.reviewCount], id: r.id };
		case 'new':
			return { sort: q.sort, values: [r.publishedAt ?? 0], id: r.id };
	}
}
