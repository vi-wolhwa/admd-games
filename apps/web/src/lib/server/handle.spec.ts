import type { RequestEvent } from '@sveltejs/kit';
import type { ResolveOptions } from '@sveltejs/kit/hooks';
import { describe, expect, it } from 'vitest';

import { chain } from './handle';

const event = {} as RequestEvent;

/** SvelteKit 의 resolve 흉내: transformPageChunk 를 실제로 적용해 본문을 만든다. */
async function fakeResolve(_e: RequestEvent, opts?: ResolveOptions): Promise<Response> {
	const html = (await opts?.transformPageChunk?.({ html: '<html %a% %b%>', done: true })) ?? '';
	return new Response(html);
}

describe('chain (handle 잇기)', () => {
	it('앞뒤 handle 의 transformPageChunk 를 둘 다 적용하고, 뒤 handle 의 응답 수정이 남는다', async () => {
		const first = chain(
			({ event: e, resolve }) =>
				resolve(e, { transformPageChunk: ({ html }) => html.replace('%a%', 'A') }),
			({ event: e, resolve }) =>
				resolve(e, { transformPageChunk: ({ html }) => html.replace('%b%', 'B') }),
			async ({ event: e, resolve }) => {
				const res = await resolve(e);
				res.headers.set('x-last', '1');
				return res;
			}
		);
		const res = await first({ event, resolve: fakeResolve });
		expect(await res.text()).toBe('<html A B>');
		expect(res.headers.get('x-last')).toBe('1');
	});
});
