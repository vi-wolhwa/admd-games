<script lang="ts">
	import { slide } from 'svelte/transition';

	import {
		REVIEW_BODY_MAX,
		REVIEW_KEYWORD_GROUPS,
		REVIEW_KEYWORDS_MAX,
		reviewHint,
		toggleKeyword
	} from '#lib/domain/review.ts';
	import Button from '#lib/ui/primitives/Button.svelte';
	import Chip from '#lib/ui/primitives/Chip.svelte';
	import Icon from '#lib/ui/primitives/Icon.svelte';

	/**
	 * 리뷰 쓰기 — 평소엔 한 줄로 닫혀 있다가 누르면 그 자리에서 펼쳐진다(쓰는 칸이 커서, 사용자 결정 2026-11-28).
	 * 키워드는 성격별 묶음에서 1~5개(네이버 방식, 좋은 점만) + 리뷰 글(빈 리뷰 불가, 500자까지).
	 * 안내는 차례로: '키워드를 1개 이상 골라 주세요' → '리뷰를 작성해 주세요' → 둘 다면 올리기 켜짐.
	 * 저장은 로그인(SH01) 뒤 — 지금은 onsubmit 이 로그인 안내를 띄운다.
	 */
	interface Props {
		onsubmit: (review: { keywords: string[]; body: string }) => void;
		/** 처음부터 펼쳐 둘지(갤러리용) */
		initiallyOpen?: boolean;
	}

	let { onsubmit, initiallyOpen = false }: Props = $props();

	// 처음 한 번만 읽는 값 — 그 뒤 열고 닫기는 이 칸이 스스로
	// svelte-ignore state_referenced_locally
	let open = $state(initiallyOpen);
	let picked = $state<string[]>([]);
	let body = $state('');
	const hint = $derived(reviewHint(picked, body));
	const full = $derived(picked.length >= REVIEW_KEYWORDS_MAX);
	const hintId = 'review-form-hint';
	const formId = 'review-form';

	const reduced =
		typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

	function close() {
		open = false;
		picked = [];
		body = '';
	}
</script>

<section class="rounded-xl inset-ring inset-ring-line-strong" aria-labelledby="review-form-title">
	{#if open}
		<div class="flex items-center gap-3 px-5 pt-5">
			<span class="flex size-9 items-center justify-center rounded-full bg-sunken text-ink-3">
				<Icon name="pen" size={16} />
			</span>
			<h2 id="review-form-title" class="flex-1 text-title font-heavy text-ink-1">리뷰 쓰기</h2>
		</div>
	{:else}
		<button
			type="button"
			aria-expanded="false"
			aria-controls={formId}
			onclick={() => (open = true)}
			class="group flex w-full items-center gap-3 rounded-xl p-4 text-left transition-colors hover:bg-sunken focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
		>
			<span class="flex size-9 items-center justify-center rounded-full bg-sunken text-ink-3">
				<Icon name="pen" size={16} />
			</span>
			<span id="review-form-title" class="flex-1 text-body text-ink-3">
				이 게임, 어떤 점이 좋았나요?
			</span>
			<span
				class="inline-flex h-(--btn-h-sm) items-center rounded-full bg-accent px-4 text-label font-bold text-on-accent group-hover:bg-accent-strong"
			>
				리뷰 쓰기
			</span>
		</button>
	{/if}

	{#if open}
		<form
			id={formId}
			transition:slide={{ duration: reduced ? 0 : 240 }}
			class="flex flex-col gap-5 px-5 pt-4 pb-5"
			onsubmit={(e) => {
				e.preventDefault();
				if (hint === null) onsubmit({ keywords: picked, body: body.trim() });
			}}
		>
			<fieldset class="flex flex-col gap-3">
				<legend class="mb-3 flex w-full items-baseline justify-between">
					<span class="text-label font-heavy text-ink-1">어떤 점이 좋았나요?</span>
					<span class="text-meta text-ink-3" aria-live="polite">
						{picked.length} / {REVIEW_KEYWORDS_MAX}개
					</span>
				</legend>
				<!-- 성격별 묶음(네이버처럼) — 키워드가 늘어도 찾기 쉽게 -->
				{#each REVIEW_KEYWORD_GROUPS as group (group.label)}
					<div class="grid grid-cols-[136px_minmax(0,1fr)] items-start gap-3">
						<span class="pt-1.5 text-meta font-bold text-ink-3">{group.label}</span>
						<div class="flex flex-wrap gap-1.5" role="group" aria-label={group.label}>
							{#each group.keywords as k (k)}
								<Chip
									pressed={picked.includes(k)}
									disabled={full && !picked.includes(k)}
									onclick={() => {
										picked = toggleKeyword(picked, k);
									}}
								>
									{k}
								</Chip>
							{/each}
						</div>
					</div>
				{/each}
			</fieldset>
			<label class="flex flex-col gap-1.5">
				<span class="text-label font-heavy text-ink-1">리뷰</span>
				<textarea
					bind:value={body}
					rows="4"
					maxlength={REVIEW_BODY_MAX}
					placeholder="아쉬운 점도 여기에 적어 주면 메이커에게 도움이 돼요"
					class="resize-y rounded-md bg-bg p-3 text-body leading-[1.6] text-ink-1 inset-ring inset-ring-line-strong outline-none placeholder:text-ink-3 focus:inset-ring-2 focus:inset-ring-accent"
				></textarea>
				<span class="self-end text-caption text-ink-3">
					{body.length.toLocaleString('ko-KR')} / {REVIEW_BODY_MAX.toLocaleString('ko-KR')}
				</span>
			</label>
			<div class="flex items-center justify-end gap-2">
				{#if hint}
					<span id={hintId} class="mr-1 text-meta text-ink-3" aria-live="polite">{hint}</span>
				{/if}
				<Button size="sm" onclick={close}>취소</Button>
				<Button
					type="submit"
					variant="primary"
					size="sm"
					disabled={hint !== null}
					aria-describedby={hint ? hintId : undefined}
				>
					리뷰 올리기
				</Button>
			</div>
		</form>
	{/if}
</section>
