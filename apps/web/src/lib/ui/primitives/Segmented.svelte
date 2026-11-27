<script lang="ts">
	/**
	 * 하나만 고르는 막대(정렬 등). 누를 수 있으니 테두리, 고른 칸은 먹색 채움(ADR 0011 §4).
	 * 키보드: 라디오 묶음처럼 화살표로 옮긴다.
	 */
	interface Props {
		label: string;
		items: { value: string; label: string }[];
		value: string;
		onchange: (value: string) => void;
	}

	let { label, items, value, onchange }: Props = $props();

	let group = $state<HTMLElement>();

	function onkeydown(e: KeyboardEvent) {
		if (!['ArrowRight', 'ArrowLeft', 'ArrowDown', 'ArrowUp'].includes(e.key)) return;
		e.preventDefault();
		const step = e.key === 'ArrowRight' || e.key === 'ArrowDown' ? 1 : -1;
		const i = items.findIndex((t) => t.value === value);
		const next = items[(i + step + items.length) % items.length];
		if (!next) return;
		onchange(next.value);
		group?.querySelectorAll<HTMLElement>('[role=radio]')[items.indexOf(next)]?.focus();
	}
</script>

<div
	bind:this={group}
	role="radiogroup"
	aria-label={label}
	tabindex="-1"
	class="inline-flex rounded-full bg-bg p-0.75 inset-ring inset-ring-line-strong"
	{onkeydown}
>
	{#each items as item (item.value)}
		{@const checked = item.value === value}
		<button
			type="button"
			role="radio"
			aria-checked={checked}
			tabindex={checked ? 0 : -1}
			onclick={() => {
				onchange(item.value);
			}}
			class={[
				'inline-flex h-8 items-center rounded-full px-3 text-meta font-bold transition-colors duration-(--dur-instant)',
				'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent',
				checked ? 'bg-ink-1 text-bg' : 'text-ink-3 hover:bg-sunken hover:text-ink-1'
			]}
		>
			{item.label}
		</button>
	{/each}
</div>
