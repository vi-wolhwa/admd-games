#!/usr/bin/env node
// 커밋 메시지 형식 검사 (Conventional Commits, 타입 영어 · 설명 한국어 — ADR 0005)
// simple-git-hooks 의 commit-msg 훅에서 메시지 파일 경로를 받는다.
import { readFileSync } from 'node:fs';

const file = process.argv[2];
const first = readFileSync(file, 'utf8').split('\n')[0].trim();
const TYPES = ['feat', 'fix', 'chore', 'docs', 'refactor', 'test', 'perf', 'build', 'ci', 'style', 'revert'];
const CONVENTIONAL = /^(?<type>[a-z]+)(\([\w./-]+\))?!?: \S.*/;
const m = CONVENTIONAL.exec(first);
const ok = (m !== null && TYPES.includes(m.groups.type)) || /^(Merge|Revert|fixup!|squash!) /.test(first);
if (!ok) {
	console.error(`커밋 메시지 형식이 맞지 않아요: "${first}"
  예) feat: 게임 카드에 추천 수 표시
      fix(play): 일시정지에서 나가기 버튼이 안 눌리는 문제
  타입: ${TYPES.join(', ')}`);
	process.exit(1);
}
