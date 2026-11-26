/**
 * Port(포트) = 애플리케이션이 바깥 세계(DB, 외부 API)에 요구하는 기능의 인터페이스.
 * 도메인·라우트 코드는 이 인터페이스에만 의존하고, 구현(어댑터)은 container.ts 에서 고른다.
 * DB를 바꿀 때는 adapters/ 아래에 새 구현을 추가하고 container.ts 만 고치면 된다.
 */
export interface HealthProbe {
	/** 저장소에 실제로 질의가 가능한지 확인한다. */
	check(): Promise<HealthStatus>;
}

export interface HealthStatus {
	storage: 'ok' | 'error';
	/** 어떤 어댑터가 응답했는지 (예: 'd1', 'memory') */
	adapter: string;
}
