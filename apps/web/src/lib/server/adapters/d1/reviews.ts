import { and, asc, count, desc, eq, exists, inArray, lt, or, type SQL, sql } from 'drizzle-orm';
import { alias } from 'drizzle-orm/sqlite-core';

import { type Cursor, encodeCursor } from '#lib/domain/cursor.ts';
import { mentionCandidates, splitMentions } from '#lib/domain/profile.ts';
import {
	decodeReviewCursor,
	type Person,
	type ReplyData,
	type ReviewData,
	type ReviewSort
} from '#lib/domain/review.ts';

import type { Reviews } from '../../ports/game-details';
import type { D1Client } from './client';
import { makers, profiles, replies, reviewPhrases, reviews } from './schema';

/** 글쓴이가 가진 메이커스 프로필(makers.profile_id = 글쓴이) */
const authorMaker = alias(makers, 'author_maker');

/** '고인물 순'에서 기록 없음(null)을 맨 뒤로 */
const played = sql<number>`COALESCE(${reviews.playMinutes}, -1)`;

const ORDER: Record<ReviewSort, SQL[]> = {
	recent: [desc(reviews.createdAt), desc(reviews.id)],
	played: [desc(played), desc(reviews.createdAt), desc(reviews.id)]
};

/** 커서 다음 — ORDER 와 같은 방향의 사전순 비교 */
function after(c: Cursor<ReviewSort>): SQL | undefined {
	const [a = 0, b = 0] = c.values;
	switch (c.sort) {
		case 'recent':
			return or(lt(reviews.createdAt, a), and(eq(reviews.createdAt, a), lt(reviews.id, c.id)));
		case 'played':
			return or(
				sql`${played} < ${a}`,
				and(sql`${played} = ${a}`, lt(reviews.createdAt, b)),
				and(sql`${played} = ${a}`, eq(reviews.createdAt, b), lt(reviews.id, c.id))
			);
	}
}

/** D1 리뷰 읽기. 글쓴이의 추천 여부는 recommendations 에서, 고른 말은 묶음 한 번에 */
export function createD1Reviews(db: D1Client): Reviews {
	return {
		async listReviews(gameId, query, page) {
			const cursor = page.cursor ? decodeReviewCursor(page.cursor, query.sort) : null;
			if (page.cursor && !cursor) return { items: [], nextCursor: null, total: null };

			const filter = and(
				eq(reviews.gameId, gameId),
				query.phrase
					? exists(
							db
								.select({ one: sql`1` })
								.from(reviewPhrases)
								.where(
									and(
										eq(reviewPhrases.reviewId, reviews.id),
										eq(reviewPhrases.phrase, query.phrase)
									)
								)
						)
					: undefined
			);
			const listQuery = db
				.select({
					id: reviews.id,
					body: reviews.body,
					playMinutes: reviews.playMinutes,
					version: reviews.version,
					createdAt: reviews.createdAt,
					updatedAt: reviews.updatedAt,
					name: profiles.displayName,
					faceChar: profiles.faceChar,
					faceMouth: profiles.faceMouth,
					faceColor: profiles.faceColor,
					reviewCount: profiles.reviewCount,
					// 글쓴이의 메이커스 프로필 주소(없으면 null) — 묶음(batch) 결과는 열 이름으로 오므로 별칭
					makerSlug: sql<string | null>`${authorMaker.slug}`.as('author_maker_slug'),
					recommended: sql<number>`EXISTS (SELECT 1 FROM recommendations AS rc WHERE rc.game_id = ${reviews.gameId} AND rc.user_id = ${reviews.authorId})`
				})
				.from(reviews)
				.innerJoin(profiles, eq(profiles.id, reviews.authorId))
				.leftJoin(authorMaker, eq(authorMaker.profileId, reviews.authorId))
				.where(cursor ? and(filter, after(cursor)) : filter)
				.orderBy(...ORDER[query.sort])
				.limit(page.limit + 1);

			let rows;
			let total: number | null = null;
			if (cursor) rows = await listQuery;
			else {
				const [r, c] = await db.batch([
					listQuery,
					db.select({ n: count() }).from(reviews).where(filter)
				]);
				rows = r;
				total = c[0]?.n ?? 0;
			}

			const hasMore = rows.length > page.limit;
			const pageRows = hasMore ? rows.slice(0, page.limit) : rows;
			const phrases = new Map<string, string[]>();
			if (pageRows.length > 0) {
				const phraseRows = await db
					.select({ reviewId: reviewPhrases.reviewId, phrase: reviewPhrases.phrase })
					.from(reviewPhrases)
					.where(
						inArray(
							reviewPhrases.reviewId,
							pageRows.map((r) => r.id)
						)
					)
					.orderBy(asc(reviewPhrases.reviewId), asc(reviewPhrases.position));
				for (const p of phraseRows) {
					phrases.set(p.reviewId, [...(phrases.get(p.reviewId) ?? []), p.phrase]);
				}
			}

			const repliesByReview = await loadReplies(
				db,
				gameId,
				pageRows.map((r) => r.id)
			);

			const items: ReviewData[] = pageRows.map((r) => ({
				id: r.id,
				author: {
					name: r.name,
					faceChar: r.faceChar,
					faceMouth: r.faceMouth,
					faceColor: r.faceColor,
					makerSlug: r.makerSlug,
					reviewCount: r.reviewCount
				},
				recommended: Boolean(r.recommended),
				playMinutes: r.playMinutes,
				version: r.version,
				createdAt: r.createdAt,
				updatedAt: r.updatedAt,
				phrases: phrases.get(r.id) ?? [],
				body: r.body,
				replies: repliesByReview.get(r.id) ?? []
			}));

			const last = pageRows.at(-1);
			let nextCursor: string | null = null;
			if (hasMore && last) {
				const values = {
					recent: [last.createdAt],
					played: [last.playMinutes ?? -1, last.createdAt]
				}[query.sort];
				nextCursor = encodeCursor({ sort: query.sort, values, id: last.id });
			}
			return { items, nextCursor, total };
		},

		async topPhrases(gameId, limit) {
			const n = count();
			return db
				.select({ phrase: reviewPhrases.phrase, count: n })
				.from(reviewPhrases)
				.innerJoin(reviews, eq(reviews.id, reviewPhrases.reviewId))
				.where(eq(reviews.gameId, gameId))
				.groupBy(reviewPhrases.phrase)
				.orderBy(desc(n), asc(reviewPhrases.phrase))
				.limit(limit);
		}
	};
}

