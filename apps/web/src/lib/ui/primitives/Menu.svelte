<script lang="ts">
	import { DropdownMenu } from 'bits-ui';

	/**
	 * ⋯ 메뉴(리뷰 메뉴 등). 키보드 · 스크린리더 처리는 Bits UI. danger = 신고처럼 조심할 항목(빨간 글자).
	 */
	interface Props {
		/** 단추 이름(스크린리더) — 예: '새벽배송 리뷰 메뉴' */
		label: string;
		items: { label: string; onselect: () => void; danger?: boolean }[];
	}

	let { label, items }: Props = $props();
</script>

<DropdownMenu.Root>
	<DropdownMenu.Trigger
		aria-label={label}
		class="grid size-8 place-items-center rounded-sm text-lead leading-none tracking-[1px] text-ink-3 transition-colors hover:bg-sunken-hover hover:text-ink-1 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent data-[state=open]:bg-sunken-hover"
	>
		···
	</DropdownMenu.Trigger>
	<DropdownMenu.Portal>
		<DropdownMenu.Content
			align="end"
			sideOffset={6}
			class="z-(--z-dropdown) flex w-44 flex-col rounded-lg bg-bg p-1.5 shadow-pop ring-1 ring-line-strong"
		>
			{#each items as item (item.label)}
				<DropdownMenu.Item
					onSelect={item.onselect}
					class={[
						'flex h-9 cursor-pointer items-center rounded-sm px-2.5 text-label font-medium select-none data-highlighted:bg-sunken-hover',
						item.danger ? 'text-danger-text' : 'text-ink-1'
					]}
				>
					{item.label}
				</DropdownMenu.Item>
			{/each}
		</DropdownMenu.Content>
	</DropdownMenu.Portal>
</DropdownMenu.Root>
