<script lang="ts">
	import Icon from '#lib/ui/primitives/Icon.svelte';

	/**
	 * 검색 상자. 타자를 멈추고 300ms 뒤(또는 Enter 즉시) onsearch — 글자마다 서버에 묻지 않는다.
	 * 바깥에서 value 가 바뀌면(모두 지우기 등) 상자도 따라간다.
	 */
	interface Props {
		value: string;
		label: string;
		placeholder?: string;
		maxlength?: number;
		onsearch: (value: string) => void;
	}

	let { value, label, placeholder, maxlength, onsearch }: Props = $props();

	let text = $derived(value);
	let timer: ReturnType<typeof setTimeout> | undefined;

	function emit(now = false) {
		clearTimeout(timer);
		const v = text.trim();
		if (now) onsearch(v);
		else
			timer = setTimeout(() => {
				onsearch(v);
			}, 300);
	}
</script>

<label
	class="flex h-(--chip-h) w-70 items-center gap-2 rounded-full bg-bg px-3.5 text-ink-3 inset-ring inset-ring-line-strong transition-colors duration-(--dur-instant) ease-soft focus-within:inset-ring-2 focus-within:inset-ring-accent hover:inset-ring-ink-4"
>
	<Icon name="search" size={16} />
	<input
		type="search"
		aria-label={label}
		{placeholder}
		{maxlength}
		bind:value={text}
		oninput={() => {
			emit();
		}}
		onkeydown={(e) => {
			if (e.key === 'Enter') emit(true);
		}}
		class="min-w-0 flex-1 bg-transparent text-label font-medium text-ink-1 outline-none placeholder:text-ink-3"
	/>
</label>
