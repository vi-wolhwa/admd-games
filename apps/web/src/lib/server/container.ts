import { createD1Client } from './adapters/d1/client';
import { createD1HealthProbe } from './adapters/d1/health';
import { createMemoryHealthProbe } from './adapters/memory/health';
import type { HealthProbe } from './ports/health';

/**
 * 컴포지션 루트(composition root): 어떤 어댑터를 쓸지 결정하는 유일한 곳.
 * 요청마다 hooks.server.ts 에서 만들어 event.locals.services 에 넣는다.
 * (Cloudflare 바인딩은 요청 안에서만 존재하므로 모듈 최상단에서 만들지 않는다.)
 */
export interface Services {
	health: HealthProbe;
}

export function createServices(env: Partial<Env> | undefined): Services {
	if (env?.DB) {
		const db = createD1Client(env.DB);
		return { health: createD1HealthProbe(db) };
	}
	return { health: createMemoryHealthProbe() };
}
