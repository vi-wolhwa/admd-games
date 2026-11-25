import type { Handle } from '@sveltejs/kit/hooks';
// Cloudflare 바인딩(D1 등). 개발 중에는 어댑터가 wrangler.jsonc 를 읽어 로컬 에뮬레이션을 제공한다.
import { env } from 'cloudflare:workers';

import { createServices } from '#lib/server/container.ts';

export const handle: Handle = async ({ event, resolve }) => {
	event.locals.services = createServices(env);
	return resolve(event);
};
