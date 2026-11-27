<script lang="ts">
	import { splitMentions } from '#lib/domain/profile.ts';

	/**
	 * 답글 글 — @닉네임 은 파란 글씨, 메이커스 프로필이 있으면 누르면 그리로(없으면 이동 없음, 사용자 결정 2026-11-28).
	 * mentions = 아는 닉네임 → 프로필 주소(서버가 찾아 줌). 목록에 없는 '@…' 은 그냥 글.
	 */
	interface Props {
		text: string;
		mentions: Record<string, string | null>;
		/** 메이커스 프로필 주소 만들기(라우트를 아는 쪽이 줌) */
		profileHref: (slug: string) => string;
	}

	let { text, mentions, profileHref }: Props = $props();

	const parts = $derived(splitMentions(text, (n) => n in mentions));
</script>

<!-- 한 줄로 — 줄바꿈 공백이 멘션과 조사 사이에 끼지 않게. 주소는 부르는 쪽이 resolve() 로 만든 것 -->
<!-- eslint-disable svelte/no-navigation-without-resolve -->
<!-- prettier-ignore -->
{#each parts as part, i (i)}{#if 'mention' in part}{@const slug = mentions[part.mention]}{#if slug}<a href={profileHref(slug)} class="font-bold text-accent-text hover:underline hover:underline-offset-3">@{part.mention}</a>{:else}<span class="font-bold text-accent-text">@{part.mention}</span>{/if}{:else}{part.text}{/if}{/each}
<!-- eslint-enable svelte/no-navigation-without-resolve -->
