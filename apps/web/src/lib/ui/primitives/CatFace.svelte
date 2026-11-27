<script lang="ts">
	/**
	 * 고양이 얼굴 — 사람(플레이어 · 메이커)의 얼굴(사용자 결정 2026-11-28, 캔버스 SH01 · DS05).
	 * 고양이 머리 실루엣(귀 둘 + 둥근 얼굴) 위에 흰 글자로 눈 · 입 · 눈(예: ^ω^).
	 * 귀는 상자 위로 조금 나간다 — 상자 크기(--face-*)는 얼굴 부분 기준이라 옆 글자와 줄이 맞는다.
	 * 색은 같은 휘도 12색(tokens.css --color-face-*) — 흰 글자 5.1:1. 장식이라 스크린리더는 이름을 읽는다.
	 * color 'blank' = 아직 얼굴이 없는 자리(로그인 전 '나') — 회색 실루엣만.
	 */
	interface Props {
		/** 눈 글자(한 글자) */
		eyes: string;
		/** 입 글자(한 글자) */
		mouth: string;
		/** hong · ju · gyul · hwang · olive · pul · bichwi · cheongnok · haneul · jjok · bora · jadu · blank */
		color: string;
		/** two-line = 이름 · 정보 두 줄 옆(리뷰 글쓴이) */
		size?: 'sm' | 'md' | 'two-line' | 'lg';
	}

	let { eyes, mouth, color, size = 'md' }: Props = $props();

	/* 얼굴 12색은 이 컴포넌트만 쓰는 원시 팔레트(tokens.css --color-face-*). 클래스로 적어야 빌드에 들어간다 */
	const FILL: Record<string, string> = {
		hong: 'fill-face-hong',
		ju: 'fill-face-ju',
		gyul: 'fill-face-gyul',
		hwang: 'fill-face-hwang',
		olive: 'fill-face-olive',
		pul: 'fill-face-pul',
		bichwi: 'fill-face-bichwi',
		cheongnok: 'fill-face-cheongnok',
		haneul: 'fill-face-haneul',
		jjok: 'fill-face-jjok',
		bora: 'fill-face-bora',
		jadu: 'fill-face-jadu',
		blank: 'fill-sunken-hover'
	};
	/** 고양이 머리 — 100×100 안에 귀 끝(위) · 볼(양옆) · 턱(아래) */
	const HEAD =
		'M8 44Q8 24 11 8Q12 2 17 5L36 20Q50 16 64 20L83 5Q88 2 89 8Q92 24 92 44Q99 56 97 69Q93 97 50 97Q7 97 3 69Q1 56 8 44Z';
	const FONT = { sm: '10px', md: '12px', 'two-line': '16px', lg: '20px' } as const;
</script>

<span
	aria-hidden="true"
	style:font-size={FONT[size]}
	class={[
		'relative isolate inline-flex shrink-0 items-center justify-center pt-[0.5em] leading-none font-heavy whitespace-nowrap text-on-ink',
		size === 'sm' && 'size-(--face-sm)',
		size === 'md' && 'size-(--face-md)',
		size === 'two-line' && 'size-(--face-two-line)',
		size === 'lg' && 'size-(--face-lg)'
	]}
>
	<!-- 귀가 상자 위로(14%), 볼이 양옆으로(12%) 조금 나가게. svg 는 대체 요소라 inset 으로 늘지 않아 크기를 직접 -->
	<svg
		viewBox="0 0 100 100"
		preserveAspectRatio="none"
		class={['absolute top-[-14%] left-[-12%] -z-1 h-[118%] w-[124%]', FILL[color] ?? FILL.jjok]}
	>
		<path d={HEAD} />
	</svg>
	{#if color !== 'blank'}
		<b class="inline-flex items-center tracking-[-0.1em]" style:font-size="0.8em">
			{eyes}<i class="relative top-[0.02em] mx-[0.02em] not-italic" style:font-size="0.78em">
				{mouth}
			</i>{eyes}
		</b>
	{/if}
</span>
