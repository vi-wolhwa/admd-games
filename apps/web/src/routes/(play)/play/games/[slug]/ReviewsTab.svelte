<script lang="ts">
	import {
		myReviewForVersion,
		REVIEW_SORT_LABEL,
		REVIEW_SORTS,
		type ReviewData,
		type ReviewQuery,
		reviewSearchParams,
		type ReviewSort
	} from '#lib/domain/review.ts';
	import ReviewItem from '#lib/ui/entities/review/ReviewItem.svelte';
	import ReplyForm from '#lib/ui/features/review-write/ReplyForm.svelte';
	import ReviewForm from '#lib/ui/features/review-write/ReviewForm.svelte';
	import Button from '#lib/ui/primitives/Button.svelte';
	import Chip from '#lib/ui/primitives/Chip.svelte';
	import Segmented from '#lib/ui/primitives/Segmented.svelte';
	import { resolve } from '$app/paths';

	/**
	 * 리뷰 탭(PG05 전용) — 왼쪽 = '리뷰 쓰기'(누르면 폼이 펼쳐짐) + 한 열 목록, 오른쪽 = 요약 · 키워드로 보기 · 정렬.
	 * 리뷰 · 답글 올리기 · 신고는 로그인(SH01) 뒤 — 지금은 누르면 onneedlogin(결정 2026-11-28).
	 */
	interface Props {
		gameId: string;
		recommendCount: number;
		reviewCount: number;
		query: ReviewQuery;
		first: { items: ReviewData[]; nextCursor: string | null; total: number | null };
		phrases: { phrase: string; count: number }[];
		/** 이 게임의 지금 버전 — 리뷰는 버전마다 한 사람 하나 */
		version: string | null;
		/** 내가 이 게임에 쓴 리뷰들(로그인 뒤 — SH01 전에는 빈 목록) */
		mine: ReviewData[];
		now: number;
		onquery: (query: ReviewQuery) => void;
		onneedlogin: (reason: string) => void;
	}

	let {
		gameId,
		recommendCount,
		reviewCount,
		query,
		first,
		phrases,
		version,
		mine,
		now,
		onquery,
		onneedlogin
	}: Props = $props();

	// 거르기 · 정렬이 바뀌면(first 가 새로 오면) 처음 묶음으로 — 쓰기 가능한 $derived
	/** 지금 버전에 쓴 내 리뷰 — 있으면 '리뷰 쓰기' 대신 맨 위에(사용자 결정 2026-11-28) */
	const myReview = $derived(myReviewForVersion(mine, version));
	let editingMine = $state(false);
	let items = $derived(first.items.filter((r) => r.id !== myReview?.id));
	let nextCursor = $derived(first.nextCursor);
	let loading = $state(false);
	let failed = $state(false);
	/** 답글을 쓰고 있는 리뷰와 답할 사람 */
	let replyTo = $state<{ reviewId: string; name: string } | null>(null);
	const total = $derived(first.total ?? first.items.length);

	const profileHref = (slug: string) => resolve('/(makers)/makers/[slug]', { slug });

	async function loadMore() {
		if (loading || !nextCursor) return;
		loading = true;
		failed = false;
		const params = reviewSearchParams(query);
		params.set('game', gameId);
		params.set('cursor', nextCursor);
		try {
			const res = await fetch(`/api/reviews?${params.toString()}`);
			if (!res.ok) throw new Error(String(res.status));
			const more = await res.json<{ items: ReviewData[]; nextCursor: string | null }>();
			items = [...items, ...more.items];
			nextCursor = more.nextCursor;
		} catch {
			failed = true;
		} finally {
			loading = false;
		}
	}
</script>

