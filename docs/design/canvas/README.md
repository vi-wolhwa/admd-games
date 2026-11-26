# 캔버스 페이지 목록 · 파일 이름 규칙

원본은 디자인 캔버스다(https://claude.ai/code/artifact/57ed3789-695b-4f2c-8ae6-b210fafc167d). 이 폴더는 캔버스 페이지의 **백업 스냅샷**이며 파일 이름이 캔버스와 같다. 편집은 캔버스에서 한다 — 절차와 함정은 [../canvas-notes.md](../canvas-notes.md).

## 이름 규칙 (2026-11-26)

```
파일:  PG05-game.dc.html      ← 영역 2글자 + 번호 2자리 + 영문 이름(소문자, 하이픈)
메뉴:  PG05 게임 상세          ← 캔버스 페이지 메뉴에 보이는 이름 (compat.json 의 name)
링크:  …/57ed3789-…#page-PG05-game
```

| 영역 | 뜻 | 번호 |
| --- | --- | --- |
| `DS` | 디자인 시스템 · 견본 | 01~ |
| `PG` | PlayGround (플레이어) | 01~ PC 화면, [pages.md](../pages.md) 순서 · **91~ 모바일 묶음** |
| `MG` | MakersGround (메이커) | 01~ PC 화면 · **91~ 모바일 묶음** |
| `SH` | 공통 (로그인 · 설정 · 알림 · 신고 · 고객센터) | 01~ |
| `AD` | 운영자 | 01~ |

- **찾는 법**: 대화·문서에서는 코드로 부른다("PG05 고쳐줘"). 메뉴와 파일 목록이 코드 순서로 정렬된다.
- **번호는 한 번 붙이면 바꾸지 않는다.** 새 페이지는 그 영역의 다음 번호, 없어진 번호는 비워 둔다.
- 출시 후(L2) 페이지는 메뉴 이름 끝에 `· L2`.
- 시안이 여러 안이면 `PG05a-…` · `PG05b-…`, 채택되면 접미사를 떼고 나머지는 보관한다.
- 영문 이름은 링크가 깨지지 않게 하려는 것(한글 파일 이름은 `#page-` 링크가 안 된다).

## 전체 목록

묶음 = [12-confirm-order.md](../12-confirm-order.md) 의 확정 순서. 생성기 = [`../tools/ds-canvas/`](../tools/ds-canvas/) 의 스크립트(손으로 만든 페이지는 —).

| 코드 | 파일 | 메뉴 이름 | pages.md | 묶음 | 생성기 | 옛 이름 |
| --- | --- | --- | --- | --- | --- | --- |
| DS01 | `DS01-foundations` | 기초 | — | 1 | `build.py` | 디자인 시스템 · 기초 |
| DS02 | `DS02-components` | 컴포넌트 | SH-NAV · SH-ERR | 1 | `build.py` | 디자인 시스템 · 컴포넌트 |
| DS03 | `DS03-components-2` | 컴포넌트 2 | — | 1 | `ds_comp2.py` | 디자인 시스템 · 컴포넌트 2 |
| DS04 | `DS04-game-cards` | 게임 카드 | — | 1 | — | 게임 카드 컴포넌트 |
| DS05 | `DS05-cat-face` | 고양이 얼굴 | — | 1 | — | aDmD 고양이 얼굴 |
| PG01 | `PG01-home` | 홈 | PG-HOME | 1 | — (확정본) | PlayGround v10 |
| PG02 | `PG02-issues` | 지난 PICK · 컬렉션 | PG-ISSUE · PG-COLL | 2 | `pages6.py` | 지난 PICK · 컬렉션 |
| PG03 | `PG03-catalog` | 전체 게임 | PG-CAT | 1 | `pages5.py` | 전체 게임 |
| PG04 | `PG04-search` | 검색 결과 | PG-SRCH | 2 | `pages3.py` | 검색 결과 |
| PG05 | `PG05-game` | 게임 상세 | PG-GAME | 1 | `detail.py` | 게임 상세 A |
| PG06 | `PG06-play` | 플레이 화면 | PG-PLAY | 1 | `play.py` | 플레이 화면 |
| PG07 | `PG07-play-end` | 플레이 종료 | PG-END | 1 | `play.py` | 플레이 종료 |
| PG08 | `PG08-download` | 다운로드 안내 | PG-DL | 2 | `pages2.py` | 다운로드 안내 |
| PG09 | `PG09-scan-report` | 보안 검사 리포트 | PG-SCAN | 2 | `pages2.py` | 보안 검사 리포트 |
| PG10 | `PG10-reviews` | 리뷰 전체 | PG-REVIEWS | 2 | `pages7.py` | 리뷰 전체 |
| PG11 | `PG11-ranking` | 랭킹 전체 · L2 | PG-RANK | L2 | `pages9.py` | 랭킹 전체 |
| PG12 | `PG12-room` | 같이 하기 대기실 · L2 | PG-ROOM | L2 | `pages9.py` | 같이 하기 대기실 |
| PG13 | `PG13-maker` | 메이커 페이지 | PG-MAKER | 2 | `pages4.py` | 메이커 페이지 |
| PG14 | `PG14-library` | 내 라이브러리 | PG-LIB | 1 | `pages2.py` | 내 라이브러리 |
| PG15 | `PG15-profile` | 공개 프로필 | PG-PROFILE | 2 | `pages5.py` | 공개 프로필 |
| PG16 | `PG16-friends` | 친구 · L2 | PG-FRIENDS | L2 | `pages9.py` | 친구 |
| PG91 | `PG91-mobile-home` | 모바일 · 홈 | PG-HOME (M) | 2 | `pg_mobile.py` | PlayGround 모바일 · 홈 |
| PG92 | `PG92-mobile-games` | 모바일 · 게임 (탐색 · 상세 · 라이브러리 · 플레이) | PG-CAT · GAME · LIB · PLAY (M) | 2 | `pg_mobile.py` | PlayGround 모바일 · 게임 |
| MG01 | `MG01-home` | 홈 | MG-HOME | 3 | `mg_c.py` | MakersGround 홈 C |
| MG02 | `MG02-start` | 처음 올리는 분 | MG-START | 3 | `pages6.py` | 처음 올리는 분 |
| MG03 | `MG03-new-maker` | 메이커 프로필 만들기 | MG-NEWMAKER | 3 | `pages7.py` | 메이커 프로필 만들기 |
| MG04 | `MG04-upload` | 업로드 마법사 | MG-UPLOAD | 3 | `pages3.py` | 업로드 마법사 |
| MG05 | `MG05-my-games` | 내 게임 | MG-GAMES | 3 | `pages7.py` | 내 게임 |
| MG06 | `MG06-game-manage` | 게임 관리 · 통계 | MG-GAME · MG-STATS | 3 | `pages4.py` | 게임 관리 · 통계 |
| MG07 | `MG07-feedback` | 리뷰 · 피드백함 | MG-FEEDBACK | 3 | `pages7.py` | 리뷰 · 피드백함 |
| MG08 | `MG08-community` | 커뮤니티 목록 | MG-LOG · QA · RECRUIT | 3 | `mg_c.py` | 커뮤니티 목록 |
| MG09 | `MG09-post` | 커뮤니티 글 보기 | MG-LOG | 3 | `mg_c.py` | 커뮤니티 글 보기 |
| MG10 | `MG10-write` | 글쓰기 · 개발일지 | MG-LOG | 3 | `pages6.py` | 글쓰기 · 개발일지 |
| MG11 | `MG11-jam` | 잼 상세 · L2 | MG-JAMS | L2 | `pages9.py` | 잼 · 상세 |
| MG12 | `MG12-jam-vote` | 잼 투표 · 결과 · L2 | MG-JAMS | L2 | `pages9.py` | 잼 · 투표 · 결과 |
| MG13 | `MG13-team` | 팀 관리 · L2 | MG-TEAM | L2 | `pages9.py` | 팀 관리 |
| MG91 | `MG91-mobile` | 모바일 | MG-HOME 외 (M) | 3 | `mg_c.py` | MakersGround 모바일 |
| SH01 | `SH01-login` | 로그인 · 내 얼굴 만들기 | SH-LOGIN · SH-ONBOARD | 1 | `pages3.py` | 로그인 · 내 얼굴 만들기 |
| SH02 | `SH02-settings` | 설정 | SH-SETTINGS | 2 | `pages5.py` | 설정 |
| SH03 | `SH03-notifications` | 알림 | SH-NOTI | 2 | `pages5.py` | 알림 |
| SH04 | `SH04-report` | 신고 | SH-REPORT | 2 | `pages7.py` | 신고 |
| SH05 | `SH05-help` | 고객센터 · 약관 | SH-HELP · SH-LEGAL | 4 | `pages7.py` | 고객센터 · 약관 |
| AD01 | `AD01-review-queue` | 심사 대기열 | AD-REVIEW | 3 | `pages4.py` | 심사 대기열 |
| AD02 | `AD02-reports` | 신고 처리 | AD-REPORTS | 4 | `pages8.py` | 운영 · 신고 처리 |
| AD03 | `AD03-curation` | 큐레이션 편집 | AD-CURATE | 4 | `pages8.py` | 운영 · 큐레이션 편집 |
| AD04 | `AD04-notice-users` | 공지 · 사용자 | AD-NOTICE · AD-USERS | 4 | `pages8.py` | 운영 · 공지 · 사용자 |

캔버스에는 이 46개 페이지와 런타임 파일(`support.js`, `fonts/`)만 있다. 지난 반복본 · 채택 안 된 시안 · Claude Design 원본은 [`../archive/`](../archive/) 에 있다.

`.dc.html` 은 캔버스 런타임이 있어야 그대로 렌더된다. 구현 단계에서는 이 마크업·CSS 를 SvelteKit 컴포넌트와 디자인 토큰으로 옮긴다.
