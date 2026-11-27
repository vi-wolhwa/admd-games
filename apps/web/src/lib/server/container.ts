import { createD1Catalog } from './adapters/d1/catalog';
import { createD1Client } from './adapters/d1/client';
import { createD1GameDetails } from './adapters/d1/game-details';
import { createD1HealthProbe } from './adapters/d1/health';
import { createD1Reviews } from './adapters/d1/reviews';
import { createMemoryHealthProbe } from './adapters/memory/health';
import type { Catalog } from './ports/catalog';
import type { GameDetails, Reviews } from './ports/game-details';
import type { HealthProbe } from './ports/health';

/**
 * 컴포지션 루트(composition root): 어떤 어댑터를 쓸지 결정하는 유일한 곳.
 * 요청마다 hooks.server.ts 에서 만들어 event.locals.services 에 넣는다.
 * (Cloudflare 바인딩은 요청 안에서만 존재하므로 모듈 최상단에서 만들지 않는다.)
 */
export interface Services {
	health: HealthProbe;
	catalog: Catalog;
	gameDetails: GameDetails;
	reviews: Reviews;
}

export function createServices(env: Partial<Env> | undefined): Services {
	if (env?.DB) {
		const db = createD1Client(env.DB);
		return {
			health: createD1HealthProbe(db),
			catalog: createD1Catalog(db),
			gameDetails: createD1GameDetails(db),
			reviews: createD1Reviews(db)
		};
	}
	return {
		health: createMemoryHealthProbe(),
		catalog: missingDatabase,
		gameDetails: { getGame: noDb, similarGames: noDb, makerProfile: noDb },
		reviews: { listReviews: noDb, topPhrases: noDb }
	};
}

/** DB 바인딩이 없을 때(설정 오류) — 빈 목록으로 숨기지 않고 오류로 드러낸다 */
const noDb = () => Promise.reject(new Error('D1 바인딩(DB)이 없어요.'));
const missingDatabase: Catalog = {
	listGames: () => Promise.reject(new Error('D1 바인딩(DB)이 없어 게임 목록을 읽을 수 없어요.')),
	listTags: () => Promise.reject(new Error('D1 바인딩(DB)이 없어 태그를 읽을 수 없어요.'))
};
