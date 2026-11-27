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

	// 답글 4개(3개만 보이고 '더 보기') · 메이커 답글 · 프로필 있는 멘션(링크) · 없는 멘션(파란 글씨만)
	const threads = [
		...sampleReviewData('loop-debugger').filter((r) => r.replies.length > 3),
		...paper.filter((r) => Object.values(r.replies.at(-1)?.mentions ?? {}).some(Boolean))
	];

	const { Story } = defineMeta({ title: 'Entities/Review/ReviewItem', component: ReviewItem });
</script>

<Story
	name="긴 글 · 수정 · 기록 없음"
	asChild
	play={async ({ canvas, userEvent }) => {
		// 긴 리뷰는 세 줄로 접고, 잘린 마지막 줄 끝의 '더 보기'로 전체를 편다
		const more = await canvas.findByRole('button', { name: '더 보기' });
		await userEvent.click(more);
		await expect(canvas.queryByRole('button', { name: '더 보기' })).toBeNull();
		await expect(canvas.getByText(/수정/, { selector: 'time' })).toBeVisible();
		await expect(canvas.getByText('플레이 기록 없음')).toBeVisible();
	}}
>
	<div class="w-180">
		{#each reviews as review (review.id)}
			<ReviewItem
				{review}
				now={STORY_NOW}
				profileHref={(slug: string) => `#${slug}`}
				onreplyto={fn()}
				onreport={fn()}
			/>
		{/each}
	</div>
</Story>

<Story
	name="답글 · 멘션"
	asChild
	play={async ({ canvas, userEvent }) => {
		// 답글이 넷 이상이면 셋만 보이고 나머지는 '답글 n개 더 보기'
		await userEvent.click(await canvas.findByRole('button', { name: '답글 1개 더 보기' }));
		await expect(canvas.queryByRole('button', { name: /개 더 보기/ })).toBeNull();
		await expect(canvas.getAllByText('메이커').length).toBeGreaterThan(0);
		// 메이커스 프로필이 있는 멘션만 링크
		await expect(canvas.getByRole('link', { name: '@벡터공방' })).toHaveAttribute(
			'href',
			'#vector-studio'
		);
	}}
>
	<div class="w-180">
		{#each threads as review (review.id)}
			<ReviewItem
				{review}
				now={STORY_NOW}
				profileHref={(slug: string) => `#${slug}`}
				onreplyto={fn()}
				onreport={fn()}
			/>
		{/each}
	</div>
</Story>
