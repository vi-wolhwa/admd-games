// See https://svelte.dev/docs/kit/types#app.d.ts
import type { Services } from '#lib/server/container.ts';

declare global {
	namespace App {
		interface Error {
			message: string;
			/** 로그에서 찾을 오류 번호(요청 번호) */
			id?: string;
		}
		interface Locals {
			requestId: string;
			services: Services;
		}
		// interface PageData {}
		// interface PageState {}
		// Cloudflare 바인딩은 event.platform 이 아니라 `import { env } from 'cloudflare:workers'` 로 쓴다.
	}
}

export {};
