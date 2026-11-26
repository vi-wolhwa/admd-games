<script lang="ts">
	import {
		type CatalogQuery,
		catalogSearchParams,
		DEFAULT_QUERY,
		MAX_SEARCH,
		PAGE_SIZE
	} from '#lib/domain/catalog.ts';
	import type { GameCardData } from '#lib/domain/game.ts';
	import GameCard from '#lib/ui/entities/game/GameCard.svelte';
	import Button from '#lib/ui/primitives/Button.svelte';
	import Icon from '#lib/ui/primitives/Icon.svelte';
	import SearchBox from '#lib/ui/primitives/SearchBox.svelte';
	import Skeleton from '#lib/ui/primitives/Skeleton.svelte';
	import CatalogFilters from '#lib/ui/widgets/CatalogFilters.svelte';
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';

	import type { PageProps } from './$types';

	/**
	 * PG03 전체 게임 — 4열 갤러리 + 무한 스크롤(ADR 0010).
	 * 바닥 600px 전에 12개씩 이어 불러오고, 불러온 개수는 주소(n)에 남긴다.
	 */
	let { data }: PageProps = $props();

	// 필터가 바뀌면(data 가 새로 오면) 처음 묶음으로 돌아간다 — 쓰기 가능한 $derived
	let items = $derived<GameCardData[]>(data.games);
	let nextCursor = $derived(data.nextCursor);
	let loading = $state(false);
	let failed = $state(false);
	let sentinel = $state<HTMLElement>();
	let scrollY = $state(0);

	const highlightNames = $derived(
		data.query.tags.map((slug) => data.tags.find((t) => t.slug === slug)?.name ?? slug)
	);
	const remaining = $derived(Math.min(PAGE_SIZE, data.total - items.length));

	function applyQuery(query: CatalogQuery) {
		const search = catalogSearchParams(query).toString();
		// eslint-disable-next-line svelte/no-navigation-without-resolve -- 경로는 resolve(), 뒤는 질의 문자열
		void goto(`${resolve('/(play)/play/games')}${search ? `?${search}` : ''}`, { reset: false });
	}

	async function loadMore() {
		if (loading || !nextCursor) return;
		loading = true;
		failed = false;
		const params = catalogSearchParams(data.query);
		params.set('cursor', nextCursor);
		try {
			const res = await fetch(`/api/games?${params.toString()}`);
			if (!res.ok) throw new Error(String(res.status));
			const more = await res.json<{ items: GameCardData[]; nextCursor: string | null }>();
			items = [...items, ...more.items];
			nextCursor = more.nextCursor;
			// 불러온 개수만 주소에 — load 를 다시 돌리지 않는 얕은 이동
			const search = catalogSearchParams(data.query, items.length).toString();
			// eslint-disable-next-line svelte/no-navigation-without-resolve -- 경로는 resolve(), 뒤는 질의 문자열
			void goto(`${resolve('/(play)/play/games')}${search ? `?${search}` : ''}`, {
				state: page.state,
				shallow: true,
				replace: true
			});
		} catch {
			failed = true;
		} finally {
			loading = false;
		}
		// 화면이 커서 바닥이 아직 보이면 관찰자가 다시 알리지 않으므로 직접 한 번 더
		if (!failed && sentinel && sentinel.getBoundingClientRect().top < window.innerHeight + 600) {
			void loadMore();
		}
	}

	function observe(node: HTMLElement) {
		const io = new IntersectionObserver(
			(entries) => {
				if (entries.some((e) => e.isIntersecting)) void loadMore();
			},
			{ rootMargin: '0px 0px 600px 0px' }
		);
		io.observe(node);
		return () => {
			io.disconnect();
		};
	}

	function toTop() {
		const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
	}
</script>

<svelte:head>
	<title>전체 게임 · PlayGround</title>
</svelte:head>

<svelte:window bind:scrollY />

<main class="mx-auto w-(--page-width) pt-8">
	<div class="flex items-center justify-between gap-4">
		<h1 class="text-heading-lg font-heavy text-ink-1">전체 게임</h1>
		<SearchBox
			value={data.query.q}
			label="전체 게임에서 찾기"
			placeholder="게임 이름, 메이커"
			maxlength={MAX_SEARCH}
			onsearch={(q: string) => {
				if (q !== data.query.q) applyQuery({ ...data.query, q });
			}}
		/>
	</div>

	<CatalogFilters tags={data.tags} query={data.query} total={data.total} onchange={applyQuery} />

	{#if data.total === 0}
		<div class="mt-16 flex flex-col items-center gap-3 rounded-2xl bg-sunken py-16 text-center">
			<p class="text-lead font-bold text-ink-1">
				{data.query.q ? `‘${data.query.q}’에 맞는 게임이 없어요` : '조건에 맞는 게임이 없어요'}
			</p>
			<p class="text-body text-ink-3">검색어나 조건을 바꿔 보세요.</p>
			<Button
				size="sm"
				onclick={() => {
					applyQuery({ ...DEFAULT_QUERY, sort: data.query.sort });
				}}
			>
				조건 모두 지우기
			</Button>
		</div>
	{:else}
		<h2 class="sr-only">게임 목록</h2>
		<ul class="mt-6 grid grid-cols-4 gap-x-6 gap-y-10" aria-label="게임 목록">
			{#each items as game (game.id)}
				<li>
					<GameCard
						{game}
						href={`/play/games/${game.slug}`}
						now={data.now}
						highlightTags={highlightNames}
					/>
				</li>
			{/each}
			{#if loading}
				{#each { length: remaining } as _, i (i)}
					<li aria-hidden="true" class="flex flex-col gap-2">
						<Skeleton class="mb-1 aspect-video rounded-lg" />
						<Skeleton class="h-5 w-[70%]" />
						<Skeleton class="h-3.5 w-1/2" />
						<Skeleton class="h-3.5 w-2/5" />
					</li>
				{/each}
			{/if}
		</ul>

		<div bind:this={sentinel} {@attach observe} class="mt-7 flex flex-col items-center gap-3">
			<p role="status" class="text-label text-ink-3">
				{#if loading}
					{remaining}개 더 불러오는 중 · {items.length} / {data.total}
				{:else if failed}
					더 불러오지 못했어요.
				{/if}
			</p>
			{#if failed}
				<Button size="sm" onclick={loadMore}>다시 시도</Button>
			{:else if nextCursor && !loading}
				<!-- 키보드 사용자용 대체 — 평소엔 보이지 않고 포커스가 오면 보임(ADR 0010) -->
				<Button size="sm" class="sr-only focus:not-sr-only" onclick={loadMore}>더 불러오기</Button>
			{/if}
		</div>
	{/if}

	{#if scrollY > 800}
		<button
			type="button"
			onclick={toTop}
			aria-label="맨 위로"
			class="fixed right-10 bottom-10 z-(--z-tooltip) grid size-12 place-items-center rounded-full bg-bg text-ink-1 shadow-pop ring-1 ring-line-strong hover:bg-sunken-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
		>
			<Icon name="up" size={16} />
		</button>
	{/if}
</main>
