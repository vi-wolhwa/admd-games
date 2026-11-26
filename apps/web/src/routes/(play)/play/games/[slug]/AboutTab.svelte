<script lang="ts">
	import { formatFullDate } from '#lib/domain/format.ts';
	import {
		CAUTION_LABEL,
		CONTROL_LABEL,
		DEVICE_LABEL,
		type GameDetail,
		LANGUAGE_LABEL,
		LENGTH_LABEL,
		playersLabel,
		splitDescription
	} from '#lib/domain/game.ts';
	import MakerCard from '#lib/ui/entities/maker/MakerCard.svelte';
	import InfoList from '#lib/ui/patterns/InfoList.svelte';
	import Icon from '#lib/ui/primitives/Icon.svelte';

	/**
	 * 소개 탭(PG05 전용 — 다른 곳에서 쓰이면 그때 내림). 왼쪽 = 메이커가 쓴 소개 · 특징,
	 * 오른쪽 = 메이커 카드 → 플레이 정보 · 정보. 문제 알리기는 로그인(SH01) 때 이 아래에 붙인다.
	 */
	interface Props {
		game: GameDetail;
	}

	let { game }: Props = $props();

	const text = $derived(splitDescription(game.description));
	const join = (xs: string[]) => xs.join(' · ');
	const playInfo = $derived([
		{
			label: '실행',
			value: game.launch === 'web' ? '브라우저에서 바로 · 설치 없음' : '설치형 · 다운로드'
		},
		{ label: '기기', value: join(game.devices.map((d) => DEVICE_LABEL[d])) },
		...(game.controls.length > 0
			? [{ label: '조작', value: join(game.controls.map((c) => CONTROL_LABEL[c])) }]
			: []),
		{ label: '한 판', value: LENGTH_LABEL[game.length] },
		{ label: '인원', value: playersLabel(game.playersMin, game.playersMax) },
		...(game.languages.length > 0
			? [{ label: '언어', value: join(game.languages.map((l) => LANGUAGE_LABEL[l] ?? l)) }]
			: []),
		{
			label: '이용 주의',
			value: game.cautions.length > 0 ? join(game.cautions.map((c) => CAUTION_LABEL[c])) : '없음'
		},
		...(game.minSpec ? [{ label: '사양', value: game.minSpec }] : []),
		...(game.launch === 'download' && game.scanPassed
			? [{ label: '보안 검사', value: scanned }]
			: [])
	]);
</script>

{#snippet scanned()}<span class="font-heavy text-ok-text">통과</span>{/snippet}

<div class="grid grid-cols-[minmax(0,1fr)_392px] items-start gap-14">
	<div class="max-w-180">
		<h2 class="mb-3.5 text-heading font-heavy text-ink-1">소개</h2>
		{#each text.paragraphs as p, i (i)}
			<p class="mb-4 text-lead leading-[1.8] text-ink-1">{p}</p>
		{/each}
		{#if text.features.length > 0}
			<ul class="mt-5 flex flex-col gap-2.5">
				{#each text.features as f, i (i)}
					<li class="flex gap-2.5 text-body leading-[1.6] text-ink-1">
						<Icon name="check" size={14} class="mt-1.25 text-accent-text" />
						<span>{f}</span>
					</li>
				{/each}
			</ul>
		{/if}
	</div>
	<aside class="sticky top-[calc(var(--header-h)+80px)] flex flex-col gap-4">
		<MakerCard name={game.makerName} gameCount={game.makerGameCount} />
		<div class="rounded-lg bg-sunken px-4.5 py-4">
			<h3 class="mb-1.5 text-caption font-heavy text-ink-3">플레이</h3>
			<InfoList items={playInfo} />
			<div class="my-3 h-px bg-line"></div>
			<h3 class="mb-1.5 text-caption font-heavy text-ink-3">정보</h3>
			<InfoList items={[{ label: '공개', value: formatFullDate(game.publishedAt) }]} />
		</div>
	</aside>
</div>
