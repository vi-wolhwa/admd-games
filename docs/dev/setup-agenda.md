# 개발 환경 결정 안건 (2026-11-27~)

코드를 쓰기 전에 정할 것들. 사용자와 한 묶음씩(최대 4문항) 논의하고, 정해지면 이 표의 상태를 바꾸고 ADR(A등급) 또는 `decisions/log.md`(B등급)에 남긴다. **정해진 것은 바로 설정 파일 · 린트 규칙 · 문서로 옮겨 "말로만 있는 규칙"이 없게 한다.**

이미 정해진 것(ADR 0001~0005 · 0012): Cloudflare Workers 무료 · SvelteKit 3 + Svelte 5 · D1 + Drizzle(포트/어댑터) · better-auth · Tailwind 4 · npm 워크스페이스 · Node 24 · ESLint flat + Prettier(탭 · 작은따옴표 · 100자) · Vitest · GitHub Flow · Conventional Commits(타입 영어 · 설명 한국어) · CI(lint → check → test → build) · 디자인 원본 = 코드 + 갤러리.

설치된 버전(2026-11-27): kit 3.3.1 · svelte 5.58 · vite 8.3 · vitest 4.1 · typescript 6.0 · eslint 10.15 · tailwind 4.3 · wrangler 4.164.

## 1묶음 — 구조 (뒤의 모든 것에 영향)

| # | 안건 | 추천 | 상태 |
| --- | --- | --- | --- |
| 1-1 | 두 그라운드의 주소 구조 | **한 앱 · 경로: PlayGround `/play` · MakersGround `/makers`, `/` 로 오면 `/play` 로 이동**(307 임시 이동 — 나중에 `/` 를 소개 페이지로 쓸 여지) | **결정** |
| 1-2 | UI 컴포넌트 위치 | **`apps/web/src/lib/ui`**. 두 번째 앱이 생기면 `packages/ui` 로 분리 | **결정** |
| 1-3 | 컴포넌트 갤러리 도구 | **Storybook, 안 되면 `/design`** — 기준은 Claude 가 만들고 확인하기 가장 효율적인 쪽(이야기마다 자동 테스트 · 캡처를 돌릴 수 있는지까지 설치 때 확인) | **결정** |
| 1-4 | 데이터 읽기 · 쓰기 방식 | **`load` + form actions**. remote functions 는 안정화 뒤 재검토 | **결정** |

## 2묶음 — 코드 컨벤션

| # | 안건 | 추천 | 상태 |
| --- | --- | --- | --- |
| 2-1 | 이름 규칙 | **Svelte 관례형**: 컴포넌트 `PascalCase.svelte`, 그 외 `kebab-case.ts`, 변수 · 함수 `camelCase`, 타입 `PascalCase`, 상수 `UPPER_SNAKE`, 참/거짓 `is/has/can` | **결정** |
| 2-2 | 코드 안 언어 | **식별자 영어 · 주석과 테스트 이름 한국어** · 화면 문구 한국어 | **결정** |
| 2-3 | Svelte 5 규칙 | runes 만(`$props` · `$state` · `$derived`), 이벤트는 콜백 props, slot 대신 snippet, `$effect` 는 외부 동기화에만, 공유 상태는 `.svelte.ts` 클래스 + context | 논의 |
| 2-4 | 스타일 작성법 | **Tailwind 유틸리티 + 의미 토큰만 + 자체 변형 헬퍼**(외부 라이브러리 없음), `<style>` 은 유틸리티로 안 되는 것만 | **결정** |
| 2-5 | 컴포넌트 단위 · 폴더 | **가벼운 FSD + 패턴 층**: primitives → patterns → entities → features → widgets → 라우트, import 는 아래로만. 변형 규칙(토큰 · props · 합성 · snippet · 별도 · 특화 래퍼 · 라우트 폴더에서 시작) 그대로. 헤드리스 = **Bits UI 를 primitives 안에서만** — [component-architecture.md](component-architecture.md) | **결정** |
| 2-6 | 다국어 | MVP 한국어만, 문구는 컴포넌트에 직접. 나중을 위해 날짜 · 숫자는 `Intl` 로 | 논의 |

## 3묶음 — 린트 · 품질 장치

