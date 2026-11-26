<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';

	import { DEFAULT_QUERY } from '#lib/domain/catalog.ts';
	import { tagSlug } from '#lib/domain/game.ts';
	import { sampleCards, sampleGames, STORY_NOW } from '#lib/fixtures/games.ts';
	import SiteFooter from '#lib/ui/widgets/SiteFooter.svelte';
	import SiteHeader from '#lib/ui/widgets/SiteHeader.svelte';

	import Page from './+page.svelte';

	// 페이지 전체(헤더 + PG03 + 바닥글)를 가짜 데이터로. 첫 묶음 12개, 이어 불러오기는 끝난 상태
	const games = sampleCards()
		.toSorted((a, b) => b.recommendCount - a.recommendCount)
		.slice(0, 12);
	const counts: Record<string, number> = {};
	for (const g of sampleGames()) for (const t of g.tags) counts[t] = (counts[t] ?? 0) + 1;
	const tags = Object.entries(counts)
		.map(([name, count]) => ({ slug: tagSlug(name), name, count }))
		.toSorted((a, b) => b.count - a.count || a.name.localeCompare(b.name, 'ko'));

	const data = {
		theme: 'light' as const,
		query: DEFAULT_QUERY,
		tags,
		games,
		nextCursor: null,
		total: games.length,
		now: STORY_NOW
	};

	const { Story } = defineMeta({
		title: 'Pages/PG03 전체 게임',
		component: Page,
		parameters: { layout: 'fullscreen' }
	});
</script>

<Story name="기본" asChild>
	<SiteHeader theme="light" current="games" />
	<Page {data} params={{}} form={undefined} />
	<SiteFooter />
</Story>

<Story name="검색 결과 없음" asChild>
	<SiteHeader theme="light" current="games" />
	<Page
		data={{
			...data,
			query: { ...DEFAULT_QUERY, q: '없는 게임', tags: ['퍼즐'] },
			games: [],
			total: 0
		}}
		params={{}}
		form={undefined}
	/>
	<SiteFooter />
</Story>
