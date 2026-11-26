<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn } from 'storybook/test';

	import ReportDialog from './ReportDialog.svelte';

	const onsubmit = fn();

	// 로그인(SH01) 때 게임 상세 소개 탭에 붙는다 — 지금은 모습만(결정 2026-11-28)
	const { Story } = defineMeta({ title: 'Features/Report/ReportDialog', component: ReportDialog });
</script>

<Story
	name="고르고 보내기"
	asChild
	play={async ({ canvas, userEvent }) => {
		const send = canvas.getByRole('button', { name: '보내기' });
		await expect(send).toBeDisabled();
		await userEvent.click(canvas.getByRole('radio', { name: /실행이 안 돼요/ }));
		await userEvent.click(send);
		await expect(onsubmit).toHaveBeenCalledWith({ reason: 'broken', detail: '' });
		send.blur();
	}}
>
	<ReportDialog open inline gameTitle="루프 디버거" onopenchange={fn()} {onsubmit} />
</Story>
