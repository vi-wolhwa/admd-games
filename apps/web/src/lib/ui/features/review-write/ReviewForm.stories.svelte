<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn } from 'storybook/test';

	import ReviewForm from './ReviewForm.svelte';

	const onsubmit = fn();

	// 키워드를 1개 이상 골라야 올릴 수 있다(네이버 방식). 올리기를 누르면 로그인 안내(SH01 전까지 — Features/Auth)
	const { Story } = defineMeta({ title: 'Features/Review/ReviewForm', component: ReviewForm });
</script>

<Story
	name="키워드 필수"
	asChild
	play={async ({ canvas, userEvent }) => {
		const send = canvas.getByRole('button', { name: '리뷰 올리기' });
		await expect(send).toBeDisabled();
		await userEvent.click(canvas.getByRole('button', { name: '짧고 굵음' }));
		await expect(send).toBeEnabled();
		await userEvent.click(send);
		await expect(onsubmit).toHaveBeenCalledWith({ keywords: ['짧고 굵음'], body: '' });
		send.blur();
	}}
>
	<div class="w-180"><ReviewForm {onsubmit} /></div>
</Story>
