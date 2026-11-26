import type { TextSize } from './text-size.types';

/**
 * 트래킹은 크기의 함수다. 역할(Display / Headline / Body)과 무관하게
 * 크기가 정해지면 트래킹도 정해진다. 커질수록 조인다.
 *
 * 한글은 라틴보다 자폭이 넓어 큰 크기에서 기본 트래킹이 눈에 띄게 헐렁하다.
 * 37px 이상에서 이 보정이 없으면 히어로 헤드라인이 흩어져 보인다.
 */
export const textSizeToTrackingStyle: Record<TextSize, string> = {
	/* 12px */ '4xs': 'tracking-[-0.008em]',
	/* 14px */ '3xs': 'tracking-[-0.014em]',
	/* 16px */ '2xs': 'tracking-[-0.020em]',
	/* 18px */ xs: 'tracking-[-0.024em]',
	/* 21px */ sm: 'tracking-[-0.028em]',
	/* 24px */ md: 'tracking-[-0.030em]',
	/* 28px */ lg: 'tracking-[-0.034em]',
	/* 32px */ xl: 'tracking-[-0.036em]',
	/* 37px */ '2xl': 'tracking-[-0.038em]',
	/* 43px */ '3xl': 'tracking-[-0.040em]',
	/* 50px */ '4xl': 'tracking-[-0.040em]'
};
