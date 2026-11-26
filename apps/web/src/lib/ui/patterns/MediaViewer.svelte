<script lang="ts">
	import type { Snippet } from 'svelte';

	import Icon from '#lib/ui/primitives/Icon.svelte';

	/**
	 * 큰 미리보기 + 아래 썸네일 줄(게임 상세 — ADR 0009 #9 · #10).
	 * 순서는 부르는 쪽이 정한다(대표 → 영상 → 이미지). 자동으로 넘긴다: 이미지 4초, 영상은 소리 끈 채 끝까지 본 뒤.
	 * 마우스를 올리면 멈춤, 썸네일을 누르면 그 항목으로 가고 자동 넘김은 끝(주도권을 사용자에게).
	 * 움직임 줄이기면 자동 넘김 없음. 썸네일이 6개보다 많으면 줄을 가로로 넘긴다.
	 */
	interface Item {
		kind: 'image' | 'video';
		url: string;
		/** 썸네일 위 작은 표시(예: 대표) */
		tag?: string;
	}

	interface Props {
		items: Item[];
		/** 스크린리더용 이름(예: '루프 디버거 미리보기') */
		label: string;
		/** 큰 그림 오른쪽 위 자리 */
		topRight?: Snippet;
	}

	let { items, label, topRight }: Props = $props();

	const IMAGE_MS = 4000;

	let index = $state(0);
	let auto = $state(true);
	let hovered = $state(false);
	let muted = $state(true);
	/** 움직임 줄이기 — 처음 한 번 읽는다(서버에서는 false) */
	const reduced =
		typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
	let strip = $state<HTMLElement>();

	const current = $derived(items[index]);

	function go(i: number) {
		index = (i + items.length) % items.length;
	}

	function pick(i: number) {
		auto = false;
		go(i);
	}

	// 이미지는 4초 뒤 다음으로(영상은 끝날 때 onended) — 외부 타이머와 맞추는 일이라 $effect
	$effect(() => {
		if (!auto || hovered || reduced || items.length < 2 || current?.kind !== 'image') return;
		const t = setTimeout(() => {
			go(index + 1);
		}, IMAGE_MS);
		return () => {
			clearTimeout(t);
		};
	});

	// 지금 항목의 썸네일이 줄 안에 보이게
	$effect(() => {
		const el = strip?.children[index] as HTMLElement | undefined;
		el?.scrollIntoView({ block: 'nearest', inline: 'nearest', behavior: 'smooth' });
	});

	function videoEnded() {
		if (auto && items.length > 1) go(index + 1);
	}

	function scrollStrip() {
		strip?.scrollBy({ left: strip.clientWidth, behavior: reduced ? 'auto' : 'smooth' });
	}
</script>

<div aria-roledescription="미리보기" aria-label={label} role="region">
	<div
		class="relative aspect-video overflow-hidden rounded-xl bg-sunken"
		role="presentation"
		onpointerenter={() => (hovered = true)}
		onpointerleave={() => (hovered = false)}
	>
		{#if current?.kind === 'video'}
			{#key current.url}
				<video
					src={current.url}
					class="size-full object-cover"
					{muted}
					playsinline
					autoplay={!reduced}
					controls={reduced}
					loop={!auto || items.length === 1}
					onended={videoEnded}
				></video>
			{/key}
			<span
				class="absolute bottom-3 left-3 inline-flex h-7 items-center gap-1.5 rounded-full bg-scrim px-2.5 text-meta font-bold text-on-ink"
			>
				<Icon name="play" size={12} />영상{muted ? ' · 소리 꺼짐' : ''}
			</span>
			<button
				type="button"
				aria-label={muted ? '소리 켜기' : '소리 끄기'}
				aria-pressed={!muted}
				onclick={() => (muted = !muted)}
				class="absolute right-3 bottom-3 grid size-8 place-items-center rounded-full bg-scrim text-on-ink hover:bg-scrim-strong focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-on-ink"
			>
				<Icon name={muted ? 'muted' : 'sound'} size={16} />
			</button>
		{:else if current}
			<img src={current.url} alt="" class="size-full object-cover" />
			<span
				class="absolute right-3 bottom-3 inline-flex h-7 items-center rounded-full bg-scrim px-2.5 text-meta font-bold text-on-ink"
			>
				{index + 1} / {items.length}
			</span>
		{/if}
		{#if topRight}
			<div class="absolute top-3 right-3 z-(--z-art-overlay)">{@render topRight()}</div>
		{/if}
	</div>

	{#if items.length > 1}
		<div class="relative mt-2.5">
			<div
				bind:this={strip}
				class="-m-0.75 flex snap-x snap-mandatory [scrollbar-width:none] gap-2 overflow-x-auto p-0.75"
			>
				{#each items as item, i (item.url)}
					<button
						type="button"
						aria-label={`${item.kind === 'video' ? '영상' : (item.tag ?? '이미지')} ${String(i + 1)} / ${String(items.length)}`}
						aria-current={i === index ? 'true' : undefined}
						onclick={() => {
							pick(i);
						}}
						class={[
							'relative aspect-video w-[calc((100%-40px)/6)] shrink-0 snap-start overflow-hidden rounded-[9px] transition-opacity duration-(--dur-fast)',
							'focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent',
							i === index ? 'ring-2 ring-ink-1' : 'opacity-60 hover:opacity-100'
						]}
					>
						{#if item.kind === 'video'}
							<video src={item.url} class="size-full object-cover" muted preload="metadata"></video>
						{:else}
							<img src={item.url} alt="" class="size-full object-cover" loading="lazy" />
						{/if}
						{#if item.kind === 'video' || item.tag}
							<span
								class="absolute bottom-1.5 left-1.25 inline-flex h-4.5 items-center gap-0.75 rounded-xs bg-scrim px-1.5 text-caption font-heavy text-on-ink"
							>
								{#if item.kind === 'video'}<Icon name="play" size={12} />영상{:else}{item.tag}{/if}
							</span>
						{/if}
					</button>
				{/each}
			</div>
			{#if items.length > 6}
				<button
					type="button"
					aria-label="썸네일 더 보기"
					onclick={scrollStrip}
					class="absolute top-1/2 right-0 grid size-8 -translate-y-1/2 place-items-center rounded-full bg-bg text-ink-1 shadow-pop ring-1 ring-line-strong hover:bg-sunken-hover focus-visible:outline-2 focus-visible:outline-accent"
				>
					<Icon name="chevron" size={14} />
				</button>
			{/if}
		</div>
	{/if}
</div>
