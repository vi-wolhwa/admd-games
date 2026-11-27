import { expect, it } from 'vitest';

import { REVIEW_SORTS, type ReviewSort } from '#lib/domain/review.ts';

import type { GameSeed } from './catalog';
import { CONTRACT_GAMES } from './catalog.contract';
import type { GameDetails, ProfileSeed, Reviews, ReviewSeed } from './game-details';

/**
 * 계약 테스트: 게임 상세 · 리뷰 어댑터가 통과해야 하는 동작.
 * makeStore 는 주어진 게임 · 사람 · 리뷰를 넣은 저장소를 만들어 돌려준다.
 */
const DAY = 86_400_000;
const NOW = 100 * DAY;

const GAMES: GameSeed[] = CONTRACT_GAMES.map((g) =>
	g.id === 'g1'
		? {
				...g,
				summary: '모든 방이 하나의 함수인 퍼즐',
				detail: {
					description: '첫 문단\n\n- 특징 하나',
					devices: ['pc', 'phone'],
					online: true,
					languages: ['ko', 'en'],
					minSpec: null
				}
			}
		: g
);

const PROFILES: ProfileSeed[] = [
	{ id: 'p1', displayName: '새벽코딩', faceChar: 'ㅅ', faceColor: 'hong' },
	{ id: 'p2', displayName: '모래시계', faceChar: 'ㅁ', faceColor: 'bora' },
	{ id: 'p3', displayName: '귤껍질', faceChar: 'ㄱ', faceColor: 'gyul' },
	// 메이커스 프로필(m1 = 노을공방)을 가진 사람
	{ id: 'pm1', displayName: '노을공방', faceChar: 'ㄴ', faceColor: 'olive', makerId: 'm1' }
];

function review(id: string, o: Partial<ReviewSeed>): ReviewSeed {
	return {
		id,
		gameId: 'g1',
		authorId: 'p1',
		body: `리뷰 ${id}`,
		playMinutes: null,
		version: 'v1.1',
		createdAt: NOW,
		updatedAt: null,
		phrases: [],
		recommended: false,
		replies: [],
		...o
	};
}

const REVIEWS: ReviewSeed[] = [
	review('r1', {
		createdAt: NOW - 10 * DAY,
		updatedAt: NOW - 8 * DAY,
		playMinutes: 66,
		phrases: ['짧고 굵어요', '안내가 친절해요'],
		recommended: true,
		replies: [
			{
				id: 'x1',
				authorId: 'pm1',
				body: '@새벽코딩님 고마워요!',
				createdAt: NOW - 9 * DAY,
				updatedAt: null
			},
			{
				id: 'x2',
				authorId: 'p2',
				body: '@노을공방 저도 기다려요 @없는사람',
				createdAt: NOW - 8 * DAY,
				updatedAt: NOW - 7 * DAY
			}
		]
	}),
	review('r2', { authorId: 'p2', createdAt: NOW - 12 * DAY, playMinutes: 66 }),
	// 같은 사람이 같은 게임에 쓴 리뷰는 버전이 달라야 함(버전마다 하나)
	review('r3', { createdAt: NOW - 20 * DAY, playMinutes: 300, version: 'v1.0' }),
	review('r4', { authorId: 'p3', createdAt: NOW - 5 * DAY, version: 'v1.0' }),
	review('r5', {
		authorId: 'p3',
		createdAt: NOW - 3 * DAY,
		playMinutes: 30,
		phrases: ['짧고 굵어요']
	}),
	review('r6', { gameId: 'g2' })
];

