<script lang="ts" generics="T">
	import type { Snippet } from 'svelte';

	import Icon from '#lib/ui/primitives/Icon.svelte';

	/**
	 * 가로 레일 — 제목 + 왼쪽/오른쪽 화살표, 한 화면에 `perView` 개씩(비슷한 게임 · 앞으로 홈의 줄들).
	 * 끝에 닿으면 그쪽 화살표는 흐리게 · 누를 수 없게.
	 */
	interface Props {
		title: string;
		items: T[];
		key: (item: T) => string;
		perView?: number;
		item: Snippet<[T]>;
	}

	let { title, items, key, perView = 4, item }: Props = $props();

	let track = $state<HTMLElement>();
	let atStart = $state(true);
	let atEnd = $state(false);

	function update() {
		if (!track) return;
		atStart = track.scrollLeft <= 1;
		atEnd = track.scrollLeft + track.clientWidth >= track.scrollWidth - 1;
	}

	function move(dir: 1 | -1) {
		const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		track?.scrollBy({ left: dir * track.clientWidth, behavior: reduce ? 'auto' : 'smooth' });
	}

	$effect(() => {
		if (items.length >= 0) update();
	});

	const arrow =
		'grid size-(--arrow-btn) place-items-center rounded-full bg-bg text-ink-1 inset-ring inset-ring-line-strong transition-colors hover:bg-sunken hover:inset-ring-ink-4 disabled:cursor-default disabled:opacity-40 disabled:hover:bg-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent';
</script>

<section aria-label={title}>
	<div class="mb-(--section-head-gap) flex items-center gap-3">
		<h2 class="text-heading font-heavy text-ink-1">{title}</h2>
		<div class="ml-auto flex gap-2">
			<button
				type="button"
				aria-label="이전"
				class={arrow}
				disabled={atStart}
				onclick={() => {
					move(-1);
				}}
			>
				<Icon name="chevron" size={14} class="rotate-180" />
			</button>
			<button
				type="button"
				aria-label="다음"
				class={arrow}
				disabled={atEnd}
				onclick={() => {
					move(1);
				}}
			>
				<Icon name="chevron" size={14} />
			</button>
		</div>
	</div>
	<ul
		bind:this={track}
		onscroll={update}
		class="-mx-1 -my-2 flex snap-x snap-mandatory [scrollbar-width:none] gap-6 overflow-x-auto px-1 py-2"
	>
		{#each items as it (key(it))}
			<li
				class="shrink-0 snap-start"
				style:width={`calc((100% - ${String((perView - 1) * 24)}px) / ${String(perView)})`}
			>
				{@render item(it)}
			</li>
		{/each}
	</ul>
</section>
