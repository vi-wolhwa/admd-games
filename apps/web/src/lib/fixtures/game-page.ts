/**
 * 가짜 게임 상세 화면 데이터 — 이야기(갤러리) 전용. 시드 모양(GameSeed · ReviewSeed)을 화면 데이터로 바꾼다.
 */
import type { GameCardData, GameDetail } from '#lib/domain/game.ts';
import { splitMentions } from '#lib/domain/profile.ts';
import type { ReviewData } from '#lib/domain/review.ts';
import { SAMPLE_MAKERS, sampleCards, sampleGames, STORY_NOW } from '#lib/fixtures/games.ts';
import { sampleProfiles, sampleReviews } from '#lib/fixtures/reviews.ts';

export function sampleGameDetail(slug: string, now: number = STORY_NOW): GameDetail {
	const games = sampleGames(now);
	const g = games.find((x) => x.slug === slug);
	if (!g) throw new Error(`가짜 게임 없음: ${slug}`);
	const card = sampleCards(now).find((c) => c.slug === slug);
	if (!card) throw new Error(slug);
	return {
		...card,
		summary: g.summary,
		description: g.detail?.description ?? '',
		makerSlug: g.maker.slug,
		makerGameCount: games.filter((x) => x.maker.id === g.maker.id).length,
		devices: g.detail?.devices ?? ['pc'],
		online: g.detail?.online ?? false,
		languages: g.detail?.languages ?? [],
		minSpec: g.detail?.minSpec ?? null,
		playersMin: g.playersMin
	};
}

/** 태그가 겹치는 게임(간단히 — 실제 순서는 D1 어댑터가 정함) */
export function sampleSimilar(slug: string, limit = 8, now: number = STORY_NOW): GameCardData[] {
	const cards = sampleCards(now);
	const me = cards.find((c) => c.slug === slug);
	if (!me) return [];
	return cards
		.filter((c) => c.slug !== slug && c.tags.some((t) => me.tags.includes(t)))
		.toSorted((a, b) => b.recommendCount - a.recommendCount)
		.slice(0, limit);
}

/** 그 게임의 가짜 리뷰를 최신 순으로(답글 · 멘션 포함 — D1 어댑터와 같은 모양) */
export function sampleReviewData(slug: string, now: number = STORY_NOW): ReviewData[] {
	const all = sampleReviews(now);
	const people = sampleProfiles();
	const slugOfMaker = new Map(Object.entries(SAMPLE_MAKERS).map(([, s]) => [`maker-${s}`, s]));
	const gameMaker = sampleGames(now).find((g) => g.slug === slug)?.maker.id;
	const person = (id: string) => {
		const p = people.find((x) => x.id === id);
		return {
			name: p?.displayName ?? '?',
			faceChar: p?.faceChar ?? '?',
			faceColor: p?.faceColor ?? 'jjok',
			makerSlug: (p?.makerId && slugOfMaker.get(p.makerId)) ?? null
		};
	};
	const byName = new Map(people.map((p) => [p.displayName, p]));
	return all
		.filter((r) => r.gameId === `sample-${slug}`)
		.toSorted((a, b) => b.createdAt - a.createdAt)
		.map((r) => ({
			id: r.id,
			author: {
				...person(r.authorId),
				reviewCount: all.filter((x) => x.authorId === r.authorId).length
			},
			recommended: r.recommended,
			playMinutes: r.playMinutes,
			version: r.version,
			createdAt: r.createdAt,
			updatedAt: r.updatedAt,
			phrases: r.phrases,
			body: r.body,
			replies: r.replies.map((x) => {
				const mentions: Record<string, string | null> = {};
				for (const part of splitMentions(x.body, (n) => byName.has(n))) {
					if ('mention' in part)
						mentions[part.mention] = person(byName.get(part.mention)?.id ?? '').makerSlug;
				}
				const author = people.find((p) => p.id === x.authorId);
				return {
					id: x.id,
					author: person(x.authorId),
					byGameMaker: author?.makerId != null && author.makerId === gameMaker,
					body: x.body,
					createdAt: x.createdAt,
					updatedAt: x.updatedAt,
					mentions
				};
			})
		}));
}
