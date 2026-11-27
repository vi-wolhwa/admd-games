<script lang="ts">
	import type { Snippet } from 'svelte';
	import { slide } from 'svelte/transition';

	import { formatAgo, formatFullDate, formatPlayTime } from '#lib/domain/format.ts';
	import type { Person, ReviewData } from '#lib/domain/review.ts';
	import Icon from '#lib/ui/primitives/Icon.svelte';
	import JamoFace from '#lib/ui/primitives/JamoFace.svelte';
	import Menu from '#lib/ui/primitives/Menu.svelte';

	import MentionText from './MentionText.svelte';
	import PersonPopover from './PersonPopover.svelte';

	/**
	 * 리뷰 한 개 + 답글(한 단계) — 누가 · 어떤 맥락에서 · 무엇을 · 다른 사람이 어떻게 답했는지(research/04-reviews.md).
	 * - 맥락 줄: 'n시간 플레이했을 때 · 3일 전에 (v1.1) 작성|수정' — 연도까지의 날짜는 시간에 마우스를 올리면
	 * - 글쓴이(얼굴 · 닉네임) · @멘션은 누구든 누르면 프로필 카드(메이커스 프로필이 있으면 카드에서 그리로)
	 * - 행동은 본문 아래 글자 버튼 한 줄: '답글 달기' · '답글 n개'(접혀 있다가 펼침 — YouTube · TapTap 선례)
	 * - 답글은 시간 순서 그대로(메이커 답글도 고정하지 않음 — 대화 맥락, 사용자 결정 2026-11-28).
	 *   메이커가 답했으면 접힌 상태에서도 '메이커' 꼬리표로 알린다. 답글 안 @닉네임은 파란 글씨
	 * - 답글 쓰는 칸(replyForm)은 행동이라 부르는 쪽(features)이 넣는다
	 */
	interface Props {
		review: ReviewData;
		now: number;
		profileHref: (slug: string) => string;
		/** '답글' 을 눌렀을 때 — 답할 사람 닉네임 */
		onreplyto: (name: string) => void;
		/** 신고(남의 리뷰) — 내 리뷰(onedit)면 없음 */
		onreport?: () => void;
		/** 내 리뷰면 — ⋯(신고) 대신 '수정' 버튼 */
		onedit?: () => void;
		/** 답글 목록을 닫았을 때 — 열려 있던 답글 쓰기 칸도 닫게(사용자 피드백) */
		onreplyclose?: () => void;
		/** 열린 답글 쓰기 칸(이 리뷰에 답글을 쓰는 중일 때만) */
		replyForm?: Snippet;
	}

	let { review, now, profileHref, onreplyto, onreport, onedit, onreplyclose, replyForm }: Props =
		$props();

	let expanded = $state(false);
	let showReplies = $state(false);
	let body = $state<HTMLElement>();
	/** 세 줄을 넘는지 — 글자 수가 아니라 실제로 잘렸는지 잰다(폭 · 글꼴에 따라 다름) */
	let long = $state(false);

	$effect(() => {
		if (body && !expanded) long = body.scrollHeight > body.clientHeight + 1;
	});

	const bodyId = $derived(`review-${review.id}-body`);
	const repliesId = $derived(`review-${review.id}-replies`);
	const makerReplied = $derived(review.replies.some((r) => r.byGameMaker));
	const reduced =
		typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

	/** 답글 달기 — 답글을 펼치고 맨 아래 쓰는 칸을 연다(@닉네임 은 부르는 쪽이 채움) */
	function replyTo(name: string) {
		showReplies = true;
		onreplyto(name);
	}
</script>

