<script lang="ts">
	import {
		DEVICE_LABEL,
		type GameCardData,
		hoverMedia,
		LENGTH_LABEL,
		playersLabel,
		tagSlug
	} from '#lib/domain/game.ts';
	import { playAction } from '#lib/domain/play-action.ts';
	import { type ReviewQuery, reviewSearchParams } from '#lib/domain/review.ts';
	import GameCard from '#lib/ui/entities/game/GameCard.svelte';
	import PlatIcons from '#lib/ui/entities/game/PlatIcons.svelte';
	import PlayAction from '#lib/ui/features/play/PlayAction.svelte';
	import CountLine from '#lib/ui/patterns/CountLine.svelte';
	import KeyFacts from '#lib/ui/patterns/KeyFacts.svelte';
	import MediaViewer from '#lib/ui/patterns/MediaViewer.svelte';
	import Rail from '#lib/ui/patterns/Rail.svelte';
	import Icon from '#lib/ui/primitives/Icon.svelte';
	import Tabs from '#lib/ui/primitives/Tabs.svelte';
	import Tag from '#lib/ui/primitives/Tag.svelte';
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';

	import type { PageProps } from './$types';
	import AboutTab from './AboutTab.svelte';
	import ReviewsTab from './ReviewsTab.svelte';

	/**
	 * PG05 게임 상세 — 미리보기 + 오른쪽 패널, 붙는 탭(소개 · 리뷰), 비슷한 게임.
	 * 시안 PG05-game v5 · ADR 0009 · 0011 · 결정 2026-11-28(없는 기능은 핵심 버튼만 비활성).
	 */
	let { data }: PageProps = $props();

	const game = $derived(data.game);
	const viewerItems = $derived([
		{ kind: 'image' as const, url: game.cover, tag: '대표' },
		...hoverMedia(game.media)
	]);
	const action = $derived(playAction(game, null, data.device));
	const facts = $derived([
		{ label: '실행', value: game.launch === 'web' ? '바로 플레이' : '설치형' },
		{ label: '기기', value: game.devices.map((d) => DEVICE_LABEL[d]).join(' · ') },
		{ label: '한 판', value: LENGTH_LABEL[game.length] },
		{ label: '인원', value: playersLabel(game.playersMin, game.playersMax) }
	]);
	const firstTag = $derived(game.tags[0]);

	/** 탭 · 리뷰 거르기는 주소에 — 새로 고침 · 공유 · 뒤로 가기에 그대로 */
	function navigate(params: URLSearchParams) {
		const search = params.toString();
		/* eslint-disable svelte/no-navigation-without-resolve -- 경로는 resolve(), 뒤는 질의 문자열 */
		void goto(
			`${resolve('/(play)/play/games/[slug]', { slug: game.slug })}${search ? `?${search}` : ''}`,
			{
				reset: false
			}
		);
		/* eslint-enable svelte/no-navigation-without-resolve */
	}

	function setTab(tab: string) {
		// 함수 안에서 잠깐 쓰는 값이라 반응형일 필요 없음
		// eslint-disable-next-line svelte/prefer-svelte-reactivity
		const params = new URLSearchParams(page.url.search);
		if (tab === 'reviews') params.set('tab', 'reviews');
		else {
			params.delete('tab');
			params.delete('rsort');
			params.delete('rphrase');
		}
		navigate(params);
	}

	function setReviewQuery(q: ReviewQuery) {
		navigate(reviewSearchParams(q, new URLSearchParams(page.url.search)));
	}
</script>

<svelte:head>
	<title>{game.title} · PlayGround</title>
	<meta name="description" content={game.summary} />
</svelte:head>

<main class="mx-auto w-(--page-width) pt-6">
	<nav aria-label="위치" class="flex items-center gap-1.5 text-meta font-medium text-ink-3">
		<a href={resolve('/(play)/play/games')} class="hover:text-ink-1">게임</a>
		{#if firstTag}
			<Icon name="chevron" size={12} />
			<!-- eslint-disable svelte/no-navigation-without-resolve -- 경로는 resolve(), 뒤는 질의 문자열 -->
			<a
				href={`${resolve('/(play)/play/games')}?tag=${encodeURIComponent(tagSlug(firstTag))}`}
				class="hover:text-ink-1"
			>
				{firstTag}
			</a>
			<!-- eslint-enable svelte/no-navigation-without-resolve -->
		{/if}
	</nav>

	<div class="mt-5 grid grid-cols-[minmax(0,1fr)_392px] items-start gap-9">
		<MediaViewer items={viewerItems} label={`${game.title} 미리보기`}>
			{#snippet topRight()}<PlatIcons {game} />{/snippet}
		</MediaViewer>

		<aside aria-label="게임 요약과 플레이" class="flex flex-col gap-4.5">
			<div>
				<h1 class="text-heading-lg font-heavy text-ink-1">
					{game.title}
				</h1>
				<p class="mt-2 text-lead leading-[1.6] text-ink-2">{game.summary}</p>
			</div>
			{#if game.tags.length > 0}
				<p class="flex flex-wrap gap-2">
					{#each game.tags as tag (tag)}<Tag>{tag}</Tag>{/each}
				</p>
			{/if}
			<KeyFacts items={facts} />
			<PlayAction {action} scanPassed={game.scanPassed} />
			<div class="border-t border-line pt-4">
				<CountLine
					items={[
						{ icon: 'thumb', label: '추천', value: game.recommendCount },
						{ icon: 'comment', label: '리뷰', value: game.reviewCount }
					]}
				/>
			</div>
		</aside>
	</div>
</main>

<div
	class="sticky top-(--header-h) z-10 mt-12 border-b border-line-strong bg-bg/94 backdrop-blur-md"
>
	<div class="mx-auto w-(--page-width)">
		<Tabs
			label="게임 내용"
			idPrefix="game"
			value={data.tab}
			items={[
				{ value: 'about', label: '소개' },
				{ value: 'reviews', label: '리뷰', count: game.reviewCount }
			]}
			onchange={setTab}
		/>
	</div>
</div>

<div class="mx-auto w-(--page-width)">
	<section
		id="game-panel"
		role="tabpanel"
		aria-labelledby={`game-tab-${data.tab}`}
		class="mt-9 min-h-155"
	>
		{#if data.tab === 'reviews' && data.reviewPage && data.phrases}
			<ReviewsTab
				gameId={game.id}
				makerName={game.makerName}
				recommendCount={game.recommendCount}
				reviewCount={game.reviewCount}
				query={data.reviewQuery}
				first={data.reviewPage}
				phrases={data.phrases}
				now={data.now}
				onquery={setReviewQuery}
			/>
		{:else}
			<AboutTab {game} />
		{/if}
	</section>

	{#if data.similar.length > 0}
		<div class="mt-18 border-t border-line pt-10">
			<Rail title="비슷한 게임" items={data.similar} key={(g: GameCardData) => g.id}>
				{#snippet item(g: GameCardData)}
					<GameCard game={g} href={`/play/games/${g.slug}`} now={data.now} />
				{/snippet}
			</Rail>
		</div>
	{/if}
</div>