<div class="grid grid-cols-[minmax(0,1fr)_392px] items-start gap-14">
	<div class="flex max-w-180 min-w-0 flex-col gap-8">
		{#if myReview && editingMine}
			<ReviewForm
				editing={{ keywords: myReview.phrases, body: myReview.body }}
				onsubmit={() => {
					onneedlogin('리뷰를 고치려면');
				}}
				oncancel={() => (editingMine = false)}
			/>
		{:else if myReview}
			<!-- 버전마다 하나 — 이미 쓴 사람에게는 쓰기 대신 내 리뷰를 먼저, 가볍게 이유를 알림 -->
			<section aria-label="내 리뷰" class="rounded-xl p-5 inset-ring inset-ring-line-strong">
				<p class="mb-5 flex flex-wrap items-center gap-2 text-meta text-ink-3">
					<span
						class="inline-flex h-5 items-center rounded-full bg-accent-tint px-2 text-caption font-heavy text-accent-text"
					>
						내 리뷰{version ? ` · ${version}` : ''}
					</span>
					리뷰는 버전마다 하나씩 남길 수 있어요. 새 버전이 나오면 또 들려주세요!
				</p>
				<ReviewItem
					review={myReview}
					{now}
					{profileHref}
					onreplyto={(name: string) => (replyTo = { reviewId: myReview.id, name })}
					onedit={() => (editingMine = true)}
					onreplyclose={() => {
						if (replyTo?.reviewId === myReview.id) replyTo = null;
					}}
					replyForm={replyTo?.reviewId === myReview.id ? replyFormFor : undefined}
				/>
			</section>
		{:else}
			<ReviewForm
				onsubmit={() => {
					onneedlogin('리뷰를 올리려면');
				}}
			/>
		{/if}
		<div class="flex flex-col">
			{#if items.length === 0}
				<p class="rounded-2xl bg-sunken px-6 py-14 text-center text-body break-words text-ink-3">
					{query.phrase
						? `‘${query.phrase}’를 고른 리뷰가 없어요`
						: '아직 리뷰가 없어요. 첫 리뷰를 남겨 주세요!'}
				</p>
			{:else}
				<h2 class="sr-only">리뷰 목록</h2>
				{#each items as review (review.id)}
					<ReviewItem
						{review}
						{now}
						{profileHref}
						onreplyto={(name: string) => (replyTo = { reviewId: review.id, name })}
						onreport={() => {
							onneedlogin('리뷰를 신고하려면');
						}}
						onreplyclose={() => {
							if (replyTo?.reviewId === review.id) replyTo = null;
						}}
						replyForm={replyTo?.reviewId === review.id ? replyFormFor : undefined}
					/>
				{/each}
				{#if nextCursor !== null || failed}
					<div class="pt-2">
						<Button onclick={loadMore} disabled={loading}>
							{#if failed}다시 시도{:else if loading}불러오는 중{:else}리뷰 {(
									total - items.length
								).toLocaleString('ko-KR')}개 더 보기{/if}
						</Button>
					</div>
				{/if}
			{/if}
		</div>
	</div>

	<aside class="sticky top-[calc(var(--header-h)+80px)] flex flex-col gap-4">
		<div class="grid grid-cols-2 rounded-lg bg-sunken">
			<p class="flex flex-col gap-0.5 px-4.5 py-4">
				<b class="text-heading-lg font-heavy text-ink-1">
					{recommendCount.toLocaleString('ko-KR')}
				</b>
				<span class="text-meta font-medium text-ink-3">명이 추천</span>
			</p>
			<p class="flex flex-col gap-0.5 border-l border-line px-4.5 py-4">
				<b class="text-heading-lg font-heavy text-ink-1">{reviewCount.toLocaleString('ko-KR')}</b>
				<span class="text-meta font-medium text-ink-3">개 리뷰</span>
			</p>
		</div>
		{#if phrases.length > 0}
			<div>
				<b class="mb-2 block text-meta font-heavy text-ink-3">키워드로 보기</b>
				<div
					role="group"
					aria-label="키워드 — 하나를 고르면 그 키워드를 고른 리뷰만"
					class="flex flex-wrap gap-1.5"
				>
					{#each phrases as p (p.phrase)}
						<Chip
							pressed={query.phrase === p.phrase}
							count={p.count}
							onclick={() => {
								onquery({ ...query, phrase: query.phrase === p.phrase ? null : p.phrase });
							}}
						>
							{p.phrase}
						</Chip>
					{/each}
				</div>
			</div>
		{/if}
		<div>
			<b class="mb-2 block text-meta font-heavy text-ink-3">정렬</b>
			<Segmented
				label="리뷰 정렬"
				value={query.sort}
				items={REVIEW_SORTS.map((s) => ({ value: s, label: REVIEW_SORT_LABEL[s] }))}
				onchange={(v) => {
					onquery({ ...query, sort: v as ReviewSort });
				}}
			/>
		</div>
	</aside>
</div>

{#snippet replyFormFor()}
	{#if replyTo}
		{#key replyTo.name}
			<ReplyForm
				to={replyTo.name}
				me={null}
				onsubmit={() => {
					onneedlogin('답글을 달려면');
				}}
				oncancel={() => (replyTo = null)}
			/>
		{/key}
	{/if}
{/snippet}
