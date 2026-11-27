<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn } from 'storybook/test';

	import PlayAction from '#lib/ui/features/play/PlayAction.svelte';

	import RecommendButton from './RecommendButton.svelte';

	const onclick = fn();

	// 주 버튼 오른쪽의 정사각형 하트 — 안 누름 · 누름(추천함), 이 기기 불가 안내 옆에서도
	const { Story } = defineMeta({
		title: 'Features/Recommend/RecommendButton',
		component: RecommendButton
	});
</script>

<Story
	name="안 누름 · 누름"
	asChild
	play={async ({ canvas, userEvent }) => {
		const [first, second] = canvas.getAllByRole('button', { name: '이 게임 추천' });
		if (!first || !second) throw new Error('추천 버튼이 없어요');
		await expect(second).toHaveAttribute('aria-pressed', 'true');
		await userEvent.click(first);
		await expect(onclick).toHaveBeenCalled();
		first.blur();
	}}
>
	<div class="grid w-200 grid-cols-3 items-start gap-6">
		<PlayAction action={{ kind: 'first' }} scanPassed={false}>
			{#snippet side()}<RecommendButton {onclick} />{/snippet}
		</PlayAction>
		<PlayAction action={{ kind: 'first' }} scanPassed={false} ready>
			{#snippet side()}<RecommendButton pressed onclick={fn()} />{/snippet}
		</PlayAction>
		<PlayAction action={{ kind: 'unsupported', devices: ['phone', 'pad'] }} scanPassed={false}>
			{#snippet side()}<RecommendButton onclick={fn()} />{/snippet}
		</PlayAction>
	</div>
</Story>
