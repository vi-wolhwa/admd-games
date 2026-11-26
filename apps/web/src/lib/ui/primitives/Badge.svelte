<script lang="ts">
	import type { Snippet } from 'svelte';

	import Icon from '#lib/ui/primitives/Icon.svelte';
	import type { IconName } from '#lib/ui/primitives/icons.ts';

	/** 그림 위 배지(신작 등). 자리는 부모가 정한다 */
	interface Props {
		icon?: IconName;
		children: Snippet;
	}

	let { icon, children }: Props = $props();
</script>

<span
	class="inline-flex h-(--badge-h) items-center gap-1.25 rounded-full bg-accent pr-2.25 pl-1.75 text-caption font-heavy text-on-accent shadow-chip"
>
	{#if icon}<Icon name={icon} size={12} />{/if}
	{@render children()}
</span>
