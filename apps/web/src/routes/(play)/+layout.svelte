<script lang="ts">
	import SiteFooter from '#lib/ui/widgets/SiteFooter.svelte';
	import SiteHeader from '#lib/ui/widgets/SiteHeader.svelte';
	import { page } from '$app/state';

	import type { LayoutProps } from './$types';

	let { data, children }: LayoutProps = $props();

	const current = $derived(page.url.pathname.startsWith('/play/games') ? 'games' : undefined);
</script>

<SiteHeader theme={data.theme} {current} />
{@render children()}
<SiteFooter />
