<script lang="ts">
	/**
	 * 탭 줄(내용 전환 — 앵커 스크롤이 아님, 사용자 피드백 PG05). 고른 탭 = 먹색 밑줄.
	 * 키보드: 왼쪽 · 오른쪽 화살표로 옮기고 바로 고른다(자동 활성). 패널은 부르는 쪽이 id 로 잇는다.
	 */
	interface Props {
		label: string;
		items: { value: string; label: string; count?: number }[];
		value: string;
		/** 탭 버튼 · 패널 id 앞부분 — 탭 = `${idPrefix}-tab-${value}`, 패널 = `${idPrefix}-panel` */
		idPrefix: string;
		onchange: (value: string) => void;
	}

	let { label, items, value, idPrefix, onchange }: Props = $props();

	let list = $state<HTMLElement>();

	function onkeydown(e: KeyboardEvent) {
		if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
		e.preventDefault();
		const i = items.findIndex((t) => t.value === value);
		const next = items[(i + (e.key === 'ArrowRight' ? 1 : -1) + items.length) % items.length];
		if (!next) return;
		onchange(next.value);
		list?.querySelector<HTMLElement>(`#${idPrefix}-tab-${next.value}`)?.focus();
	}
</script>

<div
	bind:this={list}
	role="tablist"
	aria-label={label}
	tabindex="-1"
	class="flex items-center gap-1"
	{onkeydown}
>
	{#each items as item (item.value)}
		{@const selected = item.value === value}
		<button
			type="button"
			role="tab"
			id={`${idPrefix}-tab-${item.value}`}
			aria-selected={selected}
			aria-controls={`${idPrefix}-panel`}
			tabindex={selected ? 0 : -1}
			onclick={() => {
				onchange(item.value);
			}}
			class={[
				'inline-flex h-14 items-center px-4 text-lead font-bold transition-colors duration-(--dur-instant)',
				'focus-visible:outline-2 focus-visible:-outline-offset-4 focus-visible:outline-accent',
				selected
					? 'relative text-ink-1 after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-ink-1'
					: 'text-ink-3 hover:text-ink-1'
			]}
		>
			{item.label}
			{#if item.count !== undefined}
				<span class="ml-1.25 text-label font-medium text-ink-3">
					{item.count.toLocaleString('ko-KR')}
				</span>
			{/if}
		</button>
	{/each}
</div>
