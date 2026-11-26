export type TextColor = 'primary' | 'secondary' | 'tertiary' | 'quaternary' | 'inverse';

export type DisplayColor = TextColor;
export type HeadlineColor = TextColor;
export type BodyColor = TextColor;

/**
 * primary     본문 · 제목 — 기본값
 * secondary   설명문 · 2차 텍스트
 * tertiary    메타 · 라벨 · 보조 — 16px 이상 또는 비필수 정보에만
 * quaternary  비활성 · 구분선 텍스트 — 판독을 요구하지 않는 자리
 * inverse     어두운 배경 위
 */
