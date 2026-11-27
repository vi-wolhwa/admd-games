<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn, waitFor } from 'storybook/test';

	import ReviewForm from './ReviewForm.svelte';

	const onsubmit = fn();

	// 닫힌 한 줄 → 누르면 펼쳐짐. 키워드는 성격별 묶음에서 1~5개 + 글이 있어야 올릴 수 있다(빈 리뷰 금지).
	// 올리기를 누르면 로그인 안내(SH01 전까지 — Features/Auth)
	const { Story } = defineMeta({ title: 'Features/Review/ReviewForm', component: ReviewForm });
</script>

<Story
	name="펼치기 · 키워드 · 글 필수"
	asChild
	play={async ({ canvas, userEvent }) => {
		await userEvent.click(canvas.getByRole('button', { name: /어떤 점이 좋았나요/ }));
		const send = await canvas.findByRole('button', { name: '리뷰 올리기' });
		await expect(send).toBeDisabled();
		// 펼치는 움직임이 끝날 때까지 기다린다(느린 CI 에서는 도중에 보이지 않음)
		await waitFor(() => expect(canvas.getByText('키워드를 1개 이상 골라 주세요')).toBeVisible());
		await userEvent.click(canvas.getByRole('button', { name: '짧고 굵음' }));
		await expect(send).toBeDisabled();
		await expect(canvas.getByText('리뷰를 작성해 주세요')).toBeVisible();
		await userEvent.type(canvas.getByRole('textbox', { name: /^리뷰/ }), '  짧은데 손에 남아요  ');
		await expect(send).toBeEnabled();
		await userEvent.click(send);
		await expect(onsubmit).toHaveBeenCalledWith({
			keywords: ['짧고 굵음'],
			body: '짧은데 손에 남아요'
		});
		send.blur();
	}}
>
	<div class="w-180"><ReviewForm {onsubmit} /></div>
</Story>

<!-- 예외: 5개를 고르면 나머지 키워드는 눌리지 않음 -->
<Story
	name="키워드 5개 가득"
	asChild
	play={async ({ canvas, userEvent }) => {
		for (const k of [
			'짧고 굵음',
			'오래 붙잡게 돼요',
			'그림이 예뻐요',
			'음악이 좋아요',
			'한 손으로'
		]) {
			await userEvent.click(canvas.getByRole('button', { name: k }));
		}
		await expect(canvas.getByText('5 / 5개')).toBeVisible();
		await expect(canvas.getByRole('button', { name: '조작이 편해요' })).toBeDisabled();
		const last = canvas.getByRole('button', { name: '한 손으로' });
		await expect(last).toBeEnabled();
		last.blur();
	}}
>
	<div class="w-180"><ReviewForm onsubmit={fn()} initiallyOpen /></div>
</Story>
