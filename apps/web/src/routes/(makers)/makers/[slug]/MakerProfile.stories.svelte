<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';

	import { sampleCards, STORY_NOW } from '#lib/fixtures/games.ts';
	import SiteFooter from '#lib/ui/widgets/SiteFooter.svelte';
	import SiteHeader from '#lib/ui/widgets/SiteHeader.svelte';

	import Page from './+page.svelte';

	// 메이커스 프로필(최소) — 게임 여럿인 메이커 · 아주 긴 이름에 게임 하나(예외)
	const cards = sampleCards();
	const profileOf = (name: string) => ({
		slug: 'story',
		name,
		games: cards.filter((c) => c.makerName === name)
	});

	const { Story } = defineMeta({
		title: 'Pages/메이커스 프로필',
		component: Page,
		parameters: { layout: 'fullscreen' }
	});
</script>

<Story name="기본" asChild>
	<SiteHeader theme="light" ground="make" />
	<Page
		data={{ theme: 'light', profile: profileOf('벡터공방'), now: STORY_NOW }}
		params={{ slug: 'story' }}
		form={undefined}
	/>
	<SiteFooter />
</Story>

<Story name="긴 이름 · 게임 하나" asChild>
	<SiteHeader theme="light" ground="make" />
	<Page
		data={{ theme: 'light', profile: profileOf('새벽세시에만문을여는작은공방'), now: STORY_NOW }}
		params={{ slug: 'story' }}
		form={undefined}
	/>
	<SiteFooter />
</Story>
