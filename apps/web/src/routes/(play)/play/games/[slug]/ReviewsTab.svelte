<script lang="ts">
	import {
		REVIEW_SORT_LABEL,
		REVIEW_SORTS,
		type ReviewData,
		type ReviewQuery,
		reviewSearchParams,
		type ReviewSort
	} from '#lib/domain/review.ts';
	import ReviewItem from '#lib/ui/entities/review/ReviewItem.svelte';
	import ReviewForm from '#lib/ui/features/review-write/ReviewForm.svelte';
	import Button from '#lib/ui/primitives/Button.svelte';
	import Chip from '#lib/ui/primitives/Chip.svelte';
	import Segmented from '#lib/ui/primitives/Segmented.svelte';

	/**
	 * 리뷰 탭(PG05 전용) — 왼쪽 = 리뷰 쓰기 + 한 열 목록, 오른쪽 = 요약 · 키워드로 보기 · 정렬(research/04-reviews.md).
	 * 쓰기 · 답글 · 신고는 로그인(SH01) 뒤 — 지금은 누르면 onneedlogin(결정 2026-11-28).
	 */
	interface Props {
		gameId: string;
		makerName: string;
		recommendCount: number;
		reviewCount: number;
		query: ReviewQuery;
		first: { items: ReviewData[]; nextCursor: string | null; total: number | null };
		phrases: { phrase: string; count: number }[];
		now: number;
		onquery: (query: ReviewQuery) => void;
		onneedlogin: (reason: string) => void;
	}

	let {
		gameId,
		makerName,
		recommendCount,
		reviewCount,
		query,
		first,
		phrases,
		now,
		onquery,
		onneedlogin
	}: Props = $props();

	// 거르기 · 정렬이 바뀌면(first 가 새로 오면) 처음 묶음으로 — 쓰기 가능한 $derived
	let items = $derived(first.items);
	let nextCursor = $derived(first.nextCursor);
	let loading = $state(false);
	let failed = $state(false);
	const total = $derived(first.total ?? first.items.length);

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
		<ReviewForm
			onsubmit={() => {
				onneedlogin('리뷰를 올리려면');
			}}
		/>
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
						{makerName}
						{now}
						onreply={() => {
							onneedlogin('메이커로 답글을 달려면');
						}}
						onreport={() => {
							onneedlogin('리뷰를 신고하려면');
						}}
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
		<p class="text-meta leading-[1.6] text-ink-3">
			싫어요는 없어요 — 아쉬운 점은 리뷰 글로 알려 줘요.
		</p>
	</aside>
</div>
