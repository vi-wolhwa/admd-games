# 디자인 캔버스 작업 노트

디자인 원본은 Claude 캔버스(Migrated Design 아티팩트)다: https://claude.ai/code/artifact/57ed3789-695b-4f2c-8ae6-b210fafc167d
저장소의 [`canvas/`](canvas/) 는 확정본 **백업 스냅샷**일 뿐이다. 사용자가 캔버스 편집기에서 직접 고칠 수 있으므로 **편집 전에는 항상 캔버스에서 최신본을 다시 읽는다.**

## 편집 절차 (Artifact 도구)

1. `action: read`, `url` = 위 주소, `paths` = `["project/compat.json", "project/<페이지>.dc.html"]` → 세션 스크래치 폴더의 `artifact-files/57ed…/project/` 에 저장된다.
2. 같은 폴더에서 파일을 고치거나 새 `.dc.html` 을 만든다(루트에 두면 페이지 메뉴에 나타남).
3. `action: publish`, `url` 동일, `root` = `…/artifact-files/57ed3789-695b-4f2c-8ae6-b210fafc167d`, `file_path` = 그 안의 `project/compat.json`, `files` = 바꾼 파일만 `{"project/X.dc.html": "project/X.dc.html"}`. 폰트(woff2)는 `{"from": …, "contentType": "font/woff2"}`.
4. **새 페이지는 [이름 규칙](canvas/README.md#이름-규칙-2026-11-26)을 따른다**(`PG17-xxx.dc.html`). `compat.json` 의 `pages` 끝에 `{"path", "title", "kind": "page", "name": "PG17 한글 이름"}` 을 넣어 함께 게시하고(메뉴 이름 · 순서), `report` 는 그대로 둔다. 같은 내용을 [`canvas/README.md`](canvas/README.md) 목록과 생성기 출력 이름에도 적는다.
5. 이름 바꾸기 = 새 이름 게시 + 옛 경로 `null` 을 한 호출에, `pages` · `entry` 도 함께. 삭제는 사용자 승인 후, 먼저 [`archive/`](archive/) 에 보관.

## 캔버스 페이지 목록

전체 목록 · 코드 · 생성기 · 옛 이름: **[`canvas/README.md`](canvas/README.md)**. 첫 화면(`entry`)은 `PG01-home`.

## 화면 확인

- 브라우저 패널에서 캔버스 주소를 열면 된다(claude.ai 로그인 필요 — 사용자가 이미 로그인함).
- 페이지는 해시로 바로 열린다: `…/57ed3789-…#page-PG05-game`(파일 이름에서 `.dc.html` 을 뺀 것). 메뉴에서는 코드 순서로 보인다.
- 게시 직후 화면이 새 버전으로 다시 그려지며 스크롤이 맨 위로 돌아갈 수 있다.
- 캔버스 Tweaks: `startSignedIn`(게스트/회원), `ground`(play/make 색 미리보기), 디자인 시스템 페이지는 `theme`(light/dark).
- **페이지 메뉴가 안 열리거나 브라우저 패널이 좁을 때 — 로컬 미리보기**: `.dc.html` 의 `<helmet>` 안쪽(head)과 `</helmet>…</x-dc>` 사이(body)를 꺼내 `{{ 값 }}` 을 채운 일반 HTML 로 만들고, 스크래치 폴더에서 `python -m http.server` 를 띄워(`.claude/launch.json` 에 임시 설정 → `preview_start`) 브라우저 패널로 본다. `file://` 는 스크린샷이 안 된다. 끝나면 임시 설정을 지운다.

## 공통 후처리

- 모든 생성 페이지는 `cat_face.py` 의 `catify()` 를 거친다(얼굴 = 고양이 실루엣). 손으로 만든 페이지(`PG01 홈`, `DS04 게임 카드`)에도 같은 함수를 한 번 적용했다 — 새로 손으로 만드는 페이지도 게시 전 적용.
- 테마 전환 버튼은 `onClick="{{ toggleTheme }}"` + `renderVals` 의 `this.state.theme`. 브라우저 패널에서는 캔버스 안 클릭이 잘 안 먹으니 로컬 미리보기로 확인하고, 실제 클릭은 사용자 확인.

## 겪은 함정 (다시 하지 말 것)

| 증상 | 원인 | 해결 |
| --- | --- | --- |
| 자모 얼굴 `ㅍㅅㅍ` 이 세로로 쌓임 | `.jf` 를 `inline-grid` 로 만들면 글자 노드가 행으로 나뉨 | `display:inline-flex; align-items:center` |
| 고양이 귀가 글자 위에 떠 있음 | 줄 높이 안의 빈 공간을 계산에 안 넣음 | 귀 SVG `top:-.21em; height:.46em` |
| 실행 칩 툴팁이 잘림 | 썸네일 `.art` 에 `overflow:hidden` | 안쪽 이미지 층 `.shots` 만 자르고 `.art` 는 `overflow:visible` |
| 툴팁이 빠른 플레이 버튼에 가려짐 | 칩과 버튼이 같은 z-index | `.plat:hover,.plat:focus-visible{z-index:8}`, 호버 카드 `z-index:6` |
| 범례 설명 글자가 검은 동그라미로 | `.legend li span` 이 모든 span 에 적용 | 자식 선택자 `.legend li > span` |
| 대체 아트 제목이 메이커 얼굴에 가림 | 패딩 부족 | `.fallback{padding-bottom:42px}` |
| **파일 전체의 "x" 가 다른 문자열로 바뀜** | 변환 스크립트에서 조건부 치환의 기본값을 `'x'` 로 두고 `str.replace` 실행 | 조건부 치환은 `if` 로 감싸고, 치환 후 원래 없어야 할 문자열 개수를 검사한다 |
| `<form onsubmit="return false">` | dc 형식에서 문자열 이벤트 속성은 동작하지 않음 | 폼 대신 `div role="search"`, 이벤트는 `onClick="{{ fn }}"` |
| Gasoek One 작은 글자가 안 읽힘 | 두꺼운 디스플레이 서체 | **28px 이상에서만** |
| 설명 칸의 로고·버튼·배지가 작게 · 회색으로 | `.imp span{font-size:12px}` 같은 자손 선택자가 안쪽 모든 span 에 적용 (범례 문제와 같은 원인) | **설명 글 선택자는 항상 자식 선택자 `>`** |
| 다크 안의 라이트 견본이 어두운 옅은 바탕으로 | `[data-theme='dark'] [data-ground]` 가 안쪽 라이트 섬의 그라운드 요소까지 덮음 | 테마별 `--dark` 0/1 + `color-mix` 로 경계마다 재계산(tokens.css) |
| 큰 자모 얼굴(`.jf.lg`)이 세로로 쌓임 | 컴포넌트 클래스 `.lg`(일지 카드, flex column)와 크기 클래스 이름 충돌 | **크기 클래스와 겹치는 짧은 이름(lg·md·sm) 을 컴포넌트에 쓰지 않는다** → `.logc` |
| 얼굴 글자가 사라지거나 위아래로 밀림 | `padding-top: 24%` 의 %는 **부모 폭** 기준 | 자기 크기에 비례하게 `em` 사용 |
| 아트 클래스(`.a-halcyon`)가 안 보임 | `.imp .stage{background}` 가 우선순위로 덮음 | 아트는 안쪽 별도 요소에 칠한다 |

## 형식 메모

- `.dc.html`: `<x-dc>` 안에 마크업, `<helmet>` 에 `<style>`·Google Fonts 링크, 마지막에 `<script type="text/x-dc" data-dc-script data-props='{…}'>class Component extends DCLogic { renderVals(){…} }</script>`.
- `{{ }}` 는 점 경로만(식 금지). 상태 전환은 `this.setState`. 조건부는 `<sc-if value="{{ x }}" hint-placeholder-val="{{ false }}">`.
- 웹폰트는 Google Fonts 만 로드됨. Pretendard 는 캔버스에 `project/fonts/PretendardVariable.woff2`(OFL) 로 올려 두었고 `@font-face{src:url('fonts/PretendardVariable.woff2')}` 로 쓴다.
- 게임 아트는 CSS 추상 플레이스홀더(`.a-loop`, `.a-ash` …). 실제 타사 IP·AI 일러스트 쓰지 않음.
- 형식 전체 규칙: 캔버스의 `artifact-type/reference/format.md`.
