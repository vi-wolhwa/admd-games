<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, fn, screen } from 'storybook/test';

	import Select from './Select.svelte';

	const items = [
		{ value: '', label: '전체' },
		{ value: '1', label: '5분 이하' },
		{ value: '2', label: '15분 이하' }
	];
	const onchange = fn();

	const { Story } = defineMeta({ title: 'Primitives/Select', component: Select });
</script>

<Story
	name="고르기"
	asChild
	play={async ({ canvas, userEvent }) => {
		await userEvent.click(canvas.getByRole('combobox', { name: '한 판: 전체' }));
		await userEvent.click(await screen.findByRole('option', { name: '15분 이하' }));
		await expect(onchange).toHaveBeenCalledWith('2');
	}}
>
	<div class="flex gap-2">
		<Select label="한 판" value="" {items} {onchange} />
		<Select label="한 판" value="1" {items} onchange={fn()} />
	</div>
</Story>
