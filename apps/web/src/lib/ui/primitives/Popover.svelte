<script lang="ts">
	import { Popover } from 'bits-ui';
	import type { Snippet } from 'svelte';

	/**
	 * 팝오버(Bits UI 로 키보드 · 포커스 · 바깥 누르면 닫힘 처리 — component-architecture 6절).
	 * 누르면 열리는 작은 카드. trigger 는 받은 props 를 자기 버튼에 펼쳐야 한다.
	 */
	interface Props {
		trigger: Snippet<[{ props: Record<string, unknown> }]>;
		children: Snippet;
		side?: 'top' | 'bottom';
		align?: 'start' | 'center' | 'end';
	}

	let { trigger, children, side = 'bottom', align = 'start' }: Props = $props();
</script>

<Popover.Root>
	<Popover.Trigger>
		{#snippet child({ props })}{@render trigger({ props })}{/snippet}
	</Popover.Trigger>
	<Popover.Portal>
		<Popover.Content
			{side}
			{align}
			sideOffset={8}
			class="z-(--z-dropdown) rounded-xl bg-bg p-4 shadow-pop ring-1 ring-line-strong"
		>
			{@render children()}
		</Popover.Content>
	</Popover.Portal>
</Popover.Root>
