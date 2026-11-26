<script lang="ts">
	import type { Snippet } from 'svelte';

	/**
	 * 16:9 그림 틀 + 그림 위 자리(왼쪽 위 · 오른쪽 위). 게임 카드 · 앞으로 개발일지 · 잼 카드가 같이 쓴다.
	 * active 가 되면 300ms 뒤에야 미리보기를 불러온다(스쳐 가는 마우스는 안 받음 — ADR 0009 성능 규칙):
	 *   영상 1개 → 소리 없이 반복 / 이미지 여러 장 → 2.5초마다 순환. 움직임 줄이기면 대표 그림 그대로.
	 */
	interface Media {
		kind: 'image' | 'video';
		url: string;
	}

	interface Props {
		cover: string;
		/** 호버 때 보여 줄 것(이미 고른 목록 — 영상 1개 또는 이미지들) */
		media?: Media[];
		active?: boolean;
		/** 들림(호버 중인 카드) */
		lifted?: boolean;
		topLeft?: Snippet;
		topRight?: Snippet;
	}

	let { cover, media = [], active = false, lifted = false, topLeft, topRight }: Props = $props();

	const HOVER_DELAY = 300;
	const ROTATE_EVERY = 2500;

	let started = $state(false);
	let index = $state(0);

	// 외부(타이머 · 사용자 설정)와 맞추는 일이라 $effect
	$effect(() => {
		if (!active || media.length === 0) return;
		if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
		let rotate: ReturnType<typeof setInterval> | undefined;
		const start = setTimeout(() => {
			started = true;
			index = 0;
			if (media.length > 1 && media[0]?.kind === 'image') {
				rotate = setInterval(() => (index = (index + 1) % media.length), ROTATE_EVERY);
			}
		}, HOVER_DELAY);
		return () => {
			clearTimeout(start);
			clearInterval(rotate);
			started = false;
		};
	});
</script>

<div
	class={[
		'relative aspect-video rounded-lg bg-sunken transition-[translate,box-shadow] duration-(--dur-base) ease-soft',
		lifted && '-translate-y-0.75 shadow-lift'
	]}
>
	<div class="absolute inset-0 overflow-hidden rounded-[inherit]">
		<img src={cover} alt="" class="size-full object-cover" loading="lazy" decoding="async" />
		{#if started}
			{#each media as m, i (m.url)}
				{#if m.kind === 'video'}
					<video
						src={m.url}
						class="absolute inset-0 size-full object-cover"
						muted
						loop
						playsinline
						autoplay
						preload="none"
					></video>
				{:else}
					<img
						src={m.url}
						alt=""
						class={[
							'absolute inset-0 size-full object-cover transition-opacity duration-(--dur-base) ease-soft',
							i === index ? 'opacity-100' : 'opacity-0'
						]}
						decoding="async"
					/>
				{/if}
			{/each}
		{/if}
	</div>
	{#if topLeft}
		<div class="absolute top-(--overlay-inset) left-(--overlay-inset) z-(--z-art-overlay)">
			{@render topLeft()}
		</div>
	{/if}
	{#if topRight}
		<div class="absolute top-(--overlay-inset) right-(--overlay-inset) z-(--z-art-overlay)">
			{@render topRight()}
		</div>
	{/if}
</div>
