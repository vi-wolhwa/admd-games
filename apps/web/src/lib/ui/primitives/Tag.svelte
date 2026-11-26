<script lang="ts">
	import type { Snippet } from 'svelte';

	/**
	 * 붙은 꼬리표(카드의 장르 등) — 누를 수 없으니 바탕 · 테두리 없이 '#글자'(카카오페이지 키워드 방식).
	 * 회색 알약은 흰 바탕에서 거의 안 보여 글자만 떠 보였다(사용자 피드백 11/28). highlight = 지금 고른 태그
	 */
	interface Props {
		highlight?: boolean;
		children: Snippet;
	}

	let { highlight = false, children }: Props = $props();
</script>

<span
	class={[
		'text-meta whitespace-nowrap',
		highlight ? 'font-bold text-accent-text' : 'font-medium text-ink-3'
	]}
>
	#{@render children()}
</span>
