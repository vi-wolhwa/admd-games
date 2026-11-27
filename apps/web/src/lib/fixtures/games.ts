/**
 * 가짜 게임 24개 — 이야기(갤러리) · 테스트 · 미리보기/로컬 D1 시드 전용(운영 코드에서 import 금지).
 * 그림은 scripts/sample-art.ts 가 만든 static/sample/<slug>-<0~5>.svg (0 = 대표 그림).
 * 이름 · 메이커는 모두 지어낸 것.
 */
import type { GameCardData, LengthBucket } from '#lib/domain/game.ts';
import { SAMPLE_DETAILS, sampleReviewCount, sampleVersion } from '#lib/fixtures/game-details.ts';
import type { GameSeed } from '#lib/server/ports/catalog.ts';

/** 이야기의 '오늘' — 신작 배지가 매번 같게 보이도록 고정 */
export const STORY_NOW = Date.UTC(2026, 10, 28);

const DAY = 86_400_000;
export const SAMPLE_SHOTS = 5;
/** 미리보기 영상이 있는 가짜 게임(scripts/sample-video.ts 가 만든 4초 영상) */
export const SAMPLE_VIDEO_SLUGS = ['ashfall-runner', 'paper-vector', 'beat-garden'];

type Row = [
	slug: string,
	title: string,
	maker: string,
	tags: string[],
	length: LengthBucket,
	run: 'web' | 'web phone' | 'download',
	players: [number, number],
	recommend: number,
	review: number,
	daysAgo: number,
	summary: string
];

// 한 줄 = 게임 하나(표처럼 읽기)
// prettier-ignore
const ROWS: Row[] = [
	['ashfall-runner', '애쉬폴 러너', '잿빛토끼', ['액션', '아케이드'], 1, 'web phone', [1, 1], 2031, 296, 120, '재가 내리는 도시를 끝없이 달린다'],
	['loop-debugger', '루프 디버거', '픽셀상점', ['퍼즐', '프로그래밍'], 1, 'web phone', [1, 1], 214, 38, 60, '버그를 잡으면 칭찬받는 퍼즐'],
	['tessellate', '테셀레이트', '노을공방', ['퍼즐'], 2, 'web', [1, 1], 342, 54, 3, '조각을 겹치지 않게 빈틈없이 채운다'],
	['grid-runner', '그리드 러너', '보라네', ['액션', '퍼즐'], 1, 'web phone', [1, 1], 61, 6, 6, '격자 위에서 길을 바꾸며 달린다'],
	['tilt-theory', '틸트 이론', '기울기연구소', ['퍼즐', '물리'], 4, 'download', [1, 1], 284, 41, 90, '판을 기울여 구슬을 집으로'],
	['refactor-rush', '리팩터 러시', '새벽코딩', ['액션', '아케이드'], 1, 'web phone', [1, 1], 18, 3, 2, '마감 3분 전, 코드를 정리하라'],
	['solvent', '솔벤트', '물방울', ['퍼즐', '협동'], 2, 'web', [1, 2], 112, 17, 45, '둘이 섞여야 풀리는 물방울 퍼즐'],
	['paper-vector', '페이퍼 벡터', '벡터공방', ['액션', '대전'], 1, 'web', [2, 4], 1442, 216, 200, '종이비행기로 하는 네 명 대전'],
	['null-pointer', '널 포인터', '레몬게임즈', ['액션', '로그라이크'], 5, 'download', [1, 1], 96, 11, 30, '가리키는 곳이 사라지는 던전'],
	['block-post', '블록 우체국', '보라네', ['퍼즐', '경영'], 2, 'web phone', [1, 1], 188, 26, 75, '꾸러미를 쌓아 마을에 배달한다'],
	['city-of-ash', '재의 도시', '잿빛토끼', ['탐험', '이야기'], 5, 'download', [1, 1], 233, 35, 150, '타 버린 도시에 남은 이야기를 줍는다'],
	['lighthouse-night', '등대지기의 밤', '노을공방', ['이야기', '탐험'], 3, 'web', [1, 1], 521, 88, 20, '하룻밤 동안 등대를 지키는 이야기'],
	['beat-garden', '박자 정원', '귤껍질스튜디오', ['리듬'], 1, 'web phone', [1, 1], 377, 49, 10, '박자에 맞춰 꽃을 피운다'],
	['harbor-shop', '작은 항구 상회', '귤껍질스튜디오', ['경영', '전략'], 4, 'web', [1, 1], 145, 22, 55, '항구 가게를 키워 무역로를 연다'],
	['stardust', '별가루 채집', '물방울', ['탐험'], 2, 'web phone', [1, 1], 66, 9, 12, '밤하늘 아래 별가루를 모은다'],
	['three-walls', '성벽 셋', '벡터공방', ['전략'], 3, 'web', [1, 2], 98, 14, 80, '성벽 세 개로 마을을 지킨다'],
	['cat-mail', '고양이 우편', '새벽코딩', ['퍼즐', '이야기'], 2, 'web phone', [1, 1], 803, 120, 33, '고양이가 배달하는 편지 퍼즐'],
	['desert-radio', '사막 무전', '레몬게임즈', ['탐험', '이야기'], 4, 'download', [1, 1], 41, 7, 8, '모래바람 속 무전을 따라간다'],
	['echo-tower', '메아리 탑', '기울기연구소', ['퍼즐', '리듬'], 2, 'web', [1, 1], 29, 4, 1, '소리가 돌아오는 길을 찾는다'],
	['tofu-factory', '두부 공장', '픽셀상점', ['경영', '아케이드'], 3, 'web phone', [1, 1], 254, 31, 110, '두부를 쉬지 않고 찍어 낸다'],
	['shadow-tag', '그림자 술래', '보라네', ['대전', '아케이드'], 1, 'web', [2, 4], 77, 12, 40, '그림자를 밟히면 술래'],
	['forest-library', '깊은 숲 도서관', '노을공방', ['이야기'], 5, 'download', [1, 1], 162, 40, 65, '숲속 도서관에서 잃어버린 책을 찾는다'],
	['planet-gardener', '행성 정원사', '물방울', ['경영', '탐험'], 4, 'web', [1, 1], 58, 8, 25, '작은 행성에 정원을 가꾼다'],
	['lightning-delivery', '번개 배달', '잿빛토끼', ['아케이드', '액션'], 1, 'web phone', [1, 1], 410, 52, 18, '번개보다 빨리 배달한다'],
	// 예외 확인용: 제목 · 메이커 이름이 아주 길고, 태그 하나, 리뷰 없음, 오늘 공개
	['cloud-post-office', '구름 위 작은 우체국에서 일하는 고양이와 비 오는 날의 긴 편지', '새벽세시에만문을여는작은공방', ['이야기'], 3, 'web', [1, 1], 3, 0, 0, '구름 사이를 건너며 편지를 나르는 고양이의 하루, 서두르지 않아도 되는 느린 배달 이야기'],
];

