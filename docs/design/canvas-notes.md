# 디자인 캔버스 작업 노트

디자인 원본은 Claude 캔버스(Migrated Design 아티팩트)다: https://claude.ai/code/artifact/57ed3789-695b-4f2c-8ae6-b210fafc167d
저장소의 [`canvas/`](canvas/) 는 확정본 **백업 스냅샷**일 뿐이다. 사용자가 캔버스 편집기에서 직접 고칠 수 있으므로 **편집 전에는 항상 캔버스에서 최신본을 다시 읽는다.**

## 편집 절차 (Artifact 도구)

1. `action: read`, `url` = 위 주소, `paths` = `["project/compat.json", "project/<페이지>.dc.html"]` → 세션 스크래치 폴더의 `artifact-files/57ed…/project/` 에 저장된다.
2. 같은 폴더에서 파일을 고치거나 새 `.dc.html` 을 만든다(루트에 두면 페이지 메뉴에 나타남).
3. `action: publish`, `url` 동일, `root` = `…/artifact-files/57ed3789-695b-4f2c-8ae6-b210fafc167d`, `file_path` = 그 안의 `project/compat.json`, `files` = 바꾼 파일만 `{"project/X.dc.html": "project/X.dc.html"}`. 폰트(woff2)는 `{"from": …, "contentType": "font/woff2"}`.
4. `compat.json` 의 `pages` 는 건드리지 않는다. 기존 페이지(v2 등)는 지우지 않는다(삭제는 사용자 승인 필요).

## 캔버스 페이지 목록 (2026-11-26)

| 페이지 | 상태 |
| --- | --- |
| `PlayGround v10` | **확정된 PlayGround 홈** |
| `게임 카드 컴포넌트` | 카드 7종 · 상태 · 해부도 · 툴팁 (v10 과 같은 규칙) |
| `aDmD 고양이 얼굴` | 고양이 DmD 표정 5종 · 그라운드 색 · 404 예시 |
| `PlayGround v3 ~ v9` | 반복 이력 (참고용) |
| `콘셉트 A 판` · `B 놀이터` · `C 크레딧` | 채택하지 않은 시안 |
| `PlayGround v2` · `MakersGround v2` · `components/` · `docs/` | 사용자 원본 (Claude Design 에서 이관) |

## 화면 확인

- 브라우저 패널에서 캔버스 주소를 열면 된다(claude.ai 로그인 필요 — 사용자가 이미 로그인함).
- `#page-PlayGround-v10` 처럼 **영문 페이지 이름은 해시로 바로 열린다.** 한글 이름 페이지(`게임 카드 컴포넌트` 등)는 해시가 안 먹으니 상단 왼쪽 페이지 메뉴(클릭 → 목록)에서 고른다.
- 게시 직후 화면이 새 버전으로 다시 그려지며 스크롤이 맨 위로 돌아갈 수 있다.
- 캔버스 Tweaks: `startSignedIn`(게스트/회원), `ground`(play/make 색 미리보기).

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

## 형식 메모

- `.dc.html`: `<x-dc>` 안에 마크업, `<helmet>` 에 `<style>`·Google Fonts 링크, 마지막에 `<script type="text/x-dc" data-dc-script data-props='{…}'>class Component extends DCLogic { renderVals(){…} }</script>`.
- `{{ }}` 는 점 경로만(식 금지). 상태 전환은 `this.setState`. 조건부는 `<sc-if value="{{ x }}" hint-placeholder-val="{{ false }}">`.
- 웹폰트는 Google Fonts 만 로드됨. Pretendard 는 캔버스에 `project/fonts/PretendardVariable.woff2`(OFL) 로 올려 두었고 `@font-face{src:url('fonts/PretendardVariable.woff2')}` 로 쓴다.
- 게임 아트는 CSS 추상 플레이스홀더(`.a-loop`, `.a-ash` …). 실제 타사 IP·AI 일러스트 쓰지 않음.
- 형식 전체 규칙: 캔버스의 `artifact-type/reference/format.md`.
