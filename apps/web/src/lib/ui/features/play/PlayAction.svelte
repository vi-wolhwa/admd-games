<script lang="ts">
	import type { Snippet } from 'svelte';

	import { formatPlayTime } from '#lib/domain/format.ts';
	import { DEVICE_LABEL } from '#lib/domain/game.ts';
	import type { PlayAction } from '#lib/domain/play-action.ts';
	import Icon from '#lib/ui/primitives/Icon.svelte';

	/**
	 * 게임 상세의 주 버튼 — 무엇을 보일지는 순수 함수 playAction 이 정한다(ADR 0011 §1).
	 * 지금은 플레이 화면(PG06) · 다운로드 파일 저장이 없어 버튼을 비활성으로 둔다(결정 2026-11-28).
	 */
	interface Props {
		action: PlayAction;
		/** 설치형 보안 검사 통과(공개된 설치형은 모두 통과 — 상세에서는 알려 줌) */
		scanPassed: boolean;
		/** 기능이 아직 없음 — 비활성 + 안내 */
		ready?: boolean;
		/** 주 버튼 오른쪽에 붙는 정사각형 버튼(추천 등 — 부르는 쪽이 넣음) */
		side?: Snippet;
	}

	let { action, scanPassed, ready = false, side }: Props = $props();

	const label = $derived(
		{
			first: '지금 플레이',
			played: '플레이',
			resume: '이어하기',
			download: '다운로드',
			unsupported: ''
		}[action.kind]
	);
	const noteId = 'play-action-note';
</script>

<div class="flex flex-col gap-2">
	{#if action.kind === 'unsupported'}
		<div class="flex items-start gap-2">
			<div class="flex flex-1 gap-3 rounded-lg bg-sunken p-4 text-label leading-[1.55] text-ink-2">
				<Icon name="phone" size={20} class="mt-0.5 text-ink-3" />
				<span>
					<b class="mb-0.5 block text-body font-bold text-ink-1">
						{action.devices.map((d) => DEVICE_LABEL[d]).join(' · ')}에서 열어 주세요
					</b>
					이 게임은 이 기기에서 할 수 없어요.
				</span>
			</div>
			{@render side?.()}
		</div>
	{:else}
		<div class="flex gap-2">
			<button
				type="button"
				disabled={!ready}
				aria-describedby={ready ? undefined : noteId}
				class="inline-flex h-14 flex-1 items-center justify-center gap-1.5 rounded-lg bg-accent text-title font-heavy text-on-accent transition-colors hover:bg-accent-strong focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent disabled:cursor-not-allowed disabled:opacity-45 disabled:hover:bg-accent"
			>
				<Icon name={action.kind === 'download' ? 'download' : 'play'} size={16} />
				{label}
			</button>
			{@render side?.()}
		</div>
		<!-- 준비 중 안내는 화면에서 뺌(사용자 피드백) — 화면 읽기 프로그램에만 이유를 알림 -->
		{#if !ready}
			<p id={noteId} class="sr-only">
				{action.kind === 'download' ? '다운로드는 준비 중이에요' : '플레이 화면은 준비 중이에요'}
			</p>
		{/if}
		{#if action.kind === 'resume'}
			<div class="rounded-md bg-sunken px-3.5 py-3">
				<div class="flex justify-between text-meta text-ink-3">
					<b class="text-ink-1">진행 {Math.round(action.progress * 100)}%</b>
					<span>모두 {formatPlayTime(action.record.totalMinutes)}</span>
				</div>
				<div class="mt-2 h-1.5 overflow-hidden rounded-full bg-sunken-hover">
					<i
						class="block h-full bg-accent"
						style:width={`${String(Math.round(action.progress * 100))}%`}
					></i>
				</div>
				<p class="mt-1.5 text-caption text-ink-3">이 게임이 진행도를 알려 줘요</p>
			</div>
		{:else if action.kind === 'played'}
			<p class="text-center text-meta text-ink-3">
				모두 {formatPlayTime(action.record.totalMinutes)} 했어요
			</p>
		{/if}
		{#if action.kind === 'download' && scanPassed}
			<p
				class="flex items-center gap-2.5 rounded-md bg-ok-tint px-3.5 py-3 text-label font-bold text-ok-text"
			>
				<Icon name="shield" size={16} />보안 검사 통과
			</p>
		{/if}
	{/if}
</div>
