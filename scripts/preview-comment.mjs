#!/usr/bin/env node
// PR 미리보기 주소를 PR 댓글 하나에 남긴다(있으면 고치고, 없으면 새로). env: URL · PR · GITHUB_REPOSITORY · GITHUB_SHA · GH_TOKEN
import { execFileSync } from 'node:child_process';

const { URL: url, PR: pr, GITHUB_REPOSITORY: repo, GITHUB_SHA: sha = '' } = process.env;
const MARK = '**미리보기**';
const body = `${MARK}: ${url} (커밋 ${sha.slice(0, 7)}, 가짜 데이터 D1)`;
const gh = (...args) => execFileSync('gh', args, { encoding: 'utf8' });

const comments = JSON.parse(gh('api', `repos/${repo}/issues/${pr}/comments`, '--paginate'));
const mine = comments.find((c) => c.user.login === 'github-actions[bot]' && c.body.startsWith(MARK));
if (mine) gh('api', '-X', 'PATCH', `repos/${repo}/issues/comments/${mine.id}`, '-f', `body=${body}`);
else gh('pr', 'comment', pr, '--body', body);
console.log(body);
