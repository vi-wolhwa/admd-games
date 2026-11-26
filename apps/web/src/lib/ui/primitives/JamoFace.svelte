<script lang="ts">
	/**
	 * 자모 얼굴 — 사람(리뷰어 · 메이커)의 얼굴. 글자 두 개가 눈, 'ㅅ' 이 입(예: ㅅㅅㅅ).
	 * 색은 같은 휘도 12색(tokens.css --color-face-*) — 흰 글자 5.1:1. 장식이라 스크린리더는 이름을 읽는다.
	 */
	interface Props {
		char: string;
		/** hong · ju · gyul · hwang · olive · pul · bichwi · cheongnok · haneul · jjok · bora · jadu */
		color: string;
		size?: 'sm' | 'md' | 'lg';
	}

	let { char, color, size = 'md' }: Props = $props();

	/* 얼굴 타일 12색은 이 컴포넌트만 쓰는 원시 팔레트(tokens.css --color-face-*). 클래스로 적어야 빌드에 들어간다 */
	const BG: Record<string, string> = {
		hong: 'bg-face-hong',
		ju: 'bg-face-ju',
		gyul: 'bg-face-gyul',
		hwang: 'bg-face-hwang',
		olive: 'bg-face-olive',
		pul: 'bg-face-pul',
		bichwi: 'bg-face-bichwi',
		cheongnok: 'bg-face-cheongnok',
		haneul: 'bg-face-haneul',
		jjok: 'bg-face-jjok',
		bora: 'bg-face-bora',
		jadu: 'bg-face-jadu'
	};
</script>

<span
	aria-hidden="true"
	style:font-size={{ sm: '10px', md: '12px', lg: '20px' }[size]}
	class={[
		'inline-flex shrink-0 items-center justify-center leading-none font-heavy tracking-[-0.06em] whitespace-nowrap text-on-ink',
		BG[color] ?? BG.jjok,
		size === 'sm' && 'size-(--face-sm) rounded-[7px]',
		size === 'md' && 'size-(--face-md) rounded-[9px]',
		size === 'lg' && 'size-(--face-lg) rounded-[14px]'
	]}
>
	{char}<i class="relative top-[0.06em] mx-[0.02em] not-italic" style:font-size="0.78em">
		ㅅ
	</i>{char}
</span>
