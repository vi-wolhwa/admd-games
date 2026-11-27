<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn, screen } from 'storybook/test';

	import Select from './Select.svelte';

	const items = [
		{ value: '', label: '전체' },
		{ value: '1', label: '10분 안쪽' },
		{ value: '2', label: '10~30분' }
	];
	const onchange = fn();

	const { Story } = defineMeta({ title: 'Primitives/Select', component: Select });
</script>

<Story
	name="고르기"
	asChild
	play={async ({ canvas, userEvent }) => {
		await userEvent.click(canvas.getByRole('combobox', { name: '한 판에: 전체' }));
		await userEvent.click(await screen.findByRole('option', { name: '10~30분' }));
		await expect(onchange).toHaveBeenCalledWith('2');
	}}
>
	<div class="flex gap-2">
		<Select label="한 판에" value="" {items} {onchange} />
		<Select label="한 판에" value="1" {items} onchange={fn()} />
	</div>
</Story>
