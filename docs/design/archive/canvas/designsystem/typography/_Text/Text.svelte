<script lang="ts">
	import type { Snippet } from 'svelte';
	import type { HTMLAttributes } from 'svelte/elements';

	import type { TextAs } from './text-as.types';
	import type { TextColor } from './text-color.types';
	import type { TextSize } from './text-size.types';
	import { textSizeToTrackingStyle } from './text-tracking.types';
	import type { TextWeight } from './text-weight.types';

	interface TextProps extends HTMLAttributes<HTMLElement> {
		children: Snippet;
		as: TextAs;
		size: TextSize;
		weight: TextWeight;
		color: TextColor;
	}

	const textSizeToStyle: Record<TextSize, string> = {
		/* 12px */ '4xs': 'text-[0.75rem]',
		/* 14px */ '3xs': 'text-[0.875rem]',
		/* 16px */ '2xs': 'text-[1rem]',
		/* 18px */ xs: 'text-[1.125rem]',
		/* 21px */ sm: 'text-[1.3125rem]',
		/* 24px */ md: 'text-[1.5rem]',
		/* 28px */ lg: 'text-[1.75rem]',
		/* 32px */ xl: 'text-[2rem]',
		/* 37px */ '2xl': 'text-[2.3125rem]',
		/* 43px */ '3xl': 'text-[2.6875rem]',
		/* 50px */ '4xl': 'text-[3.125rem]'
	};

	const textWeightToStyle: Record<TextWeight, string> = {
		thin: 'font-thin',
		extralight: 'font-extralight',
		light: 'font-light',
		normal: 'font-normal',
		medium: 'font-medium',
		semibold: 'font-semibold',
		bold: 'font-bold',
		extrabold: 'font-extrabold',
		black: 'font-black'
	};

	const textSizeToLineHeightStyle: Record<TextSize, string> = {
		'4xs': 'leading-[1.5]',
		'3xs': 'leading-[1.5]',
		'2xs': 'leading-[1.5]',
		xs: 'leading-[1.5]',
		sm: 'leading-[1.4625]',
		md: 'leading-[1.425]',
		lg: 'leading-[1.375]',
		xl: 'leading-[1.325]',
		'2xl': 'leading-[1.2625]',
		'3xl': 'leading-[1.1875]',
		'4xl': 'leading-[1.1]'
	};

	const textColorToStyle: Record<TextColor, string> = {
		primary: 'text-primary',
		secondary: 'text-secondary',
		tertiary: 'text-tertiary',
		quaternary: 'text-quaternary',
		inverse: 'text-inverse'
	};

	const {
		children,
		class: className = '',
		as,
		size,
		weight,
		color,
		...props
	}: TextProps = $props();

	const sizeStyle = $derived(textSizeToStyle[size]);
	const weightStyle = $derived(textWeightToStyle[weight]);
	const colorStyle = $derived(textColorToStyle[color]);
	const lineHeightStyle = $derived(textSizeToLineHeightStyle[size]);
	const trackStyle = $derived(textSizeToTrackingStyle[size]);
</script>

<svelte:element
	this={as}
	class="{sizeStyle} {weightStyle} {colorStyle} {lineHeightStyle} {trackStyle} {className}"
	{...props}
>
	{@render children()}
</svelte:element>
