<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn } from 'storybook/test';

	import { sampleReviewData } from '#lib/fixtures/game-page.ts';
	import { STORY_NOW } from '#lib/fixtures/games.ts';

	import ReviewItem from './ReviewItem.svelte';

	// 예외 사례 모음: 아주 긴 글(접힘) · 고쳐 쓴 리뷰 + 메이커 답글 · 플레이 기록 없음 · 짧은 글
	const cat = sampleReviewData('cat-mail');
	const paper = sampleReviewData('paper-vector');
	const reviews = [
		...cat.filter((r) => r.body.length > 300).slice(0, 1),
		...paper.filter((r) => r.updatedAt !== null).slice(0, 1),
		...sampleReviewData('tilt-theory').slice(0, 1),
		...paper.filter((r) => r.body.length < 30).slice(0, 1)
	];

	const { Story } = defineMeta({ title: 'Entities/Review/ReviewItem', component: ReviewItem });
</script>

<Story
	name="긴 글 · 수정 · 기록 없음"
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
		await expect(canvas.getByText(/수정/, { selector: 'time' })).toBeVisible();
		await expect(canvas.getByText('플레이 기록 없음')).toBeVisible();
	}}
>
	<div class="w-180">
		{#each reviews as review (review.id)}
			<ReviewItem {review} makerName="노을공방" now={STORY_NOW} onreply={fn()} onreport={fn()} />
		{/each}
	</div>
</Story>
