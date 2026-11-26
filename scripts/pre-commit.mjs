#!/usr/bin/env node
// 커밋 전 검사: 바뀐 파일만 포맷 · 린트 · 구조 경계 (전체 검사는 CI 가 함)
import { execFileSync } from 'node:child_process';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const run = (cmd, args, cwd = ROOT) => execFileSync(cmd, args, { cwd, stdio: 'inherit', shell: process.platform === 'win32' });
const staged = execFileSync('git', ['diff', '--cached', '--name-only', '--diff-filter=ACMR'], { cwd: ROOT, encoding: 'utf8' })
	.split('\n')
	.filter(Boolean);

const web = staged.filter((f) => f.startsWith('apps/web/')).map((f) => f.slice('apps/web/'.length));
const fmt = web.filter((f) => /\.(ts|js|svelte|css|json|md|html)$/.test(f));
const lint = web.filter((f) => /\.(ts|js|svelte)$/.test(f));
const webDir = path.join(ROOT, 'apps/web');
try {
	if (fmt.length) run('npx', ['--no-install', 'prettier', '--check', ...fmt], webDir);
	if (lint.length) run('npx', ['--no-install', 'eslint', '--max-warnings=0', ...lint], webDir);
	const src = staged.filter((f) => f.startsWith('apps/web/src/') && /\.(ts|js|svelte)$/.test(f));
	if (src.length) run('node', ['scripts/check-boundaries.mjs', ...src]);
} catch {
	console.error('\n커밋 전 검사 실패 — 위 내용을 고친 뒤 다시 커밋하세요. (포맷: npm run format)');
	process.exit(1);
}
