# 캔버스 확정본 스냅샷

원본은 디자인 캔버스다(https://claude.ai/code/artifact/57ed3789-695b-4f2c-8ae6-b210fafc167d). 이 폴더는 **확정된 페이지의 백업**이며, 편집은 캔버스에서 한다 — 절차와 함정은 [../canvas-notes.md](../canvas-notes.md).

| 파일 | 내용 | 확정 |
| --- | --- | --- |
| `PlayGround v10.dc.html` | PlayGround 홈 (PC) | 2026-11-26 사용자 확정 |
| `게임 카드 컴포넌트.dc.html` | 게임 카드 7종 · 상태 · 툴팁 | v10 과 같은 규칙 |
| `aDmD 고양이 얼굴.dc.html` | 고양이 DmD 표정 · 404 예시 | — |

`.dc.html` 은 캔버스 런타임(`support.js`, `fonts/`)이 있어야 그대로 렌더된다. 구현 단계에서는 이 마크업·CSS 를 SvelteKit 컴포넌트와 디자인 토큰으로 옮긴다.
