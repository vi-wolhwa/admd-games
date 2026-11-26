<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { fn } from 'storybook/test';

	import LoginRequiredDialog from './LoginRequiredDialog.svelte';

	// 로그인이 필요한 행동(리뷰 쓰기 · 답글 · 신고 · 팔로우 · 문제 알리기)을 눌렀을 때 — SH01 전까지
	const { Story } = defineMeta({
		title: 'Features/Auth/LoginRequiredDialog',
		component: LoginRequiredDialog
	});
</script>

<Story name="리뷰를 올리려면" asChild>
	<LoginRequiredDialog reason="리뷰를 올리려면" onclose={fn()} inline />
</Story>
