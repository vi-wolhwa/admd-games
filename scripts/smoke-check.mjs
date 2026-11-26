#!/usr/bin/env node
// 배포 직후 자동 점검: 상태 API 와 첫 페이지가 200 인지 몇 번 확인한다. 실패하면 배포 작업이 되돌리기를 한다.
// env: URL (배포된 주소)
const base = process.env.URL;
if (!base) {
	console.error('::error::배포 주소를 찾지 못했어요.');
	process.exit(1);
}
const CHECKS = ['/api/health', '/play'];
for (let attempt = 1; attempt <= 5; attempt++) {
	const codes = await Promise.all(CHECKS.map(async (p) => (await fetch(base + p, { redirect: 'manual' })).status));
	if (codes.every((c) => c === 200)) {
		console.log(`점검 통과: ${CHECKS.map((p, i) => `${p} ${codes[i]}`).join(' · ')}`);
		process.exit(0);
	}
	console.log(`점검 ${attempt}/5: ${CHECKS.map((p, i) => `${p} ${codes[i]}`).join(' · ')}`);
	await new Promise((r) => setTimeout(r, 5000));
}
console.error('::error::점검 실패');
process.exit(1);
