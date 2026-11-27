<script lang="ts">
	import { REPLY_BODY_MAX } from '#lib/domain/review.ts';
	import Button from '#lib/ui/primitives/Button.svelte';

	/**
	 * 답글 쓰기 — 누구나(로그인 뒤). 답할 사람의 '@닉네임 '이 앞에 자동으로 들어간다(사용자 결정 2026-11-28).
	 * @닉네임 말고 내용이 없으면 올릴 수 없다. 저장은 SH01 — 지금은 onsubmit 이 로그인 안내를 띄운다.
	 */
	interface Props {
		/** 답할 사람 닉네임 */
		to: string;
		onsubmit: (body: string) => void;
		oncancel: () => void;
	}

	let { to, onsubmit, oncancel }: Props = $props();

	// 처음 한 번만 '@닉네임 '을 채운다(이후는 사용자 글)
	// svelte-ignore state_referenced_locally
	let body = $state(`@${to} `);
	const content = $derived(body.replace(/^@[가-힣A-Za-z]{1,15}\s*/, '').trim());
	const ready = $derived(content.length > 0);

	function focusEnd(node: HTMLTextAreaElement) {
		node.focus();
		node.setSelectionRange(node.value.length, node.value.length);
	}
</script>

<form
	class="flex flex-col gap-2"
	onsubmit={(e) => {
		e.preventDefault();
		if (ready) onsubmit(body.trim());
	}}
>
	<textarea
		{@attach focusEnd}
		bind:value={body}
		rows="2"
		maxlength={REPLY_BODY_MAX}
		aria-label={`${to}에게 답글`}
		class="resize-y rounded-md bg-bg p-2.5 text-body leading-[1.6] text-ink-1 inset-ring inset-ring-line-strong outline-none focus:inset-ring-2 focus:inset-ring-accent"
	></textarea>
	<div class="flex items-center justify-end gap-2">
		<span class="mr-auto text-caption text-ink-3">
			{body.length.toLocaleString('ko-KR')} / {REPLY_BODY_MAX.toLocaleString('ko-KR')}
		</span>
		<Button size="sm" onclick={oncancel}>취소</Button>
		<Button type="submit" size="sm" variant="primary" disabled={!ready}>답글 올리기</Button>
	</div>
</form>
