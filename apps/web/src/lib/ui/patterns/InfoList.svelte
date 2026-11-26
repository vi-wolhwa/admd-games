<script lang="ts">
	import type { Snippet } from 'svelte';

	/** 이름 → 값 목록(게임 정보 · 앞으로 설정 · 심사 정보). 값은 글자 또는 snippet */
	interface Props {
		items: { label: string; value: string | Snippet }[];
	}

	let { items }: Props = $props();
</script>

<dl>
	{#each items as item (item.label)}
		<div class="grid grid-cols-[76px_minmax(0,1fr)] gap-3 py-1.5 text-label leading-normal">
			<dt class="font-medium text-ink-3">{item.label}</dt>
			<dd class="font-medium text-ink-1">
				{#if typeof item.value === 'string'}{item.value}{:else}{@render item.value()}{/if}
			</dd>
		</div>
	{/each}
</dl>
