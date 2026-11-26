<script lang="ts">
	import type { Snippet } from 'svelte';
	import type { HTMLButtonAttributes } from 'svelte/elements';

	/**
	 * 버튼. 누를 수 있는 보조 버튼은 테두리(ADR 0011 §4).
	 *   primary: 강조색 채움 · secondary: 흰 바탕 + 테두리 · link: 글자만
	 */
	interface Props extends Omit<HTMLButtonAttributes, 'class'> {
		variant?: 'primary' | 'secondary' | 'link';
		size?: 'md' | 'sm';
		/** 있으면 링크(<a>)로 그린다 */
		href?: string;
		class?: string;
		children: Snippet;
	}

	let {
		variant = 'secondary',
		size = 'md',
		href,
		class: className,
		children,
		type = 'button',
		...rest
	}: Props = $props();

	const classes = $derived([
		'inline-flex items-center justify-center gap-1.5 font-bold whitespace-nowrap transition-colors duration-(--dur-fast) ease-soft',
		'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent',
		variant !== 'link' &&
			(size === 'md'
				? 'h-(--btn-h) rounded-md px-5 text-body'
				: 'h-(--btn-h-sm) rounded-full px-4 text-label'),
		variant === 'primary' && 'bg-accent text-on-accent hover:bg-accent-strong',
		variant === 'secondary' && 'bg-bg text-ink-1 inset-ring inset-ring-line-strong hover:bg-sunken',
		variant === 'link' && 'text-label text-ink-3 underline underline-offset-3 hover:text-ink-1',
		className
	]);
</script>

{#if href}
	<!-- eslint-disable-next-line svelte/no-navigation-without-resolve -- href 는 부르는 쪽이 resolve() 한 값 -->
	<a {href} class={classes}>{@render children()}</a>
{:else}
	<button {type} class={classes} {...rest}>{@render children()}</button>
{/if}
