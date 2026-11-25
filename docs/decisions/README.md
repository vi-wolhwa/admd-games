# 결정 기록

- A등급 결정은 `NNNN-제목.md` ADR(Architecture Decision Record: 배경 · 선택지 · 결정 · 이유 · 결과)로 남긴다.
- B등급 결정은 [log.md](log.md) 에 한 줄씩 남긴다. 사용자가 언제든 뒤집을 수 있다.
- 결정을 뒤집을 때는 기존 ADR 을 지우지 않고 상태를 `대체됨 → NNNN` 으로 바꾼 뒤 새 ADR 을 쓴다.

| 번호 | 제목 | 상태 |
| --- | --- | --- |
| [0001](0001-hosting-cloudflare-workers.md) | 호스팅: Cloudflare Workers 무료 플랜 | 승인 |
| [0002](0002-framework-sveltekit.md) | 프레임워크: SvelteKit | 승인 |
| [0003](0003-database-d1-behind-ports.md) | DB: D1 + Drizzle, 포트/어댑터 뒤에 격리 | 승인 |
| [0004](0004-auth-better-auth.md) | 인증: better-auth (게스트 → OAuth) | 승인 (미구현) |
| [0005](0005-repository-and-workflow.md) | 저장소·모노레포·브랜치·커밋 규칙 | 승인 |
