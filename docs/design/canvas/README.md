# 캔버스 확정본 스냅샷

원본은 디자인 캔버스다(https://claude.ai/code/artifact/57ed3789-695b-4f2c-8ae6-b210fafc167d). 이 폴더는 **확정된 페이지의 백업**이며, 편집은 캔버스에서 한다 — 절차와 함정은 [../canvas-notes.md](../canvas-notes.md).

| 파일 | 내용 | 확정 |
| --- | --- | --- |
| `PlayGround v10.dc.html` | PlayGround 홈 (PC) | 2026-11-26 사용자 확정 |
| `게임 카드 컴포넌트.dc.html` | 게임 카드 7종 · 상태 · 툴팁 | v10 과 같은 규칙 |
| `aDmD 고양이 얼굴.dc.html` | 고양이 DmD 표정 · 404 예시 | — |
| `디자인 시스템 · 기초.dc.html` | 색·글자·간격·반경·그림자·모션·자모 얼굴·그라운드 각인 (Tweaks: theme·ground) | 생성물 — [`../tools/ds-canvas/`](../tools/ds-canvas/) 에서 `python build.py` |
| `MakersGround 홈 A.dc.html` · `홈 B` · `모바일` | MakersGround 홈 시안(검토 대기) | 생성물 — `mg.py`, `mg_mobile.py` |
| `게임 상세 A/B` · `플레이 화면` · `플레이 종료` · `다운로드 안내` · `보안 검사 리포트` · `내 라이브러리` | PlayGround 페이지 시안(검토 대기) | 생성물 — `detail.py`, `play.py`, `pages2.py` |
| `로그인 · 내 얼굴 만들기` · `업로드 마법사` · `검색 결과` | 추가 시안(검토 대기) | 생성물 — `pages3.py` |
| `메이커 페이지` · `게임 관리 · 통계` · `심사 대기열` | 추가 시안(검토 대기) | 생성물 — `pages4.py` |
| `MakersGround 홈 C` · `커뮤니티 목록` · `커뮤니티 글 보기` · `MakersGround 모바일`(개정) | 커뮤니티 중심 개정 | 생성물 — `mg_c.py` |
| `전체 게임` · `공개 프로필` · `알림` · `설정` · `처음 올리는 분` · `글쓰기 · 개발일지` · `지난 PICK · 컬렉션` | 추가 시안 2 | 생성물 — `pages5.py`, `pages6.py` |
| `디자인 시스템 · 컴포넌트.dc.html` | 헤더·버튼·칩/탭·아트 위 요소·툴팁·띠·입력·메뉴/대화상자/토스트·상태 화면·푸터 | 같음 |

`.dc.html` 은 캔버스 런타임(`support.js`, `fonts/`)이 있어야 그대로 렌더된다. 구현 단계에서는 이 마크업·CSS 를 SvelteKit 컴포넌트와 디자인 토큰으로 옮긴다.
