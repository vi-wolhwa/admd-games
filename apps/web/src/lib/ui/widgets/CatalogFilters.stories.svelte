<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn } from 'storybook/test';

	import { DEFAULT_QUERY } from '#lib/domain/catalog.ts';

	import CatalogFilters from './CatalogFilters.svelte';

	const tags = [
		{ slug: '퍼즐', name: '퍼즐', count: 38 },
		{ slug: '액션', name: '액션', count: 27 },
		{ slug: '아케이드', name: '아케이드', count: 18 },
		{ slug: '탐험', name: '탐험', count: 14 },
		{ slug: '이야기', name: '이야기', count: 12 }
	];
	const onchange = fn();

	const { Story } = defineMeta({ title: 'Widgets/CatalogFilters', component: CatalogFilters });
</script>

<Story
	name="태그 여러 개 · 조건"
	asChild
	play={async ({ canvas, userEvent }) => {
		// 고른 태그를 다시 누르면 빠지고, 나머지는 그대로
		await userEvent.click(canvas.getByRole('button', { name: /퍼즐/ }));
		await expect(onchange).toHaveBeenLastCalledWith(
			expect.objectContaining({ tags: ['액션'], length: 1 })
		);
	}}
>
	<div class="w-300">
		<CatalogFilters
			{tags}
			query={{ ...DEFAULT_QUERY, tags: ['퍼즐', '액션'], length: 1 }}
			total={46}
			{onchange}
		/>
	</div>
</Story>
