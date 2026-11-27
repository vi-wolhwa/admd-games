<script lang="ts">
	/** 핵심 칸 묶음(예: 실행 · 기기 · 한 판에 · 인원) — 정보라 회색 바탕, 테두리 없음(ADR 0011 §4). 값의 줄바꿈(\n)은 그대로 */
	interface Props {
		items: { label: string; value: string }[];
	}

	let { items }: Props = $props();
</script>

<dl
	class="grid rounded-md bg-sunken"
	style:grid-template-columns={`repeat(${String(items.length)}, minmax(0, 1fr))`}
>
	{#each items as item, i (item.label)}
		<div class={['flex flex-col gap-1.25 px-2.5 py-3', i > 0 && 'border-l border-line']}>
			<dt class="text-caption font-medium text-ink-3">{item.label}</dt>
			<dd class="text-label leading-tight font-heavy whitespace-pre-line text-ink-1">
				{item.value}
			</dd>
		</div>
	{/each}
</dl>
