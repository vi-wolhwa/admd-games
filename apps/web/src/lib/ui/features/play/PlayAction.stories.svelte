<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';

	import PlayAction from './PlayAction.svelte';

	const record = { lastPlayedAt: 0, totalMinutes: 72, progress: null };

	// 상태마다 무엇을 보이는지(ADR 0011 §1). '해 본 적 있음' · '진행 중' 은 플레이 기록(PG06) · SDK 뒤에 실제로 생김
	const { Story } = defineMeta({ title: 'Features/Play/PlayAction', component: PlayAction });
</script>

<Story name="상태 모음" asChild>
	<div class="grid w-200 grid-cols-3 items-start gap-6">
		<PlayAction action={{ kind: 'first' }} scanPassed={false} />
		<PlayAction action={{ kind: 'played', record }} scanPassed={false} ready />
		<PlayAction action={{ kind: 'resume', record, progress: 0.45 }} scanPassed={false} ready />
		<PlayAction action={{ kind: 'download' }} scanPassed />
		<PlayAction action={{ kind: 'unsupported', devices: ['phone', 'pad'] }} scanPassed={false} />
	</div>
</Story>
