import type { StorybookConfig } from '@storybook/sveltekit';

// 컴포넌트 갤러리(ADR 0012 · setup-agenda 1-3). 이야기 경로 = 컴포넌트 층 구조(docs/dev/component-architecture.md 7절)
const config: StorybookConfig = {
	framework: '@storybook/sveltekit',
	stories: ['../src/**/*.stories.@(svelte|ts)'],
	addons: ['@storybook/addon-svelte-csf', '@storybook/addon-a11y', '@storybook/addon-vitest'],
	// 가짜 게임 그림(static/sample) 등 정적 파일
	staticDirs: ['../static'],
	core: { disableTelemetry: true }
};

export default config;
