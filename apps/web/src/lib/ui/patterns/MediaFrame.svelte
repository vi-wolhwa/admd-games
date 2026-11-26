<script lang="ts">
	import type { Snippet } from 'svelte';

	/**
	 * 16:9 그림 틀 + 그림 위 자리(왼쪽 위 · 오른쪽 위). 게임 카드 · 앞으로 개발일지 · 잼 카드가 같이 쓴다.
	 * active 가 되면 300ms 뒤에야 미리보기를 불러온다(스쳐 가는 마우스는 안 받음 — ADR 0009 성능 규칙).
	 * 차례(media 순서): 영상은 소리 없이 **끝까지** 튼 뒤 다음으로, 이미지는 2.5초씩, 끝나면 처음부터(ADR 0009 보강 #11).
	 * 그림은 받아(decode) 둔 뒤 한 번에 바꾸고, 영상은 재생이 시작될 때까지 앞 그림을 그대로 둔다 — 깜빡임 · 잔상 없음.
	 * 움직임 줄이기면 대표 그림 그대로.
	 */
	interface Media {
		kind: 'image' | 'video';
		url: string;
	}

	interface Props {
		cover: string;
		/** 호버 때 보여 줄 차례(영상 먼저 — hoverMedia) */
		media?: Media[];
		active?: boolean;
		/** 들림(호버 중인 카드) */
		lifted?: boolean;
		topLeft?: Snippet;
		topRight?: Snippet;
	}

	let { cover, media = [], active = false, lifted = false, topLeft, topRight }: Props = $props();

	const HOVER_DELAY = 300;
	const IMAGE_SECONDS = 2500;

	/** 대표 그림 위에 깔린 마지막 이미지 */
	let image = $state<string | null>(null);
	/** 지금 트는 영상(재생이 시작되면 이미지 위로 보인다) */
	let video = $state<string | null>(null);
	let videoPlaying = $state(false);

	// 순서를 진행시키는 것들 — 화면에 그리지 않으므로 반응형이 아님
	let run = 0;
	let position = 0;
	let timer: ReturnType<typeof setTimeout> | undefined;

	function decode(url: string): Promise<void> {
		const img = new Image();
		img.src = url;
		return img.decode().catch(() => undefined);
	}

	async function show(index: number, token: number) {
		const item = media[index % media.length];
		if (!item || token !== run) return;
		position = index;
		if (item.kind === 'video') {
			videoPlaying = false;
			video = item.url;
			return; // 다음 차례는 영상이 끝날 때(onended)
		}
		await decode(item.url);
		if (token !== run) return;
		image = item.url;
		video = null;
		if (media.length > 1) timer = setTimeout(() => void show(index + 1, token), IMAGE_SECONDS);
	}

	function videoEnded() {
		if (media.length > 1) void show(position + 1, run);
	}

	// 외부(타이머 · 그림 받기 · 사용자 설정)와 맞추는 일이라 $effect
	$effect(() => {
		if (!active || media.length === 0) return;
		if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
		const token = ++run;
		timer = setTimeout(() => {
			// 이미지는 미리 받아 두기 시작(영상이 도는 동안 받아 놓으면 넘어갈 때 바로 보임)
			for (const m of media) if (m.kind === 'image') void decode(m.url);
			void show(0, token);
		}, HOVER_DELAY);
		return () => {
			run++;
			clearTimeout(timer);
			image = null;
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
		{#if image}
			<img src={image} alt="" class="absolute inset-0 size-full object-cover" />
		{/if}
		{#if video}
			<video
				src={video}
				class={['absolute inset-0 size-full object-cover', !videoPlaying && 'invisible']}
				muted
				playsinline
				autoplay
				loop={media.length === 1}
				onplaying={() => (videoPlaying = true)}
				onended={videoEnded}
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
