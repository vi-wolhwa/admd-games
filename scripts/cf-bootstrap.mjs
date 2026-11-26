#!/usr/bin/env node
// Cloudflare 첫 설정: 운영 · 미리보기 D1 이 없으면 만들고, 두 ID 를 Actions 요약에 남긴다.
// apps/web 에서 실행(cloudflare-bootstrap 워크플로). 시크릿: CLOUDFLARE_API_TOKEN · CLOUDFLARE_ACCOUNT_ID
import { execFileSync } from 'node:child_process';
import { appendFileSync } from 'node:fs';

const wrangler = (...args) => execFileSync('npx', ['--no-install', 'wrangler', ...args], { encoding: 'utf8' });
const list = () => JSON.parse(wrangler('d1', 'list', '--json'));

const lines = [];
for (const name of ['admd-games', 'admd-games-preview']) {
	let db = list().find((d) => d.name === name);
	if (!db) {
		wrangler('d1', 'create', name);
		db = list().find((d) => d.name === name);
	}
	if (!db) throw new Error(`${name} D1 을 만들지 못했어요.`);
	lines.push(`- \`${name}\`: \`${db.uuid}\``);
}
const summary = `### D1 ID\n${lines.join('\n')}\n`;
console.log(summary);
if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY, summary);
