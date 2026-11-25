import { describe } from 'vitest';

import { runHealthProbeContract } from '../../ports/health.contract';
import { createMemoryHealthProbe } from './health';

describe('memory HealthProbe', () => {
	runHealthProbeContract(() => createMemoryHealthProbe());
});
