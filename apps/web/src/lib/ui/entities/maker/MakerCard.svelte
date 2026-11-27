<script lang="ts">
	import type { Snippet } from 'svelte';

	import { faceOf } from '#lib/domain/face.ts';
	import Icon from '#lib/ui/primitives/Icon.svelte';
	import JamoFace from '#lib/ui/primitives/JamoFace.svelte';

	/**
	 * 메이커 카드 — 카드 전체가 메이커스 프로필 링크.
	 * 오른쪽 자리(action)에 팔로우 같은 행동을 넣는다(행동은 features 층이 맡음).
	 */
	interface Props {
		name: string;
		gameCount: number;
		href: string;
		action?: Snippet;
	}

	let { name, gameCount, href, action }: Props = $props();
	const face = $derived(faceOf(name));
</script>

<div
	class="group relative grid grid-cols-[auto_minmax(0,1fr)_auto] items-center gap-3 rounded-lg bg-bg p-4 inset-ring inset-ring-line-strong transition-colors hover:bg-sunken hover:inset-ring-ink-4"
>
	<JamoFace char={face.char} color={face.color} size="lg" />
	<span class="min-w-0">
		<!-- eslint-disable svelte/no-navigation-without-resolve -- href 는 부르는 쪽이 resolve() 한 값 -->
		<a
			{href}
			class="block truncate text-lead font-heavy text-ink-1 outline-none after:absolute after:inset-0 after:rounded-lg focus-visible:after:outline-2 focus-visible:after:outline-offset-2 focus-visible:after:outline-accent"
		>
			{name}
		</a>
		<!-- eslint-enable svelte/no-navigation-without-resolve -->
		<span class="mt-0.5 flex items-center gap-1 text-meta text-ink-3">
			메이커 · 게임 {gameCount.toLocaleString('ko-KR')}개
			<Icon name="chevron" size={12} class="transition-transform group-hover:translate-x-0.5" />
		</span>
	</span>
	{#if action}
		<div class="relative z-(--z-art-overlay)">{@render action()}</div>
	{/if}
</div>
