import { expect, it } from 'vitest';

import type { HealthProbe } from './health';

/**
 * 계약 테스트(contract test): 모든 HealthProbe 어댑터가 통과해야 하는 공통 테스트.
 * 새 어댑터를 만들면 그 어댑터의 테스트 파일에서 이 함수를 호출한다.
 * → DB를 교체해도 같은 테스트가 동작을 보장한다.
 */
export function runHealthProbeContract(makeProbe: () => HealthProbe | Promise<HealthProbe>) {
	it('정상 저장소에서 storage: ok 를 반환한다', async () => {
		const probe = await makeProbe();
		const status = await probe.check();
		expect(status.storage).toBe('ok');
		expect(status.adapter.length).toBeGreaterThan(0);
	});
}
