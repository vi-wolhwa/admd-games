import type { HealthProbe } from '../../ports/health';

/** 테스트와 DB 바인딩이 없는 환경용 인메모리 구현. */
export function createMemoryHealthProbe(): HealthProbe {
	return {
		check() {
			return Promise.resolve({ storage: 'ok', adapter: 'memory' });
		}
	};
}
