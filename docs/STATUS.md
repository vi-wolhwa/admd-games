# STATUS

- 마지막 업데이트: 2026-11-26 (Asia/Seoul)
- 현재 Phase: **4. 저장소·개발 환경** 완료 → 다음은 **1. 기획(PRD)**

## 완료

- 기술 스택 결정과 ADR 0001~0005 (Cloudflare Workers · SvelteKit 3 · D1+Drizzle(포트/어댑터) · better-auth · 저장소 규칙)
- 모노레포 스캐폴드(`apps/web`), 로컬 D1 에뮬레이션, `/api/health` 로 포트→어댑터→D1 연결 확인
- `npm run verify`(lint·check·test·build) 통과, GitHub Actions CI, PR·이슈 템플릿
- 연속성 문서: CLAUDE.md, STATUS.md, docs/decisions/

## 진행 중

- 없음

## 다음 할 일

1. **Phase 0~1 킥오프 인터뷰 → `docs/PRD.md`**: 문제 정의, 타깃, MVP 기능(PlayGround), 성공 기준, 하지 않을 것
2. PRD 기반 GitHub Milestone/Issue 등록
3. **Phase 2 디자인**: 사용자 플로우 → IA → 시각 방향 시안 2~3개 → 디자인 토큰·컴포넌트 목록(`docs/design/`)

## 열린 질문

- MVP 에 넣을 첫 게임(직접 만들 게임 1~2개)은 무엇인가?
- 게임 실행 방식(별도 출처 iframe) 세부 — 게임 SDK 마일스톤에서 ADR

## 블로커

- 없음 (배포 단계에서 Cloudflare 무료 계정·API 토큰이 필요 — 사용자 작업)
