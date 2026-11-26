# 컴포넌트 구조 (안건 2-5) — 2026-11-27 **결정: 4절 구조 · 5절 규칙 · 6절 Bits UI**

사용자 요청: "도메인은 달라도 공통으로 쓰는 것이 많을 수 있다. base 를 확장하면 도메인별로 조금 다른 디자인도 풀 수 있다. 최대한 다양한 상황을 가정하고, 다양한 아키텍처를 조사 · 분석하라."

## 1. 우리 화면에 실제로 있는 컴포넌트 (캔버스 PG01 · PG03 · PG05 · MG · SH 에서 추림)

| 성격 | 예 |
| --- | --- |
| 도메인을 모르는 기본 부품 | Button(주 · 보조 · 유리 · 색 위) · IconButton · Chip(고르기) · Tag(붙은 꼬리표) · Badge(그림 위) · Tooltip · Icon · Tabs(밑줄 · 묶음) · Menu(⋯) · Dialog · Dropdown · Switch · Input/Search · Skeleton · ProgressBar · CatFace(고양이 얼굴) · Logo |
| 도메인을 모르지만 여러 도메인이 같은 **구조**를 공유 | 16:9 그림 틀 + 오버레이 자리(게임 카드 · 개발일지 카드 · 잼 카드 · 미리보기) · 글쓴이 머리 + 본문 + 행동 줄(리뷰 · 커뮤니티 글 · 댓글 · 메이커 답글) · 아이콘+숫자 줄(추천 · 리뷰 · 댓글) · 키-값 목록(게임 정보 · 설정 · 심사 정보) · 구역 머리(귀 아이콘 + 제목 + 오른쪽 행동) · 가로 레일(화살표) · 붙는 탭 줄 · 빈 상태 · 오류 화면 |
| 한 도메인을 **보여 주는** 것 | GameCard(격자 · PICK · 랭킹 줄 · 최근 플레이 · 라이브러리 줄 · 메이커 '내 게임' 줄) · 실행 칩(+툴팁) · ReviewItem · MakerCard · MakerChip · LogCard · JamBanner |
| 사용자 **행동**과 상태 | 추천하기 · 즐겨찾기 · 문제 알리기(+대화상자) · 리뷰 쓰기 · 팔로우 · 플레이/이어하기/다운로드 버튼(상태 기계) · 테마 전환 |
| 페이지 덩어리 | 사이트 헤더(Play/Make) · 게임 첫 화면(미리보기 + 패널) · 리뷰 구역 · 카탈로그 필터 띠 · 홈 배너 |

## 2. 가정한 상황 (어떤 구조든 이걸 다 풀어야 한다)

| # | 상황 | 예 |
| --- | --- | --- |
| S1 | 같은 부품, 그라운드 · 테마만 다름 | Play 쪽빛 버튼 / Make 인주 버튼, 라이트/다크 |
| S2 | 다른 도메인, **같은 뼈대** | 리뷰 · 커뮤니티 글 · 댓글 · 메이커 답글 = 글쓴이 + 본문 + 행동 |
| S3 | 같은 도메인, **다른 배치** | 게임 카드 격자 / PICK / 랭킹 줄 / 최근 플레이 / 라이브러리 줄 |
| S4 | 같은 도메인, 크기 · 일부 표시만 다름 | 카드 M · L, 메타 줄을 숨김 |
| S5 | 다른 그라운드가 같은 도메인 컴포넌트에 **덧붙임** | 메이커 '내 게임'에서 게임 카드에 '심사 중' 표시 · 통계 |
| S6 | 화면 하나에만 있는 것 | PG05 핵심 4칸 |
| S7 | 판단 로직이 있는 것 | 플레이 버튼: 처음 · 해 본 적 있음 · 진행 중 · 다운로드 · 이 기기 불가 |
| S8 | 모바일 · PC 가 다른 것 | 헤더 ↔ 아래 탭바 |
| S9 | 공통 부품을 바꿀 때 **어디가 영향받나** | 칩 테두리 규칙 변경(3차 피드백) |
| S10 | 도메인마다 **조금 다른 디자인** (사용자 예) | 리뷰 답글은 들여쓰고, 커뮤니티 댓글은 대댓글 2단까지 |

## 3. 조사한 구조

| 구조 | 핵심 | 출처 |
| --- | --- | --- |
| A. 아토믹 디자인 | 원자 → 분자 → 유기체 → 템플릿 → 페이지 (크기 단계) | Brad Frost |
| B. Feature-Sliced Design (FSD) | 층: shared → entities(도메인 '것') → features(사용자 행동) → widgets(덩어리) → pages, **아래로만 import**. v2.1 은 "페이지에서 시작하고 재사용될 때 아래 층으로 내린다" | feature-sliced.design |
| C. shadcn 식 | `ui/`(소유한 기본 부품) + 앱 컴포넌트(자유) | ui.shadcn.com |
| D. 기능 폴더(Bulletproof) | `features/<기능>/` 에 화면 · 상태 · API 를 함께, 공용은 `components/` | bulletproof-react |
| E. 기본 + 도메인 (지난 추천안) | `ui/base` + `ui/<도메인>` | — |
| F. 헤드리스 + 스킨 (별개 축) | 접근성 · 키보드 동작은 헤드리스 라이브러리(Bits UI 등), 모양은 우리 토큰 | bits-ui.com |

