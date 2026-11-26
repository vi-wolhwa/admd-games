import { and, count, desc, eq, inArray, ne, sql } from 'drizzle-orm';

import type { Caution, Control, Device, GameDetail } from '#lib/domain/game.ts';

import type { GameDetails } from '../../ports/game-details';
import { cardColumns, toCards } from './cards';
import type { D1Client } from './client';
import { games, gameTags, makers } from './schema';

const list = <T extends string>(csv: string) => (csv ? (csv.split(',') as T[]) : []);

/** D1 게임 상세 — 게임 1행 + 태그 · 미디어 묶음 한 번, 비슷한 게임은 태그 겹침으로 */
export function createD1GameDetails(db: D1Client): GameDetails {
	return {
		async getGame(slug) {
			const [row] = await db
				.select({
					...cardColumns,
					summary: games.summary,
					description: games.description,
					// games.slug 와 이름이 겹치므로 별칭(D1 결과는 열 이름으로 옴)
					makerSlug: sql<string>`${makers.slug}`.as('maker_slug'),
					makerGameCount: sql<number>`(SELECT COUNT(*) FROM games AS mg WHERE mg.maker_id = ${games.makerId} AND mg.status = 'published')`,
					pc: games.pc,
					pad: games.pad,
					controls: games.controls,
					languages: games.languages,
					cautions: games.cautions,
					minSpec: games.minSpec,
					playersMin: games.playersMin
				})
				.from(games)
				.innerJoin(makers, eq(makers.id, games.makerId))
				.where(and(eq(games.slug, slug), eq(games.status, 'published')))
				.limit(1);
			if (!row) return null;
			const [card] = await toCards(db, [row]);
			if (!card) return null;
			const devices: Device[] = [];
			if (row.pc) devices.push('pc');
			if (row.phone) devices.push('phone');
			if (row.pad) devices.push('pad');
			const detail: GameDetail = {
				...card,
				summary: row.summary,
				description: row.description,
				makerSlug: row.makerSlug,
				makerGameCount: row.makerGameCount,
				devices,
				controls: list<Control>(row.controls),
				languages: list<string>(row.languages),
				cautions: list<Caution>(row.cautions),
				minSpec: row.minSpec,
				playersMin: row.playersMin
			};
			return detail;
		},

		async similarGames(gameId, limit) {
			const myTags = db
				.select({ tagId: gameTags.tagId })
				.from(gameTags)
				.where(eq(gameTags.gameId, gameId));
			const rows = await db
				.select(cardColumns)
				.from(gameTags)
				.innerJoin(games, eq(games.id, gameTags.gameId))
				.innerJoin(makers, eq(makers.id, games.makerId))
				.where(
					and(inArray(gameTags.tagId, myTags), ne(games.id, gameId), eq(games.status, 'published'))
				)
				.groupBy(games.id)
				.orderBy(desc(count()), desc(games.recommendCount), desc(games.id))
				.limit(limit);
			return toCards(db, rows);
		}
	};
}
