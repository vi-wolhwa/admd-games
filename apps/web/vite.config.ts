import adapter from '@sveltejs/adapter-cloudflare';
import { sveltekit } from '@sveltejs/kit/vite';
import tailwindcss from '@tailwindcss/vite';
import { playwright } from '@vitest/browser-playwright';
import { defineConfig } from 'vitest/config';

export default defineConfig({
	plugins: [
		tailwindcss(),
		sveltekit({
			compilerOptions: {
				// Force runes mode for the project, except for libraries. Can be removed in svelte 6.
				runes: ({ filename }) =>
					filename.split(/[/\\]/).includes('node_modules') ? undefined : true
			},
			adapter: adapter(),
			// 보안 헤더(setup-agenda 7-4): 스크립트는 SvelteKit 이 nonce/해시를 붙인 것만. 게임 출처는 PG06 때 frame-src 에 추가
			csp: {
				mode: 'auto',
				directives: {
					'default-src': ['self'],
					'script-src': ['self'],
					'style-src': ['self', 'unsafe-inline'],
					'img-src': ['self', 'data:', 'blob:'],
					'font-src': ['self'],
					'connect-src': ['self'],
					'frame-src': ['self'],
					'frame-ancestors': ['none'],
					'base-uri': ['self'],
					'form-action': ['self'],
					'object-src': ['none']
				}
			}
		})
	],
	// 개발 서버 SSR 사전 번들(#14). adapter-cloudflare 가 SSR 의존성을 미리 번들하는데, SvelteKit 은 클라이언트에만
	// @sveltejs/kit 를 빼 둔다. 그대로면 앱 코드의 kit(번들 사본)과 개발 서버 런타임의 kit(원본)이 갈려
	// redirect() · error() 가 500 이 되고 sequence 가 'Could not get the request store' 를 낸다.
	// include: 첫 요청 때 늦게 발견돼 재번들되면 그 요청에서 svelte 사본이 갈려 500 이 나므로 서버 의존성은 미리 넣는다.
	environments: {
		ssr: {
			optimizeDeps: {
				exclude: ['@sveltejs/kit'],
				include: ['drizzle-orm', 'drizzle-orm/d1']
			}
		}
	},
	test: {
		expect: { requireAssertions: true },
		projects: [
			{
				extends: './vite.config.ts',
				test: {
					name: 'client',
					browser: {
						enabled: true,
						provider: playwright(),
						instances: [{ browser: 'chromium', headless: true }]
					},
					include: ['src/**/*.svelte.{test,spec}.{js,ts}'],
					exclude: ['src/lib/server/**']
				}
			},

			{
				extends: './vite.config.ts',
				test: {
					name: 'server',
					environment: 'node',
					include: ['src/**/*.{test,spec}.{js,ts}'],
					exclude: ['src/**/*.svelte.{test,spec}.{js,ts}']
				}
			}
		]
	}
});
