/**
 * 가짜 사람 · 리뷰 · 답글 — 이야기(갤러리) · 테스트 · 미리보기/로컬 D1 시드 전용(운영 코드에서 import 금지).
 * 메이커마다 같은 이름의 사람이 메이커스 프로필을 가진다(답글의 '메이커' 표시 · 멘션 링크 확인용).
 */
import { faceOf } from '#lib/domain/face.ts';
import { REVIEW_ROWS, SAMPLE_PROFILES } from '#lib/fixtures/game-details.ts';
import { SAMPLE_MAKERS, sampleGames } from '#lib/fixtures/games.ts';
import type { ProfileSeed, ReviewSeed } from '#lib/server/ports/game-details.ts';

const DAY = 86_400_000;

const ownerId = (makerSlug: string) => `sample-owner-${makerSlug}`;

/** 리뷰어 12명 + 메이커스 프로필 주인(메이커 이름과 같은 닉네임) */
export function sampleProfiles(): ProfileSeed[] {
	const owners = Object.entries(SAMPLE_MAKERS).map(([name, slug]) => {
		const face = faceOf(name);
		return {
			id: ownerId(slug),
			displayName: name,
			faceChar: face.char,
			faceColor: face.color,
			makerId: `maker-${slug}`
		};
	});
	return [...SAMPLE_PROFILES, ...owners];
}

const person = (n: number) => `sample-person-${String(n)}`;

/**
 * 메이커 답글 말고 더 단 답글 — [게임, 리뷰 쓴 사람 번호, 답글 쓴 사람(번호 · 'maker'), 며칠 뒤, 글].
 * 루프 디버거 첫 리뷰는 답글이 4개라 '답글 더 보기'가 보인다.
 */
const EXTRA: [
	slug: string,
	reviewer: number,
	who: number | 'maker',
	daysAfter: number,
	body: string
][] = [
	['paper-vector', 1, 2, 1, '@새벽배송 저도 주말마다 해요! 넷이 하면 정말 시끄러워요'],
	['paper-vector', 1, 11, 2, '@모래시계 다음에 같이 해요'],
	['paper-vector', 6, 9, 4, '@벡터공방님 업데이트 후로는 멈춤 없이 잘 돼요. 고마워요!'],
	['loop-debugger', 1, 9, 2, '@새벽배송 15스테이지 저도 한참 막혔어요'],
	['loop-debugger', 1, 1, 3, '@청록 힌트 두 번째 단계까지 보면 풀려요!'],
	[
		'loop-debugger',
		1,
		'maker',
		4,
		'@청록 새로 넣은 연습 스테이지를 먼저 해 보시면 도움이 될 거예요'
	]
];

/** 가짜 리뷰 전부. now 기준으로 며칠 전에 썼는지 정한다 */
export function sampleReviews(now: number): ReviewSeed[] {
	const makerOfGame = new Map(sampleGames(now).map((g) => [g.slug, g.maker.slug]));
	const nameOf = new Map(SAMPLE_PROFILES.map((p) => [p.id, p.displayName]));
	return REVIEW_ROWS.map(
		(
			[
				slug,
				who,
				minutes,
				version,
				daysAgo,
				_unused,
				recommended,
				phrases,
				body,
				reply,
				editedAfter
			],
			i
		) => {
			const createdAt = now - daysAgo * DAY - i * 60_000;
			const owner = ownerId(makerOfGame.get(slug) ?? '');
			const author = person(who);
			const replies: ReviewSeed['replies'] = [];
			if (reply) {
				replies.push({
					id: `sample-reply-${String(i + 1)}-0`,
					authorId: owner,
					body: `@${nameOf.get(author) ?? ''} ${reply[0]}`,
					createdAt: createdAt + reply[2] * DAY,
					updatedAt: null
				});
			}
			for (const [k, [game, reviewer, by, after, text]] of EXTRA.entries()) {
				if (game !== slug || reviewer !== who) continue;
				replies.push({
					id: `sample-reply-${String(i + 1)}-${String(k + 1)}`,
					authorId: by === 'maker' ? owner : person(by),
					body: text,
					createdAt: createdAt + after * DAY,
					updatedAt: null
				});
			}
			return {
				id: `sample-review-${String(i + 1)}`,
				gameId: `sample-${slug}`,
				authorId: author,
				body,
				playMinutes: minutes,
				version,
				createdAt,
				updatedAt: editedAfter === undefined ? null : createdAt + editedAfter * DAY,
				phrases,
				recommended,
				replies: replies.toSorted((a, b) => a.createdAt - b.createdAt)
			};
		}
	);
}