/**
 * 그 묶음의 답글(오래된 순) + 글에 나온 멘션의 프로필 주소.
 * 답글 쓴 사람의 메이커스 프로필 · 그 게임의 메이커인지(byGameMaker)도 함께. 쿼리 두 번(답글, 멘션 닉네임).
 */
async function loadReplies(
	db: D1Client,
	gameId: string,
	reviewIds: string[]
): Promise<Map<string, ReplyData[]>> {
	const out = new Map<string, ReplyData[]>();
	if (reviewIds.length === 0) return out;
	const rows = await db
		.select({
			id: replies.id,
			reviewId: replies.reviewId,
			body: replies.body,
			createdAt: replies.createdAt,
			updatedAt: replies.updatedAt,
			name: profiles.displayName,
			faceChar: profiles.faceChar,
			faceMouth: profiles.faceMouth,
			faceColor: profiles.faceColor,
			makerSlug: sql<string | null>`${authorMaker.slug}`.as('author_maker_slug'),
			byGameMaker: sql<number>`(${authorMaker.id} IS NOT NULL AND ${authorMaker.id} = (SELECT g.maker_id FROM games AS g WHERE g.id = ${gameId}))`
		})
		.from(replies)
		.innerJoin(profiles, eq(profiles.id, replies.authorId))
		.leftJoin(authorMaker, eq(authorMaker.profileId, replies.authorId))
		.where(inArray(replies.reviewId, reviewIds))
		.orderBy(asc(replies.reviewId), asc(replies.createdAt), asc(replies.id));

	// 멘션 후보 닉네임을 한 번에 찾는다(아는 닉네임 → 그 사람: 얼굴 · 메이커스 프로필 주소)
	const candidates = [...new Set(rows.flatMap((r) => mentionCandidates(r.body)))];
	const known = new Map<string, Person>();
	if (candidates.length > 0) {
		const people = await db
			.select({
				name: profiles.displayName,
				faceChar: profiles.faceChar,
				faceMouth: profiles.faceMouth,
				faceColor: profiles.faceColor,
				makerSlug: makers.slug
			})
			.from(profiles)
			.leftJoin(makers, eq(makers.profileId, profiles.id))
			.where(inArray(profiles.displayName, candidates));
		for (const p of people) known.set(p.name, p);
	}

	for (const r of rows) {
		const mentions: Record<string, Person> = {};
		for (const part of splitMentions(r.body, (n) => known.has(n))) {
			const who = 'mention' in part ? known.get(part.mention) : undefined;
			if (who) mentions[who.name] = who;
		}
		const reply: ReplyData = {
			id: r.id,
			author: {
				name: r.name,
				faceChar: r.faceChar,
				faceMouth: r.faceMouth,
				faceColor: r.faceColor,
				makerSlug: r.makerSlug
			},
			byGameMaker: Boolean(r.byGameMaker),
			body: r.body,
			createdAt: r.createdAt,
			updatedAt: r.updatedAt,
			mentions
		};
		out.set(r.reviewId, [...(out.get(r.reviewId) ?? []), reply]);
	}
	return out;
}
