import { expect, it } from 'vitest';

import { type CatalogQuery, DEFAULT_QUERY, SORTS } from '#lib/domain/catalog.ts';
import type { LengthBucket } from '#lib/domain/game.ts';

import type { Catalog, GameSeed } from './catalog';

/**
 * 계약 테스트: 모든 Catalog 어댑터가 통과해야 하는 동작.
 * makeCatalog 는 주어진 게임을 넣은 저장소를 만들어 돌려준다.
 */
const DAY = 86_400_000;

function game(
	id: string,
	o: Partial<GameSeed> & { tags: string[]; recommendCount: number; length: LengthBucket }
): GameSeed {
	return {
		id,
		slug: id,
		title: `게임 ${id}`,
		summary: '한 줄 소개',
		maker: { id: 'm1', slug: 'maker-1', name: '노을공방' },
		status: 'published',
		launch: 'web',
		phone: false,
		playersMin: 1,
		playersMax: 1,
		scanPassed: false,
		cover: `/art/${id}.svg`,
		media: [1, 2, 3, 4, 5].map((n) => ({
			kind: 'image' as const,
			url: `/art/${id}-${String(n)}.svg`
		})),
		reviewCount: 0,
		playCount: 0,
		publishedAt: 100 * DAY,
		...o
	};
}

export const CONTRACT_GAMES: GameSeed[] = [
	game('g1', {
		tags: ['퍼즐', '액션'],
		recommendCount: 50,
		reviewCount: 3,
		playCount: 100,
		length: 1,
		publishedAt: 10 * DAY,
		phone: true
	}),
	game('g2', {
		tags: ['퍼즐'],
		recommendCount: 50,
		reviewCount: 9,
		length: 2,
		publishedAt: 20 * DAY,
		playersMax: 4
	}),
	game('g3', {
		tags: ['액션'],
		recommendCount: 10,
		reviewCount: 9,
		playCount: 100,
		length: 3,
		publishedAt: 30 * DAY,
		launch: 'download',
		scanPassed: true
	}),
	game('g4', {
		tags: ['이야기'],
		recommendCount: 5,
		reviewCount: 1,
		playCount: 7,
		length: 5,
		publishedAt: 40 * DAY,
		launch: 'download',
		maker: { id: 'm2', slug: 'maker-2', name: '픽셀상점' }
	}),
	game('g5', {
		tags: ['퍼즐', '심사중태그'],
		recommendCount: 999,
		length: 1,
		status: 'review',
		publishedAt: null
	}),
	game('g6', {
		tags: ['퍼즐'],
		recommendCount: 0,
		length: 1,
		publishedAt: 5 * DAY,
		playersMin: 2,
		playersMax: 2
	})
];

