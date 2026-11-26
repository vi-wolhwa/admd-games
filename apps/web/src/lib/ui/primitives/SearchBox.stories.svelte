<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn, waitFor } from 'storybook/test';

	import SearchBox from './SearchBox.svelte';

	const onsearch = fn();

	const { Story } = defineMeta({ title: 'Primitives/SearchBox', component: SearchBox });
</script>

<Story
	name="찾기"
	asChild
	play={async ({ canvas, userEvent }) => {
		// 타자를 멈추면 한 번만 묻는다(글자마다 묻지 않음)
		await userEvent.type(canvas.getByRole('searchbox'), '러너');
		await waitFor(() => expect(onsearch).toHaveBeenCalledWith('러너'));
		await expect(onsearch).toHaveBeenCalledTimes(1);
	}}
>
	<SearchBox value="" label="전체 게임에서 찾기" placeholder="게임 이름, 메이커" {onsearch} />
</Story>