export function runGameDetailsContract(
	makeStore: (
		games: GameSeed[],
		profiles: ProfileSeed[],
		reviews: ReviewSeed[]
	) => Promise<{ details: GameDetails; reviews: Reviews }>
) {
	const make = () => makeStore(GAMES, PROFILES, REVIEWS);

	it('공개된 게임만 상세를 돌려준다 — 소개 · 플레이 정보 · 메이커의 공개 게임 수 포함', async () => {
		const { details } = await make();
		const g1 = await details.getGame('g1');
		expect(g1).toMatchObject({
			id: 'g1',
			title: '게임 g1',
			summary: '모든 방이 하나의 함수인 퍼즐',
			description: '첫 문단\n\n- 특징 하나',
			makerName: '노을공방',
			slug: 'g1',
			makerSlug: 'maker-1',
			makerGameCount: 4,
			devices: ['pc', 'phone'],
			online: true,
			languages: ['ko', 'en'],
			minSpec: null,
			tags: ['퍼즐', '액션'],
			playersMin: 1
		});
		expect(g1?.media).toHaveLength(5);
		expect(await details.getGame('g5')).toBeNull();
		expect(await details.getGame('없는-게임')).toBeNull();
	});

	it('비슷한 게임 = 태그가 겹치는 공개 게임, 추천 많은 순, 자기 자신 · 심사 중 제외', async () => {
		const { details } = await make();
		const similar = await details.similarGames('g1', 5);
		expect(similar.map((g) => g.id)).toEqual(['g2', 'g3', 'g6']);
		expect(similar[0]?.media).toHaveLength(5);
		expect((await details.similarGames('g1', 2)).map((g) => g.id)).toEqual(['g2', 'g3']);
	});

	const ids = async (r: Reviews, sort: ReviewSort, phrase: string | null = null) =>
		(await r.listReviews('g1', { sort, phrase }, { cursor: null, limit: 50 })).items.map(
			(x) => x.id
		);

	it('리뷰는 그 게임 것만, 정렬마다 정해진 순서(같으면 최신 → id)', async () => {
		const { reviews } = await make();
		expect(await ids(reviews, 'recent')).toEqual(['r5', 'r4', 'r1', 'r2', 'r3']);
		// 플레이 기록이 없는 리뷰는 '고인물 순'에서 맨 뒤
		expect(await ids(reviews, 'played')).toEqual(['r3', 'r1', 'r2', 'r5', 'r4']);
		expect(await ids(reviews, 'recent', '짧고 굵어요')).toEqual(['r5', 'r1']);
	});

	it('커서로 이어 불러오면 겹치지도 빠지지도 않는다', async () => {
		const { reviews } = await make();
		for (const sort of REVIEW_SORTS) {
			const seen: string[] = [];
			let cursor: string | null = null;
			let pages = 0;
			do {
				const page = await reviews.listReviews('g1', { sort, phrase: null }, { cursor, limit: 2 });
				expect(page.total).toBe(pages === 0 ? 5 : null);
				seen.push(...page.items.map((x) => x.id));
				cursor = page.nextCursor;
				pages++;
			} while (cursor && pages < 10);
			expect(seen).toEqual(await ids(reviews, sort));
		}
	});

	it('리뷰 한 개에 글쓴이 · 추천함 · 키워드 · 수정 시각 · 답글을 담는다', async () => {
		const { reviews } = await make();
		const { items } = await reviews.listReviews(
			'g1',
			{ sort: 'recent', phrase: '안내가 친절해요' },
			{ cursor: null, limit: 1 }
		);
		expect(items[0]).toEqual({
			id: 'r1',
			// 리뷰 수는 이 사람이 쓴 전체(g2 의 r6 포함)
			author: {
				name: '새벽코딩',
				faceChar: 'ㅅ',
				faceColor: 'hong',
				makerSlug: null,
				reviewCount: 3
			},
			recommended: true,
			playMinutes: 66,
			version: 'v1.1',
			createdAt: NOW - 10 * DAY,
			updatedAt: NOW - 8 * DAY,
			phrases: ['짧고 굵어요', '안내가 친절해요'],
			body: '리뷰 r1',
			replies: [
				{
					id: 'x1',
					// 이 게임 메이커의 답글 — 프로필 주소 있음
					author: { name: '노을공방', faceChar: 'ㄴ', faceColor: 'olive', makerSlug: 'maker-1' },
					byGameMaker: true,
					body: '@새벽코딩님 고마워요!',
					createdAt: NOW - 9 * DAY,
					updatedAt: null,
					// 아는 닉네임이면 그 사람(얼굴 · 메이커스 프로필 — 없으면 null)
					mentions: {
						새벽코딩: { name: '새벽코딩', faceChar: 'ㅅ', faceColor: 'hong', makerSlug: null }
					}
				},
				{
					id: 'x2',
					author: { name: '모래시계', faceChar: 'ㅁ', faceColor: 'bora', makerSlug: null },
					byGameMaker: false,
					body: '@노을공방 저도 기다려요 @없는사람',
					createdAt: NOW - 8 * DAY,
					updatedAt: NOW - 7 * DAY,
					// 모르는 이름(@없는사람)은 멘션이 아님
					mentions: {
						노을공방: { name: '노을공방', faceChar: 'ㄴ', faceColor: 'olive', makerSlug: 'maker-1' }
					}
				}
			]
		});
	});

	it('메이커스 프로필 = 이름 + 공개 게임(추천 많은 순), 없으면 null', async () => {
		const { details } = await make();
		const p = await details.makerProfile('maker-1');
		expect(p?.name).toBe('노을공방');
		expect(p?.games.map((g) => g.id)).toEqual(['g2', 'g1', 'g3', 'g6']);
		expect(await details.makerProfile('없는-메이커')).toBeNull();
	});

	it('자주 고른 말은 많은 순', async () => {
		const { reviews } = await make();
		expect(await reviews.topPhrases('g1', 10)).toEqual([
			{ phrase: '짧고 굵어요', count: 2 },
			{ phrase: '안내가 친절해요', count: 1 }
		]);
	});
}
