<script lang="ts">
	import type { Snippet } from 'svelte';

	import type { Person } from '#lib/domain/review.ts';
	import CatFace from '#lib/ui/primitives/CatFace.svelte';
	import Popover from '#lib/ui/primitives/Popover.svelte';

	/**
	 * 사람(리뷰 · 답글 글쓴이, @멘션)을 누르면 뜨는 프로필 카드(사용자 결정 2026-11-28).
	 * 누구든 누를 수 있다 — 얼굴 · 닉네임 · (알면) 리뷰 수, 메이커스 프로필이 있으면 그리로 가는 링크.
	 * 플레이어 프로필 페이지(PG15)가 생기면 이 카드에서 잇는다.
	 */
	interface Props {
		person: Person & { reviewCount?: number };
		profileHref: (slug: string) => string;
		trigger: Snippet<[{ props: Record<string, unknown> }]>;
	}

	let { person, profileHref, trigger }: Props = $props();
</script>

<Popover {trigger}>
	<div class="flex w-60 flex-col gap-3.5">
		<div class="flex min-w-0 items-center gap-3">
			<CatFace eyes={person.faceChar} mouth={person.faceMouth} color={person.faceColor} size="lg" />
			<div class="min-w-0">
				<b class="block truncate text-body font-heavy text-ink-1">{person.name}</b>
				<span class="text-meta text-ink-3">
					{person.makerSlug ? '메이커' : '플레이어'}{person.reviewCount === undefined
						? ''
						: ` · 리뷰 ${person.reviewCount.toLocaleString('ko-KR')}개`}
				</span>
			</div>
		</div>
		{#if person.makerSlug}
			<!-- eslint-disable svelte/no-navigation-without-resolve -- 부르는 쪽이 resolve() 로 만든 주소 -->
			<a
				href={profileHref(person.makerSlug)}
				class="inline-flex h-(--btn-h-sm) items-center justify-center rounded-full bg-sunken text-label font-bold text-ink-1 transition-colors hover:bg-sunken-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
			>
				메이커스 프로필 보기
			</a>
			<!-- eslint-enable svelte/no-navigation-without-resolve -->
		{/if}
	</div>
</Popover>
