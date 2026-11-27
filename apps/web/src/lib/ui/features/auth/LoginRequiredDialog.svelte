<script lang="ts">
	import { Dialog } from 'bits-ui';

	import Button from '#lib/ui/primitives/Button.svelte';

	/**
	 * 로그인이 필요한 행동을 눌렀을 때(리뷰 쓰기 · 답글 · 신고 · 팔로우 · 문제 알리기).
	 * 로그인 화면(SH01)이 생기면 '로그인' 버튼을 거기로 잇는다 — 지금은 준비 중 안내(결정 2026-11-28).
	 */
	interface Props {
		/** 무엇을 하려 했는지 — 예: '리뷰를 올리려면' . null 이면 닫힘 */
		reason: string | null;
		onclose: () => void;
		/** 갤러리 캡처용 — 그 자리에 그린다 */
		inline?: boolean;
	}

	let { reason, onclose, inline = false }: Props = $props();
</script>

<Dialog.Root
	open={reason !== null}
	onOpenChange={(open) => {
		if (!open) onclose();
	}}
>
	<Dialog.Portal disabled={inline}>
		<Dialog.Overlay class={[inline ? 'hidden' : 'fixed inset-0 z-(--z-modal) bg-scrim']} />
		<Dialog.Content
			class={[
				'z-(--z-modal) flex w-95 flex-col gap-4 rounded-2xl bg-bg p-6 shadow-pop ring-1 ring-line-strong',
				!inline && 'fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2'
			]}
		>
			<div>
				<Dialog.Title class="text-heading font-heavy text-ink-1">로그인이 필요해요</Dialog.Title>
				<Dialog.Description class="mt-1.5 text-body leading-[1.6] text-ink-2">
					{reason ?? ''} 로그인해 주세요. 로그인은 곧 열려요.
				</Dialog.Description>
			</div>
			<div class="flex justify-end gap-2">
				<Button size="sm" onclick={onclose}>닫기</Button>
				<Button size="sm" variant="primary" disabled>로그인 · 준비 중</Button>
			</div>
		</Dialog.Content>
	</Dialog.Portal>
</Dialog.Root>
