import { and, asc, count, desc, eq, exists, inArray, lt, or, type SQL, sql } from 'drizzle-orm';

import { type Cursor, encodeCursor } from '#lib/domain/cursor.ts';
import { decodeReviewCursor, type ReviewData, type ReviewSort } from '#lib/domain/review.ts';

import type { Reviews } from '../../ports/game-details';
import type { D1Client } from './client';
import { profiles, reviewPhrases, reviewReplies, reviews } from './schema';

/** '오래 한 사람' 순에서 기록 없음(null)을 맨 뒤로 */
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
					faceColor: profiles.faceColor,
					reviewCount: profiles.reviewCount,
					recommended: sql<number>`EXISTS (SELECT 1 FROM recommendations AS rc WHERE rc.game_id = ${reviews.gameId} AND rc.user_id = ${reviews.authorId})`,
					// 묶음(batch) 결과는 열 이름으로 오므로 reviews 와 겹치는 이름(body · created_at)에는 별칭
					replyBody: sql<string | null>`${reviewReplies.body}`.as('reply_body'),
					replyNote: sql<string | null>`${reviewReplies.note}`.as('reply_note'),
					replyAt: sql<number | null>`${reviewReplies.createdAt}`.as('reply_at')
				})
				.from(reviews)
				.innerJoin(profiles, eq(profiles.id, reviews.authorId))
				.leftJoin(reviewReplies, eq(reviewReplies.reviewId, reviews.id))
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

			const items: ReviewData[] = pageRows.map((r) => ({
				id: r.id,
				author: {
					name: r.name,
					faceChar: r.faceChar,
					faceColor: r.faceColor,
					reviewCount: r.reviewCount
				},
				recommended: Boolean(r.recommended),
				playMinutes: r.playMinutes,
				version: r.version,
				createdAt: r.createdAt,
				updatedAt: r.updatedAt,
				phrases: phrases.get(r.id) ?? [],
				body: r.body,
				reply:
					r.replyBody === null || r.replyAt === null
						? null
						: { body: r.replyBody, note: r.replyNote, createdAt: r.replyAt }
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