const MAKER_SLUG: Record<string, string> = {
	잿빛토끼: 'ash-rabbit',
	픽셀상점: 'pixel-shop',
	노을공방: 'noeul-studio',
	보라네: 'bora',
	기울기연구소: 'tilt-lab',
	새벽코딩: 'dawn-code',
	물방울: 'droplet',
	벡터공방: 'vector-studio',
	레몬게임즈: 'lemon-games',
	귤껍질스튜디오: 'tangerine-studio',
	새벽세시에만문을여는작은공방: 'three-am-studio'
};

/** 메이커 이름 → 주소 이름(메이커스 프로필 주인 = 같은 이름의 사람) */
export const SAMPLE_MAKERS = MAKER_SLUG;

/** 가짜 게임 전부(공개 상태). now 기준으로 며칠 전 공개됐는지 정한다 */
export function sampleGames(now: number = STORY_NOW): GameSeed[] {
	return ROWS.map(
		(
			[slug, title, maker, tags, length, run, [min, max], recommend, review, daysAgo, summary],
			i
		) => {
			const makerSlug = MAKER_SLUG[maker] ?? slug;
			return {
				id: `sample-${slug}`,
				slug,
				title,
				summary,
				maker: { id: `maker-${makerSlug}`, slug: makerSlug, name: maker },
				status: 'published',
				tags,
				length,
				launch: run === 'download' ? 'download' : 'web',
				phone: run === 'web phone',
				playersMin: min,
				playersMax: max,
				scanPassed: run === 'download',
				cover: `/sample/${slug}-0.svg`,
				media: [
					...(SAMPLE_VIDEO_SLUGS.includes(slug)
						? [{ kind: 'video' as const, url: `/sample/${slug}-video.webm` }]
						: []),
					...Array.from({ length: SAMPLE_SHOTS }, (_, n) => ({
						kind: 'image' as const,
						url: `/sample/${slug}-${String(n + 1)}.svg`
					}))
				],
				// 플레이 수(가짜) — 추천 순서와 일부러 조금 다르게(표의 리뷰 열은 이 계산에만 씀)
				playCount: recommend * (3 + (i % 5)) + review * 11,
				recommendCount: recommend,
				// 리뷰 수는 실제 가짜 리뷰 개수와 맞춘다(탭 · 목록과 어긋나지 않게)
				reviewCount: sampleReviewCount(slug),
				detail: { ...SAMPLE_DETAILS[slug], version: sampleVersion(slug) },
				publishedAt: now - daysAgo * DAY
			};
		}
	);
}

/** 카드 이야기용 — 시드 모양을 카드 데이터로 */
export function sampleCards(now: number = STORY_NOW): GameCardData[] {
	return sampleGames(now).map(
		({
			maker,
			summary: _s,
			status: _st,
			playersMin: _p,
			playCount: _pc,
			detail: _d,
			publishedAt,
			...card
		}) => ({
			...card,
			makerName: maker.name,
			publishedAt: publishedAt ?? now
		})
	);
}
