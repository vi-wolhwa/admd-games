<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, waitFor } from 'storybook/test';

	import Badge from '#lib/ui/primitives/Badge.svelte';

	import MediaFrame from './MediaFrame.svelte';

	const shots = [1, 2, 3, 4, 5].map((n) => ({
		kind: 'image' as const,
		url: `/sample/tessellate-${String(n)}.svg`
	}));

	const { Story } = defineMeta({ title: 'Patterns/MediaFrame', component: MediaFrame });
</script>

<Story
	name="대표 그림 · 호버 미리보기"
	asChild
	play={async ({ canvasElement }) => {
		// 켜진 틀은 300ms 뒤 미리보기를 받아 둔 다음 한 장만 대표 그림 위에 얹는다(반쯤 비치는 전환 없음)
		await waitFor(() => expect(canvasElement.querySelectorAll('img')).toHaveLength(1 + 2));
	}}
>
	<div class="grid w-150 grid-cols-2 gap-6">
		<MediaFrame cover="/sample/tessellate-0.svg" media={shots}>
			{#snippet topLeft()}<Badge icon="spark">신작</Badge>{/snippet}
		</MediaFrame>
		<MediaFrame cover="/sample/tessellate-0.svg" media={shots} active lifted />
	</div>
</Story>
