<script lang="ts">
	import { splitMentions } from '#lib/domain/profile.ts';
	import type { Person } from '#lib/domain/review.ts';

	import PersonPopover from './PersonPopover.svelte';

	/**
	 * 답글 글 — @닉네임 은 파란 글씨, 누구든 누르면 프로필 카드(사용자 결정 2026-11-28).
	 * mentions = 아는 닉네임 → 그 사람(서버가 찾아 줌). 목록에 없는 '@…' 은 그냥 글.
	 */
	interface Props {
		text: string;
		mentions: Record<string, Person>;
		/** 메이커스 프로필 주소 만들기(라우트를 아는 쪽이 줌) */
		profileHref: (slug: string) => string;
	}

	let { text, mentions, profileHref }: Props = $props();

	const parts = $derived(splitMentions(text, (n) => n in mentions));
</script>

<!-- 한 줄로 — 줄바꿈 공백이 멘션과 조사 사이에 끼지 않게 -->
<!-- prettier-ignore -->
{#each parts as part, i (i)}{#if 'mention' in part}{@const who = mentions[part.mention]}{#if who}<PersonPopover person={who} {profileHref}>{#snippet trigger({ props })}<button {...props} type="button" class="cursor-pointer rounded-xs font-bold text-accent-text hover:underline hover:underline-offset-3 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent">@{part.mention}</button>{/snippet}</PersonPopover>{:else}@{part.mention}{/if}{:else}{part.text}{/if}{/each}
