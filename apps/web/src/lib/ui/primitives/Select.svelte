<script lang="ts">
	import { Select } from 'bits-ui';

	import Icon from '#lib/ui/primitives/Icon.svelte';

	/**
	 * 고르기 상자(필터 · 정렬). 모양은 칩과 같은 알약 + 테두리, 값을 고르면 먹색 채움(ADR 0011 §4).
	 * 폭은 가장 긴 항목에 맞춰 고정 — 값을 바꿔도 옆 요소가 밀리지 않는다.
	 * 키보드 · 스크린리더 처리는 Bits UI. 첫 항목은 보통 '전체'(value = '').
	 */
	interface Props {
		label: string;
		value: string;
		items: { value: string; label: string }[];
		onchange: (value: string) => void;
		/** 기본값('전체')이 아닐 때 채움으로 강조 — 정렬처럼 늘 값이 있는 것은 false */
		highlightWhenSet?: boolean;
	}

	let { label, value, items, onchange, highlightWhenSet = true }: Props = $props();

	const selected = $derived(items.find((i) => i.value === value) ?? items[0]);
	const isSet = $derived(highlightWhenSet && value !== '');
</script>

<Select.Root type="single" {value} {items} onValueChange={onchange}>
	<Select.Trigger
		aria-label={`${label}: ${selected?.label ?? ''}`}
		class={[
			'inline-flex h-(--chip-h) cursor-pointer items-center gap-1.5 rounded-full pr-3 pl-3.5 text-label font-bold whitespace-nowrap transition-colors duration-(--dur-instant) ease-soft',
			'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent',
			isSet
				? 'bg-ink-1 text-bg hover:bg-ink-2'
				: 'bg-bg text-ink-3 inset-ring inset-ring-line-strong hover:bg-sunken hover:inset-ring-ink-4 data-[state=open]:bg-sunken data-[state=open]:inset-ring-ink-4'
		]}
	>
		<span>{label}</span>
		<!-- 모든 항목을 같은 칸에 겹쳐 두고 고른 것만 보인다 → 폭 = 가장 긴 항목 -->
		<span class="grid">
			{#each items as item (item.value)}
				<span
					aria-hidden="true"
					class={[
						'col-start-1 row-start-1',
						item.value === selected?.value ? (isSet ? 'text-bg' : 'text-ink-1') : 'invisible'
					]}
				>
					{item.label}
				</span>
			{/each}
		</span>
		<Icon name="chevron" size={12} class="rotate-90" />
	</Select.Trigger>
	<Select.Portal>
		<Select.Content
			sideOffset={8}
			align="end"
			class="z-(--z-dropdown) w-50 rounded-lg bg-bg p-1.5 shadow-pop ring-1 ring-line-strong"
		>
			<Select.Viewport>
				{#each items as item (item.value)}
					<Select.Item
						value={item.value}
						label={item.label}
						class="flex h-9.5 cursor-pointer items-center justify-between rounded-sm px-2.5 text-label font-medium text-ink-1 transition-colors duration-(--dur-instant) select-none data-highlighted:bg-sunken-hover data-selected:font-heavy"
					>
						{#snippet children({ selected: isSelected })}
							{item.label}
							{#if isSelected}<Icon name="check" size={13} />{/if}
						{/snippet}
					</Select.Item>
				{/each}
			</Select.Viewport>
		</Select.Content>
	</Select.Portal>
</Select.Root>
