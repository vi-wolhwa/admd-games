import type { GameCardData, GameDetail } from '#lib/domain/game.ts';
import type { ReviewData, ReviewQuery } from '#lib/domain/review.ts';

/** 게임 상세(PG05) — 공개된 게임 하나 + 비슷한 게임. 구현: adapters/d1/game-details.ts */
export interface GameDetails {
	/** 공개된 게임만(심사 중 · 숨김은 null) */
	getGame(slug: string): Promise<GameDetail | null>;
	/** 태그가 많이 겹치는 공개 게임 순(같으면 추천 많은 순), 자기 자신 제외 */
	similarGames(gameId: string, limit: number): Promise<GameCardData[]>;
}

/** 리뷰 읽기. 쓰기 · 도움이 됐어요는 로그인(SH01) 뒤 */
export interface Reviews {
	/** cursor 가 없을 때(첫 묶음)만 total 을 센다 */
	listReviews(
		gameId: string,
		query: ReviewQuery,
		page: { cursor: string | null; limit: number }
	): Promise<{ items: ReviewData[]; nextCursor: string | null; total: number | null }>;
	/** 이 게임 리뷰에서 자주 고른 말, 많은 순 */
	topPhrases(gameId: string, limit: number): Promise<{ phrase: string; count: number }[]>;
}

/** 가짜 데이터 · 계약 테스트용 사람과 리뷰 */
export interface ProfileSeed {
	id: string;
	displayName: string;
	faceChar: string;
	faceColor: string;
}

export interface ReviewSeed {
	id: string;
	gameId: string;
	authorId: string;
	body: string;
	playMinutes: number | null;
	version: string | null;
	createdAt: number;
	updatedAt: number | null;
	phrases: string[];
	/** 글쓴이가 이 게임을 추천했나(recommendations 에 넣음) */
	recommended: boolean;
	reply: { body: string; note: string | null; createdAt: number } | null;
}
