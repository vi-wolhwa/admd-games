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
				{ phrase: '짧고 굵어요', count: 2 },
				{ phrase: '그림이 예뻐요', count: 1 },
				{ phrase: '안내가 친절해요', count: 1 }
			]
		}}
		params={{ slug }}
		form={undefined}
	/>
	<SiteFooter />
</Story>

<!-- 예외: 아주 긴 제목 · 메이커 이름, 태그 하나, 영상 없음 -->
<Story name="긴 제목 · 긴 메이커 이름" asChild>
	<SiteHeader theme="light" current="games" />
	<Page
		data={{
			...base,
			game: sampleGameDetail('cloud-post-office'),
			similar: sampleSimilar('cloud-post-office'),
			tab: 'about',
			reviewPage: null,
			phrases: null
		}}
		params={{ slug: 'cloud-post-office' }}
		form={undefined}
	/>
	<SiteFooter />
</Story>

<!-- 예외: 리뷰가 하나도 없는 게임의 리뷰 탭 -->
<Story name="리뷰 없음" asChild>
	<SiteHeader theme="light" current="games" />
	<Page
		data={{
			...base,
			game: sampleGameDetail('cloud-post-office'),
			similar: sampleSimilar('cloud-post-office'),
			tab: 'reviews',
			reviewPage: { items: [], nextCursor: null, total: 0 },
			phrases: []
		}}
		params={{ slug: 'cloud-post-office' }}
		form={undefined}
	/>
	<SiteFooter />
</Story>
