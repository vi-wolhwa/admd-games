# aDmD Games — Claude 작업 안내

웹 게임 플랫폼. 첫 출시(MVP)는 플레이어용 **PlayGround**, 메이커용 **MakersGround** 는 후속 마일스톤.
표기는 항상 `aDmD` (D 두 개가 대문자 — "DmD"가 표정처럼 보이도록 한 의도된 표기).

## 세션 시작 루틴 (반드시)

1. 이 파일 → `docs/STATUS.md` → `git log --oneline -15` → 열린 PR/이슈(`gh pr list`, `gh issue list`) 순으로 읽는다.
2. 현재 상태를 5줄로 요약하고 다음 작업을 제안한다.
3. 저장소가 유일한 기억 장치다. 대화에만 남은 결정은 없는 것으로 본다.

## 세션 종료 루틴 ("정리해줘" 또는 마일스톤마다)

- `docs/STATUS.md` 갱신(현재 Phase, 완료, 진행 중, 다음 3가지, 열린 질문, 블로커, 마지막 업데이트 시각) → 커밋 → 푸시.
- 미완성 작업은 `wip/<주제>` 브랜치로 푸시해 다른 기기에서 이어받게 한다.

## 협업 방식

- 사용자 = 최종 결정자. Claude = 제안·실행·기록. 대부분의 구현은 Claude가 직접 한다.
- 결정이 필요하면 객관식(2~4개, 추천안 첫 번째 "(추천)" + 한 줄 이유, 한 번에 최대 4문항)으로 묻는다.
- **결정 등급**
  - A (되돌리기 어려움: 프레임워크·DB·인증·호스팅·도메인·라이선스·비용·프로덕션 배포·핵심 UX): 묻고 답을 받기 전엔 진행하지 않는다. 확정 시 `docs/decisions/` 에 ADR.
  - B (관례 있음, 되돌릴 수 있음): 추천안으로 진행하고 `docs/decisions/log.md` 에 한 줄 기록.
  - C (사소함): 묻지 않는다.
- **승인 필수**: 유료 가입/결제(이 프로젝트는 무료만 사용), 프로덕션 배포, 파일·브랜치·저장소 삭제, force push, 원격 DB 마이그레이션, 외부로 데이터 전송.
- 시크릿은 절대 커밋하지 않는다. `.env.example` 에 키 이름만 두고 값은 사용자가 넣는다.
- 응답은 한국어로 간결하게: ① 진행 결과 → ② 결정 질문 → ③ 다음 단계. 전문 용어는 처음 나올 때 한 줄 풀이.

## 기술 스택 (근거: docs/decisions/)

| 영역 | 선택 |
| --- | --- |
| 호스팅 | Cloudflare Workers 무료 플랜 (`*.workers.dev`) |
| 프레임워크 | SvelteKit 3 + Svelte 5 (runes), `@sveltejs/adapter-cloudflare` 8 |
| DB | Cloudflare D1 (SQLite) + Drizzle ORM, **포트/어댑터 뒤에 격리** |
| 인증 | better-auth (게스트 익명 → OAuth 연결) — 아직 미구현 |
| 스타일 | Tailwind CSS 4 (디자인 토큰은 Phase 2에서 설계) |
| 테스트 | Vitest (server: node / client: 브라우저 Playwright) |
| 런타임 | Node 24, npm 11 워크스페이스 모노레포 |

## 명령어 (저장소 루트에서)

```sh
npm run setup      # 최초 1회: 의존성 설치 + Playwright Chromium + 로컬 D1 마이그레이션
npm run dev        # 개발 서버 http://localhost:5173
npm run verify     # lint → check → test → build (PR 전 필수)
npm run db:generate -w web        # 스키마 변경 → 마이그레이션 SQL 생성
npm run db:migrate:local -w web   # 로컬 D1 에 적용
```

## 구조

```
apps/web/                  SvelteKit 앱 (Cloudflare Worker 하나로 배포)
  src/lib/server/
    ports/                 인터페이스 + 계약 테스트(*.contract.ts). 도메인·라우트는 여기에만 의존
    adapters/d1/           D1 + Drizzle 구현, schema.ts (어댑터 밖에서 import 금지)
    adapters/memory/       인메모리 구현 (테스트·폴백)
    container.ts           어떤 어댑터를 쓸지 고르는 유일한 곳
  migrations/              wrangler 가 적용하는 SQL 마이그레이션
packages/                  (예정) 게임 SDK 등 공유 패키지
docs/                      STATUS, 결정(ADR), 아키텍처, 참고 자료
```

자세한 규칙: `docs/architecture.md`.

## 코드 컨벤션 (실수하기 쉬운 것 위주)

- SvelteKit 3: 앱 내부 import 는 `#lib/...` 이고 **`.ts` 확장자를 붙인다** (`#lib/server/container.ts`). TypeScript 가 package.json `imports` 경로에 확장자를 자동으로 붙이지 않기 때문.
- `Handle` 등 훅 타입은 `@sveltejs/kit/hooks` 에서 import.
- Cloudflare 바인딩은 `event.platform` 이 아니라 `import { env } from 'cloudflare:workers'` (hooks.server.ts 에서만). 테스트 가능한 코드에는 env 를 인자로 넘긴다.
- 무료 플랜 제약: Worker CPU 10ms/요청, 코드 3MB(gzip), D1 읽기 500만 행/일·쓰기 10만 행/일. 비싼 연산(비밀번호 해싱 등)과 풀 테이블 스캔을 피한다.
- 포매팅: Prettier(탭, 작은따옴표, 100자). 린트: ESLint flat config.
- 의존성: `.npmrc` 의 `min-release-age=7` 로 공개 7일 미만 버전은 설치하지 않는다. 설치 스크립트가 필요한 패키지는 `npm install-scripts approve <pkg>` 로 명시 허용(package.json `allowScripts`).

## Git

- GitHub Flow: `main` 은 항상 배포 가능. 작업은 `feat/…`, `fix/…`, `chore/…`, `docs/…` 브랜치 → PR → 사용자 리뷰 → 머지. **main 직접 푸시 금지** (비공개 무료 저장소라 보호 규칙을 못 걸어서 관례로 지킨다).
- 커밋 메시지: Conventional Commits, 타입은 영어·설명은 한국어. 예) `feat: 게임 카탈로그 필터 추가`.
- 이슈 단위로 작업하고 PR 본문에 `Closes #n`.
