/**
 * D1(SQLite) 테이블 정의. 이 파일은 D1 어댑터 내부 구현이다 —
 * 어댑터 밖(ports, 도메인, 라우트)에서 import 하지 않는다.
 *
 * 다른 DB로 옮기기 쉽게 하는 규칙 (docs/architecture.md 참고):
 * - ID 는 text (UUID), 시각은 integer (epoch ms)
 * - SQLite 전용 기능(JSON1 함수, 동적 타입)에 기대지 않는다
 *
 * 변경 후: npm run db:generate → npm run db:migrate:local
 * 이관은 더하기만(docs/operations.md 'DB 이관 규칙').
 */
import { index, integer, primaryKey, sqliteTable, text } from 'drizzle-orm/sqlite-core';

export const makers = sqliteTable('makers', {
	id: text('id').primaryKey(),
	slug: text('slug').notNull().unique(),
	name: text('name').notNull(),
	createdAt: integer('created_at').notNull()
});

/** 게임 정보 필드 정의: docs/product/game-metadata.md */
export const games = sqliteTable(
	'games',
	{
		id: text('id').primaryKey(),
		slug: text('slug').notNull().unique(),
		makerId: text('maker_id')
			.notNull()
			.references(() => makers.id),
		/** draft · review · published · hidden — 목록에는 published 만 */
		status: text('status').notNull(),
		title: text('title').notNull(),
		summary: text('summary').notNull(),
		/** web · download */
		launch: text('launch').notNull(),
		/** 한 판 길이 구간 1~5 */
		length: integer('length').notNull(),
		phone: integer('phone', { mode: 'boolean' }).notNull(),
		playersMin: integer('players_min').notNull(),
		playersMax: integer('players_max').notNull(),
		scanPassed: integer('scan_passed', { mode: 'boolean' }).notNull(),
		coverUrl: text('cover_url').notNull(),
		publishedAt: integer('published_at'),
		/** 개수 캐시 — 플레이(PG06 기록) · 추천 · 리뷰 때 갱신(목록마다 세지 않음) */
		playCount: integer('play_count').notNull().default(0),
		recommendCount: integer('recommend_count').notNull().default(0),
		reviewCount: integer('review_count').notNull().default(0),
		createdAt: integer('created_at').notNull()
	},
	(t) => [
		index('games_by_played').on(t.status, t.playCount, t.recommendCount, t.id),
		index('games_by_recommended').on(t.status, t.recommendCount, t.id),
		index('games_by_reviews').on(t.status, t.reviewCount, t.id),
		index('games_by_new').on(t.status, t.publishedAt, t.id)
	]
);

/** 태그는 게임이 공개될 때 생긴다(ADR 0010). game_count = 공개 게임 수 캐시 */
export const tags = sqliteTable('tags', {
	id: text('id').primaryKey(),
	slug: text('slug').notNull().unique(),
	name: text('name').notNull(),
	/** 운영자가 합친 태그면 대표 태그 id — 필터에는 안 보임 */
	aliasOf: text('alias_of'),
	gameCount: integer('game_count').notNull().default(0)
});

export const gameTags = sqliteTable(
	'game_tags',
	{
		gameId: text('game_id')
			.notNull()
			.references(() => games.id),
		tagId: text('tag_id')
			.notNull()
			.references(() => tags.id),
		/** 메이커가 적은 순서 */
		position: integer('position').notNull()
	},
	(t) => [
		primaryKey({ columns: [t.gameId, t.tagId] }),
		index('game_tags_by_tag').on(t.tagId, t.gameId)
	]
);

/** 미리보기 미디어 — 이미지 · 영상 합쳐 5개 이상(ADR 0009 #7) */
export const gameMedia = sqliteTable(
	'game_media',
	{
		id: text('id').primaryKey(),
		gameId: text('game_id')
			.notNull()
			.references(() => games.id),
		/** image · video */
		kind: text('kind').notNull(),
		url: text('url').notNull(),
		position: integer('position').notNull()
	},
	(t) => [index('game_media_by_game').on(t.gameId, t.position)]
);
