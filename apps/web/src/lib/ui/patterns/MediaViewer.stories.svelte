<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect } from 'storybook/test';

	import MediaViewer from './MediaViewer.svelte';

	const items = [
		{ kind: 'image' as const, url: '/sample/tessellate-0.svg', tag: '대표' },
		...[1, 2, 3, 4, 5].map((n) => ({
			kind: 'image' as const,
			url: `/sample/tessellate-${String(n)}.svg`
		}))
	];

	const { Story } = defineMeta({ title: 'Patterns/MediaViewer', component: MediaViewer });
</script>

<Story
	name="썸네일 고르기"
	asChild
	play={async ({ canvas, userEvent }) => {
		// 썸네일을 누르면 그 항목으로 — 자동 넘김은 끝나서 캡처가 늘 같다
		const third = canvas.getByRole('button', { name: '이미지 3 / 6' });
		await userEvent.click(third);
		await expect(third).toHaveAttribute('aria-current', 'true');
		await expect(canvas.getByText('3 / 6')).toBeVisible();
	}}
>
	<div class="w-190">
		<MediaViewer {items} label="테셀레이트 미리보기" />
	</div>
</Story>