export function runCatalogContract(makeCatalog: (games: GameSeed[]) => Promise<Catalog>) {
	const ids = async (catalog: Catalog, q: Partial<CatalogQuery>) =>
		(
			await catalog.listGames(
				{ ...DEFAULT_QUERY, sort: 'recommended', ...q },
				{ cursor: null, limit: 50 }
			)
		).items.map((g) => g.id);

	it('공개된 게임만, 정렬마다 정해진 순서(같은 값이면 id 역순)', async () => {
		const catalog = await makeCatalog(CONTRACT_GAMES);
		const first = await catalog.listGames(
			{ ...DEFAULT_QUERY, sort: 'recommended' },
			{ cursor: null, limit: 50 }
		);
		expect(first.items.map((g) => g.id)).toEqual(['g2', 'g1', 'g3', 'g4', 'g6']);
		expect(first.total).toBe(5);
		expect(await ids(catalog, { sort: 'new' })).toEqual(['g4', 'g3', 'g2', 'g1', 'g6']);
		expect(await ids(catalog, { sort: 'reviews' })).toEqual(['g3', 'g2', 'g1', 'g4', 'g6']);
		// 플레이 수가 같으면 추천 수 → id (플레이 기록이 없는 동안은 추천 순과 같아진다)
		expect(await ids(catalog, { sort: 'played' })).toEqual(['g1', 'g3', 'g4', 'g2', 'g6']);
	});

	it('태그를 여러 개 고르면 하나라도 해당, 다른 필터와는 모두 해당', async () => {
		const catalog = await makeCatalog(CONTRACT_GAMES);
		expect(await ids(catalog, { tags: ['액션', '이야기'] })).toEqual(['g1', 'g3', 'g4']);
		expect(await ids(catalog, { tags: ['퍼즐'], length: 1 })).toEqual(['g1', 'g6']);
		expect(await ids(catalog, { length: 2 })).toEqual(['g2', 'g1', 'g6']);
		expect(await ids(catalog, { length: 5 })).toEqual(['g4']);
		expect(await ids(catalog, { launch: 'download' })).toEqual(['g3', 'g4']);
		expect(await ids(catalog, { players: 'solo' })).toEqual(['g2', 'g1', 'g3', 'g4']);
		expect(await ids(catalog, { players: 'group' })).toEqual(['g2', 'g6']);
		expect(await ids(catalog, { tags: ['없는태그'] })).toEqual([]);
	});

	it('검색어는 제목 · 메이커 이름에서 찾고, 다른 필터와 함께 걸린다', async () => {
		const catalog = await makeCatalog(CONTRACT_GAMES);
		expect(await ids(catalog, { q: '픽셀' })).toEqual(['g4']);
		expect(await ids(catalog, { q: 'g2' })).toEqual(['g2']);
		expect(await ids(catalog, { q: '게임', tags: ['액션'] })).toEqual(['g1', 'g3']);
		// 공백은 검색어 · 제목 양쪽에서 무시('게임 g1' 을 '게임g1' · '게 임 g 1' 로도)
		expect(await ids(catalog, { q: '게임g1' })).toEqual(['g1']);
		expect(await ids(catalog, { q: '게 임 g 1' })).toEqual(['g1']);
		// 끝의 조합되지 않은 자모는 빼고 찾는다
		expect(await ids(catalog, { q: '픽셀ㅅ' })).toEqual(['g4']);
		// LIKE 의 특수 문자는 글자 그대로
		expect(await ids(catalog, { q: '%' })).toEqual([]);
		expect(await ids(catalog, { q: '_' })).toEqual([]);
	});

	it('커서로 이어 불러오면 겹치지도 빠지지도 않고, 끝에서 멈춘다', async () => {
		const catalog = await makeCatalog(CONTRACT_GAMES);
		for (const sort of SORTS) {
			const query = { ...DEFAULT_QUERY, sort };
			const seen: string[] = [];
			let cursor: string | null = null;
			let pages = 0;
			do {
				const page = await catalog.listGames(query, { cursor, limit: 2 });
				expect(page.total).toBe(pages === 0 ? 5 : null);
				seen.push(...page.items.map((g) => g.id));
				cursor = page.nextCursor;
				pages++;
			} while (cursor && pages < 10);
			expect(seen).toEqual(await ids(catalog, { sort }));
			expect(pages).toBe(3);
		}
	});

	it('카드에 필요한 정보를 그대로 돌려준다(태그 · 미디어 순서 포함)', async () => {
		const catalog = await makeCatalog(CONTRACT_GAMES);
		const { items } = await catalog.listGames(
			{ ...DEFAULT_QUERY, tags: ['이야기'] },
			{ cursor: null, limit: 5 }
		);
		const g4 = CONTRACT_GAMES[3];
		expect(items[0]).toEqual({
			id: 'g4',
			slug: 'g4',
			title: '게임 g4',
			makerName: '픽셀상점',
			tags: ['이야기'],
			length: 5,
			launch: 'download',
			phone: false,
			playersMax: 1,
			scanPassed: false,
			cover: '/art/g4.svg',
			media: g4?.media,
			recommendCount: 5,
			reviewCount: 1,
			publishedAt: 40 * DAY
		});
		const { items: g1 } = await catalog.listGames(
			{ ...DEFAULT_QUERY, length: 1, tags: ['액션'] },
			{ cursor: null, limit: 5 }
		);
		expect(g1[0]?.tags).toEqual(['퍼즐', '액션']);
	});

	it('태그 목록은 공개 게임이 있는 것만, 게임 수 많은 순', async () => {
		const catalog = await makeCatalog(CONTRACT_GAMES);
		expect(await catalog.listTags()).toEqual([
			{ slug: '퍼즐', name: '퍼즐', count: 3 },
			{ slug: '액션', name: '액션', count: 2 },
			{ slug: '이야기', name: '이야기', count: 1 }
		]);
	});
}
