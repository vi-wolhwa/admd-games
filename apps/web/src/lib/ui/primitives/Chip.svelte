<script lang="ts">
	import type { Snippet } from 'svelte';

	import Icon from '#lib/ui/primitives/Icon.svelte';

	/**
	 * 고르기 칩(필터 · 태그 고르기). 누를 수 있으니 테두리, 고르면 먹색 채움(ADR 0011 §4).
	 * count 는 뒤에 옅게(예: 퍼즐 38).
	 */
	interface Props {
		pressed: boolean;
		count?: number;
		onclick: () => void;
		children: Snippet;
	}

	let { pressed, count, onclick, children }: Props = $props();
</script>

<button
	type="button"
	aria-pressed={pressed}
	{onclick}
	class={[
		'inline-flex h-(--chip-h) items-center gap-1.5 rounded-full px-3.5 text-label font-bold transition-colors duration-(--dur-instant) ease-soft',
		'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent',
		pressed
			? 'bg-ink-1 text-bg'
			: 'bg-bg text-ink-2 inset-ring inset-ring-line-strong hover:bg-sunken'
	]}
>
	{#if pressed}<Icon name="check" size={13} />{/if}
	{@render children()}
	{#if count !== undefined}
		<span class={['text-meta font-medium', pressed ? 'opacity-80' : 'text-ink-3']}>
			{count.toLocaleString('ko-KR')}
		</span>
	{/if}
</button>
