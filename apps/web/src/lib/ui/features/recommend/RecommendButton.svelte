<script lang="ts">
	import Icon from '#lib/ui/primitives/Icon.svelte';

	/**
	 * 게임 추천(하트) — 주 버튼 오른쪽의 정사각형 버튼(사용자 결정 2026-11-28).
	 * 싫어요는 없다(ADR 0009). 추천 저장은 로그인(SH01) 뒤 — 지금은 onclick 이 로그인 안내를 띄운다.
	 */
	interface Props {
		/** 내가 이미 추천했는지 */
		pressed?: boolean;
		onclick: () => void;
	}

	let { pressed = false, onclick }: Props = $props();
</script>

<button
	type="button"
	aria-pressed={pressed}
	aria-label="이 게임 추천"
	title={pressed ? '추천함' : '추천'}
	{onclick}
	class={[
		'inline-flex size-14 shrink-0 items-center justify-center rounded-lg text-heart transition-colors focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent',
		pressed
			? 'bg-heart-tint inset-ring inset-ring-heart'
			: 'inset-ring inset-ring-line-strong hover:bg-heart-tint hover:inset-ring-heart'
	]}
>
	<Icon name={pressed ? 'heart-fill' : 'heart'} size={20} />
</button>
