#!/usr/bin/env node
// main · develop 으로 직접 푸시 금지 (ADR 0013). 원격 규칙 세트가 최종 방어선이고 이건 빠른 안내용.
import { readFileSync } from 'node:fs';

const lines = readFileSync(0, 'utf8').split('\n').filter(Boolean);
for (const line of lines) {
	const remoteRef = line.split(' ')[2] ?? '';
	if (remoteRef === 'refs/heads/main' || remoteRef === 'refs/heads/develop') {
		console.error(`${remoteRef.replace('refs/heads/', '')} 으로 직접 푸시할 수 없어요. 작업 브랜치에서 PR 을 여세요.`);
		process.exit(1);
	}
}
