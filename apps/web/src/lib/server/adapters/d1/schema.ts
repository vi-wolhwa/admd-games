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
		/** 소개 · 특징 — 빈 줄로 문단, '- ' 줄은 특징 */
		description: text('description').notNull().default(''),
		/** web · download */
		launch: text('launch').notNull(),
		/** 한 판 길이 구간 1~5 */
		length: integer('length').notNull(),
		pc: integer('pc', { mode: 'boolean' }).notNull().default(true),
		phone: integer('phone', { mode: 'boolean' }).notNull(),
		pad: integer('pad', { mode: 'boolean' }).notNull().default(false),
		/** 쉼표로 구분한 코드(JSON 함수에 기대지 않음): keyboard,mouse,touch,gamepad */
		controls: text('controls').notNull().default(''),
		/** 쉼표로 구분한 언어 코드: ko,en */
		languages: text('languages').notNull().default(''),
		/** 쉼표로 구분: violence,horror,flashing,loud — 빈 문자열 = 없음 */
		cautions: text('cautions').notNull().default(''),
		/** 최소 사양(설치형만) */
		minSpec: text('min_spec'),
		/** 온라인 — 다른 사람과 인터넷으로 함께함(멀티플레이 · 순위). false = 오프라인 */
		online: integer('online', { mode: 'boolean' }).notNull().default(false),
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

/**
 * 사람 프로필(이 앱이 가진 것). 로그인(better-auth, SH01)의 사용자와 같은 id 를 쓴다 — 인증 라이브러리를 바꿔도 남는다.
 * 얼굴 = 자모 얼굴(글자 + 12색 중 하나).
 */
export const profiles = sqliteTable('profiles', {
	id: text('id').primaryKey(),
	displayName: text('display_name').notNull(),
	faceChar: text('face_char').notNull(),
	faceColor: text('face_color').notNull(),
	/** 쓴 리뷰 수 캐시 */
	reviewCount: integer('review_count').notNull().default(0),
	createdAt: integer('created_at').notNull()
});

/** 추천 — 계정당 게임당 한 번(ADR 0009 · 0011). 개수는 games.recommend_count 캐시 */
export const recommendations = sqliteTable(
	'recommendations',
	{
		gameId: text('game_id')
			.notNull()
			.references(() => games.id),
		userId: text('user_id')
			.notNull()
			.references(() => profiles.id),
		createdAt: integer('created_at').notNull()
	},
	(t) => [primaryKey({ columns: [t.gameId, t.userId] })]
);

/** 리뷰 — 찬반 열 없음(ADR 0009). 정렬마다 (game_id, 정렬 열, created_at, id) 색인 */
export const reviews = sqliteTable(
	'reviews',
	{
		id: text('id').primaryKey(),
		gameId: text('game_id')
			.notNull()
			.references(() => games.id),
		authorId: text('author_id')
			.notNull()
			.references(() => profiles.id),
		body: text('body').notNull(),
		/** 쓸 때까지 플레이한 분 — 기록 없으면 null */
		playMinutes: integer('play_minutes'),
		/** 쓸 때 버전 */
		version: text('version'),
		/** 쓰지 않음(도움이 됐어요를 없앰, 2026-11-28) — 이관은 더하기만이라 다음 정리 때 지운다 */
		helpfulCount: integer('helpful_count').notNull().default(0),
		createdAt: integer('created_at').notNull(),
		/** 고쳐 쓴 시각 — 있으면 '수정' */
		updatedAt: integer('updated_at')
	},
	(t) => [
		index('reviews_by_helpful').on(t.gameId, t.helpfulCount, t.createdAt, t.id),
		index('reviews_by_recent').on(t.gameId, t.createdAt, t.id),
		index('reviews_by_played').on(t.gameId, t.playMinutes, t.createdAt, t.id)
	]
);

/** 리뷰에 글쓴이가 고른 말 */
export const reviewPhrases = sqliteTable(
	'review_phrases',
	{
		reviewId: text('review_id')
			.notNull()
			.references(() => reviews.id),
		phrase: text('phrase').notNull(),
		position: integer('position').notNull()
	},
	(t) => [
		primaryKey({ columns: [t.reviewId, t.phrase] }),
		index('review_phrases_by_phrase').on(t.phrase, t.reviewId)
	]
);

/** 메이커 답글 — 리뷰 하나에 하나 */
export const reviewReplies = sqliteTable('review_replies', {
	reviewId: text('review_id')
		.primaryKey()
		.references(() => reviews.id),
	body: text('body').notNull(),
	/** 예: 'v1.2 에서 고침' */
	note: text('note'),
	createdAt: integer('created_at').notNull()
});
