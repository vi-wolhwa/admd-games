# STATUS

- 마지막 업데이트: 2026-11-28 (Asia/Seoul) — PG05 게임 상세 확정 · 병합(#26)
- 현재 Phase: **4. 페이지 구현** — 디자인 원본은 코드(ADR 0012). 완료: **PG03 전체 게임**(#23) · **PG05 게임 상세**(#26) · 다음: **SH01 로그인 · 내 얼굴 만들기**([docs/dev/page-order.md](dev/page-order.md))
- 저장소: **공개** `vi-wolhwa/admd-games`, 기본 브랜치 `develop`, 운영 = `main` 병합 시 자동 배포(ADR 0013, [operations.md](operations.md))
- 개발 환경 결정: [docs/dev/setup-agenda.md](dev/setup-agenda.md) · 실행 계획: [setup-plan.md](dev/setup-plan.md) · 컴포넌트 구조: [component-architecture.md](dev/component-architecture.md)
- 디자인 캔버스(아직 코드로 옮기지 않은 페이지의 기획 시안): https://claude.ai/code/artifact/57ed3789-695b-4f2c-8ae6-b210fafc167d — 페이지 목록 [docs/design/canvas/README.md](design/canvas/README.md)

## 개발 환경 (2026-11-27)

| 단계 | 상태 |
| --- | --- |
| 0 저장소 정리 · 공개 · develop | 완료 (#1 · #8) |
| 1 저장소 규칙(템플릿 · 규칙 세트 · Dependabot · 보안) | 완료 (#2 · #9) |
| 2 품질 장치 · 바뀐 것만 도는 CI | 완료 (#3 · #12) |
| 3 앱 뼈대(/play · /makers · 토큰 · 테마 · 보안 헤더 · 로그) | 완료 (#4 · #15) |
| 4 갤러리(Storybook · 이야기 테스트 · 접근성 · 캡처 비교) | 완료 (#5 · #17) |
| 5 배포 파이프라인(미리보기 · 운영 자동 배포 · 되돌리기) | 완료 — 시크릿 · D1 · 미리보기 확인(#20), develop 고정 주소. 운영 첫 배포는 출시 때 (#6) |
| 6 문서(CLAUDE.md · operations · STATUS) | 완료 (#7) |
| 버그: 개발 서버에서 redirect · sequence 실패 | 해결 (#16) |

## 완료

- 개발 환경 셋업(Phase 4 선행): SvelteKit 3 + Cloudflare Workers/D1, ADR 0001~0005, CI
- 킥오프 인터뷰 → `docs/product/kickoff.md` · 시나리오 23개·요구사항 → `docs/product/scenarios.md` · 페이지 44개 → `docs/design/pages.md`
- 디자인 리서치 3종 → `docs/design/research/` (플랫폼·트렌드 / 원칙·AI 티 / 게임 카드)
- 콘셉트: 기존 Ground 콘셉트 계승·발전 → `docs/design/02-concept-ground.md`
- **PlayGround 홈 확정 = 캔버스 `PG01 홈`** (2026-11-26)
- 게임 카드 7종 → `docs/design/03-game-cards.md` · 브랜드 고양이 DmD → 캔버스 `DS05 고양이 얼굴`
- **디자인 시스템** → `docs/design/system/` (tokens.css — Tailwind 4, 라이트·다크, play·make / 기초 · 브랜드 · 컴포넌트 · 패턴), 캔버스 `DS01 기초` · `DS02 컴포넌트` · `DS03 컴포넌트 2`
- 사용자 부재 중 자율 진행한 **시안 (모두 검토 대기)**:
  - MakersGround 홈 A(작업 먼저) · B(일지 먼저) · 모바일 → `docs/design/04-makersground-home.md`
  - 게임 상세 A(결정 패널, 상태 5종) · B(무대) · 플레이 화면(4상태) · 플레이 종료 · 다운로드 안내 · 보안 검사 리포트 · 내 라이브러리 → `docs/design/05-playground-pages.md`
  - 로그인 · 내 얼굴 만들기 · 업로드 마법사 · 검색 결과 · 메이커 페이지 · 게임 관리·통계 · 심사 대기열 → `docs/design/06-more-pages.md`
- 조사: 무료 보안 검사·설치 파일 저장소(D4) → `docs/product/research-scan-storage.md`

## 확정된 디자인 결정 (요약 — 근거는 02·03·system 문서)

- PC 는 사이드바 없는 한 열(1200px), 헤더 한 줄, 배너 캐러셀(수동), 가로 레일, 탭 랭킹, 촘촘한 카드 그리드(홈 전체 게임 4열). 흰 바탕 + 여백 구분, 상자 위젯·옛 포털 장치 금지. 모바일 PlayGround 는 나중에 별도 디자인.
- 색: 흑연 무채색 UI + 그라운드 강조색 — **쪽빛 `#046DCE`(Play) / 인주 `#D22C02`(Make)**, 비취(통과), 다홍(오류·상승). Tailwind 기본 팔레트 제거. 강조색은 각인 장치에만.
- 글자: Pretendard(본문·UI) + Gasoek One(28px 이상만).
- 브랜드 얼굴: **고양이 DmD**(D 회전 표정, 가끔 눈 굴림) · 사람 얼굴: **고양이 얼굴**(실루엣 + 눈 · 입 글자, 같은 휘도 12색 — `CatFace`, 2026-11-28 코드 반영).
- 카드: 아트 16:9 하나, 아트 위 자리 고정, **카드 배경색 없음**, 허영 지표 금지(메이커 본인 통계는 예외).
- 문구: 자연스러운 한국어, "누가 골랐다" 금지, 번역투·이모지 금지.

## 다음 할 일

1. **SH01 로그인 · 내 얼굴 만들기** — better-auth(게스트 → OAuth), 고양이 얼굴 만들기. PG05 에서 미뤄 둔 것을 여기서 켠다:
   추천 · 리뷰/답글/신고 저장, `me`(답글 쓰기 얼굴) · `mine`(버전당 내 리뷰), 답글 1분 제한 서버 검사
2. 이후 page-order.md 순서: PG06 → PG07 → PG14 → PG01. PG15(플레이어 프로필)는 리뷰 프로필 카드에서 잇는다
3. 정리: 안 쓰는 `helpful_count` 열 · `review_replies` 표 지우기(별도 마이그레이션)
- 운영 첫 배포는 출시할 만큼 갖춰졌을 때(사용자 승인). 그 전까지 중간 결과는 develop 고정 주소 https://admd-games-preview.vi-wolhwa.workers.dev

## 열린 질문 (A등급 — `feedback-queue.md` §1)

- D1~D4 결정 완료(2026-11-26) → ADR 0006 · 0007 · 0008. 결정 대기 질문 없음(D · M · P · S · K · F 모두 결정). 남은 것 · 디자인 피드백(F) · 자모 얼굴 다양성(후속)
- 프로필 얼굴 = 고양이 얼굴 실루엣(S2) · 심사 48시간(K3) · 헤더 테마 전환 버튼(라이트로 시작)
- 다크 모드: MVP 포함으로 개정(ADR 0008) — 모든 시안을 라이트·다크로 검증
- R2 활성화 때 결제수단 등록이 필요하면 **사용자가 직접** (구현 단계)

## 블로커

- 없음 (시안 확정은 사용자 검토 후)
