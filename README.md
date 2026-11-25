# aDmD Games

브라우저에서 바로 플레이하는 웹 게임 플랫폼.

- **PlayGround** — 플레이어용 사이트 (첫 출시 범위)
- **MakersGround** — 메이커용 사이트 (후속)

## 빠른 시작

필요한 것: Node 24, npm 11 (Docker·DB 설치 불필요 — 로컬 DB는 파일로 돌아갑니다)

```sh
npm run setup   # 최초 1회
npm run dev     # http://localhost:5173
```

`http://localhost:5173/api/health` 가 `{"storage":"ok","adapter":"d1"}` 이면 정상입니다.

## 명령어

| 명령 | 설명 |
| --- | --- |
| `npm run dev` | 개발 서버 |
| `npm run verify` | 린트 → 타입 검사 → 테스트 → 빌드 |
| `npm run format` | 코드 포매팅 |
| `npm run db:generate -w web` | DB 스키마 변경을 마이그레이션 SQL로 생성 |
| `npm run db:migrate:local -w web` | 로컬 DB에 마이그레이션 적용 |

## 문서

- [현재 상태](docs/STATUS.md)
- [아키텍처](docs/architecture.md)
- [기술 결정 기록(ADR)](docs/decisions/)
- [작업 안내 (Claude용)](CLAUDE.md)

© vi-wolhwa. All rights reserved.
