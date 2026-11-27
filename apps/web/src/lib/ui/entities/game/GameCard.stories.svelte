<script module lang="ts">
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import { expect, screen } from 'storybook/test';

	import { sampleCards, STORY_NOW } from '#lib/fixtures/games.ts';

	import GameCard from './GameCard.svelte';

	const cards = sampleCards();
	const pick = (slug: string) => {
		const c = cards.find((g) => g.slug === slug);
		if (!c) throw new Error(slug);
		return c;
	};
	// 브라우저 + 휴대폰 · 신작 · 둘이서 · 다운로드
	const shown = [
		pick('loop-debugger'),
		pick('tessellate'),
		pick('paper-vector'),
		pick('null-pointer'),
		// 예외: 아주 긴 제목 · 메이커 이름
		pick('cloud-post-office')
	];

	const { Story } = defineMeta({ title: 'Entities/Game/GameCard', component: GameCard });
</script>

<Story
	name="상태 모음"
	asChild
	play={async ({ canvas }) => {
		// 실행 칩에 키보드 포커스가 오면 뜻을 펼친다. 설치형은 다운로드 아이콘만(보안 검사는 상세에서)
		const chip = canvas.getByRole('button', { name: '다운로드해서 설치' });
		chip.focus();
		await expect(await screen.findByText('다운로드해서 설치', { selector: 'span' })).toBeVisible();
		// 포커스를 풀어 캡처는 늘 같은 모습으로(켜진 카드는 미리보기가 돌아 찍는 순간마다 달라짐)
		chip.blur();
	}}
>
	<ul class="grid w-280 grid-cols-4 gap-6">
		{#each shown as game (game.id)}
			<li><GameCard {game} href={`#${game.slug}`} now={STORY_NOW} highlightTags={['퍼즐']} /></li>
		{/each}
	</ul>
</Story>
