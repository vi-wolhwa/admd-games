<script lang="ts">
	import SiteFooter from '#lib/ui/widgets/SiteFooter.svelte';
	import SiteHeader from '#lib/ui/widgets/SiteHeader.svelte';

	import type { LayoutProps } from './$types';

	/** MakersGround 공용 틀 — 지금은 최소(메이커스 프로필). 메이커스 헤더 디자인은 3묶음에서 */
	let { data, children }: LayoutProps = $props();
</script>

<SiteHeader theme={data.theme} ground="make" />
{@render children()}
<SiteFooter />
