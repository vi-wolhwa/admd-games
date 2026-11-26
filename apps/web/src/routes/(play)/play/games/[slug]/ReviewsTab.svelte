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
	import Button from '#lib/ui/primitives/Button.svelte';
	import Chip from '#lib/ui/primitives/Chip.svelte';
	import Segmented from '#lib/ui/primitives/Segmented.svelte';

	/**
	 * 리뷰 탭(PG05 전용) — 한 열 목록 + 오른쪽 요약 · 거르기(research/04-reviews.md).
	 * 읽기만: 추천하기 · 리뷰 쓰기 · 도움이 됐어요는 로그인(SH01) 뒤(결정 2026-11-28).
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
		onquery
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
	<div class="flex max-w-180 flex-col">
		{#if items.length === 0}
			<p class="rounded-2xl bg-sunken py-14 text-center text-body text-ink-3">
				{query.phrase ? `‘${query.phrase}’를 고른 리뷰가 없어요` : '아직 리뷰가 없어요'}
			</p>
		{:else}
			<h2 class="sr-only">리뷰 목록</h2>
			{#each items as review (review.id)}
				<ReviewItem {review} {makerName} {now} />
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

	<aside class="sticky top-[calc(var(--header-h)+80px)] flex flex-col gap-4">
		<div class="grid grid-cols-2 rounded-lg bg-sunken">
			<p class="flex flex-col gap-0.5 px-4.5 py-4">
				<b class="text-heading-lg font-heavy text-ink-1">
					{recommendCount.toLocaleString('ko-KR')}
				</b>
				<span class="text-meta font-medium text-ink-3">명이 추천</span>
			</p>
			<p class="flex flex-col gap-0.5 border-l border-line px-4.5 py-4">
				<b class="text-heading-lg font-heavy text-ink-1">
					{reviewCount.toLocaleString('ko-KR')}
				</b>
				<span class="text-meta font-medium text-ink-3">개 리뷰</span>
			</p>
		</div>
		{#if phrases.length > 0}
			<div>
				<b class="mb-2 block text-meta font-heavy text-ink-3">자주 고른 말로 보기</b>
				<div
					role="group"
					aria-label="자주 고른 말 — 하나를 고르면 그 말을 고른 리뷰만"
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