### 상황별로 풀리나

| | A 아토믹 | B FSD | C shadcn | D 기능 폴더 | E 기본+도메인 |
| --- | --- | --- | --- | --- | --- |
| S1 그라운드 · 테마 | 토큰 | 토큰 | 토큰 | 토큰 | 토큰 |
| S2 같은 뼈대 · 다른 도메인 | ○ 분자 | △ shared 에 둬야 함(명시 규칙 없음) | ✕ 자리 없음 | ✕ 기능마다 복제되기 쉬움 | ✕ base 는 '부품', 뼈대 자리 없음 |
| S3 같은 도메인 · 다른 배치 | △ 분자? 유기체? 논쟁 | ○ entity 안에 여러 컴포넌트 | △ | ○ | ○ |
| S5 덧붙임 | △ | ○ widget 에서 조합 | △ | △ | △ |
| S6 한 화면 전용 | 템플릿/페이지 | ○ pages-first | ○ | ○ | △ |
| S7 판단 로직 | ✕ 자리 없음 | ○ features / model | △ | ○ | ✕ |
| S9 영향 파악 | △ | ○ 층 규칙 + import 그래프 | △ | △ | ○ |
| 의존 방향 린트 | 어려움(크기 기준) | **쉬움**(층 기준) | 보통 | 보통 | 쉬움 |
| 찾기 | 크기로 찾아야 함 | 층 + 도메인 | 쉬움(작을 때) | 기능 | 도메인 |
| 의례 비용 | 낮음 | **높음**(슬라이스마다 공개 API · 세그먼트) | 낮음 | 보통 | 낮음 |

- **A** 는 '크기'로 나누는데, 우리가 실제로 헷갈리는 건 크기가 아니라 "도메인을 아느냐 · 행동을 하느냐"다. 카드는 분자인가 유기체인가 같은 논쟁만 남는다.
- **B** 는 S2 를 빼면 거의 다 풀고, 의존 방향을 린트로 강제하기 쉽다. 다만 정식 FSD 는 의례(슬라이스마다 index · ui/model/api 세그먼트)가 무겁고, SvelteKit 의 `routes` 와 pages 층이 겹친다.
- **E**(지난 추천)는 S2 · S7 을 못 푼다 — 사용자가 짚은 그 문제다.

## 4. 추천: FSD 를 가볍게 + '패턴' 층 (B 의 변형)

```
apps/web/src/lib/ui/
  primitives/        도메인 모름 · 행동 없음        Button, Chip, Tag, Badge, Tooltip, Icon, Tabs, Menu, Dialog, CatFace …
  patterns/          도메인 모름 · 여러 도메인이 같은 뼈대  MediaFrame(16:9 + 오버레이 자리), EntryShell(글쓴이 + 본문 + 행동),
                                                     CountLine, MetaLine, KeyValueList, SectionHeader, Rail, StickyTabs, EmptyState
  entities/<도메인>/  도메인을 '보여 줌' · 행동 없음    game/GameCard · GameRankRow · GameArt · PlatChip, review/ReviewItem,
                                                     maker/MakerChip · MakerCard, log/LogCard, jam/JamBanner
  features/<행동>/    사용자 행동 + 상태 · 서버 호출   recommend/RecommendButton, favorite/FavoriteButton, report/ReportDialog,
                                                     review-write/ReviewForm, play/PlayAction(상태 기계는 순수 함수로 분리)
  widgets/           페이지 덩어리(조합)             SiteHeader, GameHero(미리보기 + 패널), ReviewSection, CatalogFilters
routes/(play)/play/… · routes/(makers)/makers/…     페이지 = widgets 조립. 한 페이지 전용 조각은 그 라우트 폴더 안에(+ 없는 파일)
```

**import 는 아래로만**: routes → widgets → features → entities → patterns → primitives. 같은 층끼리는 import 하지 않는다(entities/game 이 entities/review 를 부르지 않음 — 둘을 함께 쓰려면 위층에서 조합). ESLint 로 강제(`eslint-plugin-boundaries` 또는 `no-restricted-imports`).

