<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect } from 'storybook/test';

	import { sampleReviewData } from '#lib/fixtures/game-page.ts';
	import { STORY_NOW } from '#lib/fixtures/games.ts';

	import ReviewItem from './ReviewItem.svelte';

	// 긴 글 + 메이커 답글 + 추천함 / 짧은 글 · 고른 말 없음
	const reviews = sampleReviewData('loop-debugger');

	const { Story } = defineMeta({ title: 'Entities/Review/ReviewItem', component: ReviewItem });
</script>

<Story
	name="긴 글 · 답글"
	asChild
	play={async ({ canvas, userEvent }) => {
		// 긴 리뷰는 세 줄로 접고 '더 보기' 로 펼친다
		const more = await canvas.findByRole('button', { name: '더 보기' });
		await userEvent.click(more);
		await expect(canvas.getByRole('button', { name: '접기' })).toHaveAttribute(
			'aria-expanded',
			'true'
		);
		await userEvent.click(canvas.getByRole('button', { name: '접기' }));
	}}
>
	<div class="w-180">
		{#each reviews as review (review.id)}
			<ReviewItem {review} makerName="픽셀상점" now={STORY_NOW} />
		{/each}
	</div>
</Story>
