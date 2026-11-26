<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';

	import Badge from './Badge.svelte';
	import Tag from './Tag.svelte';

	// 누를 수 없는 표시 두 가지 — 붙은 꼬리표(회색 · 고른 것은 강조)와 그림 위 배지
	const { Story } = defineMeta({ title: 'Primitives/Tag · Badge', component: Tag });
</script>

<Story name="꼬리표 · 배지" asChild>
	<div class="flex items-center gap-2">
		<Tag>아케이드</Tag>
		<Tag highlight>퍼즐</Tag>
		<Badge icon="spark">신작</Badge>
	</div>
</Story>
