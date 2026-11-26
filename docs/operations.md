# 운영 · 배포

결정: ADR 0001(Workers 무료) · 0013(브랜치 · 자동 배포) · setup-agenda 6-4 · 6-5.

## 흐름

```
feat/… ─PR─▶ develop ─'내보내기' PR─▶ main ──(자동)──▶ 운영
  │            (PR 마다 미리보기 주소)          출처 확인 → D1 이관 → 배포 → 점검 → 실패 시 되돌리기
```

| 워크플로 | 언제 | 하는 일 |
| --- | --- | --- |
| `ci.yml` | 모든 PR | `verify`(필수 검사) — 바뀐 것 관련만 |
| `main-source.yml` | main 으로의 PR | develop 에서 온 PR 인지(필수 검사) |
| `preview.yml` | develop 으로의 PR(앱 코드 바뀜) | 별도 Worker `admd-games-preview` + 별도 D1 로 `pr-<번호>` 미리보기, 주소를 PR 댓글에 |
| `deploy.yml` | main 에 커밋이 들어옴 | develop → main PR 병합인지 확인(아니면 거부 + 이슈) → 운영 D1 이관 → `wrangler deploy` → `/api/health` · `/play` 점검 → 실패 시 `wrangler rollback` + 이슈 |
| `update-screenshots.yml` | 수동 | 화면 캡처 기준 그림(리눅스) 갱신 커밋 |
| `cloudflare-bootstrap.yml` | 수동, 한 번 | 운영 · 미리보기 D1 만들고 ID 표시 |

Cloudflare 시크릿이나 D1 ID 가 없으면 미리보기 · 배포는 **건너뛴다**(실패하지 않음).

## 처음 한 번 — 완료(2026-11-28)

| 항목 | 값 · 방법 |
| --- | --- |
| 주소 | 운영 `https://admd-games.vi-wolhwa.workers.dev` · 미리보기 `https://pr-<번호>-admd-games-preview.vi-wolhwa.workers.dev` |
| 계정 하위 주소 | `vi-wolhwa.workers.dev` — 계정 전체 공용(이 계정의 다른 앱도 `<이름>.vi-wolhwa.workers.dev`). 바꾸면 모든 앱 주소가 끊김 |
| API 토큰 | 이름 `admd-games GitHub Actions`. "Cloudflare Workers 편집" 템플릿 + 계정 정책에 **D1 편집** 추가, 영역(Zone) 정책은 제거(도메인 없음). 만료 없음 |
| GitHub 시크릿 | `CLOUDFLARE_API_TOKEN`(사용자가 붙여 넣음) · `CLOUDFLARE_ACCOUNT_ID` |
| D1 | `cloudflare-bootstrap` 으로 생성, ID 는 `apps/web/wrangler.jsonc` |
| 미리보기 Worker | 처음 PR 에서 `wrangler deploy --env preview` 로 자동 생성(없을 때만), 이후 PR 은 버전 + 별칭만 올림 |

토큰을 다시 만들 때도 위 권한 그대로. 시크릿 값은 저장소 · 대화 어디에도 남기지 않는다.

## DB 이관 규칙

- 배포 순서가 **이관 → 코드**라서, 이관 직후 잠깐은 **이전 코드가 새 스키마로** 돈다. 그래서 이관은 **더하기만**(열 · 테이블 추가, 기본값 있는 열) 하고, 지우기 · 이름 바꾸기는 두 번에 나눈다(① 새 것 추가 + 코드가 둘 다 읽게 → ② 다음 배포에서 옛 것 제거).
- 코드 되돌리기(`wrangler rollback`)는 DB 를 되돌리지 않는다. DB 를 되돌려야 하면 D1 Time Travel(30일, 무료)로 — 사용자 승인 후.

## 무료 한도에 닿으면

먼저 우리 쪽 비효율(무거운 의존성 · 풀 스캔 · 불필요한 요청)을 고친다. 최적화를 다 했는데도 넘으면 무료 플랜의 한계이므로 다른 플랜 · 방안 검토를 사용자에게 올린다(setup-agenda 3-6).
