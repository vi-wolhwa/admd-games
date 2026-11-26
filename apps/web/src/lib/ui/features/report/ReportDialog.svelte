<script lang="ts">
	import { Dialog, RadioGroup } from 'bits-ui';

	import Button from '#lib/ui/primitives/Button.svelte';

	/**
	 * 문제 알리기(ADR 0011 §5). 실행 · 버그 · 설명 → 메이커 피드백함(MG07) + 운영자, 부적절 · 저작권 → 운영자(AD02).
	 * 로그인한 사람만 — 페이지에는 로그인(SH01) 때 붙인다(결정 2026-11-28). 지금은 갤러리에서 모습만 본다.
	 */
	export type ReportReason = 'broken' | 'bug' | 'mismatch' | 'inappropriate' | 'copyright';

	interface Props {
		open: boolean;
		gameTitle: string;
		onopenchange: (open: boolean) => void;
		onsubmit: (report: { reason: ReportReason; detail: string }) => void;
		/** 갤러리 캡처용 — 문서 맨 끝(portal)이 아니라 그 자리에 그린다 */
		inline?: boolean;
	}

	let { open, gameTitle, onopenchange, onsubmit, inline = false }: Props = $props();

	const REASONS: { value: ReportReason; label: string; hint: string }[] = [
		{ value: 'broken', label: '실행이 안 돼요', hint: '메이커와 운영자가 함께 봐요' },
		{ value: 'bug', label: '버그가 있어요', hint: '메이커와 운영자가 함께 봐요' },
		{ value: 'mismatch', label: '설명과 달라요', hint: '메이커와 운영자가 함께 봐요' },
		{ value: 'inappropriate', label: '부적절한 내용', hint: '운영자가 확인해요' },
		{ value: 'copyright', label: '저작권', hint: '운영자가 확인해요' }
	];

	let reason = $state<ReportReason | ''>('');
	let detail = $state('');
</script>

<Dialog.Root {open} onOpenChange={onopenchange}>
	<Dialog.Portal disabled={inline}>
		<Dialog.Overlay class={[inline ? 'hidden' : 'fixed inset-0 z-(--z-modal) bg-scrim']} />
		<Dialog.Content
			class={[
				'z-(--z-modal) flex w-110 flex-col gap-4 rounded-2xl bg-bg p-6 shadow-pop ring-1 ring-line-strong',
				!inline && 'fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2'
			]}
		>
			<div>
				<Dialog.Title class="text-heading font-heavy text-ink-1">문제 알리기</Dialog.Title>
				<Dialog.Description class="mt-1 text-label text-ink-3">
					‘{gameTitle}’에 어떤 문제가 있나요?
				</Dialog.Description>
			</div>
			<RadioGroup.Root
				value={reason}
				onValueChange={(v) => (reason = v as ReportReason)}
				aria-label="문제 종류"
				class="flex flex-col gap-1.5"
			>
				{#each REASONS as r (r.value)}
					<RadioGroup.Item
						value={r.value}
						class="flex items-center justify-between rounded-md px-3.5 py-2.5 text-left inset-ring inset-ring-line-strong transition-colors hover:bg-sunken focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent data-[state=checked]:bg-ink-1 data-[state=checked]:text-bg data-[state=checked]:inset-ring-ink-1"
					>
						{#snippet children({ checked })}
							<span class="text-label font-bold">{r.label}</span>
							<span class={['text-meta', checked ? 'opacity-80' : 'text-ink-3']}>{r.hint}</span>
						{/snippet}
					</RadioGroup.Item>
				{/each}
			</RadioGroup.Root>
			<label class="flex flex-col gap-1.5">
				<span class="text-meta font-heavy text-ink-3">자세히(선택)</span>
				<textarea
					bind:value={detail}
					rows="3"
					maxlength="500"
					placeholder="언제, 어떻게 생겼는지 적어 주면 고치기 쉬워요"
					class="resize-none rounded-md bg-bg p-3 text-label text-ink-1 inset-ring inset-ring-line-strong outline-none placeholder:text-ink-3 focus:inset-ring-2 focus:inset-ring-accent"
				></textarea>
			</label>
			<div class="flex justify-end gap-2">
				<Dialog.Close>
					{#snippet child({ props })}
						<button
							{...props}
							type="button"
							class="h-(--btn-h-sm) rounded-full px-4 text-label font-bold text-ink-1 inset-ring inset-ring-line-strong hover:bg-sunken"
						>
							닫기
						</button>
					{/snippet}
				</Dialog.Close>
				<Button
					variant="primary"
					size="sm"
					disabled={reason === ''}
					onclick={() => {
						if (reason !== '') onsubmit({ reason, detail: detail.trim() });
					}}
				>
					보내기
				</Button>
			</div>
		</Dialog.Content>
	</Dialog.Portal>
</Dialog.Root>
