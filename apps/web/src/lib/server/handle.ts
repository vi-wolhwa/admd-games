import type { Handle, ResolveOptions } from '@sveltejs/kit/hooks';

/**
 * 여러 handle 을 순서대로 잇는다 — SvelteKit 의 sequence 와 같은 동작.
 * sequence 를 쓰지 않는 이유: 개발 서버에서 Vite 가 @sveltejs/kit/hooks 를 따로 미리 번들해
 * SvelteKit 내부 상태가 둘로 갈리며 'Could not get the request store' 오류가 난다(2026-11, kit 3.3 · vite 8.3).
 * transformPageChunk 는 앞뒤 것을 모두 적용한다.
 */
export function chain(...handlers: Handle[]): Handle {
	return ({ event, resolve }) => {
		const step = (i: number, e: typeof event, outer?: ResolveOptions): ReturnType<Handle> => {
			const handler = handlers[i];
			if (!handler) return resolve(e, outer);
			return handler({
				event: e,
				resolve: async (next, inner) => step(i + 1, next, merge(outer, inner))
			});
		};
		return step(0, event);
	};
}

function merge(outer?: ResolveOptions, inner?: ResolveOptions): ResolveOptions | undefined {
	if (!outer) return inner;
	if (!inner) return outer;
	const a = outer.transformPageChunk;
	const b = inner.transformPageChunk;
	return {
		...outer,
		...inner,
		transformPageChunk:
			a && b
				? async (input) => {
						const html = await b(input);
						return html === undefined ? undefined : a({ ...input, html });
					}
				: (b ?? a)
	};
}
