<script lang="ts">
	import type { Snippet } from 'svelte';

	/**
	 * 고르기 칩(필터 · 태그 고르기). 누를 수 있으니 테두리, 고르면 먹색 채움(ADR 0011 §4).
	 * 고를 때 폭이 바뀌지 않게 아이콘을 더하지 않고 색만 바꾼다. count 는 뒤에 옅게(예: 퍼즐 38).
	 */
	interface Props {
		pressed: boolean;
		count?: number;
		/** 더 고를 수 없을 때(예: 최대 개수) — 고른 칩은 끄지 않는다 */
		disabled?: boolean;
		onclick: () => void;
		children: Snippet;
	}

	let { pressed, count, disabled = false, onclick, children }: Props = $props();
</script>

<button
	type="button"
	aria-pressed={pressed}
	{disabled}
	{onclick}
	class={[
		'inline-flex h-(--chip-h) cursor-pointer items-center gap-1.5 rounded-full px-3.5 text-label font-bold transition-colors duration-(--dur-instant) ease-soft',
		'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent',
		'disabled:cursor-not-allowed disabled:opacity-45 disabled:hover:bg-bg disabled:hover:inset-ring-line-strong',
		pressed
			? 'bg-ink-1 text-bg hover:bg-ink-2'
			: 'bg-bg text-ink-2 inset-ring inset-ring-line-strong hover:bg-sunken hover:inset-ring-ink-4'
	]}
>
	{@render children()}
	{#if count !== undefined}
		<span class={['text-meta font-medium', pressed ? 'opacity-80' : 'text-ink-3']}>
			{count.toLocaleString('ko-KR')}
		</span>
	{/if}
</button>
