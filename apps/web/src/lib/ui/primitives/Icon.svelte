<script lang="ts">
	import { type IconName, ICONS } from '#lib/ui/primitives/icons.ts';

	interface Props {
		name: IconName;
		size?: 12 | 13 | 14 | 16 | 20;
		class?: string;
	}

	let { name, size = 14, class: className }: Props = $props();
	const icon = $derived<{ d: string[]; filled?: boolean }>(ICONS[name]);
</script>

<svg
	class={['shrink-0', className]}
	width={size}
	height={size}
	viewBox="0 0 16 16"
	fill={icon.filled ? 'currentColor' : 'none'}
	stroke={icon.filled ? 'none' : 'currentColor'}
	stroke-width="1.7"
	stroke-linecap="round"
	stroke-linejoin="round"
	aria-hidden="true"
>
	{#each icon.d as d (d)}<path {d} />{/each}
</svg>
