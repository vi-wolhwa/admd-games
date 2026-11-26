<script lang="ts">
	// 본문 글꼴 Pretendard — 우리 서버에서, 글자 범위별 조각만 받는다(결정 2026-11-28)
	import 'pretendard/dist/web/variable/pretendardvariable-dynamic-subset.css';
	import './layout.css';

	import favicon from '#lib/assets/favicon.svg';

	import type { LayoutProps } from './$types';

	let { children }: LayoutProps = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{@render children()}