{#snippet when(at: number, edited: boolean, version: string | null)}
	<time datetime={new Date(at).toISOString()} title={formatFullDate(at)}>
		{formatAgo(at, now)} 전에{version ? ` (${version})` : ''}
		{edited ? '수정' : '작성'}
	</time>
{/snippet}

<!-- 얼굴 · 닉네임 — 누구든 누르면 프로필 카드(메이커면 카드에서 메이커스 프로필로) -->
{#snippet who(person: Person & { reviewCount?: number }, size: 'sm' | 'md')}
	<PersonPopover {person} {profileHref}>
		{#snippet trigger({ props })}
			<button
				{...props}
				type="button"
				class="group/who flex min-w-0 cursor-pointer items-center gap-2.5 rounded-sm text-left focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
			>
				<JamoFace char={person.faceChar} color={person.faceColor} {size} />
				<b
					class={[
						'truncate font-heavy text-ink-1 group-hover/who:underline group-hover/who:underline-offset-3',
						size === 'md' ? 'text-body' : 'text-label'
					]}
				>
					{person.name}
				</b>
			</button>
		{/snippet}
	</PersonPopover>
{/snippet}

<article class="flex flex-col gap-3 border-t border-line py-7 first:border-t-0 first:pt-0">
	<header class="flex items-center gap-3">
		<!-- 얼굴은 이름 · 정보 두 줄 높이(사용자 피드백 — 나중에 고양이 얼굴의 표정이 잘 보이게). 같은 카드를 여는 이름 버튼이 있어 얼굴은 탭 순서에서 뺌 -->
		<PersonPopover person={review.author} {profileHref}>
			{#snippet trigger({ props })}
				<button
					{...props}
					type="button"
					tabindex="-1"
					aria-hidden="true"
					class="shrink-0 cursor-pointer"
				>
					<JamoFace char={review.author.faceChar} color={review.author.faceColor} size="two-line" />
				</button>
			{/snippet}
		</PersonPopover>
		<div class="min-w-0 flex-1">
			<div class="flex min-w-0 items-center gap-2">
				<PersonPopover person={review.author} {profileHref}>
					{#snippet trigger({ props })}
						<button
							{...props}
							type="button"
							class="min-w-0 cursor-pointer truncate rounded-sm text-body font-heavy text-ink-1 hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
						>
							{review.author.name}
						</button>
					{/snippet}
				</PersonPopover>
				<span class="shrink-0 text-meta text-ink-3">
					리뷰 {review.author.reviewCount.toLocaleString('ko-KR')}개
				</span>
			</div>
			<p class="mt-0.5 flex flex-wrap gap-x-1.5 text-meta text-ink-3">
				<b class="font-bold text-ink-2">
					{review.playMinutes === null
						? '플레이 기록 없음'
						: `${formatPlayTime(review.playMinutes)} 플레이했을 때`}
				</b>
				<span aria-hidden="true">·</span>
				{@render when(
					review.updatedAt ?? review.createdAt,
					review.updatedAt !== null,
					review.version
				)}
			</p>
		</div>
		{#if review.recommended}
			<span class="inline-flex shrink-0 items-center gap-1 text-meta font-heavy text-heart-text">
				<Icon name="heart-fill" size={12} />추천
			</span>
		{/if}
		{#if onedit}
			<button
				type="button"
				onclick={onedit}
				class="inline-flex h-8 shrink-0 items-center gap-1.5 rounded-full px-3 text-meta font-bold text-ink-2 inset-ring inset-ring-line-strong transition-colors hover:bg-sunken hover:text-ink-1 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
			>
				<Icon name="pen" size={13} />수정
			</button>
		{:else}
			<Menu
				label={`${review.author.name} 리뷰 메뉴`}
				items={[{ label: '리뷰 신고', onselect: () => onreport?.(), danger: true }]}
			/>
		{/if}
	</header>

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
		<!-- 긴 글은 세 줄로 접고, 잘린 마지막 줄의 오른쪽 끝에 '더 보기'(사용자 피드백) -->
		<div class="relative">
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
			{#if long && !expanded}
				<button
					type="button"
					aria-expanded="false"
					aria-controls={bodyId}
					onclick={() => (expanded = true)}
					class="absolute right-0 bottom-0 bg-linear-to-r from-transparent via-bg via-30% to-bg pl-10 text-lead leading-[1.75] font-bold text-ink-2 underline underline-offset-3 hover:text-ink-1"
				>
					더 보기
				</button>
			{/if}
		</div>
	{/if}

	<!-- 행동 한 줄(글자 버튼) — 답글 달기 · 답글 n개 펼치기 -->
	<div class="-ml-2 flex items-center gap-1">
		<button
			type="button"
			onclick={() => {
				replyTo(review.author.name);
			}}
			class="inline-flex h-8 items-center gap-1.5 rounded-full px-2 text-meta font-bold text-ink-2 transition-colors hover:bg-sunken hover:text-ink-1 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
		>
			<Icon name="comment" size={13} />답글 달기
		</button>
		{#if review.replies.length > 0}
			<button
				type="button"
				aria-expanded={showReplies}
				aria-controls={repliesId}
				onclick={() => {
					showReplies = !showReplies;
					if (!showReplies) onreplyclose?.();
				}}
				class="inline-flex h-8 items-center gap-1.5 rounded-full px-2 text-meta font-bold text-accent-text transition-colors hover:bg-accent-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
			>
				<Icon
					name="chevron"
					size={12}
					class={showReplies ? '-rotate-90 transition-transform' : 'rotate-90 transition-transform'}
				/>
				답글 {review.replies.length.toLocaleString('ko-KR')}개
				{#if makerReplied}
					<span
						class="inline-flex h-5 items-center rounded-full bg-accent-tint px-1.75 text-caption font-heavy text-accent-text"
					>
						메이커 답글
					</span>
				{/if}
			</button>
		{/if}
	</div>

	{#if (showReplies && review.replies.length > 0) || replyForm}
		<div
			id={repliesId}
			transition:slide={{ duration: reduced ? 0 : 200 }}
			class="ml-14 flex flex-col gap-5"
		>
			{#if showReplies}
				{#each review.replies as reply (reply.id)}
					<div class="flex flex-col gap-1">
						<div class="flex flex-wrap items-center gap-x-1.5 gap-y-0.5 text-meta text-ink-3">
							{@render who(reply.author, 'sm')}
							{#if reply.byGameMaker}
								<span
									class="inline-flex h-5 items-center rounded-full bg-accent-tint px-1.75 text-caption font-heavy text-accent-text"
								>
									메이커
								</span>
							{/if}
							<span aria-hidden="true">·</span>
							{@render when(reply.updatedAt ?? reply.createdAt, reply.updatedAt !== null, null)}
						</div>
						<p class="ml-9 text-body leading-[1.7] break-words whitespace-pre-line text-ink-1">
							<MentionText text={reply.body} mentions={reply.mentions} {profileHref} />
						</p>
						<button
							type="button"
							onclick={() => {
								replyTo(reply.author.name);
							}}
							aria-label={`${reply.author.name}님에게 답글`}
							class="ml-7.5 self-start rounded-full px-1.5 py-0.5 text-meta font-bold text-ink-3 hover:bg-sunken hover:text-ink-1 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
						>
							답글
						</button>
					</div>
				{/each}
			{/if}
			{#if replyForm}{@render replyForm()}{/if}
		</div>
	{/if}
</article>
