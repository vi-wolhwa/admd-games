# 0005. 저장소 · 모노레포 · 브랜치 · 커밋 규칙

- 상태: 승인 (2026-11-26) · **일부 대체: 저장소 공개 · 브랜치 모델 · 배포는 [0013](0013-branches-deploy-public-repo.md)** — 저장소 소유자·이름·공개 여부·라이선스는 사용자 결정, 나머지는 B등급 추천안
- 등급: A(저장소) + B(도구·규칙)

## 결정

| 항목 | 결정 | 등급 |
| --- | --- | --- |
| 저장소 | `vi-wolhwa/admd-games`, **비공개**, **라이선스 없음**(All rights reserved) | A — 사용자 |
| 이전 자료 | GitHub 조직 `aDmD-Ground` 의 저장소·문서는 사용하지 않음. 디자인 캔버스와 8월 문서는 참고만 ([references.md](../references.md)) | A — 사용자 |
| 모노레포 | npm 워크스페이스 (`apps/*`, `packages/*`) | B |
| 패키지 매니저 | npm 11 (Node 24 기본 포함 → 추가 설치 없음) | B |
| 런타임 | Node 24 (`.nvmrc`, `engines`, `engine-strict`) | B |
| 공급망 보호 | `min-release-age=7`, 설치 스크립트는 `allowScripts` 로 명시 허용 | B |
| 린트·포맷 | ESLint(flat) + Prettier(탭, 작은따옴표, 100자) | B |
| 테스트 | Vitest (server/client 프로젝트), E2E 는 필요 시 Playwright 추가 | B |
| 브랜치 | GitHub Flow + `wip/*` 브랜치로 기기 간 인계 | B |
| 커밋 | Conventional Commits, 타입 영어 · 설명 한국어 | B |
| CI | GitHub Actions: lint → check → test → build (비공개 저장소 무료 2,000분/월) | B |

## 결과

- 비공개 무료 저장소는 브랜치 보호 규칙을 쓸 수 없어 "main 직접 푸시 금지"는 관례로 지킨다. 최초 부트스트랩 커밋만 main 에 직접 올렸다.
- `npm audit` 의 moderate 4건은 drizzle-kit(개발 전용)이 쓰는 구버전 esbuild 개발 서버 취약점으로, 우리는 그 개발 서버를 실행하지 않아 영향이 없다. drizzle-kit 업데이트 시 재확인.
