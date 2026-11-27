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
	/** 호버 미리보기 — 영상을 끝까지 튼 뒤 이미지를 순환 (ADR 0009 #6, 보강 #11) */
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

/**
 * 호버 때 보여 줄 차례: 영상 먼저(끝까지 재생) → 이미지 순환 → 다시 처음.
 * 영상이 사진보다 게임을 잘 보여 주므로 맨 앞(사용자 결정 2026-11-28, ADR 0009 보강 #11)
 */
export function hoverMedia(media: GameMedia[]): GameMedia[] {
	return [...media.filter((m) => m.kind === 'video'), ...media.filter((m) => m.kind === 'image')];
}

/** 기기 — 메이커가 고름(브라우저 게임만 휴대폰 · 패드 가능) */
export type Device = 'pc' | 'phone' | 'pad';
export const DEVICE_LABEL: Record<Device, string> = { pc: 'PC', phone: '휴대폰', pad: '패드' };

/** 게임 안 글자의 언어(코드 → 이름) */
export const LANGUAGE_LABEL: Record<string, string> = {
	ko: '한국어',
	en: '영어',
	ja: '일본어',
	zh: '중국어'
};

/** 상세(PG05)에 필요한 것 — 카드 정보 + 소개 · 플레이 정보. 정의: docs/product/game-metadata.md */
export interface GameDetail extends GameCardData {
	summary: string;
	/** 소개 · 특징 — 빈 줄로 문단, '- ' 로 시작하는 줄은 특징 목록 */
	description: string;
	makerSlug: string;
	/** 이 메이커의 공개 게임 수 */
	makerGameCount: number;
	devices: Device[];
	/** 온라인 — 다른 사람과 인터넷으로 함께하거나(멀티플레이) 순위 등을 볼 수 있음. false = 오프라인(혼자 하는 게임, 다른 사람과 상호작용 없음) */
	online: boolean;
	languages: string[];
	/** 최소 사양(설치형만) */
	minSpec: string | null;
	/** 지금 버전(예: v1.3) — 리뷰는 버전마다 한 사람 하나 */
	version: string | null;
	playersMin: number;
}

/** 소개 글을 문단과 특징 목록으로 나눈다 */
export function splitDescription(text: string): { paragraphs: string[]; features: string[] } {
	const paragraphs: string[] = [];
	const features: string[] = [];
	for (const block of text.split(/\n\s*\n/)) {
		const lines = block
			.split('\n')
			.map((l) => l.trim())
			.filter(Boolean);
		const prose = lines.filter((l) => !l.startsWith('- '));
		features.push(...lines.filter((l) => l.startsWith('- ')).map((l) => l.slice(2).trim()));
		if (prose.length > 0) paragraphs.push(prose.join(' '));
	}
	return { paragraphs, features };
}

/** 사람 수 표기 — 혼자 · 2명 · 2~4명 */
export function playersLabel(min: number, max: number): string {
	if (max <= 1) return '혼자';
	return min === max ? `${String(max)}명` : `${String(min)}~${String(max)}명`;
}
