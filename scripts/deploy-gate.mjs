#!/usr/bin/env node
// 배포 관문 — 배포할지 판단해 GITHUB_OUTPUT 에 go=true|false 를 남긴다.
//   preview    : 앱 코드가 바뀐 PR + Cloudflare 시크릿 + D1 ID 가 있을 때만
//   production : main 커밋이 develop → main PR 병합으로 들어왔는지 확인(아니면 실패 + 이슈 — ADR 0013),
//                그다음 시크릿 · D1 ID 가 있을 때만
import { execFileSync } from 'node:child_process';
import { appendFileSync, readFileSync } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const mode = process.argv[2];
const out = (k, v) => process.env.GITHUB_OUTPUT && appendFileSync(process.env.GITHUB_OUTPUT, `${k}=${v}\n`);
const notice = (m) => console.log(`::notice::${m}`);

function cloudflareReady() {
	if (!process.env.CLOUDFLARE_API_TOKEN) {
		notice('Cloudflare 시크릿이 없어 배포를 건너뜁니다(docs/operations.md).');
		return false;
	}
	const cfg = readFileSync(path.join(ROOT, 'apps/web/wrangler.jsonc'), 'utf8');
	if (cfg.includes('"database_id": "00000000-0000-0000-0000-000000000000"')) {
		notice('D1 ID 가 아직 없어 배포를 건너뜁니다(Actions 의 cloudflare-bootstrap 실행 후 ID 반영).');
		return false;
	}
	return true;
}

if (mode === 'preview') {
	const scope = execFileSync('node', [path.join(ROOT, 'scripts/ci-scope.mjs')], { encoding: 'utf8', env: { ...process.env, GITHUB_OUTPUT: '' } });
	const app = scope.includes('앱 검사 실행');
	if (!app) notice('앱 코드가 바뀌지 않아 미리보기를 건너뜁니다.');
	out('go', String(app && cloudflareReady()));
} else if (mode === 'production') {
	const sha = process.env.GITHUB_SHA;
	const repo = process.env.GITHUB_REPOSITORY;
	const pulls = JSON.parse(execFileSync('gh', ['api', `repos/${repo}/commits/${sha}/pulls`], { encoding: 'utf8' }));
	const release = pulls.find((p) => p.base.ref === 'main' && p.head.ref === 'develop' && p.merged_at);
	if (!release) {
		execFileSync('gh', [
			'issue', 'create', '--label', '환경',
			'--title', `운영 배포 거부: develop 을 거치지 않은 main 커밋 ${sha.slice(0, 7)}`,
			'--body', `main 에 develop → main PR 이 아닌 커밋이 들어와 배포하지 않았습니다(ADR 0013). 커밋: ${sha}`
		]);
		console.error('::error::develop → main PR 로 들어온 커밋이 아니라 배포하지 않습니다.');
		process.exit(1);
	}
	console.log(`출처 확인: PR #${release.number}(develop → main)`);
	out('go', String(cloudflareReady()));
} else {
	console.error('사용: node scripts/deploy-gate.mjs preview|production');
	process.exit(2);
}
