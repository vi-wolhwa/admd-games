<script lang="ts">
	import { type Person, REPLY_BODY_MAX } from '#lib/domain/review.ts';
	import Button from '#lib/ui/primitives/Button.svelte';
	import CatFace from '#lib/ui/primitives/CatFace.svelte';

	/**
	 * 답글 쓰기 — 누구나(로그인 뒤). 답할 사람의 '@닉네임 '이 앞에 자동으로 들어간다(사용자 결정 2026-11-28).
	 * 다른 답글처럼 내 얼굴 · 닉네임 줄 아래, 답글 글이 시작하는 자리에서 입력 칸이 시작한다(들여쓰기).
	 * @닉네임 말고 내용이 없으면 올릴 수 없다. 200자까지, 도배 방지로 1분에 하나(waitSeconds 동안 못 올림).
	 * 저장은 SH01 — 지금은 onsubmit 이 로그인 안내를 띄운다.
	 */
	interface Props {
		/** 답할 사람 닉네임 */
		to: string;
		/** 나 — 로그인 전(SH01 전)이면 null: 빈 얼굴 + '나' */
		me: Person | null;
		/** 방금 답글을 올려 다음 답글까지 남은 초(0 이면 바로) */
		waitSeconds?: number;
		onsubmit: (body: string) => void;
		oncancel: () => void;
	}

	let { to, me, waitSeconds = 0, onsubmit, oncancel }: Props = $props();

	// 처음 한 번만 '@닉네임 '을 채운다(이후는 사용자 글)
	// svelte-ignore state_referenced_locally
	let body = $state(`@${to} `);
	const content = $derived(body.replace(/^@[가-힣A-Za-z]{1,15}\s*/, '').trim());
	const ready = $derived(content.length > 0 && waitSeconds <= 0);
	const waitId = 'reply-wait';

	function focusEnd(node: HTMLTextAreaElement) {
		node.focus();
		node.setSelectionRange(node.value.length, node.value.length);
	}
</script>

<form
	class="flex flex-col gap-1"
	onsubmit={(e) => {
		e.preventDefault();
		if (ready) onsubmit(body.trim());
	}}
>
	<div class="flex items-center gap-2.5">
		{#if me}
			<CatFace eyes={me.faceChar} mouth={me.faceMouth} color={me.faceColor} size="sm" />
			<b class="truncate text-label font-heavy text-ink-1">{me.name}</b>
		{:else}
			<CatFace eyes="" mouth="" color="blank" size="sm" />
			<b class="text-label font-heavy text-ink-1">나</b>
		{/if}
	</div>
	<div class="ml-9 flex flex-col gap-2">
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
			{#if waitSeconds > 0}
				<span id={waitId} class="mr-1 text-meta text-ink-3" aria-live="polite">
					답글은 1분에 하나씩 — {waitSeconds}초 뒤에 올릴 수 있어요
				</span>
			{/if}
			<Button size="sm" onclick={oncancel}>취소</Button>
			<Button
				type="submit"
				size="sm"
				variant="primary"
				disabled={!ready}
				aria-describedby={waitSeconds > 0 ? waitId : undefined}
			>
				답글 올리기
			</Button>
		</div>
	</div>
</form>
