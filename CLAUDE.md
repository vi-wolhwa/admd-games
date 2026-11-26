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
- 사용자는 **코드 리뷰를 하지 않는다.** UI · 디자인처럼 사용자가 직접 봐야 하는 결과물이 아닌 PR(환경 · 도구 · 문서 · 의존성 · 리팩터링)은 CI 통과 후 Claude 가 직접 병합하고 결과만 보고한다. 화면이 바뀌는 PR 은 확정 전 병합 금지.
- 결정의 근거로 **"사람이 편해서"는 쓰지 않는다** — 구현 · 검증은 Claude 가 한다. 기준: Claude 의 정확성 · 검증 가능성, 제품 품질, 비용.
- 중요한 도메인 규칙 · 기획은 반드시 사용자와 상의한다. 이미 만든 컴포넌트를 다른 곳에서 쓰거나 바꿀 때는 영향 목록 · 전략 후보 · 추천을 들고 함께 검토한다(ADR 0012).
- PR 본문 끝에 "Generated with Claude Code" 문구를 넣지 않는다.

## 기술 스택 (근거: docs/decisions/, docs/dev/setup-agenda.md)

| 영역 | 선택 |
| --- | --- |
| 호스팅 | Cloudflare Workers 무료 플랜 (`*.workers.dev`) — 운영 `admd-games`, PR 미리보기 `admd-games-preview` |
| 프레임워크 | SvelteKit 3 + Svelte 5 (runes), `@sveltejs/adapter-cloudflare` 8. 데이터는 `load` + form actions |
| DB | Cloudflare D1 (SQLite) + Drizzle ORM, **포트/어댑터 뒤에 격리** |
| 인증 | better-auth (게스트 익명 → OAuth 연결) — SH01 에서 구현 |
| 스타일 | Tailwind CSS 4 + 디자인 토큰(`apps/web/src/lib/styles/tokens.css` = 디자인 원본) |
| 헤드리스 부품 | Bits UI 를 `lib/ui/primitives` 안에서만 감싸 씀 |
| 갤러리 | Storybook 10 (`@storybook/sveltekit`) — 이야기 = 테스트 · 접근성 · 라이트/다크 캡처 비교 |
| 테스트 | Vitest (server: node / client · storybook: 브라우저 Playwright) |
| 검증 | Zod 4 (서버에서만 — 처음 쓸 때 설치) |
| 런타임 | Node 24, npm 11 워크스페이스 모노레포 |

## 명령어 (저장소 루트에서)

```sh
npm run setup                  # 최초 1회: 의존성 + Playwright Chromium + 로컬 D1 마이그레이션 (+ 커밋 훅 설치)
npm run dev                    # 개발 서버 http://localhost:5173  (redirect · sequence 개발 서버 문제: #14)
npm run storybook -w web       # 갤러리 http://localhost:6006
npm run verify                 # lint(+구조 경계) → check → test → knip → build → Worker 크기 (PR 전)
npm run design:build -w web    # 갤러리 정적 빌드 → apps/web/storybook-static (아티팩트 게시용)
npm run db:generate -w web     # 스키마 변경 → 마이그레이션 SQL 생성
npm run db:migrate:local -w web
```

운영 빌드 확인: `npm run build -w web && cd apps/web && npx wrangler dev`.

## 구조

```
apps/web/
  src/routes/(play)/play/…       PlayGround (/ → /play 307)
  src/routes/(makers)/makers/…   MakersGround
  src/lib/ui/                    컴포넌트 — 층: primitives → patterns → entities/<도메인> → features/<행동> → widgets
                                 (import 는 아래 층으로만, 같은 층 다른 묶음 금지 — scripts/check-boundaries.mjs)
  src/lib/domain/<영역>          부작용 없는 순수 규칙(화면 · 서버 공용)
  src/lib/server/                ports/ · adapters/<기술>/ · container.ts(어댑터 고르는 유일한 곳) · handle.ts · log.ts
  src/lib/fixtures/              가짜 데이터(이야기 · 테스트 · 시드 전용, 운영 코드에서 import 금지)
  src/lib/styles/tokens.css      디자인 토큰 원본
  .storybook/                    갤러리 설정 · 캡처 비교(vitest.visual.ts)
  migrations/                    wrangler 가 적용하는 SQL
scripts/                         구조 경계 · 커밋 훅 · CI 범위 · 배포 관문 · 크기 검사
docs/                            STATUS · 결정(ADR) · dev/(환경 결정 · 컴포넌트 구조 · 페이지 순서) · operations.md · design/
```

