#!/usr/bin/env node
// CI 범위 판단: PR 에서 바뀐 파일을 보고 무엇을 돌릴지 정한다 (setup-agenda 4-1 — 바뀐 것과 관련된 것만).
// 출력(GITHUB_OUTPUT): app=true|false (앱 · 도구에 영향), deps=true|false (의존성 바뀜 → 테스트 전체)
import { execFileSync } from 'node:child_process';
import { appendFileSync } from 'node:fs';

// CI_SCOPE_BASE: 비교 기준을 직접 지정(develop 병합 뒤 미리보기는 'HEAD^' — 이번 커밋만)
const base = process.env.CI_SCOPE_BASE ?? (process.env.GITHUB_BASE_REF ? `origin/${process.env.GITHUB_BASE_REF}` : 'origin/develop');
const mergeBase = execFileSync('git', ['merge-base', base, 'HEAD'], { encoding: 'utf8' }).trim();
const files = execFileSync('git', ['diff', '--name-only', mergeBase, 'HEAD'], { encoding: 'utf8' })
	.split('\n')
	.filter(Boolean);

const APP = [/^apps\//, /^packages\//, /^scripts\//, /^package(-lock)?\.json$/, /^knip\.ts$/, /^\.npmrc$/, /^\.nvmrc$/, /^\.github\/workflows\/ci\.yml$/];
const DEPS = [/(^|\/)package\.json$/, /^package-lock\.json$/, /^\.npmrc$/, /^\.nvmrc$/];
const app = files.some((f) => APP.some((re) => re.test(f)));
const deps = files.some((f) => DEPS.some((re) => re.test(f)));

const summary = `바뀐 파일 ${files.length}개 · 앱 검사 ${app ? '실행' : '건너뜀(문서 · 설정만 바뀜)'} · 테스트 ${deps ? '전체(의존성 바뀜)' : '바뀐 것 관련만'}`;
console.log(summary);
if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, `app=${app}\ndeps=${deps}\nbase=${base}\n`);
if (process.env.GITHUB_STEP_SUMMARY) appendFileSync(process.env.GITHUB_STEP_SUMMARY, `### ${summary}\n`);
