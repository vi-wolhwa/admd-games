<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';

	import Button from './Button.svelte';

	const { Story } = defineMeta({ title: 'Primitives/Button', component: Button });
</script>

<Story name="종류 · 크기" asChild>
	<div class="flex items-center gap-3">
		<Button variant="primary">지금 플레이</Button>
		<Button>더 불러오기</Button>
		<Button size="sm">조건 모두 지우기</Button>
		<Button variant="link">모두 지우기</Button>
	</div>
</Story>