자세한 규칙: `docs/architecture.md`, `docs/dev/component-architecture.md`(변형 규칙 5절).

## 코드 컨벤션 (실수하기 쉬운 것 위주)

- 이름: 컴포넌트 `PascalCase.svelte`, 그 외 `kebab-case.ts`, 변수 · 함수 `camelCase`, 타입 `PascalCase`, 상수 `UPPER_SNAKE`, 참/거짓 `is/has/can`. 식별자는 영어, **주석과 테스트 이름은 한국어**, 화면 문구 한국어(당분간 한국어만, 날짜 · 숫자는 `Intl`).
- Svelte 5: runes 만, 자식→부모는 콜백 props, slot 대신 snippet, `$effect` 는 외부 동기화만(계산은 `$derived`), 공유 상태는 `.svelte.ts` 클래스 + context(모듈 전역 상태 금지), props 는 `interface Props`.
- 스타일: Tailwind 유틸리티 + **의미 토큰만**(`bg-accent`, `text-ink-3`). 원시 색 · 임의 색 · 없는 클래스는 린트 오류. 변형은 자체 헬퍼(외부 라이브러리 없음).
- 앱 내부 import 는 `#lib/...` 이고 **`.ts` 확장자를 붙인다** (`#lib/server/container.ts`).
- 훅 타입은 `@sveltejs/kit/hooks` 에서. handle 잇기는 `#lib/server/handle.ts` 의 `chain`(SvelteKit `sequence` 는 개발 서버에서 깨짐 — #14).
- Cloudflare 바인딩은 `import { env } from 'cloudflare:workers'` (hooks.server.ts 에서만). 테스트 가능한 코드에는 env 를 인자로 넘긴다.
- 무료 플랜 제약: Worker CPU 10ms/요청, 코드 3MB(gzip — 70% 경고 · 90% 실패), D1 읽기 500만 행/일 · 쓰기 10만 행/일. 비싼 연산과 풀 테이블 스캔을 피한다. 최적화 후에도 넘으면 사용자에게 플랜 검토를 올린다.
- TS: `strict` + `noUncheckedIndexedAccess` 등. ESLint: typescript-eslint `strictTypeChecked`, import 자동 정렬. Prettier(탭, 작은따옴표, 100자).
- 테스트: 도메인 · 포트는 테스트 먼저, UI 는 이야기 먼저(+캡처), 버그는 재현 테스트부터. 중복 · 당연한 · 과하게 느린 테스트는 쓰지 않는다.
- 의존성: `.npmrc` 의 `min-release-age=7`. 설치 스크립트가 필요한 패키지는 `npm install-scripts approve <pkg>`. 업데이트는 Dependabot(보안 즉시 · 월 1회 묶음 · 메이저 제외).

## Git · 배포 (ADR 0013 · docs/operations.md)

- 저장소는 **공개**. 브랜치: `feat/…` · `fix/…` · `chore/…` · `docs/…` → PR → **`develop`** → '내보내기' PR → **`main` = 운영 자동 배포**. main · develop 직접 푸시는 규칙 세트로 막힘(필수 검사 `verify`, main 은 `main-source` 도).
- 작업 PR 은 squash, 내보내기 PR(develop → main)은 merge commit. 병합된 브랜치는 지운다(자동 삭제 켜짐 + 로컬도 정리).
- 모든 일은 이슈로(페이지 = 이슈 하나), **중복 이슈 금지** — 같은 주제는 기존 이슈를 갱신. PR 본문에 `Closes #n`. 페이지 하나 = PR 하나, 공통 컴포넌트 변경 · 환경 변경은 별도 PR.
- 커밋 메시지: Conventional Commits, 타입은 영어 · 설명은 한국어(커밋 훅이 검사). 예) `feat: 게임 카탈로그 필터 추가`.
- 버전 · 변경 기록은 v1.0.0(정식 출시)부터. 작은 수정마다 올리지 않고 묶음 단위.
