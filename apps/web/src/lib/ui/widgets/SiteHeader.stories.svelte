<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';

	import SiteHeader from './SiteHeader.svelte';

	const { Story } = defineMeta({
		title: 'Widgets/SiteHeader',
		component: SiteHeader,
		parameters: { layout: 'fullscreen' }
	});
</script>

<Story name="전체 게임에서" args={{ theme: 'light', current: 'games' }} />
