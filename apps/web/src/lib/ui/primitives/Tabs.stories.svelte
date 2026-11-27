<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn } from 'storybook/test';

	import JamoFace from './JamoFace.svelte';
	import Segmented from './Segmented.svelte';
	import Tabs from './Tabs.svelte';

	const ontab = fn();
	const onsort = fn();
	const FACES = [
		'hong',
		'ju',
		'gyul',
		'hwang',
		'olive',
		'pul',
		'bichwi',
		'cheongnok',
		'haneul',
		'jjok',
		'bora',
		'jadu'
	];

	// 고르는 막대 두 가지(탭 · 정렬)와 사람 얼굴 — 모두 PG05 에서 처음 쓴다
	const { Story } = defineMeta({
		title: 'Primitives/Tabs · Segmented · JamoFace',
		component: Tabs
	});
</script>

<Story
	name="탭 · 정렬 · 얼굴"
	asChild
	play={async ({ canvas, userEvent }) => {
		// 화살표로 옮기면 바로 고른다
		canvas.getByRole('tab', { name: '소개' }).focus();
		await userEvent.keyboard('{ArrowRight}');
		await expect(ontab).toHaveBeenCalledWith('reviews');
		await userEvent.click(canvas.getByRole('radio', { name: '최신 순' }));
		await expect(onsort).toHaveBeenCalledWith('recent');
		canvas.getByRole('radio', { name: '최신 순' }).blur();
	}}
>
	<div class="flex w-150 flex-col gap-6">
		<div class="border-b border-line-strong">
			<Tabs
				label="게임 내용"
				idPrefix="story"
				value="about"
				items={[
					{ value: 'about', label: '소개' },
					{ value: 'reviews', label: '리뷰', count: 38 }
				]}
				onchange={ontab}
			/>
		</div>
		<div
			id="story-panel"
			role="tabpanel"
			aria-labelledby="story-tab-about"
			class="text-label text-ink-3"
		>
			소개 내용
		</div>
		<Segmented
			label="리뷰 정렬"
			value="helpful"
			items={[
				{ value: 'helpful', label: '도움 많은' },
				{ value: 'recent', label: '최신 순' },
				{ value: 'played', label: '고인물 순' }
			]}
			onchange={onsort}
		/>
		<div class="flex flex-wrap items-center gap-2">
			<JamoFace char="ㅅ" color="hong" size="lg" />
			<JamoFace char="ㅁ" color="bora" size="md" />
			{#each FACES as c (c)}<JamoFace char="ㅇ" color={c} size="sm" />{/each}
		</div>
	</div>
</Story>
