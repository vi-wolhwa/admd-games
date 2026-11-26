<script lang="ts">
	import { formatFullDate } from '#lib/domain/format.ts';
	import {
		DEVICE_LABEL,
		type GameDetail,
		LANGUAGE_LABEL,
		LENGTH_LABEL,
		playersLabel,
		splitDescription
	} from '#lib/domain/game.ts';
	import MakerCard from '#lib/ui/entities/maker/MakerCard.svelte';
	import InfoList from '#lib/ui/patterns/InfoList.svelte';
	import Button from '#lib/ui/primitives/Button.svelte';
	import Icon from '#lib/ui/primitives/Icon.svelte';
	import { resolve } from '$app/paths';

	/**
	 * 소개 탭(PG05 전용 — 다른 곳에서 쓰이면 그때 내림). 왼쪽 = 메이커가 쓴 소개 · 특징,
	 * 오른쪽 = 메이커 카드(누르면 이 메이커의 게임, 팔로우) → 게임 정보 → 문제 알리기.
	 * 정보는 머리글 없이 바로(사용자 피드백): 실행(기기 포함) · 한 판 · 인원 · 온라인/오프라인 · 언어 · 사양 · 보안 검사 · 공개.
	 */
	interface Props {
		game: GameDetail;
		/** 로그인이 필요한 행동을 눌렀을 때 — 무엇을 하려 했는지 */
		onneedlogin: (reason: string) => void;
	}

	let { game, onneedlogin }: Props = $props();

	const text = $derived(splitDescription(game.description));
	const devices = $derived(game.devices.map((d) => DEVICE_LABEL[d]).join(' · '));
	const info = $derived([
		{
			label: '실행',
			value: `${game.launch === 'web' ? '브라우저에서 바로' : '내려받아 설치'} · ${devices}`
		},
		{ label: '한 판', value: LENGTH_LABEL[game.length] },
		{ label: '인원', value: playersLabel(game.playersMin, game.playersMax) },
		{ label: '방식', value: game.online ? '온라인' : '오프라인' },
		...(game.languages.length > 0
			? [{ label: '언어', value: game.languages.map((l) => LANGUAGE_LABEL[l] ?? l).join(' · ') }]
			: []),
		...(game.minSpec ? [{ label: '사양', value: game.minSpec }] : []),
		...(game.launch === 'download' && game.scanPassed
			? [{ label: '보안 검사', value: scanned }]
			: []),
		{ label: '공개', value: formatFullDate(game.publishedAt) }
	]);
	const makerHref = $derived(
		`${resolve('/(play)/play/games')}?q=${encodeURIComponent(game.makerName)}`
	);
</script>

{#snippet scanned()}<span class="font-heavy text-ok-text">통과</span>{/snippet}

{#snippet follow()}
	<Button
		size="sm"
		onclick={() => {
			onneedlogin('메이커를 팔로우하려면');
		}}
	>
		팔로우
	</Button>
{/snippet}

<div class="grid grid-cols-[minmax(0,1fr)_392px] items-start gap-14">
	<div class="max-w-180 min-w-0">
		<h2 class="mb-3.5 text-heading font-heavy text-ink-1">소개</h2>
		{#if text.paragraphs.length === 0 && text.features.length === 0}
			<p class="text-body text-ink-3">메이커가 아직 소개를 쓰지 않았어요.</p>
		{/if}
		{#each text.paragraphs as p, i (i)}
			<p class="mb-4 text-lead leading-[1.8] break-words text-ink-1">{p}</p>
		{/each}
		{#if text.features.length > 0}
			<ul class="mt-5 flex flex-col gap-2.5">
				{#each text.features as f, i (i)}
					<li class="flex gap-2.5 text-body leading-[1.6] text-ink-1">
						<Icon name="check" size={14} class="mt-1.25 text-accent-text" />
						<span class="min-w-0 break-words">{f}</span>
					</li>
				{/each}
			</ul>
		{/if}
	</div>
	<aside class="sticky top-[calc(var(--header-h)+80px)] flex flex-col gap-4">
		<MakerCard
			name={game.makerName}
			gameCount={game.makerGameCount}
			href={makerHref}
			action={follow}
		/>
		<div class="rounded-lg bg-sunken px-4.5 py-3">
			<InfoList items={info} />
		</div>
		<div>
			<Button
				size="sm"
				onclick={() => {
					onneedlogin('문제를 알리려면');
				}}
			>
				<Icon name="flag" size={14} />문제 알리기
			</Button>
			<p class="mt-1.5 text-meta text-ink-3">
				실행이 안 돼요 · 버그 · 설명과 달라요 · 부적절한 내용 · 저작권
			</p>
		</div>
	</aside>
</div>
