<script lang="ts">
	import { faceOf } from '#lib/domain/face.ts';
	import { formatDate, formatPlayTime } from '#lib/domain/format.ts';
	import type { ReviewData } from '#lib/domain/review.ts';
	import Icon from '#lib/ui/primitives/Icon.svelte';
	import JamoFace from '#lib/ui/primitives/JamoFace.svelte';

	/**
	 * 리뷰 한 개 — 누가 · 어떤 맥락에서 · 무엇을 · 도움이 됐는지 · 메이커가 어떻게 답했는지 순서(research/04-reviews.md).
	 * 찬반 판정은 없고, 글쓴이가 추천했으면 '추천함'. 플레이 시간은 그대로(기록 없으면 '플레이 기록 없음', ADR 0011).
	 * 도움이 됐어요 · 리뷰 메뉴(링크 복사 · 신고)는 로그인(SH01) 뒤 — 지금은 숫자만.
	 */
	interface Props {
		review: ReviewData;
		/** 메이커 이름(답글 머리) */
		makerName: string;
		now: number;
	}

	let { review, makerName, now }: Props = $props();

	let expanded = $state(false);
	let body = $state<HTMLElement>();
	/** 세 줄을 넘는지 — 글자 수가 아니라 실제로 잘렸는지 잰다(폭 · 글꼴에 따라 다름) */
	let long = $state(false);

	$effect(() => {
		if (body && !expanded) long = body.scrollHeight > body.clientHeight + 1;
	});
	const makerFace = $derived(faceOf(makerName));
	const bodyId = $derived(`review-${review.id}-body`);
</script>

<article class="flex flex-col gap-2.5 border-t border-line py-7 first:border-t-0 first:pt-0">
	<header class="flex items-center gap-3">
		<JamoFace char={review.author.faceChar} color={review.author.faceColor} size="md" />
		<span>
			<b class="block text-body font-heavy text-ink-1">{review.author.name}</b>
			<span class="mt-px flex items-center gap-1.5 text-meta text-ink-3">
				리뷰 {review.author.reviewCount.toLocaleString('ko-KR')}개
				{#if review.recommended}
					<span aria-hidden="true">·</span>
					<span class="inline-flex items-center gap-1 font-heavy text-accent-text">
						<Icon name="thumb" size={12} />추천함
					</span>
				{/if}
			</span>
		</span>
	</header>

	<p class="flex flex-wrap gap-x-2.5 gap-y-1 text-meta text-ink-3">
		{#if review.playMinutes === null}
			<b class="font-bold text-ink-2">플레이 기록 없음</b>
		{:else}
			<b class="font-bold text-ink-2">쓸 때 플레이 {formatPlayTime(review.playMinutes)}</b>
		{/if}
		{#if review.version}<span>· {review.version} 에서 씀</span>{/if}
		<span>· {formatDate(review.createdAt, now)}</span>
	</p>

	{#if review.phrases.length > 0}
		<ul class="flex flex-wrap gap-1.5" aria-label="글쓴이가 고른 말">
			{#each review.phrases as phrase (phrase)}
				<li
					class="inline-flex h-6 items-center rounded-[6px] bg-sunken-hover px-2.25 text-meta font-bold text-ink-2"
				>
					{phrase}
				</li>
			{/each}
		</ul>
	{/if}

	<p
		bind:this={body}
		id={bodyId}
		class={['text-lead leading-[1.75] text-ink-1', !expanded && 'line-clamp-3']}
	>
		{review.body}
	</p>
	{#if long}
		<button
			type="button"
			aria-expanded={expanded}
			aria-controls={bodyId}
			onclick={() => (expanded = !expanded)}
			class="self-start text-label font-bold text-ink-2 underline underline-offset-3 hover:text-ink-1"
		>
			{expanded ? '접기' : '더 보기'}
		</button>
	{/if}

	<p class="mt-0.5 inline-flex items-center gap-1.5 text-meta text-ink-3">
		<Icon name="thumb" size={13} class="text-ink-4" />도움이 됐어요
		<b class="font-bold text-ink-1">{review.helpfulCount.toLocaleString('ko-KR')}</b>
	</p>

	{#if review.reply}
		<div class="mt-1.5 ml-13 grid grid-cols-[auto_minmax(0,1fr)] gap-2.5">
			<JamoFace char={makerFace.char} color={makerFace.color} size="sm" />
			<div>
				<p class="flex flex-wrap items-center gap-1.5 text-meta text-ink-3">
					<b class="text-label font-heavy text-ink-1">{makerName}</b>
					<span
						class="inline-flex h-5 items-center rounded-full bg-accent-tint px-1.75 text-caption font-heavy text-accent-text"
					>
						메이커
					</span>
					<span>{formatDate(review.reply.createdAt, now)}</span>
					{#if review.reply.note}<span>· {review.reply.note}</span>{/if}
				</p>
				<p class="mt-1 text-body leading-[1.7] text-ink-1">{review.reply.body}</p>
			</div>
		</div>
	{/if}
</article>
