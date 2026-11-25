# STATUS

- 마지막 업데이트: 2026-11-26 (Asia/Seoul)
- 현재 Phase: **2. 디자인** — PlayGround 홈 확정 · 디자인 시스템 정의 완료 · 주요 페이지 시안 1차 완료 → **사용자 검토 대기** (PRD 는 디자인과 병행 — 킥오프·시나리오 완료, 확정은 디자인 후)
- 작업 브랜치: `design/redesign` (main 에는 개발 환경 셋업만 있음. 디자인 단계가 끝나면 PR 로 합칠 예정 — 아직 PR 없음)
- 디자인 캔버스(원본): https://claude.ai/code/artifact/57ed3789-695b-4f2c-8ae6-b210fafc167d
  - 편집 절차·함정: [`docs/design/canvas-notes.md`](design/canvas-notes.md) — **캔버스 작업 전 반드시 읽기**
  - 스냅샷: [`docs/design/canvas/`](design/canvas/) · 시안 생성기: [`docs/design/tools/ds-canvas/`](design/tools/ds-canvas/)
- **사용자 돌아오면 먼저 볼 것: [`docs/design/feedback-queue.md`](design/feedback-queue.md)** (결정 D1~D4 · 시안 선택 M1~M4 · P1~P6 · S1~S3 · K1~K3 · 피드백 F1~F4)

## 완료

- 개발 환경 셋업(Phase 4 선행): SvelteKit 3 + Cloudflare Workers/D1, ADR 0001~0005, CI
- 킥오프 인터뷰 → `docs/product/kickoff.md` · 시나리오 23개·요구사항 → `docs/product/scenarios.md` · 페이지 44개 → `docs/design/pages.md`
- 디자인 리서치 3종 → `docs/design/research/` (플랫폼·트렌드 / 원칙·AI 티 / 게임 카드)
- 콘셉트: 기존 Ground 콘셉트 계승·발전 → `docs/design/02-concept-ground.md`
- **PlayGround 홈 확정 = 캔버스 `PlayGround v10`** (2026-11-26)
- 게임 카드 7종 → `docs/design/03-game-cards.md` · 브랜드 고양이 DmD → 캔버스 `aDmD 고양이 얼굴`
- **디자인 시스템** → `docs/design/system/` (tokens.css — Tailwind 4, 라이트·다크, play·make / 기초 · 브랜드 · 컴포넌트 · 패턴), 캔버스 `디자인 시스템 · 기초` · `컴포넌트`
- 사용자 부재 중 자율 진행한 **시안 (모두 검토 대기)**:
  - MakersGround 홈 A(작업 먼저) · B(일지 먼저) · 모바일 → `docs/design/04-makersground-home.md`
  - 게임 상세 A(결정 패널, 상태 5종) · B(무대) · 플레이 화면(4상태) · 플레이 종료 · 다운로드 안내 · 보안 검사 리포트 · 내 라이브러리 → `docs/design/05-playground-pages.md`
  - 로그인 · 내 얼굴 만들기 · 업로드 마법사 · 검색 결과 · 메이커 페이지 · 게임 관리·통계 · 심사 대기열 → `docs/design/06-more-pages.md`
- 조사: 무료 보안 검사·설치 파일 저장소(D4) → `docs/product/research-scan-storage.md`

## 확정된 디자인 결정 (요약 — 근거는 02·03·system 문서)

- PC 는 사이드바 없는 한 열(1200px), 헤더 한 줄, 배너 캐러셀(수동), 가로 레일, 탭 랭킹, 촘촘한 카드 그리드(홈 전체 게임 4열). 흰 바탕 + 여백 구분, 상자 위젯·옛 포털 장치 금지. 모바일 PlayGround 는 나중에 별도 디자인.
- 색: 흑연 무채색 UI + 그라운드 강조색 — **쪽빛 `#046DCE`(Play) / 인주 `#D22C02`(Make)**, 비취(통과), 다홍(오류·상승). Tailwind 기본 팔레트 제거. 강조색은 각인 장치에만.
- 글자: Pretendard(본문·UI) + Gasoek One(28px 이상만).
- 브랜드 얼굴: **고양이 DmD**(D 회전 표정, 가끔 눈 굴림) · 사람 얼굴: **자모 얼굴**(같은 휘도 12색).
- 카드: 아트 16:9 하나, 아트 위 자리 고정, **카드 배경색 없음**, 허영 지표 금지(메이커 본인 통계는 예외).
- 문구: 자연스러운 한국어, "누가 골랐다" 금지, 번역투·이모지 금지.

## 다음 할 일

1. **사용자 검토** — `feedback-queue.md` 순서대로 결정·피드백 → 시안 확정본을 고르고 문서·캔버스에 반영.
2. 확정된 시안에서 나온 새 컴포넌트(StatusChip · StageSteps · TodoRow · MakerGameRow · LogCard · QuestionRow · MobileTabBar · LibraryRow 등)를 `docs/design/system/03-components.md` 에 정식 추가.
3. 남은 페이지 시안: 카탈로그(게임 적을 때 레이아웃) · 알림 · 설정 · 컬렉션/지난 PICK · 개발일지 글/쓰기 · 잼 · 모바일 PlayGround(별도) → 이후 개발 환경 마무리(컨벤션·브랜치 전략) · PRD 확정 · 이슈/마일스톤.

## 열린 질문 (A등급 — `feedback-queue.md` §1)

- D1 다크 모드 기본값 · D2 호버 영상 · D3 친구 활동 공개 기본값 · **D4 보안 검사·저장소(R2 결제수단 등록 여부 포함)** · 자모 얼굴 다양성(후속)

## 블로커

- 없음 (시안 확정은 사용자 검토 후)
