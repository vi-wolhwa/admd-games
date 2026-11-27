<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn } from 'storybook/test';

	import ReviewForm from './ReviewForm.svelte';

	const onsubmit = fn();

	// 키워드 1개 이상 + 글이 있어야 올릴 수 있다(네이버 방식, 빈 리뷰 금지). 올리기를 누르면 로그인 안내(SH01 전까지 — Features/Auth)
	const { Story } = defineMeta({ title: 'Features/Review/ReviewForm', component: ReviewForm });
</script>

<Story
	name="키워드 · 글 필수"
	asChild
	play={async ({ canvas, userEvent }) => {
		// 키워드 1개 이상 → 글 → 둘 다 채워야 '리뷰 올리기'가 켜진다(빈 리뷰 금지)
		const send = canvas.getByRole('button', { name: '리뷰 올리기' });
		await expect(send).toBeDisabled();
		await expect(canvas.getByText('키워드를 1개 이상 골라 주세요')).toBeVisible();
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
	<div class="w-180"><ReviewForm {onsubmit} oncancel={fn()} /></div>
</Story>