**왜 이 구조인가**
1. 사용자가 짚은 "도메인은 달라도 공통" = **patterns 층**이 정확히 그 자리다(S2 · S10). 리뷰 · 댓글 · 답글은 모두 `EntryShell` 을 쓰고, 도메인 차이는 위에서 덧붙인다.
2. "보여 주기"와 "행동"을 나누면(entities ↔ features) 카드 · 리뷰 같은 표시 컴포넌트는 갤러리에서 서버 없이 모든 상태를 그릴 수 있고, 추천 · 즐겨찾기 같은 행동은 한 곳에서 권한 · 로그인 규칙을 지킨다(S7).
3. 층 = 의존 방향이라 **"이 부품을 바꾸면 누가 영향받나"가 위쪽 방향으로만** 생긴다 → 변경 검토 때 영향 목록을 import 그래프에서 자동으로 뽑을 수 있다(S9).
4. FSD v2.1 의 "페이지에서 시작, 재사용될 때 내린다"를 그대로 따른다(S6) — 처음부터 억지로 나누지 않는다.
5. 정식 FSD 의 무거운 의례(슬라이스마다 공개 API 파일 · 세그먼트 폴더)는 뺀다. 컴포넌트 하나 = 파일 하나 + 같은 이름의 이야기(story) + 테스트.

## 5. 변형 · 확장 규칙 (사용자가 말한 '전략'을 언제 쓰나)

| 상황 | 쓰는 전략 | 예 |
| --- | --- | --- |
| 그라운드 · 테마 · 밀도 | **토큰**(props 아님) | Make 의 인주색, 다크 |
| 크기 · 일부 숨김 등 작은 차이 (축 3개 이하) | **props**(문자열 enum) | `GameCard size="m" | "l"`, `showMeta` |
| 뼈대는 같고 내용이 다름 | **합성**: 패턴 + snippet 자리 | `EntryShell` 에 `header` · `body` · `actions` snippet |
| 특정 맥락에서 덧붙임 | **snippet 자리**(불리언 props 늘리지 않음) | 메이커 '내 게임'의 상태 표시 → `GameCard` 의 `badge` · `footer` 자리 |
| 같은 도메인인데 배치가 다름 | **별도 컴포넌트**, 부품(GameArt · CountLine)을 공유 | `GameCard` 와 `GameRankRow` 를 한 컴포넌트에 `layout` prop 으로 몰지 않음 |
| 기본을 '확장'해 도메인 버전을 만듦 | **특화 래퍼**: 기본을 정해진 props + 추가 snippet 으로 감싼 새 컴포넌트 (Svelte 엔 상속이 없음) | `ReviewItem` = `EntryShell` + 플레이 시간 · 버전 줄 + 도움이 됐어요 |
| 한 화면 전용 | **라우트 폴더 안**에 두고, 두 번째로 쓰일 때 내림(이때 사용자와 검토) | PG05 핵심 4칸 |
| 판단 로직 | **순수 함수**(도메인) + 표시 컴포넌트 | `playAction(game, me, device)` → `{ kind: 'play' | 'resume' | … }` |
| PC ↔ 모바일 구조 차이 | 레이아웃이 다른 컴포넌트를 고름(한 컴포넌트에 둘 다 넣지 않음) | `SiteHeader` ↔ `MobileTabBar` |

경고 신호(나오면 사용자와 검토): props 가 7개 넘음 · 불리언 props 3개 넘음 · `layout`/`type` prop 이 내부 구조를 통째로 바꿈 · 같은 층끼리 import 가 필요해짐.

## 6. 헤드리스 라이브러리 (별개 결정, 3-x 와 함께)

메뉴 · 대화상자 · 드롭다운 · 툴팁 · 탭은 키보드 · 포커스 · 스크린리더 처리가 까다롭다. **Bits UI**(Svelte 5 헤드리스, 모양 없음)를 primitives 안에서만 감싸 쓰는 안이 있다 — 바깥 코드는 우리 `Menu` · `Dialog` 만 안다(라이브러리를 바꿔도 primitives 만 고침). 설치 때 Svelte 5.58 · 7일 숙성 · 크기를 확인한다.

## 7. 갤러리(Storybook) 정리 방식

이야기 경로 = 층 구조: `Primitives/Button`, `Patterns/EntryShell`, `Entities/Game/GameCard`, `Features/Recommend`, `Widgets/GameHero`, `Pages/PG05 게임 상세`. 컴포넌트마다 "쓰는 곳" 목록을 import 그래프에서 자동 생성해 이야기 설명에 붙인다(S9).

출처: [FSD 문서(검색 색인)](https://docsearch.algolia.com/mcp/docs/repo/feature-sliced/documentation) · [FSD 경험담](https://dev.to/petrtcoi/my-experience-with-fsd-feature-sliced-design-architecture-5a6n) · [SvelteKit + FSD 템플릿 예](https://sveltethemes.dev/geodask/sveltekit-shadcn-fsd-template) · [Bits UI 문서](https://bits-ui.com/docs) · Atomic Design(Brad Frost) · shadcn/ui · bulletproof-react
