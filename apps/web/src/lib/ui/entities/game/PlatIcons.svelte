<script lang="ts">
	import { type GameCardData, LAUNCH_LABEL } from '#lib/domain/game.ts';
	import Icon from '#lib/ui/primitives/Icon.svelte';
	import type { IconName } from '#lib/ui/primitives/icons.ts';
	import Tooltip from '#lib/ui/primitives/Tooltip.svelte';

	/** 그림 오른쪽 위 실행 칩: 실행 방식 · 휴대폰 · 여럿이 · 보안 검사. 마우스 · 키보드 포커스로 뜻을 펼친다 */
	interface Props {
		game: Pick<GameCardData, 'launch' | 'phone' | 'playersMax' | 'scanPassed'>;
	}

	let { game }: Props = $props();

	const lines = $derived(
		[
			{
				icon: game.launch === 'web' ? 'web' : 'download',
				text: LAUNCH_LABEL[game.launch],
				ok: false
			},
			game.phone && { icon: 'phone', text: '휴대폰에서도 가능', ok: false },
			game.playersMax >= 2 && {
				icon: 'duo',
				text: `여럿이 같이 · 최대 ${String(game.playersMax)}명`,
				ok: false
			},
			game.scanPassed && { icon: 'shield', text: '보안 검사 통과', ok: true }
		].filter((l): l is { icon: IconName; text: string; ok: boolean } => !!l)
	);
</script>

<Tooltip>
	{#snippet trigger({ props })}
		<button
			{...props}
			type="button"
			aria-label={lines.map((l) => l.text).join(' · ')}
			class="relative z-(--z-art-overlay) inline-flex h-(--badge-h) cursor-help items-center gap-1.5 rounded-full bg-scrim px-2 text-on-ink backdrop-blur-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-on-ink"
		>
			{#each lines as l (l.icon)}
				<Icon name={l.icon} size={12} class={l.ok ? 'text-ok-on-ink' : undefined} />
			{/each}
		</button>
	{/snippet}
	{#each lines as l (l.icon)}
		<span class={['flex items-center gap-1.75', l.ok && 'text-ok-on-ink']}>
			<Icon name={l.icon} size={13} class={l.ok ? undefined : 'opacity-75'} />
			{l.text}
		</span>
	{/each}
</Tooltip>
