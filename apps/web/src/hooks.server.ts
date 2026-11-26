import type { Handle, HandleServerError } from '@sveltejs/kit/hooks';
// Cloudflare 바인딩(D1 등). 개발 중에는 어댑터가 wrangler.jsonc 를 읽어 로컬 에뮬레이션을 제공한다.
import { env } from 'cloudflare:workers';

import { groundOf, parseTheme, THEME_COOKIE } from '#lib/domain/appearance.ts';
import { createServices } from '#lib/server/container.ts';
import { chain } from '#lib/server/handle.ts';
import { log } from '#lib/server/log.ts';

/** 요청마다 번호를 붙인다 — 오류 화면에 보여 주고 로그에서 찾는 열쇠. */
const requestId: Handle = ({ event, resolve }) => {
	event.locals.requestId = crypto.randomUUID();
	return resolve(event);
};

const services: Handle = ({ event, resolve }) => {
	event.locals.services = createServices(env);
	return resolve(event);
};

/** 첫 화면부터 테마 · 그라운드가 맞게 그려지도록(깜빡임 없이) html 속성을 서버에서 채운다. */
const appearance: Handle = ({ event, resolve }) => {
	const theme = parseTheme(event.cookies.get(THEME_COOKIE));
	const ground = groundOf(event.url.pathname);
	return resolve(event, {
		transformPageChunk: ({ html }) =>
			html.replace('%admd.theme%', theme).replace('%admd.ground%', ground)
	});
};

/** 보안 헤더 — CSP 는 vite.config 의 kit.csp 가 담당(setup-agenda 7-4). */
const securityHeaders: Handle = async ({ event, resolve }) => {
	const response = await resolve(event);
	response.headers.set('X-Content-Type-Options', 'nosniff');
	response.headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');
	response.headers.set(
		'Permissions-Policy',
		'camera=(), microphone=(), geolocation=(), payment=()'
	);
	return response;
};

export const handle = chain(requestId, services, appearance, securityHeaders);

/** 예상 못 한 오류만 로그에 남기고, 사용자에게는 친절한 문구 + 오류 번호. (SvelteKit 3: kind 로 구분) */
export const handleError: HandleServerError = ({ kind, error, event }) => {
	const id = event.locals.requestId;
	if (kind === 'unknown') {
		log('error', 'unhandled', {
			requestId: id,
			path: event.url.pathname,
			message: error instanceof Error ? error.message : String(error)
		});
		return { message: '문제가 생겼어요. 잠시 뒤 다시 시도해 주세요.', id };
	}
	return { id };
};
