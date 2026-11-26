import type { KnipConfig } from 'knip';

// 안 쓰는 파일 · export · 의존성 찾기 (setup-agenda 3-5). CI 에서 실패로 처리한다.
const config: KnipConfig = {
	ignoreExportsUsedInFile: true,
	// tsconfig types 의 $app/types 는 SvelteKit 가상 모듈이라 패키지가 아님
	ignoreIssues: { 'apps/web/tsconfig.json': ['unlisted'] },
	workspaces: {
		'.': {
			entry: ['scripts/*.mjs'],
			project: ['scripts/*.mjs'],
			ignoreBinaries: ['wrangler']
		},
		'apps/web': {
			entry: ['src/routes/**/+*.{ts,svelte}', 'scripts/*.ts'],
			project: ['src/**/*.{ts,svelte}', 'scripts/*.ts'],
			// vitest-browser-svelte: 4단계(컴포넌트 테스트)에서 사용 시작 — 그때 이 줄을 지운다
			ignoreDependencies: ['vitest-browser-svelte']
		}
	}
};

export default config;
