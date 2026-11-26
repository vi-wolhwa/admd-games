# B등급 결정 로그

언제든 뒤집을 수 있는 관례적 결정. 뒤집을 때는 줄을 지우지 말고 아래에 새 줄을 추가한다.

| 날짜 | 결정 | 이유 |
| --- | --- | --- |
| 2026-11-26 | 스타일링은 Tailwind CSS 4 로 시작 | sv 공식 애드온, 디자인 토큰을 CSS 변수로 정의하기 쉬움. 디자인 시스템 설계 후 재검토 |
| 2026-11-26 | `tsconfig` 에서 `checkJs: false` | `wrangler types` 가 빌드 산출물(`_worker.js`)을 타입 참조로 끌어와 생성 JS 까지 검사되는 문제 회피. 우리 코드는 전부 TS |
| 2026-11-26 | 앱 내부 import 에 `.ts` 확장자 명시 (`#lib/...ts`) | TypeScript 가 package.json `imports` 대상에 확장자를 붙이지 않음 |
| 2026-11-26 | drizzle-kit 은 SQL 생성만, 적용은 wrangler | 로컬·원격 모두 같은 마이그레이션 파일·같은 도구로 적용, 로컬엔 토큰 불필요 |
| 2026-11-26 | 디자인 토큰 3층(원시 `@theme` → 의미 CSS 변수 → 컴포넌트), Tailwind 기본 팔레트·글자 크기·그림자·반경은 `initial` 로 제거 | 기본값(blue-600, text-xl 등)을 실수로 쓰지 못하게. 원본 `docs/design/system/tokens.css` |
| 2026-11-26 | 다크 모드: 채움색은 라이트와 같고 글자·옅은 바탕만 400/900 톤. 테마마다 `--dark` 0/1 스위치 + `color-mix` 로 테마·그라운드 경계마다 강조 토큰 재계산 | 다크 안의 라이트 섬, PlayGround 안의 인주 띠처럼 중첩돼도 선택자 우선순위 싸움 없이 맞게 풀림 |
| 2026-11-26 | v10 정리: 순위 숫자 26→28px, 태그 11.5→12px, 툴팁 12.5→13px, 240px 이상 아트 반경 12→14, 툴팁 초록·잼 주황을 비취 400·인주 400 으로 | 시스템 규칙 하나로 맞춤(Gasoek 28px 이상, 원시 색 줄이기). 화면 인상은 거의 같음 |
| 2026-11-26 | 자모 얼굴 타일 12색 = 같은 휘도(Y .155) · 채도 상한 C .12. 메이커는 대표 게임색을 같은 휘도로 맞춘 색 | 모든 얼굴이 흰 글자 5.1:1 로 같은 대비, 그라운드 강조색과 겹치지 않는 차분한 톤 |
| 2026-11-26 | 아이콘: v10 의 16 격자·1.7px 선 아이콘 17개를 기본 세트로, 부족분은 Lucide(ISC)를 같은 규격으로 맞춰 추가 | 이미 쓰는 그림과 일관, 라이선스 자유 |
| 2026-11-26 | `.claude/launch.json` 에 개발 서버(`web`) 실행 설정 추가 | 데스크톱 앱 미리보기에서 바로 띄우기 |
| 2026-11-26 | 캔버스 파일 이름 = `영역2글자+번호2자리-영문이름`(예 `PG05-game`), 메뉴 이름 = `PG05 게임 상세`. 영역 DS · PG · MG · SH · AD, 모바일 묶음 91~, 번호 고정. 옛 반복본 · 비교 시안 · Claude Design 원본은 `docs/design/archive/` 보관 후 캔버스에서 삭제(사용자 승인) | 46페이지를 코드로 부르고 정렬 · 링크(`#page-PG05-game`)가 되게. 목록은 `docs/design/canvas/README.md` |
| 2026-11-27 | PG03 전체 게임을 갤러리형으로: 화면 폭 가득 5열 큰 그림, 위쪽 띠(장르 탭 + 드롭다운 한 판 · 실행 · 인원 · 정렬, 첫 항목은 모두 '전체') | 사용자 요청(큰 그림 갤러리 느낌 참고). 필터 상자는 드롭다운으로 접어 그림 면적을 늘림 |
| 2026-11-27 | 다크 모드 홈의 주간 랭킹 띠는 쪽빛 바탕을 빼고 페이지 바탕과 같게(라이트는 옅은 쪽빛 띠 유지) | 다크에서 짙은 파란 덩어리로 보여 이유 없이 튐(사용자 지적) |
| 2026-11-27 | 카드 hover 때 아트를 transform 대신 top 으로 올린다 | transform 이 쌓임 맥락을 만들어 실행 칩 툴팁이 카드 링크 덮개 아래로 깔렸음 |
| 2026-11-27 | 이어하기 진행 막대는 SDK 로 진행도를 알려 준 게임에만, 설치형은 새 버전이 있을 때만 이어하기에 | 설치형 · SDK 없는 게임은 진행도를 알 수 없음 — docs/product/continue-and-achievements.md |
| 2026-11-27 | PG03 갤러리 v2: 화면 전체 폭 → 콘텐츠 폭(1200) 안 4열 큰 카드. 장르는 태그 여러 개 선택(고른 것 중 하나라도 해당 = 또는), 카드에도 장르 태그 표시 | 사용자 피드백 — 콘텐츠 영역만 채우는 갤러리(카카오페이지 · 라프텔 참고), 여러 장르 동시 검색 |
| 2026-11-27 | PG03: '결과가 적을 때' 예시 삭제, 더 보기 → 무한 스크롤, 태그는 게임 수 많은 순 10개 + 더 보기 | 사용자 피드백 · ADR 0010 |
| 2026-11-27 | PG05 게임 상세 v3: 미리보기(대표 → 영상 → 이미지, 7개 이상 가로 넘김) + 오른쪽 정체 · 행동 패널, 아래 탭은 내용 전환(앵커 스크롤 아님), 자세한 정보는 소개 탭 '플레이 · 만든 정보' 두 묶음. 만든 사람 띠 · 하단 정보 칸 없앰 | 사용자 피드백 — 정보가 흩어지고 아래로 너무 쌓임 |
| 2026-11-27 | PG05 v4: 제목 아래 메이커 줄 삭제(소개 탭 메이커 카드로), 핵심 4칸에서 보조 글 삭제, 탭 줄의 작은 플레이 삭제(위 큰 버튼과 중복), 정보 칸 줄 간격 통일, 게임 신고 = 버튼, 리뷰 = 한 열 목록 + ⋯ 메뉴 신고 · 도움이 됐어요 토글 · 쓸 때 플레이 시간 · 쓴 버전 · 메이커 답글 상자 | 사용자 피드백. 근거: docs/product/game-metadata.md, docs/design/research/04-reviews.md |
| 2026-11-27 | 공통 카드: hover 를 transform → top(PG03 툴팁 안 뜨던 원인), 실행 칩 툴팁 · 플레이/다운로드 버튼 · 추천/리뷰 수를 모든 생성 카드에. 비슷한 게임 왼쪽 화살표 방향 고침. 리뷰 답글 = 왼쪽 선 상자 대신 들여쓴 이어진 답글(메이커 표시) | 사용자 피드백 3차 |
| 2026-11-27 | 주소: 한 앱, PlayGround `/play` · MakersGround `/makers`, `/` → `/play`(307) | 사용자 결정(1-1). workers.dev 하나에서 하위 도메인 불가, 로그인 · 헤더 공유 |
| 2026-11-27 | UI 컴포넌트 `apps/web/src/lib/ui` · 갤러리 Storybook(호환 안 되면 `/design`) · 데이터 `load` + form actions | 사용자 결정(1-2~1-4) |
| 2026-11-27 | 이름: 컴포넌트 PascalCase.svelte · 그 외 kebab-case.ts · camelCase · 타입 PascalCase · 상수 UPPER_SNAKE · is/has/can. 주석 · 테스트 이름 한국어. 스타일 = Tailwind 유틸리티 + 의미 토큰 + 자체 변형 헬퍼 | 사용자 결정(2-1 · 2-2 · 2-4) |
| 2026-11-27 | 컴포넌트 구조 = 가벼운 FSD + 패턴 층(primitives → patterns → entities → features → widgets → 라우트, 아래로만 import), 변형 규칙(docs/dev/component-architecture.md 5절), 헤드리스는 Bits UI 를 primitives 안에서만 | 사용자 결정(2-5). 도메인이 달라도 같은 뼈대를 patterns 에서 공유 |
| 2026-11-27 | Svelte 5 규칙 세트(runes · 콜백 props · snippet · $effect 최소 · .svelte.ts + context · interface Props), 한국어만(Intl), TS strict + noUncheckedIndexedAccess 등, ESLint strictTypeChecked | 사용자 결정(2-3 · 2-6 · 3-1 · 3-2) |
| 2026-11-27 | 구조 린트(층 방향 · 포트 경계 · 원시 색/임의 값 금지 · import 정렬), simple-git-hooks(포맷 · 린트 · 커밋 메시지), knip CI 실패, Worker 크기 70% 경고 · 90% 실패 | 사용자 결정(3-3~3-6). 크기 한도는 무료 플랜의 제약 — 최적화 후에도 넘으면 플랜 · 방안 검토를 사용자에게 |
| 2026-11-27 | 테스트: 단위 · 컴포넌트 · 캡처 비교 · E2E 핵심 · axe, 쓸모없는 테스트 금지, CI 는 변경 관련 테스트만. 순서: 도메인 테스트 먼저 · UI 이야기 먼저 · 버그 재현부터. 기준: 도메인 · 권한 분기 100%, UI 상태마다 이야기. 브랜치: design/redesign 을 PR 로 병합, 병합된 브랜치는 삭제 | 사용자 결정(4-1~4-3 · 5-1). 중요 도메인 규칙 · 기획은 사용자와 상의 |
| 2026-11-27 | 작업 = 이슈(중복 금지 · 같은 주제는 기존 이슈 갱신), PR = 페이지 단위 세로 조각(공통 컴포넌트 · 환경 변경은 별도), 피드백 끝나기 전 병합 금지, 완료 기준 ①~⑦, 버전은 v1.0.0 부터 · 묶음 단위 | 사용자 결정 · 위임(5-2~5-4 · 6-1) |
| 2026-11-27 | 변경 기록 v1.0 부터 release-please + 다듬기 · 환경 = 로컬 · PR 미리보기(별도 Worker + 별도 D1) · 운영 · main 병합 = 자동 배포 · 의존성 = Dependabot 보안 즉시 + 월 1회 묶음 + 메이저 제외 | 사용자 결정 · 위임(6-3~6-6) |
| 2026-11-27 | 브랜치: feat/… → develop → (내보내기 PR) → main(자동 배포), main 은 develop 에서만 PR. 도메인 규칙 lib/domain(순수 · 공용) + lib/server. 검증 Zod 4 서버 전용. 로그 Workers Logs 만 | 사용자 결정 · 위임. 결정 근거에 '사람이 편해서' 금지(사용자 원칙) |
| 2026-11-27 | 구조 경계는 ESLint 플러그인 대신 자체 스크립트 `scripts/check-boundaries.mjs`(층 · 같은 층 다른 묶음 · 어댑터 · 가짜 데이터 규칙) | eslint-plugin-boundaries 가 `#lib` 패키지 import 경로를 안정적으로 해석하지 못함. 자체 스크립트는 Claude 가 완전히 통제 · 시험 가능하고 의존성 0 |
| 2026-11-27 | Tailwind 제한은 **색**만: 원시 팔레트(`bg-jjok-500`) · 임의 색(`bg-[#…]`) 금지, 없는 클래스(`no-unknown-classes`)도 오류. 크기 · 배치의 임의 값(`grid-cols-[…]`)은 허용 | 다크 · 그라운드 전환을 깨는 건 색. 배치 임의 값까지 막으면 토큰에 없는 레이아웃마다 우회가 생김 |
| 2026-11-27 | CI 는 PR 에서만(`verify` 한 작업, 문서만 바뀌면 앱 검사 생략, 테스트는 `vitest --changed`, 의존성 바뀌면 전체). develop · main push 에선 다시 돌리지 않음 | 이미 PR 에서 검사한 커밋. 규칙 세트 필수 검사 이름 `verify` 를 항상 남기기 위해 작업을 나누지 않음 |
| 2026-11-27 | 디자인 토큰 원본을 `apps/web/src/lib/styles/tokens.css` 로 옮김(문서 쪽 사본 삭제, 캔버스 생성기도 이 파일을 읽음). Zod · 폰트는 처음 쓰는 곳(폼 · PG03)에서 추가 | 원본은 하나(ADR 0012). 안 쓰는 의존성은 knip 이 막음 |
| 2026-11-27 | hooks 는 SvelteKit `sequence` 대신 자체 `chain`(lib/server/handle.ts) | 개발 서버에서 sequence 가 'Could not get the request store' 오류 — 같은 계열 문제로 `redirect()` 도 개발 서버에서만 실패(운영 빌드 · wrangler dev 는 정상). 이슈로 추적 |
| 2026-11-27 | wrangler compatibility_date 2026-11-25 → 2026-11-20 | 설치된 workerd 가 11-24 까지만 지원해 wrangler dev 가 시작되지 않았음 |
| 2026-11-27 | 갤러리 = Storybook 10.6.7(@storybook/sveltekit · Svelte CSF · a11y · addon-vitest) — SvelteKit 3.4 · Vite 8 에서 개발 · 정적 빌드 · 이야기 테스트 모두 동작 확인. `/design` 대체안은 불필요 | 이야기 = Vitest 브라우저 테스트(렌더 · play · axe 위반이면 실패). 캡처 비교는 `.storybook/vitest.visual.ts` 가 이야기마다 라이트 · 다크 2장, 기준 그림은 리눅스(CI)만 저장소에 — `update-screenshots` 워크플로로 생성 |
| 2026-11-28 | 위 2026-11-27 `chain` 결정을 대체: 자체 `chain` 을 걷고 SvelteKit `sequence` 로 복귀. 개발 서버 SSR 사전 번들에서 `@sveltejs/kit` 제외 · drizzle-orm 미리 포함(vite.config `environments.ssr.optimizeDeps`) | #14 원인은 SSR 사전 번들이 kit 를 따로 복사한 것(앱 코드와 개발 서버 런타임의 kit 인스턴스 분리). 설정으로 해결돼 자체 구현을 둘 이유가 없음 |
| 2026-11-28 | Cloudflare 계정 하위 주소 = `vi-wolhwa`(사용자 결정) → 운영 `admd-games.vi-wolhwa.workers.dev`, Worker 이름은 그대로 | 하위 주소는 계정 전체 공용이라 프로젝트 이름(`admd-games`)보다 개인 이름이 다른 앱과 겹치지 않음. 아무것도 올리기 전이라 변경 비용 0. 한 단계 주소(`admd-games.workers.dev`)는 workers.dev 구조상 불가, `games` 는 이미 사용 중 |
| 2026-11-28 | 운영 배포는 출시할 만큼 갖춰졌을 때만(사용자 결정). 중간 결과는 develop 고정 주소 `admd-games-preview.vi-wolhwa.workers.dev` — develop 병합마다 갱신, PR 은 별칭 주소 | 미완성 화면을 운영에 올리지 않음. 확인용 Worker · D1 은 이미 있는 미리보기 것을 재사용해 추가 비용 · 자원 없음 |
| 2026-11-28 | PG03 정렬은 플랫폼이 아는 것만: 추천 많은(기본) · 새로 나온 · 짧은 순. '많이 하는'은 PG06 플레이 기록 뒤 추가하고 그때 기본값(사용자 결정) | ADR 0011 '플랫폼이 아는 것만 약속' — 기록 없이 '많이 하는'을 보이면 근거 없는 순서 |
| 2026-11-28 | 헤더 · 바닥글은 만든 페이지만 보인다(사용자 결정) — 지금은 로고 · 게임 · 테마 전환. 검색(PG04) · 로그인(SH01) · 홈 등은 그 페이지와 함께 | 누르면 막히는 링크 · 버튼을 두지 않음 |
| 2026-11-28 | 가짜 게임 그림 = 코드로 만든 추상 그림 `static/sample/`(사용자 결정), 생성기 `apps/web/scripts/sample-art.ts` | 저작권 · 다운로드 없음, 캡처 비교가 늘 같은 그림 |
| 2026-11-28 | 글꼴 자체 호스팅(사용자 결정): Pretendard(npm `pretendard`, 글자 범위별 조각). Gasoek One 은 처음 쓰는 페이지(PG01)에서 설치 | 외부 요청 없음(CSP · 개인정보), 안 쓰는 의존성은 knip 이 막음 |
| 2026-11-28 | PG03 주소 `/play/games`, 상세 `/play/games/<slug>`. `/play` 는 홈(PG01) 전까지 `/play/games` 로 307 | 홈은 마지막에 만든다(page-order.md) |
| 2026-11-28 | '신작' 배지 = 공개 후 14일 안쪽(`isNewGame`). 시안의 '왕좌'(랭킹 1위) 배지 · '광고 없이 무료' 문구는 근거(랭킹 · 정책 결정)가 생길 때까지 뺌 | 데이터 출처가 있는 표시만 |
| 2026-11-28 | 게임 목록 포트 `Catalog` 는 D1 어댑터 하나 + 계약 테스트를 로컬 D1(wrangler getPlatformProxy, 메모리)에서 돌린다. 메모리 어댑터는 만들지 않음, DB 바인딩이 없으면 오류로 드러냄 | 같은 필터 · 커서 로직을 두 번 구현하지 않음. 실제 이관 SQL 로 검증 |
| 2026-11-28 | 헤드리스 부품 Bits UI 2.x 도입 — `primitives/Select` · `primitives/Tooltip` 안에서만 | component-architecture 6절. PG03 화면 JS 는 gzip 43KB(대부분 Bits UI · floating-ui) |
| 2026-11-28 | 이야기 테스트 화면 = 'pc' 1440×1800(.storybook/preview.ts viewport 전역값) · 캡처 전 `document.fonts.ready` | addon-vitest 가 기본 1200×900 으로 고정해 페이지 이야기가 잘렸음, 글꼴 조각이 덜 받아진 채 찍히면 그림이 흔들림 |
| 2026-11-28 | 미리보기 D1 에 배포마다 가짜 데이터 시드(`scripts/seed.ts`, 운영 DB 는 거부) | 미리보기 · develop 주소에서 실제 화면 확인. 쓰기 약 230행/회 — 무료 10만 행/일 안 |
