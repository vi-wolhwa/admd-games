<script lang="ts">
	import { faceOf } from '#lib/domain/face.ts';
	import GameCard from '#lib/ui/entities/game/GameCard.svelte';
	import JamoFace from '#lib/ui/primitives/JamoFace.svelte';

	import type { PageProps } from './$types';

	/** 메이커스 프로필(최소) — 얼굴 · 이름 · 공개한 게임 격자. 게임은 PlayGround 상세로 이어진다 */
	let { data }: PageProps = $props();

	const face = $derived(faceOf(data.profile.name));
</script>

<svelte:head>
	<title>{data.profile.name} · MakersGround</title>
</svelte:head>

<main class="mx-auto w-(--page-width) pt-10">
	<header class="flex items-center gap-5">
		<JamoFace char={face.char} color={face.color} size="lg" />
		<div class="min-w-0">
			<h1 class="truncate text-heading-lg font-heavy text-ink-1">{data.profile.name}</h1>
			<p class="mt-1 text-label text-ink-3">
				메이커 · 게임 {data.profile.games.length.toLocaleString('ko-KR')}개
			</p>
		</div>
	</header>

	<h2 class="mt-12 mb-5 text-heading font-heavy text-ink-1">올린 게임</h2>
	{#if data.profile.games.length === 0}
		<p class="rounded-2xl bg-sunken py-14 text-center text-body text-ink-3">
			아직 공개한 게임이 없어요.
		</p>
	{:else}
		<ul class="grid grid-cols-4 gap-x-6 gap-y-10">
			{#each data.profile.games as game (game.id)}
				<li><GameCard {game} href={`/play/games/${game.slug}`} now={data.now} /></li>
			{/each}
		</ul>
	{/if}
</main>
