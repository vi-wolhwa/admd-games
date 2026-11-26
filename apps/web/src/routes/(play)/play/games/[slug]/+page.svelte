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
	import LoginRequiredDialog from '#lib/ui/features/auth/LoginRequiredDialog.svelte';
	import PlayAction from '#lib/ui/features/play/PlayAction.svelte';
	import CountLine from '#lib/ui/patterns/CountLine.svelte';
	import KeyFacts from '#lib/ui/patterns/KeyFacts.svelte';
	import MediaViewer from '#lib/ui/patterns/MediaViewer.svelte';
	import Rail from '#lib/ui/patterns/Rail.svelte';
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
	/** 로그인이 필요한 행동을 눌렀을 때 띄울 안내(무엇을 하려 했는지) */
	let loginReason = $state<string | null>(null);
	function needLogin(reason: string) {
		loginReason = reason;
	}

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

<main class="mx-auto w-(--page-width) pt-8">
	<div class="grid grid-cols-[minmax(0,1fr)_392px] items-start gap-9">
		<MediaViewer items={viewerItems} label={`${game.title} 미리보기`}>
			{#snippet topRight()}<PlatIcons {game} />{/snippet}
		</MediaViewer>

		<!-- 높이 = 왼쪽 큰 미리보기(16:9)와 같게. 위 = 제목 · 소개 · 태그, 아래 = 핵심 칸 · 버튼 · 추천/리뷰(사용자 피드백) -->
		<aside
			aria-label="게임 요약과 플레이"
			class="flex h-[calc((var(--page-width)-392px-36px)*9/16)] flex-col justify-between gap-4"
		>
			<div class="min-h-0">
				<h1 class="line-clamp-2 text-heading-lg font-heavy break-words text-ink-1">
					{game.title}
				</h1>
				<p class="mt-4 line-clamp-3 text-lead leading-[1.6] break-words text-ink-2">
					{game.summary}
				</p>
				{#if game.tags.length > 0}
					<ul class="mt-4 flex flex-wrap gap-x-2 gap-y-1" aria-label="태그 — 누르면 이 태그의 게임">
						{#each game.tags as tag (tag)}
							<li>
								<!-- eslint-disable svelte/no-navigation-without-resolve -- 경로는 resolve(), 뒤는 질의 문자열 -->
								<a
									href={`${resolve('/(play)/play/games')}?tag=${encodeURIComponent(tagSlug(tag))}`}
									class="rounded-xs hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
								>
									<Tag>{tag}</Tag>
								</a>
								<!-- eslint-enable svelte/no-navigation-without-resolve -->
							</li>
						{/each}
					</ul>
				{/if}
			</div>
			<div class="flex flex-col gap-4">
				<KeyFacts items={facts} />
				<PlayAction {action} scanPassed={game.scanPassed} />
				<div class="border-t border-line pt-3.5">
					<CountLine
						items={[
							{ icon: 'thumb', label: '추천', value: game.recommendCount },
							{ icon: 'comment', label: '리뷰', value: game.reviewCount }
						]}
					/>
				</div>
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
				onneedlogin={needLogin}
			/>
		{:else}
			<AboutTab {game} onneedlogin={needLogin} />
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

<LoginRequiredDialog reason={loginReason} onclose={() => (loginReason = null)} />
