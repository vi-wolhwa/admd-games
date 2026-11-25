# 아키텍처

## 한눈에

```
브라우저 ──▶ Cloudflare Worker (SvelteKit) ──▶ D1 (SQLite)
                 │
                 └─ 정적 파일(JS·CSS·이미지)은 Workers Static Assets 가 직접 서빙 (무료·무제한)
```

예정 (해당 마일스톤에서 ADR 로 확정):

- **게임 실행**: 게임은 별도 출처(origin)의 Worker 정적 에셋으로 올리고 플랫폼은 `<iframe sandbox>` 로 띄운다. 플랫폼↔게임 통신은 `packages/game-sdk` 의 postMessage 프로토콜.
- **실시간 멀티플레이**: Cloudflare Durable Objects (무료 플랜에서 SQLite 기반 DO 사용 가능).

## 서버 코드 계층 — 포트와 어댑터

DB 를 나중에 바꿀 수 있게 하는 것이 핵심 요구사항이다. 그래서 서버 코드는 세 층으로 나눈다.

| 층 | 위치 | 하는 일 | 의존해도 되는 것 |
| --- | --- | --- | --- |
| 라우트·도메인 | `src/routes`, (예정) `src/lib/server/domain` | 화면·API·비즈니스 규칙 | `ports/` 의 타입, `event.locals.services` |
| 포트 | `src/lib/server/ports` | "무엇이 필요한가"를 인터페이스로 정의 + 계약 테스트 | 없음 (순수 TypeScript) |
| 어댑터 | `src/lib/server/adapters/<기술>` | 포트를 특정 기술로 구현 (D1, 메모리, 나중에 Postgres …) | 해당 기술 라이브러리 |

연결은 `src/lib/server/container.ts` 한 곳에서만 한다. `hooks.server.ts` 가 요청마다 `createServices(env)` 를 호출해 `event.locals.services` 에 넣는다.

### 규칙

1. 라우트·도메인은 `drizzle-orm` 이나 `adapters/` 를 **직접 import 하지 않는다**. 오직 `locals.services.*` 를 쓴다.
2. 포트의 메서드는 "도메인 언어"로 짓는다. (`findTopByPlays(limit)` ○ / `select(...)` ×) 반환 타입도 도메인 타입이지 DB 행(row)이 아니다.
3. 포트마다 `*.contract.ts` 계약 테스트를 만들고, 모든 어댑터가 같은 계약 테스트를 통과해야 한다.
4. 스키마는 이식성을 지킨다: ID 는 `text`(UUID), 시각은 `integer`(epoch ms), 불리언은 `integer` 0/1, SQLite 전용 함수(JSON1 등)에 기대지 않는다.
5. 트랜잭션이 필요한 작업(예: 게스트 데이터 병합)은 포트에 하나의 메서드로 정의해 어댑터 안에서 원자적으로 처리한다. (D1 은 일반 트랜잭션 대신 `batch()` 를 쓴다.)

### DB 를 바꾸는 방법 (예: Postgres)

1. `adapters/postgres/` 를 만들고 각 포트를 구현한다 (Drizzle `pg-core` 스키마).
2. 같은 계약 테스트를 통과시킨다.
3. `container.ts` 에서 환경에 따라 어댑터를 고른다.
4. 데이터 이관 스크립트로 D1 → 새 DB 로 옮긴다.

라우트·도메인 코드는 바뀌지 않는다.

## 무료 플랜 예산 (2026-11 기준, 재확인 필요 시 ADR 0001 링크)

| 자원 | 한도 | 설계에 주는 영향 |
| --- | --- | --- |
| Worker 요청 | 10만/일 (정적 에셋 제외) | 정적으로 낼 수 있는 페이지는 프리렌더 |
| Worker CPU | 10ms/요청 | 비밀번호 해싱 같은 무거운 연산 금지 → OAuth·익명 로그인만 |
| Worker 크기 | 3MB (gzip) | 무거운 서버 의존성 금지 |
| D1 | 읽기 500만 행/일, 쓰기 10만 행/일, DB당 500MB | 인덱스 필수, 풀 스캔 금지, 집계는 미리 계산해 저장 |
| 정적 에셋 | 무제한 요청, 버전당 2만 파일, 파일당 25MiB | 게임 빌드 파일 크기 관리 |

## 파일 저장 (ADR 0006 · 0007)

- 설치 파일은 `FileStorage` 포트 뒤에 둔다(운영 어댑터 `adapters/r2/`, 테스트 `adapters/memory/`). 포트는 구글 드라이브 같은 약한 저장소도 구현할 수 있는 최소 공통분모(업로드 대상 `presigned-multipart` | `resumable-session`, `quarantine` → `public` 승격, 짧은 수명 다운로드 주소).
- 파일 메타데이터(키 ↔ 저장소 id, 영역, SHA-256, 검사 결과)는 DB 포트에 둔다.
- `public` 승격은 **검사 `clean` + 운영자 승인** 전이 안에서만 일어난다. 자동 공개 경로는 없다.
