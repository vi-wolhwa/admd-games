# aDmD 디자인 시스템

**하나의 시스템, 두 그라운드.** 흑연 무채색 화면 위에 그라운드 색(쪽빛 Play / 인주 Make)을 정해진 각인 장치에만 쓰고, 표정은 고양이 DmD 와 자모 얼굴이 맡는다. 기준 화면: 캔버스 `PG01 홈`(2026-11-26 확정).

| 문서 | 내용 |
| --- | --- |
| [`tokens.css`](../../../apps/web/src/lib/styles/tokens.css) | **값의 원본**(앱 안 `apps/web/src/lib/styles/` — 코드가 원본, ADR 0012). Tailwind 4 `@theme` — 원시 → 의미 → 컴포넌트 3층, 라이트·다크, play·make |
| [`01-foundations.md`](01-foundations.md) | 색 · 글자 · 간격 · 반경 · 그림자 · 모션 · 아이콘 · 화면 폭, v10 대비 정리 |
| [`02-brand.md`](02-brand.md) | 고양이 DmD 표정 · 자모 얼굴 · 그라운드 색 각인 · 게임색 필드 |
| [`03-components.md`](03-components.md) | 헤더 · 버튼 · 칩/탭 · 아트 위 요소 · 툴팁 · 섹션/레일/배너/띠 · 입력 · 메뉴/대화상자/토스트 · 상태 화면 · 푸터 · **§11 시안에서 생긴 컴포넌트 40여 개**(상태 · 커뮤니티 · 메이커 도구 · 신뢰 · 탐색/알림/설정 · 플레이 · 모바일) |
| [`../03-game-cards.md`](../03-game-cards.md) | 게임 카드 7종 |
| [`04-patterns.md`](04-patterns.md) | 페이지 리듬 · 문구 · 접근성 · 다크 모드 |

캔버스(그림 견본): `DS01 기초`, `DS02 컴포넌트`, `DS03 컴포넌트 2`, `DS04 게임 카드`, `DS05 고양이 얼굴` — https://claude.ai/code/artifact/57ed3789-695b-4f2c-8ae6-b210fafc167d

## 쓰는 법 (구현)

```css
/* apps/web/src/routes/layout.css */
@import 'tailwindcss';
@import '#lib/styles/tokens.css'; /* 이 폴더의 tokens.css 를 옮긴 것 */
```
```svelte
<html lang="ko" data-ground="play">        <!-- MakersGround 는 make -->
<a class="bg-accent text-on-accent hover:bg-accent-strong rounded-md h-11 px-5 text-body font-bold">플레이</a>
<p class="text-meta text-ink-3">픽셀상점 · 퍼즐 · 5분</p>
```
- 화면 코드는 **의미 토큰만** 쓴다(`bg-sunken`, `text-ink-3`, `bg-accent`). 원시 색(`bg-jjok-500`)·임의 값(`bg-[#046DCE]`)은 린트 대상.
- Tailwind 기본 팔레트·`text-xl`·`shadow-md` 는 지워져 있다 — 쓰면 아무 스타일도 안 생긴다.
- 컴포넌트 크기는 CSS 변수(`h-(--btn-h)`)로.

## 바꾸는 법

1. 색을 바꾸면 `docs/design/tools/*.py` 로 대비를 다시 계산하고 01 문서 표를 고친다.
2. 새 컴포넌트는 03 문서에 해부 · 크기 · 상태 · 접근성을 적고 캔버스 견본에 그린다.
3. 토큰을 추가·삭제하면 `docs/decisions/log.md` 에 한 줄.
