# 0003. DB: Cloudflare D1 + Drizzle, 포트/어댑터 뒤에 격리

- 상태: 승인 (2026-11-26, 사용자 승인)
- 등급: A

## 배경

반드시 무료여야 하고, **나중에 DB 를 교체할 수 있는 구조**가 중요하다. 여러 기기에서 같은 개발 환경이 명령 한두 개로 재현되어야 한다 (현재 PC 에 Docker 없음).

## 선택지

| 후보 | 무료 한도 | 장점 | 단점 |
| --- | --- | --- | --- |
| **Cloudflare D1 (SQLite)** | 5GB(DB당 500MB), 읽기 500만 행/일, 쓰기 10만 행/일 | Worker 와 같은 네트워크(연결 관리 불필요), 잠들지 않음, 로컬은 파일로 에뮬레이션 | SQLite 방언, 일반 트랜잭션 대신 batch |
| Neon Postgres | 프로젝트당 약 0.5~1GB, 유휴 5분 후 정지(재기동 지연) | 표준 Postgres, 브랜치 | Workers 에서 연결 드라이버 필요, 콜드 스타트 |
| Supabase Postgres | 500MB, 프로젝트 2개 | Auth·Storage 일체 | **7일 비활성 시 프로젝트 일시정지**, 강한 종속 |
| Turso (libSQL) | 무료 플랜 있음 | SQLite 호환 | 외부 서비스가 하나 더 늘어남 |

## 결정

- 운영 DB: Cloudflare D1. ORM: Drizzle (`drizzle-kit generate` 로 SQL 마이그레이션 생성, `wrangler d1 migrations apply` 로 적용).
- 로컬 DB: wrangler/어댑터가 `.wrangler/` 아래 SQLite 파일로 D1 을 에뮬레이션 — 설치할 것 없음.
- **모든 DB 접근은 포트(인터페이스) 뒤의 어댑터에서만** 한다 (`docs/architecture.md`).

## 이유

무료 한도 안에서 운영 부담(연결·정지·콜드 스타트)이 가장 적고, 개발 환경 재현이 가장 쉽다. 교체 가능성은 DB 제품 선택이 아니라 코드 구조(포트/어댑터 + 계약 테스트)로 확보한다.

## 결과

- 라우트·도메인은 Drizzle 이나 D1 을 직접 쓰지 않는다.
- 스키마 이식성 규칙(UUID text, epoch ms integer, SQLite 전용 함수 금지)을 지킨다.
- D1 어댑터의 계약 테스트는 실제 D1 환경(`@cloudflare/vitest-pool-workers`)에서 돌리도록 첫 도메인 포트를 만들 때 추가한다.
- D1 무료 한도 초과 시 쿼리가 실패하므로(2026-09-01 부터 강제), 인덱스와 집계 캐싱을 설계 단계에서 챙긴다.
