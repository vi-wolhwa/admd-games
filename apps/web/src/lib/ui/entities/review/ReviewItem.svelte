<script lang="ts">
	import { faceOf } from '#lib/domain/face.ts';
	import { formatAgo, formatFullDate, formatPlayTime } from '#lib/domain/format.ts';
	import type { ReviewData } from '#lib/domain/review.ts';
	import Icon from '#lib/ui/primitives/Icon.svelte';
	import JamoFace from '#lib/ui/primitives/JamoFace.svelte';
	import Menu from '#lib/ui/primitives/Menu.svelte';

	/**
	 * 리뷰 한 개 — 누가 · 어떤 맥락에서 · 무엇을 · 메이커가 어떻게 답했는지 순서(research/04-reviews.md).
	 * 맥락 줄: 'n시간 플레이했을 때 · 3일 전에 v1.1 작성(수정)' — 정확한 날짜(연도까지)는 시간에 마우스를 올리면(사용자 피드백).
	 * 찬반 판정 · 도움이 됐어요 없음. ⋯ 메뉴: 답글 달기(메이커) · 리뷰 신고 — 둘 다 로그인 뒤라 부르는 쪽이 처리.
	 */
	interface Props {
		review: ReviewData;
		/** 메이커 이름(답글 머리) */
		makerName: string;
		now: number;
		onreply: () => void;
		onreport: () => void;
	}

	let { review, makerName, now, onreply, onreport }: Props = $props();

	let expanded = $state(false);
	let body = $state<HTMLElement>();
	/** 세 줄을 넘는지 — 글자 수가 아니라 실제로 잘렸는지 잰다(폭 · 글꼴에 따라 다름) */
	let long = $state(false);

	$effect(() => {
		if (body && !expanded) long = body.scrollHeight > body.clientHeight + 1;
	});

	const makerFace = $derived(faceOf(makerName));
	const bodyId = $derived(`review-${review.id}-body`);
	const writtenAt = $derived(review.updatedAt ?? review.createdAt);
</script>

{#snippet when(at: number, edited: boolean, version: string | null)}
	<time datetime={new Date(at).toISOString()} title={formatFullDate(at)}>
		{formatAgo(at, now)} 전에{version ? ` ${version}` : ''}
		{edited ? '수정' : '작성'}
	</time>
{/snippet}

<article class="flex flex-col gap-2.5 border-t border-line py-7 first:border-t-0 first:pt-0">
	<header class="flex items-center gap-3">
		<JamoFace char={review.author.faceChar} color={review.author.faceColor} size="md" />
		<span class="min-w-0 flex-1">
			<b class="block truncate text-body font-heavy text-ink-1">{review.author.name}</b>
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
		<Menu
			label={`${review.author.name} 리뷰 메뉴`}
			items={[
				{ label: '답글 달기(메이커)', onselect: onreply },
				{ label: '리뷰 신고', onselect: onreport, danger: true }
			]}
		/>
	</header>

	<p class="flex flex-wrap gap-x-1.5 gap-y-1 text-meta text-ink-3">
		<b class="font-bold text-ink-2">
			{review.playMinutes === null
				? '플레이 기록 없음'
				: `${formatPlayTime(review.playMinutes)} 플레이했을 때`}
		</b>
		<span aria-hidden="true">·</span>
		{@render when(writtenAt, review.updatedAt !== null, review.version)}
	</p>

	{#if review.phrases.length > 0}
		<ul class="flex flex-wrap gap-1.5" aria-label="키워드">
			{#each review.phrases as phrase (phrase)}
				<li
					class="inline-flex h-6 items-center rounded-[6px] bg-sunken-hover px-2.25 text-meta font-bold text-ink-2"
				>
					{phrase}
				</li>
			{/each}
		</ul>
	{/if}

	{#if review.body}
		<p
			bind:this={body}
			id={bodyId}
			class={[
				'text-lead leading-[1.75] break-words whitespace-pre-line text-ink-1',
				!expanded && 'line-clamp-3'
			]}
		>
			{review.body}
		</p>
		{#if long || expanded}
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
	{/if}

	{#if review.reply}
		<div class="mt-1.5 ml-13 grid grid-cols-[auto_minmax(0,1fr)] gap-2.5">
			<JamoFace char={makerFace.char} color={makerFace.color} size="sm" />
			<div class="min-w-0">
				<p class="flex flex-wrap items-center gap-x-1.5 gap-y-0.5 text-meta text-ink-3">
					<b class="text-label font-heavy text-ink-1">{makerName}</b>
					<span
						class="inline-flex h-5 items-center rounded-full bg-accent-tint px-1.75 text-caption font-heavy text-accent-text"
					>
						메이커
					</span>
					{@render when(review.reply.createdAt, false, null)}
					{#if review.reply.note}<span>· {review.reply.note}</span>{/if}
				</p>
				<p class="mt-1 text-body leading-[1.7] break-words whitespace-pre-line text-ink-1">
					{review.reply.body}
				</p>
			</div>
		</div>
	{/if}
</article>
