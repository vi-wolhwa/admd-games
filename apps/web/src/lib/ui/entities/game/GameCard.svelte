<script lang="ts">
	import { type GameCardData, hoverMedia, isNewGame, LENGTH_LABEL } from '#lib/domain/game.ts';
	import CountLine from '#lib/ui/patterns/CountLine.svelte';
	import MediaFrame from '#lib/ui/patterns/MediaFrame.svelte';
	import Badge from '#lib/ui/primitives/Badge.svelte';
	import Tag from '#lib/ui/primitives/Tag.svelte';

	import PlatIcons from './PlatIcons.svelte';

	/**
	 * 격자용 게임 카드(PG03 · 앞으로 검색 · 메이커 페이지). 카드 전체가 상세로 가는 링크(제목 링크를 늘림).
	 * 호버 · 포커스 = 그림이 들리고 미리보기 미디어가 돈다(ADR 0009 #6).
	 * 빠른 플레이 버튼은 플레이 화면(PG06)이 생기면 붙인다.
	 */
	interface Props {
		game: GameCardData;
		href: string;
		/** 신작 판단 기준 시각(서버가 준 값 — 화면마다 같게) */
		now: number;
		/** 지금 고른 태그 이름 — 카드의 같은 태그를 강조 */
		highlightTags?: string[];
	}

	let { game, href, now, highlightTags = [] }: Props = $props();

	let hovered = $state(false);
	let focused = $state(false);
	const active = $derived(hovered || focused);
</script>

<div
	class="group relative"
	role="presentation"
	onpointerenter={() => (hovered = true)}
	onpointerleave={() => (hovered = false)}
	onfocusin={() => (focused = true)}
	onfocusout={() => (focused = false)}
>
	<MediaFrame cover={game.cover} media={hoverMedia(game.media)} {active} lifted={active}>
		{#snippet topLeft()}
			{#if isNewGame(game.publishedAt, now)}<Badge icon="spark">신작</Badge>{/if}
		{/snippet}
		{#snippet topRight()}<PlatIcons {game} />{/snippet}
	</MediaFrame>
	<h3 class="mt-3 truncate text-title-lg font-heavy text-ink-1 group-hover:text-accent-text">
		<!-- eslint-disable svelte/no-navigation-without-resolve -- href 는 부르는 쪽이 resolve() 한 값 -->
		<a
			{href}
			class="outline-none after:absolute after:inset-0 after:rounded-lg focus-visible:after:outline-2 focus-visible:after:outline-offset-4 focus-visible:after:outline-accent"
		>
			{game.title}
		</a>
		<!-- eslint-enable svelte/no-navigation-without-resolve -->
	</h3>
	<p class="mt-0.5 truncate text-label text-ink-3">
		{game.makerName} · 한 판 {LENGTH_LABEL[game.length]}
	</p>
	{#if game.tags.length > 0}
		<p class="mt-1.75 flex gap-1.25 overflow-hidden">
			{#each game.tags.slice(0, 3) as tag (tag)}
				<Tag highlight={highlightTags.includes(tag)}>{tag}</Tag>
			{/each}
		</p>
	{/if}
	<p class="mt-2">
		<CountLine
			items={[
				{ icon: 'thumb', label: '추천', value: game.recommendCount },
				{ icon: 'comment', label: '리뷰', value: game.reviewCount }
			]}
		/>
	</p>
</div>
