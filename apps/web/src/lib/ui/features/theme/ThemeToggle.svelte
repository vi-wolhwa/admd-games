<script lang="ts">
	import { type Theme, THEME_COOKIE } from '#lib/domain/appearance.ts';
	import Icon from '#lib/ui/primitives/Icon.svelte';

	/**
	 * 라이트 ↔ 다크 전환(ADR 0008: 처음은 라이트, 쿠키에 기억). 서버는 쿠키를 읽어 첫 화면부터 맞는 테마로 그린다.
	 */
	interface Props {
		theme: Theme;
	}

	let { theme: initial }: Props = $props();
	let override = $state<Theme | null>(null);
	const theme = $derived(override ?? initial);

	function toggle() {
		const next: Theme = theme === 'dark' ? 'light' : 'dark';
		override = next;
		document.documentElement.dataset.theme = next;
		document.cookie = `${THEME_COOKIE}=${next}; Path=/; Max-Age=31536000; SameSite=Lax`;
	}
</script>

<button
	type="button"
	onclick={toggle}
	aria-label={theme === 'dark' ? '밝은 화면으로' : '어두운 화면으로'}
	class="grid size-(--icon-btn) place-items-center rounded-full text-ink-1 transition-colors duration-(--dur-instant) ease-soft hover:bg-sunken-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
>
	<Icon name={theme === 'dark' ? 'sun' : 'moon'} size={16} />
</button>
