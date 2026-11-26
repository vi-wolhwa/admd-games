<script lang="ts">
	import Icon from '#lib/ui/primitives/Icon.svelte';
	import type { IconName } from '#lib/ui/primitives/icons.ts';

	/** 아이콘 + 글자 + 숫자 줄. 숫자는 혼자 쓰지 않는다(ADR 0009 #4) — 예: 👍 추천 214 · 💬 리뷰 38 */
	interface Props {
		items: { icon: IconName; label: string; value: number }[];
	}

	let { items }: Props = $props();
</script>

<span class="inline-flex items-center gap-3 text-meta text-ink-3">
	{#each items as item (item.label)}
		<span class="inline-flex items-center gap-1">
			<Icon name={item.icon} size={13} class="text-ink-4" />
			{item.label}
			<b class="font-bold text-ink-1">{item.value.toLocaleString('ko-KR')}</b>
		</span>
	{/each}
</span>
