<script lang="ts">
	import type { Snippet } from 'svelte';

	/**
	 * 16:9 그림 틀 + 그림 위 자리(왼쪽 위 · 오른쪽 위). 게임 카드 · 앞으로 개발일지 · 잼 카드가 같이 쓴다.
	 * active 가 되면 300ms 뒤에야 미리보기를 불러온다(스쳐 가는 마우스는 안 받음 — ADR 0009 성능 규칙):
	 *   영상 1개 → 소리 없이 반복 / 이미지 여러 장 → 2.5초마다 순환. 움직임 줄이기면 대표 그림 그대로.
	 * 바꿀 그림은 미리 다 받아(decode) 둔 뒤 한 번에 바꾼다 — 반쯤 비치는 전환 · 덜 받은 그림의 잔상이 없게.
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

	/** 지금 대표 그림 위에 보이는 미리보기 이미지(없으면 대표 그림) */
	let shown = $state<string | null>(null);
	let video = $state<string | null>(null);
	let videoPlaying = $state(false);

	// 외부(타이머 · 이미지 받기 · 사용자 설정)와 맞추는 일이라 $effect
	$effect(() => {
		if (!active || media.length === 0) return;
		if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
		let stopped = false;
		let rotate: ReturnType<typeof setInterval> | undefined;
		const images = media.filter((m) => m.kind === 'image').map((m) => m.url);
		const first = media[0];

		const start = setTimeout(() => {
			if (first?.kind === 'video') {
				video = first.url;
				return;
			}
			const ready: string[] = [];
			for (const url of images) {
				const img = new Image();
				img.src = url;
				void img
					.decode()
					.then(() => {
						if (stopped) return;
						ready.push(url);
						if (ready.length === 1) shown = url;
					})
					.catch(() => undefined);
			}
			let i = 0;
			rotate = setInterval(() => {
				// 받아 둔 것만 차례로 — 아직 못 받은 그림은 건너뛴다
				const order = images.filter((u) => ready.includes(u));
				if (order.length < 2) return;
				i = (i + 1) % order.length;
				shown = order[i] ?? null;
			}, ROTATE_EVERY);
		}, HOVER_DELAY);

		return () => {
			stopped = true;
			clearTimeout(start);
			clearInterval(rotate);
			shown = null;
			video = null;
			videoPlaying = false;
		};
	});
</script>

<!-- 들림은 top 으로(transform 은 쌓임 맥락을 만들어 위 자리의 툴팁 단추가 카드 링크 아래로 깔림) -->
<div
	class={[
		'relative aspect-video rounded-lg bg-sunken transition-[top,box-shadow] duration-(--dur-base) ease-soft',
		lifted ? '-top-0.75 shadow-lift' : 'top-0'
	]}
>
	<div class="absolute inset-0 overflow-hidden rounded-[inherit]">
		<img src={cover} alt="" class="size-full object-cover" loading="lazy" decoding="async" />
		{#if shown}
			<img src={shown} alt="" class="absolute inset-0 size-full object-cover" />
		{/if}
		{#if video}
			<video
				src={video}
				class={['absolute inset-0 size-full object-cover', !videoPlaying && 'invisible']}
				muted
				loop
				playsinline
				autoplay
				onplaying={() => (videoPlaying = true)}
			></video>
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
