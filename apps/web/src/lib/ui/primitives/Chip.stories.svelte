<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { fn } from 'storybook/test';

	import Chip from './Chip.svelte';

	const onclick = fn();

	const { Story } = defineMeta({ title: 'Primitives/Chip', component: Chip });
</script>

<Story name="고름 · 안 고름" asChild>
	<div class="flex gap-2">
		<Chip pressed {onclick}>전체</Chip>
		<Chip pressed={false} count={38} {onclick}>퍼즐</Chip>
		<Chip pressed count={27} {onclick}>액션</Chip>
	</div>
</Story>
