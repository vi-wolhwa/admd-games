# 개발 환경 세팅 실행 계획 (2026-11-27)

결정은 [setup-agenda.md](setup-agenda.md) · ADR 0012 · 0013. 단계마다 GitHub 이슈 하나 + PR 하나(→ `develop`). 각 PR 은 사용자 확인 후 병합하고 브랜치는 지운다.

| 단계 | 내용 | 사용자 손이 필요한 것 |
| --- | --- | --- |
| **0. 저장소 정리 · 공개** | ① `design/redesign` 이력에서 `docs/design/archive/canvas/uploads` 제거 → 강제 푸시(승인됨) ② 저장소 공개 전환 ③ `main` 에서 `develop` 생성 ④ `design/redesign` → `develop` PR(디자인 문서 · 결정 기록 전부) → 확인 후 병합 · 브랜치 삭제 | ④ 병합 확인 |
| **1. 저장소 규칙** | 규칙 세트(main: PR 필수 · 'develop 출처' 검사 · 강제 푸시/삭제 금지 / develop: PR 필수 · CI 필수), 병합 후 브랜치 자동 삭제 설정, PR · 이슈 템플릿, 라벨 · 마일스톤, Dependabot(보안 즉시 · 월 1회 묶음 · 메이저 제외) | 설정 변경 확인 |
| **2. 코드 품질 장치** | TS 엄격 옵션, ESLint strictTypeChecked + 층 방향 · 포트 경계 · 토큰 전용 클래스 · import 정렬, simple-git-hooks(포맷 · 린트 · 커밋 메시지 · main/develop 직접 푸시 차단), knip, Worker 크기 검사, **CI 재설계**(바뀐 것 관련 테스트만: `vitest --changed` · 경로 분기 · 의존성 PR 은 전체) | — |
| **3. 앱 뼈대** | 폴더 구조(`lib/ui` 5층 · `lib/domain` · `lib/server` · `lib/fixtures`), 라우트 `/play` · `/makers` · `/`→`/play`(307), 디자인 토큰을 앱으로(`tokens.css`), 보안 헤더 · CSP, Zod 환경 변수 검증, 구조화 로그 도우미 | — |
| **4. 갤러리** | Storybook 설치(SvelteKit 3 · Vite 8 호환 확인 → 안 되면 `/design`), 이야기 = Vitest 테스트(브라우저) · 접근성(axe) · 화면 캡처 비교(라이트/다크), `npm run design:publish` → 비공개 아티팩트 게시 | — |
| **5. 배포 파이프라인** | 미리보기용 별도 Worker + D1(가짜 데이터 시드) · PR 미리보기 배포(앱 코드 바뀔 때만) · `main` 자동 배포(출처 확인 → DB 이관 → 배포 → 점검 → 실패 시 되돌리기) | **Cloudflare 계정 · API 토큰을 GitHub 시크릿에 직접 넣기**(넣기 전엔 이 작업들은 건너뛰도록 만듦) |
| **6. 문서** | CLAUDE.md(새 규칙 요약) · architecture.md · STATUS 갱신 | — |
| → **페이지 1: PG03 전체 게임** | [page-order.md](page-order.md) | 페이지 확정 |

예상 PR 수: 0④ · 1 · 2 · 3 · 4 · 5 · 6 = 7개(6은 다른 단계와 합칠 수 있음).
