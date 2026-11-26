<script lang="ts">
	import type { Theme } from '#lib/domain/appearance.ts';
	import ThemeToggle from '#lib/ui/features/theme/ThemeToggle.svelte';
	import { resolve } from '$app/paths';

	/**
	 * PlayGround 사이트 헤더. **만든 페이지만** 보인다(결정 2026-11-28) — 홈 · 랭킹 · 검색 · 로그인 · 그라운드 전환은
	 * 그 페이지를 만들 때 붙인다. 로고(고양이)는 BR-1 결정 뒤 — 지금은 글자.
	 */
	interface Props {
		theme: Theme;
		/** 지금 페이지가 속한 메뉴 */
		current?: 'games';
	}

	let { theme, current }: Props = $props();

	const NAV = [{ id: 'games', label: '게임', href: resolve('/(play)/play/games') }] as const;
</script>

<header class="sticky top-0 z-(--z-header) bg-bg/94 backdrop-blur-md backdrop-saturate-180">
	<div class="mx-auto flex h-(--header-h) w-(--page-width) items-center gap-7">
		<a
			href={resolve('/(play)/play/games')}
			class="flex items-end gap-1.75 rounded-sm focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-accent"
		>
			<span class="text-heading leading-none font-heavy tracking-tight text-ink-1">aDmD</span>
			<span class="text-label font-heavy text-ink-2">PlayGround</span>
		</a>
		<nav aria-label="주 메뉴" class="flex gap-0.5">
			{#each NAV as item (item.id)}
				<!-- 밑줄은 글자 바로 아래(헤더 바닥이 아니라) — 카카오페이지 방식 -->
				<a
					href={item.href}
					aria-current={current === item.id ? 'page' : undefined}
					class={[
						'rounded-sm px-3 py-1 text-lead font-bold whitespace-nowrap transition-colors duration-(--dur-instant)',
						'focus-visible:outline-2 focus-visible:outline-accent',
						current === item.id ? 'text-ink-1' : 'text-ink-3 hover:text-ink-1'
					]}
				>
					<span
						class={[
							'relative',
							current === item.id &&
								'after:absolute after:inset-x-0 after:-bottom-1.5 after:h-0.5 after:rounded-full after:bg-accent'
						]}
					>
						{item.label}
					</span>
				</a>
			{/each}
		</nav>
		<div class="ml-auto flex items-center gap-2.5">
			<ThemeToggle {theme} />
		</div>
	</div>
</header>
