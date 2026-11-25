import { sql } from 'drizzle-orm';

import type { HealthProbe } from '../../ports/health';
import type { D1Client } from './client';

export function createD1HealthProbe(db: D1Client): HealthProbe {
	return {
		async check() {
			try {
				await db.run(sql`select 1`);
				return { storage: 'ok', adapter: 'd1' };
			} catch {
				return { storage: 'error', adapter: 'd1' };
			}
		}
	};
}
