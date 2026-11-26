<script lang="ts">
	/** 불러오는 동안 자리 — 크기 · 모양은 class 로. 움직임 줄이기면 반짝임 없음 */
	interface Props {
		class?: string;
	}

	let { class: className }: Props = $props();
</script>

<span
	aria-hidden="true"
	class={['block animate-pulse rounded-sm bg-sunken motion-reduce:animate-none', className]}
></span>
