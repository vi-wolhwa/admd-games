<script lang="ts">
	import { REVIEW_BODY_MAX, REVIEW_KEYWORDS } from '#lib/domain/review.ts';
	import Button from '#lib/ui/primitives/Button.svelte';
	import Chip from '#lib/ui/primitives/Chip.svelte';

	/**
	 * 리뷰 쓰기 — 키워드 1개 이상(네이버 방식, 좋은 점만) + 리뷰 글(빈 리뷰 불가, 500자까지) — 사용자 결정 2026-11-28.
	 * 안내는 차례로: 아무것도 없으면 '키워드를 1개 이상 골라 주세요' → 키워드만 고르면 '리뷰를 작성해 주세요' → 둘 다면 올리기 켜짐.
	 * 저장은 로그인(SH01) 뒤 — 지금은 onsubmit 이 로그인 안내를 띄운다.
	 */
	interface Props {
		onsubmit: (review: { keywords: string[]; body: string }) => void;
		oncancel: () => void;
	}

	let { onsubmit, oncancel }: Props = $props();

	let picked = $state<string[]>([]);
	let body = $state('');
	const hint = $derived(
		picked.length === 0
			? '키워드를 1개 이상 골라 주세요'
			: body.trim() === ''
				? '리뷰를 작성해 주세요'
				: null
	);
	const hintId = 'review-form-hint';

	function toggle(k: string) {
		picked = picked.includes(k) ? picked.filter((x) => x !== k) : [...picked, k];
	}
</script>

<form
	class="flex flex-col gap-3.5 rounded-lg p-5 inset-ring inset-ring-line-strong"
	onsubmit={(e) => {
		e.preventDefault();
		if (hint === null) onsubmit({ keywords: picked, body: body.trim() });
	}}
>
	<h2 class="text-title font-heavy text-ink-1">리뷰 쓰기</h2>
	<fieldset>
		<legend class="mb-2 text-meta font-heavy text-ink-3">어떤 점이 좋았나요? (1개 이상)</legend>
		<div class="flex flex-wrap gap-1.5">
			{#each REVIEW_KEYWORDS as k (k)}
				<Chip
					pressed={picked.includes(k)}
					onclick={() => {
						toggle(k);
					}}
				>
					{k}
				</Chip>
			{/each}
		</div>
	</fieldset>
	<label class="flex flex-col gap-1.5">
		<span class="text-meta font-heavy text-ink-3">리뷰</span>
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
		<Button size="sm" onclick={oncancel}>취소</Button>
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
