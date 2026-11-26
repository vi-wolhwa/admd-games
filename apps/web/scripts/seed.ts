/**
 * 가짜 게임 데이터를 D1 에 넣는다 — 로컬(개발) · 미리보기 전용. 기존 목록 데이터를 지우고 새로 넣는다.
 *   node scripts/seed.ts --local              (npm run db:seed:local)
 *   node scripts/seed.ts --env preview --remote (preview 워크플로)
 * 운영 DB 는 거부한다(시드는 목록 데이터를 지우므로).
 */
import { execFileSync } from 'node:child_process';
import { mkdirSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import path from 'node:path';

import { sampleGames } from '#lib/fixtures/games.ts';
import { catalogSeedStatements } from '#lib/server/adapters/d1/catalog-seed.ts';

const args = process.argv.slice(2);
const local = args.includes('--local');
const preview = args.includes('--remote') && args[args.indexOf('--env') + 1] === 'preview';
if (!local && !preview) {
	console.error('로컬(--local) 또는 미리보기(--env preview --remote)에만 넣을 수 있어요.');
	process.exit(2);
}

const now = Date.now();
const file = path.join(import.meta.dirname, '../.wrangler/seed.sql');
mkdirSync(path.dirname(file), { recursive: true });
writeFileSync(file, catalogSeedStatements(sampleGames(now), now).join('\n') + '\n');

// npx 대신 wrangler 실행 파일을 node 로 직접 — 윈도우에서도 셸 없이
const wrangler = path.join(
	path.dirname(createRequire(import.meta.url).resolve('wrangler/package.json')),
	'bin/wrangler.js'
);
execFileSync(
	process.execPath,
	[wrangler, 'd1', 'execute', 'DB', ...args, '--file', file, '--yes'],
	{ stdio: 'inherit' }
);
console.log(`가짜 게임 ${String(sampleGames(now).length)}개를 넣었어요.`);
