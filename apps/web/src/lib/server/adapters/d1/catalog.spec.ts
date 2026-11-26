import { readdirSync, readFileSync } from 'node:fs';
import path from 'node:path';

import { afterAll, beforeAll, describe } from 'vitest';
import { getPlatformProxy } from 'wrangler';

import { runCatalogContract } from '../../ports/catalog.contract';
import { createD1Catalog } from './catalog';
import { catalogSeedStatements } from './catalog-seed';
import { createD1Client } from './client';

/** 로컬 D1(miniflare, 메모리) 에 실제 이관 SQL 을 적용하고 계약 테스트를 돌린다 */
let proxy: Awaited<ReturnType<typeof getPlatformProxy<Env>>>;

beforeAll(async () => {
	proxy = await getPlatformProxy<Env>({ persist: false });
	const dir = path.join(import.meta.dirname, '../../../../../migrations');
	for (const file of readdirSync(dir)
		.filter((f) => f.endsWith('.sql'))
		.sort()) {
		for (const stmt of readFileSync(path.join(dir, file), 'utf8').split(
			'--> statement-breakpoint'
		)) {
			if (stmt.trim()) await proxy.env.DB.prepare(stmt).run();
		}
	}
}, 30_000);

afterAll(async () => {
	await proxy.dispose();
});

describe('D1 Catalog', () => {
	runCatalogContract(async (games) => {
		await proxy.env.DB.batch(catalogSeedStatements(games).map((s) => proxy.env.DB.prepare(s)));
		return createD1Catalog(createD1Client(proxy.env.DB));
	});
});
