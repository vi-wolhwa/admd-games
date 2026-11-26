<script lang="ts">
	import { Tooltip } from 'bits-ui';
	import type { Snippet } from 'svelte';

	/**
	 * 툴팁(Bits UI 로 키보드 · 스크린리더 처리 — component-architecture 6절). 먹 바탕 + 흰 글자.
	 * trigger 는 받은 props 를 자기 요소에 펼쳐야 한다(포커스 · aria-describedby).
	 */
	interface Props {
		trigger: Snippet<[{ props: Record<string, unknown> }]>;
		children: Snippet;
		side?: 'top' | 'bottom';
		align?: 'start' | 'center' | 'end';
	}

	let { trigger, children, side = 'bottom', align = 'end' }: Props = $props();
</script>

<Tooltip.Provider delayDuration={120}>
	<Tooltip.Root>
		<Tooltip.Trigger>
			{#snippet child({ props })}{@render trigger({ props })}{/snippet}
		</Tooltip.Trigger>
		<Tooltip.Portal>
			<Tooltip.Content
				{side}
				{align}
				sideOffset={8}
				class="z-(--z-tooltip) flex flex-col gap-1.75 rounded-md bg-surface-ink px-3 py-2.5 text-meta font-medium whitespace-nowrap text-on-ink shadow-pop"
			>
				{@render children()}
				<Tooltip.Arrow class="text-surface-ink" />
			</Tooltip.Content>
		</Tooltip.Portal>
	</Tooltip.Root>
</Tooltip.Provider>
