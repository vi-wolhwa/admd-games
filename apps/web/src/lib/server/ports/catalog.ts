import type { CatalogQuery } from '#lib/domain/catalog.ts';
import type { GameCardData } from '#lib/domain/game.ts';

/** 전체 게임(PG03) 목록을 읽는 포트. 구현: adapters/d1/catalog.ts */
export interface Catalog {
	/** 공개된 게임을 질의대로. cursor 가 없을 때(첫 묶음)만 total 을 센다 */
	listGames(
		query: CatalogQuery,
		page: { cursor: string | null; limit: number }
	): Promise<CatalogPage>;
	/** 공개 게임이 1개 이상인 태그 전부, 게임 수 많은 순 (ADR 0010) */
	listTags(): Promise<TagCount[]>;
}

export interface CatalogPage {
	items: GameCardData[];
	/** 다음 묶음이 없으면 null */
	nextCursor: string | null;
	total: number | null;
}

export interface TagCount {
	slug: string;
	name: string;
	count: number;
}

/** 가짜 데이터 · 계약 테스트가 저장소에 넣는 게임 한 개 */
export interface GameSeed extends Omit<GameCardData, 'makerName' | 'publishedAt'> {
	maker: { id: string; slug: string; name: string };
	/** 플레이 수 캐시('많이 플레이한' 정렬) — 카드에는 안 보임 */
	playCount: number;
	summary: string;
	status: 'published' | 'review' | 'hidden';
	playersMin: number;
	publishedAt: number | null;
}
