/**
 * 게임 카드 한 장에 필요한 열과, 묶음의 태그 · 미디어를 한 번에(batch) 붙이는 도우미.
 * 목록(catalog) · 상세(game-details)의 비슷한 게임이 같이 쓴다.
 */
import { asc, eq, inArray } from 'drizzle-orm';

import type { GameCardData, GameMedia, Launch, LengthBucket } from '#lib/domain/game.ts';

import type { D1Client } from './client';
import { gameMedia, games, gameTags, makers, tags } from './schema';

/** games ⋈ makers 에서 고를 카드 열 */
export const cardColumns = {
	id: games.id,
	slug: games.slug,
	title: games.title,
	makerName: makers.name,
	length: games.length,
	launch: games.launch,
	phone: games.phone,
	playersMax: games.playersMax,
	scanPassed: games.scanPassed,
	cover: games.coverUrl,
	recommendCount: games.recommendCount,
	reviewCount: games.reviewCount,
	publishedAt: games.publishedAt
};

export interface CardRow {
	id: string;
	slug: string;
	title: string;
	makerName: string;
	length: number;
	launch: string;
	phone: boolean;
	playersMax: number;
	scanPassed: boolean;
	cover: string;
	recommendCount: number;
	reviewCount: number;
	publishedAt: number | null;
}

function push<T>(map: Map<string, T[]>, key: string, value: T) {
	const list = map.get(key);
	if (list) list.push(value);
	else map.set(key, [value]);
}

/** 행 묶음에 태그(메이커가 적은 순) · 미디어(올린 순)를 붙여 카드로 */
export async function toCards(db: D1Client, rows: CardRow[]): Promise<GameCardData[]> {
	const ids = rows.map((r) => r.id);
	const tagsByGame = new Map<string, string[]>();
	const mediaByGame = new Map<string, GameMedia[]>();
	if (ids.length > 0) {
		const [tagRows, mediaRows] = await db.batch([
			db
				.select({ gameId: gameTags.gameId, name: tags.name })
				.from(gameTags)
				.innerJoin(tags, eq(tags.id, gameTags.tagId))
				.where(inArray(gameTags.gameId, ids))
				.orderBy(asc(gameTags.gameId), asc(gameTags.position)),
			db
				.select({ gameId: gameMedia.gameId, kind: gameMedia.kind, url: gameMedia.url })
				.from(gameMedia)
				.where(inArray(gameMedia.gameId, ids))
				.orderBy(asc(gameMedia.gameId), asc(gameMedia.position))
		]);
		for (const t of tagRows) push(tagsByGame, t.gameId, t.name);
		for (const m of mediaRows) {
			push(mediaByGame, m.gameId, { kind: m.kind === 'video' ? 'video' : 'image', url: m.url });
		}
	}
	return rows.map((r) => ({
		id: r.id,
		slug: r.slug,
		title: r.title,
		makerName: r.makerName,
		length: r.length as LengthBucket,
		launch: r.launch as Launch,
		phone: r.phone,
		playersMax: r.playersMax,
		scanPassed: r.scanPassed,
		cover: r.cover,
		recommendCount: r.recommendCount,
		reviewCount: r.reviewCount,
		publishedAt: r.publishedAt ?? 0,
		tags: tagsByGame.get(r.id) ?? [],
		media: mediaByGame.get(r.id) ?? []
	}));
}
