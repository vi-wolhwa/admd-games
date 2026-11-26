<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';

	import { DEFAULT_REVIEW_QUERY } from '#lib/domain/review.ts';
	import { sampleGameDetail, sampleReviewData, sampleSimilar } from '#lib/fixtures/game-page.ts';
	import { STORY_NOW } from '#lib/fixtures/games.ts';
	import SiteFooter from '#lib/ui/widgets/SiteFooter.svelte';
	import SiteHeader from '#lib/ui/widgets/SiteHeader.svelte';

	import Page from './+page.svelte';

	// 페이지 전체(헤더 + PG05 + 바닥글)를 가짜 데이터로 — 소개 탭 · 리뷰 탭
	const slug = 'loop-debugger';
	const base = {
		theme: 'light' as const,
		game: sampleGameDetail(slug),
		similar: sampleSimilar(slug),
		reviewQuery: DEFAULT_REVIEW_QUERY,
		device: 'pc' as const,
		now: STORY_NOW
	};
	const reviews = sampleReviewData(slug);

	const { Story } = defineMeta({
		title: 'Pages/PG05 게임 상세',
		component: Page,
		parameters: { layout: 'fullscreen' }
	});
</script>

<Story name="소개" asChild>
	<SiteHeader theme="light" current="games" />
	<Page
		data={{ ...base, tab: 'about', reviewPage: null, phrases: null }}
		params={{ slug }}
		form={undefined}
	/>
	<SiteFooter />
</Story>

<Story name="리뷰" asChild>
	<SiteHeader theme="light" current="games" />
	<Page
		data={{
			...base,
			tab: 'reviews',
			reviewPage: { items: reviews, nextCursor: null, total: reviews.length },
			phrases: [
				{ phrase: '짧고 굵음', count: 2 },
				{ phrase: '튜토리얼이 길어요', count: 1 },
				{ phrase: '힌트가 친절해요', count: 1 }
			]
		}}
		params={{ slug }}
		form={undefined}
	/>
	<SiteFooter />
</Story>
