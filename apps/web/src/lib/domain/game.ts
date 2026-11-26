/**
 * 게임 정보 — 화면 · 서버 공용 타입과 규칙. 필드 정의 원본: docs/product/game-metadata.md
 */

/** 한 판 길이 구간(메이커가 고름). 분 단위 정확한 값은 업데이트마다 틀어져서 구간만 둔다. */
export type LengthBucket = 1 | 2 | 3 | 4 | 5;

export const LENGTH_BUCKETS: readonly LengthBucket[] = [1, 2, 3, 4, 5];

export const LENGTH_LABEL: Record<LengthBucket, string> = {
	1: '5분 이하',
	2: '15분 이하',
	3: '30분 이하',
	4: '1시간 이하',
	5: '1시간 넘게'
};

/** 실행 방식 — 올린 빌드 종류로 플랫폼이 안다. */
export type Launch = 'web' | 'download';

export const LAUNCH_LABEL: Record<Launch, string> = {
	web: '브라우저에서 바로 플레이',
	download: '설치형 · 다운로드'
};

export interface GameMedia {
	kind: 'image' | 'video';
	url: string;
}

/** 카드 한 장을 그리는 데 필요한 것만. */
export interface GameCardData {
	id: string;
	slug: string;
	title: string;
	makerName: string;
	/** 태그 이름, 메이커가 적은 순서 */
	tags: string[];
	length: LengthBucket;
	launch: Launch;
	/** 휴대폰에서도 됨(브라우저 게임만 고를 수 있음) */
	phone: boolean;
	playersMax: number;
	/** 설치형 보안 검사 통과 */
	scanPassed: boolean;
	cover: string;
	/** 호버 미리보기 — 영상이 있으면 영상 1개, 없으면 이미지 순환 (ADR 0009 #6) */
	media: GameMedia[];
	recommendCount: number;
	reviewCount: number;
	/** 공개 시각(epoch ms) */
	publishedAt: number;
}

/** 태그 주소 이름 — 메이커가 적은 이름을 다듬은 것(대소문자 · 띄어쓰기만 맞춤, 한글 그대로) */
export function tagSlug(name: string): string {
	return name.trim().toLowerCase().replace(/\s+/g, '-');
}

const DAY = 24 * 60 * 60 * 1000;
/** '신작' 배지 기간 — 공개 후 14일 */
export const NEW_GAME_DAYS = 14;

export function isNewGame(publishedAt: number, now: number): boolean {
	const age = now - publishedAt;
	return age >= 0 && age < NEW_GAME_DAYS * DAY;
}

/** 호버 때 보여 줄 것: 영상이 있으면 그 영상 하나, 없으면 이미지 전부를 순환 */
export function hoverMedia(media: GameMedia[]): GameMedia[] {
	const video = media.find((m) => m.kind === 'video');
	return video ? [video] : media.filter((m) => m.kind === 'image');
}
