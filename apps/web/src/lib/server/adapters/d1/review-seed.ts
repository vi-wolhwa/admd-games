/**
 * 리뷰 시드 SQL — 계약 테스트와 가짜 데이터가 같이 쓴다. catalogSeedStatements 다음에 돌린다
 * (그쪽이 리뷰 · 프로필까지 지우고 게임을 넣음). 운영 DB 에는 쓰지 않는다(scripts/seed.ts 가 막음).
 */
import type { ProfileSeed, ReviewSeed } from '../../ports/game-details';
import { insert } from './catalog-seed.ts';

export function reviewSeedStatements(
	profiles: ProfileSeed[],
	reviews: ReviewSeed[],
	now = Date.now()
): string[] {
	const out: string[] = [];
	for (const p of profiles) {
		out.push(
			insert('profiles', {
				id: p.id,
				display_name: p.displayName,
				face_char: p.faceChar,
				face_color: p.faceColor,
				review_count: reviews.filter((r) => r.authorId === p.id).length,
				created_at: now
			})
		);
	}
	for (const r of reviews) {
		out.push(
			insert('reviews', {
				id: r.id,
				game_id: r.gameId,
				author_id: r.authorId,
				body: r.body,
				play_minutes: r.playMinutes,
				version: r.version,
				created_at: r.createdAt,
				updated_at: r.updatedAt
			})
		);
		r.phrases.forEach((phrase, position) => {
			out.push(insert('review_phrases', { review_id: r.id, phrase, position }));
		});
		if (r.reply) {
			out.push(
				insert('review_replies', {
					review_id: r.id,
					body: r.reply.body,
					note: r.reply.note,
					created_at: r.reply.createdAt
				})
			);
		}
		if (r.recommended) {
			out.push(
				insert('recommendations', {
					game_id: r.gameId,
					user_id: r.authorId,
					created_at: r.createdAt
				})
			);
		}
	}
	return out;
}
