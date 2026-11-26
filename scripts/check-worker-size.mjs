#!/usr/bin/env node
// Worker 크기 감시: 무료 플랜 한도(gzip 3MB)의 70% 경고 · 90% 실패 (setup-agenda 3-6)
// wrangler 가 실제로 올릴 번들을 만들어(--dry-run) gzip 크기를 잰다. apps/web 에서 빌드한 뒤 실행.
import { execFileSync } from 'node:child_process';
import { readdirSync, readFileSync, rmSync, statSync, appendFileSync } from 'node:fs';
import path from 'node:path';
import { gzipSync } from 'node:zlib';

const WEB = path.resolve(import.meta.dirname, '../apps/web');
const OUT = path.join(WEB, '.wrangler/size-check');
const LIMIT = 3 * 1024 * 1024;
rmSync(OUT, { recursive: true, force: true });
execFileSync('npx', ['--no-install', 'wrangler', 'deploy', '--dry-run', '--outdir', OUT], { cwd: WEB, stdio: 'ignore', shell: process.platform === 'win32' });

let raw = 0;
const parts = [];
const walk = (d) => {
	for (const n of readdirSync(d)) {
		const p = path.join(d, n);
		if (statSync(p).isDirectory()) walk(p);
		else if (/\.(m?js|wasm)$/.test(n)) {
			const buf = readFileSync(p);
			raw += buf.length;
			parts.push(buf);
		}
	}
};
walk(OUT);
const gz = gzipSync(Buffer.concat(parts), { level: 9 }).length;
const pct = Math.round((gz / LIMIT) * 100);
const mb = (b) => (b / 1024 / 1024).toFixed(2);
const msg = `Worker 크기: gzip ${mb(gz)}MB / 한도 3MB (${pct}%) · 압축 전 ${mb(raw)}MB`;
console.log(msg);
if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY, `### ${msg}\n`);
if (pct >= 90) {
	console.error('한도의 90% 이상 — 먼저 무거운 의존성 · 비효율을 찾아 줄이고, 최적화 후에도 넘으면 플랜 검토를 사용자에게 올립니다.');
	process.exit(1);
}
if (pct >= 70) console.warn('::warning::Worker 크기가 한도의 70% 를 넘었어요.');