| # | 안건 | 추천 | 상태 |
| --- | --- | --- | --- |
| 3-1 | TypeScript 엄격도 | `strict` + `noUncheckedIndexedAccess` + `exactOptionalPropertyTypes` | 논의 |
| 3-2 | ESLint 수준 | typescript-eslint `strictTypeChecked` + `stylisticTypeChecked`, svelte `recommended` + 추가 규칙 몇 개 | 논의 |
| 3-3 | 구조 규칙을 린트로 강제 | 포트/어댑터 경계 · 원시 색 · 임의 값(`bg-[#…]`) 금지 · import 순서 | 논의 |
| 3-4 | 커밋 전 자동 검사 | Git 훅(lefthook 또는 simple-git-hooks): 바뀐 파일 포맷 · 린트 + 커밋 메시지 검사 | 논의 |
| 3-5 | 쓰지 않는 코드 · 의존성 찾기 | knip 을 CI 에 | 논의 |
| 3-6 | Worker 크기 감시 | 빌드 후 gzip 크기 검사(3MB 한도의 70% 경고) | 논의 |

## 4묶음 — 테스트

| # | 안건 | 추천 | 상태 |
| --- | --- | --- | --- |
| 4-1 | 테스트 층 | 단위(Vitest node) · 컴포넌트(Vitest 브라우저) · 화면 캡처 비교(갤러리 이야기마다 라이트/다크) · E2E(Playwright, 핵심 흐름만) | 논의 |
| 4-2 | 언제 쓰나 | 도메인 · 포트는 테스트 먼저, UI 는 이야기(story) 먼저 + 캡처, 버그는 재현 테스트부터 | 논의 |
| 4-3 | 커버리지 기준 | 숫자 목표 대신 "도메인 · 포트 100% 분기, UI 는 상태마다 이야기 1개" | 논의 |

## 5묶음 — 개발 방식 · 협업

| # | 안건 | 추천 | 상태 |
| --- | --- | --- | --- |
| 5-1 | 지금 브랜치 정리 | `design/redesign`(디자인 문서 · 캔버스) → PR → main 병합 후 개발 시작 | 논의 |
| 5-2 | 작업 단위 | 페이지 = 이슈 하나(마일스톤 = 출시 단계), 컴포넌트 변경 검토는 이슈 안에서 | 논의 |
| 5-3 | PR 규칙 | PR 템플릿(무엇 · 왜 · 화면 캡처 · 영향 페이지 · 확인한 것), 작게, 사용자 승인 후 Claude 가 병합(squash) | 논의 |
| 5-4 | 완료 기준(DoD) | verify 통과 · 갤러리 상태 전부 · 라이트/다크 · 키보드 · 문서 갱신 | 논의 |

## 6묶음 — 버저닝 · 배포

| # | 안건 | 추천 | 상태 |
| --- | --- | --- | --- |
| 6-1 | 앱 버전 | 사용자에게 보이는 버전 없이 배포 단위(커밋)로. 출시 묶음은 `v0.x` 태그 + 변경 기록 | 논의 |
| 6-2 | 게임 SDK 버전 | SemVer 엄격(메이커가 의존) — changesets 로 기록 | 논의 |
| 6-3 | 변경 기록 | Conventional Commits 로 자동 생성(release-please 또는 changesets) | 논의 |
| 6-4 | 환경 | 로컬 · PR 미리보기(Workers 미리보기 URL) · 운영. 별도 스테이징 없음 | 논의 |
| 6-5 | 운영 배포 · 원격 DB 이관 | 항상 사용자 승인 후(CLAUDE.md). 순서: 이관 → 배포, 되돌리기 절차 문서화 | 논의 |
| 6-6 | 의존성 업데이트 | Dependabot(무료) 주 1회 묶음 + 7일 숙성 규칙과 맞춤 | 논의 |

## 7묶음 — 아키텍처 세부

| # | 안건 | 추천 | 상태 |
| --- | --- | --- | --- |
| 7-1 | 폴더 구조 | 라우트는 화면, 도메인 로직은 `lib/server/domain/<기능>`, UI 는 `lib/ui` | 논의 |
| 7-2 | 입력 검증 | Valibot(작아서 Worker 3MB 에 유리) — 폼 · API · 환경 변수 | 논의 |
| 7-3 | 오류 · 로그 | 사용자 문구와 내부 오류 분리, Workers Logs(무료) 만. 외부 모니터링(Sentry 등)은 데이터 반출이라 보류 | 논의 |
| 7-4 | 보안 헤더 | CSP · iframe 샌드박스(게임) · 쿠키 설정을 hooks 한 곳에서 | 논의 |
| 7-5 | 가짜 데이터 | 갤러리 · 테스트 · 로컬 개발이 같은 가짜 데이터 모듈(fixtures)을 씀 | 논의 |
