/**
 * 게임 목록 시드 SQL — 계약 테스트와 미리보기 · 로컬 가짜 데이터(scripts/seed.ts)가 같이 쓴다.
 * 기존 목록 데이터를 지우고 새로 넣으므로 **운영 DB 에는 절대 쓰지 않는다**(scripts/seed.ts 가 막음).
 * 태그의 게임 수 캐시는 공개 게임만 센다(ADR 0010).
 */
import { tagSlug } from '#lib/domain/game.ts';

import type { GameSeed } from '../../ports/catalog';

type SqlValue = string | number | boolean | null;

function lit(v: SqlValue): string {
	if (v === null) return 'NULL';
	if (typeof v === 'boolean') return v ? '1' : '0';
	if (typeof v === 'number') return String(v);
	return `'${v.replaceAll("'", "''")}'`;
}

export function insert(table: string, row: Record<string, SqlValue>): string {
	const cols = Object.keys(row);
	return `INSERT INTO ${table} (${cols.join(', ')}) VALUES (${cols.map((c) => lit(row[c] ?? null)).join(', ')});`;
}

export function catalogSeedStatements(games: GameSeed[], now = Date.now()): string[] {
	const out = [
		// 게임을 가리키는 표부터 지운다(외래 키)
		'DELETE FROM replies;',
		'DELETE FROM review_replies;',
		'DELETE FROM review_phrases;',
		'DELETE FROM reviews;',
		'DELETE FROM recommendations;',
		'DELETE FROM profiles;',
		'DELETE FROM game_media;',
		'DELETE FROM game_tags;',
		'DELETE FROM games;',
		'DELETE FROM tags;',
		'DELETE FROM makers;'
	];

	const makers = new Map(games.map((g) => [g.maker.id, g.maker]));
	for (const m of makers.values()) {
		out.push(insert('makers', { id: m.id, slug: m.slug, name: m.name, created_at: now }));
	}

	const tagCount = new Map<string, { name: string; count: number }>();
	for (const g of games) {
		for (const name of g.tags) {
			const slug = tagSlug(name);
			const t = tagCount.get(slug) ?? { name, count: 0 };
			if (g.status === 'published') t.count++;
			tagCount.set(slug, t);
		}
	}
	for (const [slug, t] of tagCount) {
		out.push(
			insert('tags', { id: `tag-${slug}`, slug, name: t.name, alias_of: null, game_count: t.count })
		);
	}

	for (const g of games) {
		out.push(
			insert('games', {
				id: g.id,
				slug: g.slug,
				maker_id: g.maker.id,
				status: g.status,
				title: g.title,
				summary: g.summary,
				description: g.detail?.description ?? '',
				launch: g.launch,
				length: g.length,
				pc: (g.detail?.devices ?? ['pc']).includes('pc'),
				phone: g.phone,
				pad: (g.detail?.devices ?? []).includes('pad'),
				online: g.detail?.online ?? false,
				languages: (g.detail?.languages ?? []).join(','),
				min_spec: g.detail?.minSpec ?? null,
				players_min: g.playersMin,
				players_max: g.playersMax,
				scan_passed: g.scanPassed,
				cover_url: g.cover,
				published_at: g.publishedAt,
				play_count: g.playCount,
				recommend_count: g.recommendCount,
				review_count: g.reviewCount,
				created_at: now
			})
		);
		g.tags.forEach((name, position) => {
			out.push(insert('game_tags', { game_id: g.id, tag_id: `tag-${tagSlug(name)}`, position }));
		});
		g.media.forEach((m, position) => {
			out.push(
				insert('game_media', {
					id: `${g.id}-m${String(position)}`,
					game_id: g.id,
					kind: m.kind,
					url: m.url,
					position
				})
			);
		});
	}
	return out;
}
