<script lang="ts">
	import type { Snippet } from 'svelte';

	/** 붙은 꼬리표(카드의 장르 등) — 누를 수 없으니 회색 바탕, 테두리 없음(ADR 0011 §4). highlight = 지금 고른 태그 */
	interface Props {
		highlight?: boolean;
		children: Snippet;
	}

	let { highlight = false, children }: Props = $props();
</script>

<span
	class={[
		'inline-flex h-(--tag-h) items-center rounded-xs px-2 text-caption font-bold',
		highlight ? 'bg-accent-tint text-accent-text' : 'bg-sunken text-ink-2'
	]}
>
	{@render children()}
</span>
