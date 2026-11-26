# 02. 디자인 크래프트 원칙: aDmD Games 디자인 룰북

> 대상: PlayGround(플레이어 사이트)와 MakersGround(메이커 사이트), 하나의 공유 디자인 시스템
> 구현 전제: SvelteKit + Tailwind CSS 4
> 작성 기준일: 2026-11-26
> 성격: 리서치를 바탕으로 한 **실행 규칙집**. 수치는 출발점이며, 실제 화면에서 검증한 뒤 토큰으로 확정한다.
> 표기: **[규칙]**은 반드시 지킬 것, **[권장]**은 기본값, **[검증 필요]**는 출처가 약하거나 우리 환경에서 실측해야 하는 항목.

---

## 0. 이 문서를 읽는 법: 세 가지 전제

1. **"AI 같은 디자인"은 AI 탓이 아니라 기본값(default) 탓이다.** 여러 실무자 글이 같은 결론을 낸다. 모델은 학습 데이터의 평균값, 즉 Tailwind 기본 팔레트, Inter, 둥근 카드 그리드, 보라-파랑 그라데이션으로 수렴한다. 그러니 처방도 결국 기본값을 하나씩 **의도된 결정으로 바꾸는 것**이다.
2. **일관성과 단조로움은 다른 축이다.** 토큰(간격, 글자 크기, 색 역할, 포커스 링)은 엄격하게 고정한다. 그 대신 레이아웃 리듬, 이미지, 카피, 시그니처 순간에는 **허가된 변주 영역**을 둔다(3장).
3. **게임 플랫폼의 주인공은 게임이다.** 수많은 메이커가 만든 제각각의 커버 아트가 화면을 채운다. 그래서 플랫폼 UI는 아트를 돋보이게 하는 **차분한 틀**이어야 하고, 개성은 타이포그래피, 카피, 마이크로 인터랙션, 브랜드 캐릭터 같은 "틀의 디테일"에서 낸다.

---

## 1. 시각 디자인 기초

### 1.1 시각적 위계

- **[규칙] 화면마다 1순위를 하나만 둔다.** Refactoring UI의 핵심 메시지는 "모든 것이 중요할 수는 없다"이다. 위계는 크기만이 아니라 **굵기와 색(명도)** 세 가지 레버로 만든다.
- **[규칙] 강조보다 약화가 먼저다.** 부차 정보(메타데이터, 보조 링크, 날짜)를 `fg-muted`로 한 단계 낮추면 1순위가 따로 크지 않아도 드러난다.
- **[권장] 링크마다 색을 칠하지 않는다.** 본문 안 링크만 색이나 밑줄을 쓰고, 내비게이션이나 카드 안 링크는 굵기와 명도로 구분한다.
- **[권장] 폰 크기에서 3초 테스트를 한다.** 화면을 흐리게(blur 8px) 보고도 1순위 CTA와 제목이 식별되는지 확인한다.
- Laws of UX의 **폰 레스토프 효과**: 비슷한 것들 사이에서 다른 하나가 기억에 남는다. 그러니 강조 요소가 여러 개면 효과가 사라진다. 한 화면에 accent 솔리드 버튼은 **최대 1개**다.

### 1.2 레이아웃과 그리드

- **[규칙] 4px 기본 단위, 8px 리듬.** IBM Carbon 간격 스케일은 2·4·8의 배수로 짜여 있고, 단계마다 토큰이 있으며, 같은 토큰을 컴포넌트 내부와 레이아웃 간격에 모두 쓴다. Carbon은 브레이크포인트에서 스케일을 한두 단계 건너뛰는 것도 허용한다.
- **aDmD 간격 토큰(제안)**: `0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128` (px)
  - 2px는 아이콘과 텍스트 사이 미세 보정에만 쓴다.
  - Tailwind 4의 `--spacing: 0.25rem`은 4px 단위와 맞으므로 그대로 쓰되, 위 목록 밖의 값(`p-[13px]`, `gap-7` 등)은 lint로 막는다.
- **[권장] 그리드**
  - 모바일(<640): 4열, 거터 16, 좌우 여백 16
  - 태블릿(640–1023): 8열, 거터 20, 여백 24
  - 데스크톱(≥1024): 12열, 거터 24, 여백 32–48, 최대 콘텐츠 폭 1280–1440
  - 게임 카탈로그 그리드는 열 수 대신 **카드 최소 폭**으로 정의한다: `grid-template-columns: repeat(auto-fill, minmax(min(100%, 220px), 1fr))`.
- **[규칙] 밀도는 두 단계만 둔다.** `comfortable`은 PlayGround 탐색과 상세용, `compact`는 MakersGround 대시보드, 표, 설정용이다. 밀도는 컴포넌트 내부 패딩과 행 높이만 바꾸고 글자 크기 토큰은 바꾸지 않는다.
- **[규칙] 근접성으로 묶는다.** 묶음 안 간격이 묶음 사이 간격보다 확실히 작아야 한다(최소 2배). 예: 라벨과 입력 8, 필드 사이 20–24, 섹션 사이 48–64.

### 1.3 타이포그래피 (공통 원칙. 한글 세부는 2장)

- **[규칙] 글자 크기는 토큰으로만 쓴다.** 비율은 1.125–1.25(장2도–장3도) 근처에서 정하고, 작은 쪽은 촘촘하게, 큰 쪽은 넓게 벌린다. 당근 SEED는 11–48px를 14단계(t1–t14)로 나누고 각 크기에 짝이 되는 행간 토큰을 둔다. 자세한 내용은 2.3을 참고한다.
- **[규칙] 줄 길이.** 라틴 문자 본문은 50–75자가 최적이라는 연구가 있다(Baymard). WCAG 1.4.8(AAA)은 CJK에 줄당 40자 이하를 권한다. **한글 본문은 줄당 35–45자**(대략 `max-width: 40em` 안팎)를 기준으로 하고, 게임 설명이나 패치 노트처럼 긴 글은 `max-width: 42rem`으로 제한한다.
- **[규칙] 웨이트는 3–4개만 쓴다.** Regular 400, Medium 500, SemiBold 600(선택), Bold 700. SEED도 400/500/700 세 개만 쓴다.
- **[권장] 숫자 정렬.** 점수, 순위, 가격, 플레이 시간, 표의 숫자에는 `font-variant-numeric: tabular-nums`를 쓴다.

### 1.4 색 체계

- **[규칙] 3계층 토큰**(3장)으로 관리하고, 화면 코드는 **의미(semantic) 토큰만** 쓴다. Atlassian은 값이 비슷해 보인다는 이유로 토큰을 고르면 다크 모드나 고대비 테마에서 깨진다고 경고한다. 당근 SEED도 역할 기반 색을 기본으로 하고, 팔레트 색은 예외적인 경우에만 쓴다. 또 같은 값이라도 의미가 다르면 따로 갱신할 수 있어야 한다는 원칙을 둔다.
- **[권장] 톤 팔레트.** Material 3는 키 색마다 13개 톤으로 된 톤 팔레트를 만들고, 컨테이너와 on-컨테이너 짝을 접근 가능한 대비가 나오는 톤으로 정한다. 우리도 각 색상(hue)에 11–13단계 명도 스케일을 두고 **OKLCH**로 정의해 단계 간 지각 명도를 균일하게 맞춘다.
- **의미 토큰 최소 세트(제안)**
  - 배경: `bg-canvas`, `bg-surface`, `bg-surface-raised`, `bg-surface-sunken`, `bg-overlay`
  - 전경: `fg-default`, `fg-muted`, `fg-subtle`, `fg-on-accent`, `fg-disabled`
  - 테두리: `border-default`, `border-subtle`, `border-strong`, `border-focus`
  - 강조: `accent-solid`, `accent-solid-hover`, `accent-soft`(배경), `accent-fg`(텍스트/아이콘)
  - 상태: `positive-*`, `warning-*`, `critical-*`, `info-*` (각각 `solid`, `soft`, `fg`)
- **[규칙] 대비 기준(WCAG 2.2 AA)**: 본문 텍스트 4.5:1, 큰 텍스트(24px 이상, 또는 굵게 18.66px 이상) 3:1, UI 컴포넌트 경계와 아이콘 등 비텍스트 3:1. SEED는 역할 색 조합을 APCA로 검증한다. 우리는 WCAG 2 대비를 법적 기준으로 삼고 APCA는 보조 지표로 쓴다.
- **[규칙] 색만으로 정보를 전달하지 않는다.** 상태 배지는 색과 함께 아이콘이나 텍스트를 쓴다.
- **다크 모드**
  - **[규칙]** 순수 검정(#000)을 캔버스로 쓰지 않는다. 짙은 회색 계열 위에 **위로 올라갈수록 밝아지는 표면 단계**를 둔다. Material 3는 그림자나 불투명도 대신 `surface-container-lowest … highest` 같은 톤 기반 표면 역할로 위계를 표현한다.
  - **[규칙]** 다크에서는 accent의 채도를 낮추고 명도를 올린 별도 값을 매핑한다(같은 HEX를 재사용하지 않는다).
  - **[권장]** 게임 아트가 주인공인 PlayGround는 **다크를 기본 후보**로 검토한다(아트의 채도가 살아난다). 단 `prefers-color-scheme`을 존중하고 수동 전환도 제공한다.
  - **[규칙]** 라이트와 다크 둘 다에서 모든 의미 토큰 조합의 대비를 자동 테스트한다.

### 1.5 엘리베이션(고도)

- **[규칙] 그림자 어휘는 3단계만 쓴다.** `shadow-raised`(카드 호버, 드롭다운), `shadow-overlay`(팝오버, 메뉴), `shadow-modal`(다이얼로그). 정적 카드는 **그림자 없이 테두리나 배경 톤으로** 구분한다.
- **[규칙]** 다크 모드에서는 그림자가 거의 보이지 않으므로, 고도는 표면 톤(밝기 단계)과 `border-subtle`로 표현한다.
- Atlassian은 엘리베이션을 "표면 수준 + 그림자" 쌍의 토큰으로 정의한다. 우리도 `elevation.raised = { bg: surface-raised, shadow: shadow-raised }` 식으로 **쌍으로만** 쓴다.

### 1.6 아이코노그래피

- **[규칙] 한 세트, 한 획 두께.** 예: 24px 그리드에 1.5–2px 스트로크, 모서리 처리 통일. 오픈소스 세트(Lucide, Phosphor 등)를 쓰더라도 **브랜드 핵심 아이콘 8–12개는 직접 그리거나 수정**한다(플레이, 이어하기, 메이커, 좋아요, 컨트롤러 등). "AI 느낌"을 가장 빨리 지우는 투자다.
- **[규칙] 이모지를 UI 아이콘으로 쓰지 않는다.** OS마다 다르게 렌더링되고 크기와 정렬을 제어할 수 없다. 유저 생성 텍스트 안의 이모지는 허용한다.
- **[규칙]** 아이콘만 있는 버튼에는 `aria-label`과 툴팁을 단다. 아이콘 단독 의미 전달은 플레이(▶), 닫기, 검색 같은 관용 기호로 제한한다.
- 크기 토큰: 16(인라인), 20(버튼 내부), 24(기본), 32(빈 상태, 피처).

### 1.7 이미지와 일러스트

- **[규칙] 스톡 3D 일러스트, 아이소메트릭 사람 그림, AI 생성 범용 일러스트는 쓰지 않는다.** 대신 (a) 실제 게임 스크린샷과 커버 아트, (b) aDmD 고유 캐릭터나 마스코트, (c) 단순한 그래픽 모티프(브랜드 도형, 픽셀, 패턴) 중에서 고른다.
- **[권장]** 빈 상태, 404, 점검, 첫 방문 같은 "시그니처 순간"에는 브랜드 캐릭터를 쓴다(3.5).
- **[규칙]** 모든 이미지는 `aspect-ratio`를 고정해 레이아웃 이동(CLS)을 막고, 로딩 중에는 대표색이나 LQIP로 채운다(5.1).

### 1.8 모션

- **원칙**: Apple HIG는 모션을 아껴 쓰고, 상태 전달, 피드백, 직접 조작감처럼 **목적이 있을 때만** 쓰라고 말한다. 사용자가 애니메이션이 끝날 때까지 기다리게 하지 말 것, 그리고 모션을 끌 수 있게 할 것도 강조한다.
- **[규칙] 생산적(productive)과 표현적(expressive) 모션을 나눈다.** Carbon의 구분을 그대로 쓴다. 작업 중 UI(버튼, 토글, 드롭다운, 표)는 짧고 절제된 모션을, 의미 있는 순간(페이지 진입, 플레이 시작, 업적, 시스템 알림)만 눈에 띄는 모션을 쓴다.
- **duration 토큰(Carbon 값을 출발점으로)**

  | 토큰 | 값 | 용도 |
  |---|---|---|
  | `duration-instant` | 70ms | 버튼 눌림, 토글 |
  | `duration-fast` | 110ms | 페이드, 호버 |
  | `duration-moderate` | 150ms | 작은 확장, 짧은 이동 |
  | `duration-moderate-2` | 240ms | 토스트, 아코디언, 드로어 |
  | `duration-slow` | 400ms | 큰 확장, 모달, 중요 알림 |
  | `duration-slower` | 700ms | 배경 딤 등 매우 큰 전환(드물게) |

- **easing 토큰(Carbon)**
  - 생산적 표준 `cubic-bezier(0.2, 0, 0.38, 0.9)`, 진입 `cubic-bezier(0, 0, 0.38, 0.9)`, 퇴장 `cubic-bezier(0.2, 0, 1, 0.9)`
  - 표현적 표준 `cubic-bezier(0.4, 0.14, 0.3, 1)`, 진입 `cubic-bezier(0, 0, 0.3, 1)`, 퇴장 `cubic-bezier(0.4, 0.14, 1, 1)`
  - 원칙: 들어올 때는 감속, 나갈 때는 가속. 퇴장은 진입보다 짧게 한다.
- **[규칙] reduced motion.** `prefers-reduced-motion: reduce`일 때 이동, 확대, 회전, 시차(parallax), 자동 재생 영상 미리보기를 **페이드나 색 변화로 대체**한다. Apple의 Reduce Motion 평가 기준은 다축 이동, 속도가 다른 겹친 모션, 회전, 소용돌이 효과를 끄거나 바꾸라고 하고, 대안으로 디졸브, 하이라이트 페이드, 색 전환을 든다.
- **[규칙]** 스크롤에 연동된 장식 애니메이션(섹션마다 아래에서 떠오르는 fade-up)은 쓰지 않는다. 이것 자체가 대표적인 템플릿 신호다(4장).
- **[권장] 마이크로 인터랙션의 질.** Rauno Freiberg의 「Invisible Details of Interaction Design」은 제스처의 관성, 타이밍, 물리 세계에서 빌린 은유 같은 "보이지 않는 디테일"이 경험의 질을 만든다고 말한다. 우리 우선순위: 플레이 버튼 눌림 → 게임 로딩 → 좋아요/저장 → 탭 전환.

### 1.9 상태(State)

모든 인터랙티브 컴포넌트는 아래 상태를 **디자인 파일과 코드 모두에** 갖춰야 한다.

| 상태 | 규칙 |
|---|---|
| 기본 | 의미 토큰만 사용 |
| hover | 배경 톤 한 단계 변화. 위치 이동(translate-y)은 카드에만, 2px 이내 |
| **focus-visible** | **[규칙]** 2px 이상 실선 링 + 2px 오프셋, `border-focus` 토큰, 인접 색 대비 3:1 이상. `outline: none`만 쓰는 것은 금지. WCAG 2.2는 2.4.11 Focus Not Obscured(AA)를 추가했으므로 스티키 헤더나 하단 바가 포커스를 가리지 않게 `scroll-padding`을 설정한다 |
| active/pressed | 명도 한 단계 더 + `scale(0.98)` 정도(reduced motion에서는 생략) |
| selected | 색 + 형태(체크, 밑줄, 굵기) 이중 표시 |
| disabled | `fg-disabled` + 커서 기본. **비활성 이유를 툴팁이나 보조 문구로 알린다.** 대비 요구에서 면제되지만 읽을 수는 있어야 한다 |
| loading | 버튼은 폭을 유지한 채 스피너로 바꾸고 중복 클릭을 막는다. 페이지 전체 첫 로드는 스켈레톤 |
| empty | 2.6과 5.4 참고 |
| error | 원인 + 해결 방법 + 재시도 수단 |

- **로딩 표시 선택.** NN/g에 따르면 스켈레톤은 **페이지 전체 로드**에서 체감 대기 시간을 줄일 때 쓰며, 성능 최적화를 대신하지 못한다. 진행률을 알 수 있는 긴 작업(게임 빌드 업로드, 게임 에셋 다운로드)은 **퍼센트 진행 바**를 쓴다. 짧은 대기에는 스피너조차 띄우지 않는다(지연 표시, 예: 300ms 이후에만 표시) [검증 필요: 임계값은 실측으로 조정].
- **[규칙] 터치와 클릭 타깃.** WCAG 2.2 2.5.8(AA)은 최소 24×24 CSS px(또는 그만큼의 간격)를 요구한다. 우리 기준은 **모바일 주요 타깃 44px 이상, 최소 24px**이다.

### 1.10 폼

- **[규칙]** 라벨은 항상 보이는 위치(입력 위)에 둔다. placeholder를 라벨 대신 쓰지 않는다.
- **[규칙]** 오류는 필드 바로 아래에 둔다. 아이콘과 텍스트를 함께 쓰고 `aria-describedby`로 연결한다. 제출 시 첫 오류 필드로 포커스를 옮긴다.
- **[규칙]** 검증 시점: 입력 중이 아니라 blur 시 또는 제출 시. 오류를 고치는 중에는 실시간으로 해제한다.
- **[규칙]** 선택 항목에 "(선택)"을 표기한다. 필수 항목이 다수인 폼에서 \*를 남발하지 않는다.
- **[권장] MakersGround 게임 등록 폼**은 단계형으로 나누고(진행 표시), 자동 저장 상태("저장됨 · 방금")를 항상 보여준다.
- **[규칙]** WCAG 2.2 3.3.7 Redundant Entry: 같은 과정에서 이미 입력한 정보를 다시 요구하지 않는다. 3.3.8 Accessible Authentication: 로그인에 퍼즐 같은 인지 테스트를 강제하지 않는다(붙여넣기와 비밀번호 관리자 허용).
- **[권장]** 한국어 오류 문구는 "~를 입력해주세요" 같은 일반형 대신 구체적으로 쓴다. 예: "게임 제목은 40자까지 쓸 수 있어요 (지금 52자)".

### 1.11 데이터 표시 (주로 MakersGround)

- **[규칙]** 숫자는 오른쪽 정렬 + tabular-nums, 텍스트는 왼쪽 정렬. 열 머리글도 같은 정렬을 따른다.
- **[규칙]** 표는 세로선을 쓰지 않고 행 구분선이나 줄무늬 중 하나만 쓴다. 행 높이는 compact 40, comfortable 52.
- **[규칙]** 단위와 기간을 명시한다("최근 7일 플레이 수"). 0과 데이터 없음(—)을 구분한다.
- **[권장]** 지표 카드는 큰 숫자 + 변화량(▲▼와 색, 텍스트 병기) + 비교 기간으로 구성하고, **스파크라인은 공간이 있을 때만** 넣는다.
- **[규칙]** 차트 색은 의미 토큰과 분리된 데이터 팔레트를 쓴다(색각 이상 고려, 순서 고정).

---

## 2. 한국어 타이포그래피와 UI

### 2.1 서체 후보와 라이선스 (상업적 웹 사용 기준)

> 라이선스는 바뀔 수 있다. 출시 직전에 각 공식 저장소의 LICENSE 원문을 다시 확인하고 `docs/`에 사본과 확인 날짜를 남긴다. 산돌구름 같은 배포처도 안내가 법적 보증은 아니라고 명시한다.

| 서체 | 용도 | 라이선스 | 메모 |
|---|---|---|---|
| **Pretendard / Pretendard Variable** | **UI 본문 1순위** | SIL OFL 1.1: 상업적 사용, 수정, 재배포 가능. 폰트 단독 판매 불가 | 라틴은 Inter, 한글은 Source Han Sans, 가나는 M PLUS 1p를 바탕으로 재설계했다. 9개 웨이트 + 가변 폰트 + **다이내믹 서브셋** 제공. JP, Std, GOV 파생판 있음. 저자는 추가 자간이나 광학 보정 없이도 가독성이 좋다고 설명한다 |
| **SUIT / SUIT Variable** | UI 본문 대안(조금 더 기하학적이고 단정함) | SIL OFL | 한글은 Source Han Sans 기반. 9개 정적 웨이트 + 가변. OTF, TTF, WOFF2 제공 |
| **Wanted Sans** | UI와 브랜드 겸용 대안(인간적인 디테일) | SIL OFL(npm에는 OFL-1.1로 표기). 단독 판매와 라이선스 변경만 금지 | Source Han Sans 기반, 7개 웨이트 + 가변. 라틴 전용판 Wanted Sans Std 있음 |
| Spoqa Han Sans Neo | 레거시 대안 | OFL-1.1(애그리게이터 기준). 저장소 LICENSE 확인 필요 | 저장소 마지막 푸시가 2022년이라 유지보수가 불확실하다. **신규 채택 비권장** |
| Noto Sans KR | 폴백 | SIL OFL | Google Fonts 한국어 슬라이싱 제공. 시스템 폴백 체인에 넣는다 |
| **Paperlogy(페이퍼로지)** | 디스플레이와 헤드라인 후보 | SIL OFL(산돌구름 표기): 인쇄, 웹, 임베딩, BI/CI 허용. 파일 판매 금지 | 2024년, 9종 |
| G마켓 산스 | 디스플레이 후보 | 산돌구름 페이지 기준 SIL OFL, 임베딩과 로고 허용 | 너무 흔하게 쓰여 개성이 약하다. 공식 원문 확인 필요 |
| Black Han Sans | 디스플레이(굵은 헤드라인 전용) | SIL OFL 1.1 | 한글 2,580자 + 숫자와 문장부호만 있고 **라틴 미포함**. 라틴 짝 서체가 필요하다 |
| 여기어때 잘난체 | 이벤트성 디스플레이(제한적) | **OFL 아님. 자체 무료 라이선스**: 상업적 사용 가능. 수정과 재배포 금지, CI/BI 상표 등록 불가, 웹 임베딩은 조건부 | 핵심 UI나 로고에는 쓰지 않는다. 쓰기 전에 조건을 문서로 남긴다 |

**[결정 권고]**

1. **UI 텍스트: Pretendard Variable(다이내믹 서브셋, 자체 호스팅).** 한글과 라틴의 조화가 검증됐고, 라틴이 Inter 기반이라 영문 섞어쓰기가 자연스럽고, 성능 도구도 갖춰져 있다.
2. **단, Pretendard는 "한국판 Inter"다.** 국내 서비스에서 가장 흔한 선택이라 그 자체로는 개성이 없다(4장의 "Inter everywhere" 신호와 같은 구조). 그러니 **개성은 다른 레이어에서 확보한다.**
   - (a) 브랜드와 디스플레이 서체를 따로 둔다: Paperlogy, Wanted Sans 고굵기 중 시안 비교 후 결정. 또는 **aDmD 로고타입과 핵심 헤드라인 글자를 직접 레터링**한다(가장 강력한 차별화).
   - (b) 숫자와 라틴 강조용 서체를 하나 둔다: 점수, 순위, 랭킹 숫자에 OFL 라틴 디스플레이나 모노스페이스 서체를 쓴다.
   - (c) 자간, 웨이트, 크기 대비를 과감하게 설계한다(2.3).
3. 디스플레이 서체는 **헤드라인, 브랜드 순간, 시그니처 영역에만** 쓰고, 본문, 폼, 표에는 절대 쓰지 않는다.
4. OFL 폰트를 직접 서브셋하거나 변환하면 OFL상 "수정"에 해당할 수 있다. 예약 글꼴 이름(RFN)이 있는 폰트는 이름 변경 요구가 생길 수 있으니 OFL FAQ를 확인한다. 공식 배포처가 제공하는 웹폰트와 서브셋을 그대로 쓰는 것이 가장 안전하다.

### 2.2 font-family 스택

```css
/* 어느 환경에서나 같은 모양: 브랜드 일관성 우선 (권장) */
--font-sans: "Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont,
  system-ui, "Apple SD Gothic Neo", "Noto Sans KR", "Malgun Gothic", sans-serif;
--font-display: "Paperlogy", "Pretendard Variable", sans-serif; /* 후보: 시안 확정 후 교체 */
--font-mono: ui-monospace, "SFMono-Regular", Menlo, monospace;  /* 코드, 빌드 로그 (MakersGround) */
```

- Pretendard README는 두 가지 스택을 제시한다: 시스템 서체와 섞는 방식과, 어디서나 같게 보이는 방식. 우리는 **후자**를 고른다. 당근 SEED는 iOS, Android, macOS에서 시스템 서체를 쓰고 Windows에서만 Pretendard를 쓰는데, 이는 네이티브 앱 맥락의 선택이다. 웹 브랜드 일관성이 우선인 우리와는 다르다.
- SEED 문서는 Android에서 Medium(500)이 iOS보다 굵게 보일 수 있다고 지적한다. 폴백이 발생하는 환경에서는 500/600 웨이트를 실기기에서 확인한다 **[검증 필요]**.

### 2.3 한글 타입 스케일, 행간, 자간

한글은 글자가 정사각형 틀을 꽉 채우고 디센더가 없어서 같은 px에서 라틴보다 **빽빽하고 크게** 보인다. 그래서 행간은 "짧은 UI 텍스트용"과 "여러 줄 읽기용" 두 트랙으로 나눈다.

참고 기준: 당근 SEED 스케일은 16/22(≈1.375), 14/19(≈1.36), 24/32(≈1.33), 48/60(1.25)로, **크기가 커질수록 행간 비율이 줄어든다.** 이는 앱 UI의 짧은 텍스트 기준이다.

**aDmD 스케일(제안, rem은 16 기준)**

| 토큰 | 크기 | UI 행간(1–2줄) | 읽기 행간(본문) | 용도 |
|---|---|---|---|---|
| `text-2xs` | 11 | 15 | – | 법적 고지, 배지(최소) |
| `text-xs` | 12 | 16 | 18 | 캡션, 메타 |
| `text-sm` | 14 | 20 | 22–23 | 보조 본문, 버튼(소) |
| `text-md` | 15 | 21 | 24 | 버튼, 입력, 리스트 |
| `text-base` | 16 | 22 | **26 (1.625)** | 기본 본문 |
| `text-lg` | 18 | 25 | 29 | 리드 문단, 카드 제목 |
| `text-xl` | 20 | 27 | – | 섹션 소제목 |
| `text-2xl` | 24 | 32 | – | 섹션 제목 |
| `text-3xl` | 30 | 38 | – | 페이지 제목 |
| `text-4xl` | 40 | 48 | – | 히어로(모바일 최대) |
| `text-5xl` | 56 | 64 | – | 디스플레이(데스크톱) |
| `text-6xl` | 72 | 78 | – | 시그니처 순간 전용 |

- **[규칙] 본문 읽기 행간은 1.6–1.7**이다. 블로그 같은 국내 실무 자료는 1.2–1.5 범위를 무난하다고 보지만, 이는 짧은 텍스트 기준으로 보는 편이 안전하다. 게임 설명이나 공지 같은 긴 글은 1.6 이상으로 한다.
- **[규칙] 행간은 단위 없는 값이나 px 토큰으로 쓰고, 글자 크기 토큰과 짝을 지어** 쓴다(SEED 방식). Tailwind 4에서는 `--text-base: 1rem; --text-base--line-height: 1.375rem;`처럼 크기와 행간을 함께 정의한다.
- **자간 [검증 필요]**: Pretendard 제작자는 추가 자간 보정이 필요 없다고 설명한다. 큰 헤드라인에서 살짝 좁히는 것(-0.01em ~ -0.025em)은 국내 실무 관행이지만 **출처가 있는 표준은 아니다.** 규칙은 이렇다.
  - 본문(≤18px): `0`
  - 제목(20–30px): `-0.01em`
  - 디스플레이(≥40px): `-0.02em` 안팎. 실제 렌더링을 보고 확정한다.
  - 12px 이하 작은 글자와 대문자 라틴 라벨: `0` 또는 `+0.02em`
- **[규칙] 굵기 대비로 위계를 만든다.** 한글은 크기를 키우는 것보다 굵기 차이(400 ↔ 700)가 더 효과적인 경우가 많다. 그래도 한 블록 안에 3단계 이상 섞지 않는다.

### 2.4 줄바꿈: `word-break: keep-all`

```css
:root { word-break: keep-all; overflow-wrap: anywhere; } /* 또는 break-word */
h1, h2, h3, .card-title { text-wrap: balance; }
p, .prose { text-wrap: pretty; }
```

- **[규칙] `keep-all`을 전역 기본값으로 쓴다.** 한국어는 기본적으로 글자 단위로 끊기므로, 어절이 깨지지 않게 막는다. 공백이 없는 중국어와 일본어에서는 넘침이 생길 수 있고, 긴 URL이나 붙여 쓴 영문에도 넘침이 생기므로 **`overflow-wrap`을 안전장치로 반드시 함께** 둔다.
- **[권장] `text-wrap: balance`**는 제목, 카드 제목, 캡션처럼 짧은 텍스트에 쓴다. Chromium은 6줄, Firefox는 10줄까지만 적용한다. `keep-all` 없이 쓰면 균형을 맞추려고 어절을 쪼갤 수 있다.
- **[권장] `text-wrap: pretty`**는 본문 마지막 줄에 한 어절만 남는 것을 막는다. 효과는 미묘하고, 지원하지 않는 브라우저는 무시한다(점진적 향상).
- `word-break: auto-phrase`는 아직 프로덕션에 쓸 단계가 아니라는 평가가 있어 쓰지 않는다.
- **[규칙]** 버튼, 탭, 배지처럼 한 줄이어야 하는 요소는 `white-space: nowrap` + 말줄임 + 전체 텍스트 툴팁(또는 `title`)을 쓴다.
- **[규칙] 유저 생성 콘텐츠**(게임 제목, 메이커 닉네임)는 길이와 문자 종류를 예측할 수 없다. 카드 제목은 `line-clamp: 2`로 처리하고, 아주 긴 단일 문자열을 넣은 테스트 픽스처를 둔다.

### 2.5 라틴과 한글 섞어 쓰기, 숫자

- **[규칙]** UI 레이블은 한국어를 기본으로 한다. 영어 레이블("Play now", "Explore")을 장식처럼 섞지 않는다. 단, 고유명사(게임 제목, 플랫폼명, 브랜드 PlayGround/MakersGround)는 원문 그대로 쓴다.
- **[규칙]** 한글과 라틴을 다른 서체로 짝지을 때는 `@font-face`의 `unicode-range`로 라틴 서체를 할당하고, `size-adjust`로 x-height와 한글 높이를 맞춘다. Pretendard 단일 서체로 가면 이 문제는 거의 사라진다.
- **[규칙]** 숫자와 단위 사이는 붙여 쓴다(규범상 띄어 쓸 수 있으나, UI에서는 붙여 쓰는 쪽이 대세다. 프로젝트 내에서 하나로 통일). 큰 수는 천 단위 쉼표를 쓴다(`Intl.NumberFormat('ko-KR')`). 축약은 "1.2만", "3.4천" 같은 한국식 단위로 하고, "12K"를 쓰지 않는다.
- **[규칙]** 날짜는 `2026. 11. 26.` 또는 `11월 26일`, 상대 시간은 "3분 전"을 쓴다. `Intl.DateTimeFormat`과 `Intl.RelativeTimeFormat`의 `ko` 로케일을 쓴다.

### 2.6 폰트 로딩과 성능

- **배경**: 한글 폰트는 글리프가 11,172자 이상이라 라틴보다 훨씬 무겁다. Google은 한국어 웹 텍스트에서 함께 등장하는 글자 패턴을 분석해 `unicode-range` 슬라이스를 만들었다. 균등 분할보다 요청 수를 약 20배 줄였다고 보고했다. 자주 쓰는 약 2,000자를 20개 슬라이스로, 나머지를 코드포인트 순으로 100개 슬라이스로 나눈 방식이다. 또 이런 다수의 작은 파일이 HTTP/2 병렬 전송 덕분에 실용적이라고 설명한다.
- **[규칙] Pretendard 다이내믹 서브셋을 자체 호스팅한다**(npm 패키지의 `dist/web/variable/pretendardvariable-dynamic-subset.css` 계열을 빌드에 포함). 외부 CDN 의존을 줄이고, 같은 오리진에서 캐시하고, 개인정보 측면의 리스크도 줄인다.
- **[규칙]** `font-display: swap`(본문)을 쓴다. 디스플레이 서체는 `optional` 또는 `swap` + 폴백 메트릭 보정(`size-adjust`, `ascent-override`)으로 레이아웃 이동을 최소화한다.
- **[권장]** 디스플레이 서체는 **쓰이는 문자열이 정해진 곳**(로고, 고정 헤드라인)에 한해 해당 글자만 서브셋한다. 단 OFL 수정 조항을 확인한다. 메이커가 입력하는 가변 텍스트에는 디스플레이 서체를 쓰지 않는다(글리프 누락 위험).
- **[권장]** 가변 폰트 하나가 정적 웨이트 3–4개보다 가벼운지 실측해서 선택한다 **[검증 필요]**.
- **[규칙]** 폰트 성능 예산: 첫 화면 폰트 전송 합계 **150KB 이하**를 목표로 한다(woff2, 다이내믹 서브셋 기준) **[검증 필요: 실측 후 확정]**.

---

## 3. 디자인 시스템 아키텍처

### 3.1 토큰 3계층

| 계층 | 예 | 누가 쓰나 | 규칙 |
|---|---|---|---|
| **Primitive(원시)** | `gray-50…gray-950`, `coral-500`, `space-4`, `radius-md`, `duration-fast` | 토큰 파일만 | **화면 코드에서 직접 쓰지 않는다.** 색 모드를 모른다 |
| **Semantic(의미)** | `bg-surface`, `fg-muted`, `accent-solid`, `critical-fg`, `border-focus` | 모든 화면과 컴포넌트 | 테마(라이트/다크, 사이트별 accent)에 따라 값이 바뀐다 |
| **Component(컴포넌트)** | `button-primary-bg`, `card-radius`, `game-cover-radius`, `focus-ring-width` | 해당 컴포넌트 | 꼭 필요할 때만 만든다. 의미 토큰을 참조한다 |

- GitHub Primer도 같은 구조다. Base 토큰은 원시값에 직접 매핑되고 색 모드를 따르지 않아서 코드와 디자인에서 직접 쓰지 말아야 한다. Functional 토큰은 텍스트, 테두리, 배경 같은 전역 패턴을 표현하며 가장 많이 쓰인다. Component 토큰은 둘 다 참조할 수 있고 색 모드를 따른다.
- 당근 SEED도 스케일 토큰을 조합해 의미 토큰을 만들고(`$semantic.color.*` 네임스페이스), 스키마는 그대로 둔 채 값만 주입해 테마를 바꾼다.

### 3.2 이름 짓기

- Atlassian 구조를 따른다: **기반(foundation) . 속성(property) . 수식어(modifier)**. 예: `color.text.subtle`, `color.icon.success`. 수식어가 없으면 기본값이다(`color.text`).
- **aDmD 규칙**
  - CSS 변수: `--color-fg-muted`, `--color-bg-surface-raised`, `--color-accent-solid-hover`
  - Tailwind 클래스: `text-fg-muted`, `bg-surface-raised`, `bg-accent-solid`
  - 상태 수식어는 맨 끝에 붙인다: `-hover`, `-active`, `-disabled`
  - 크기 이름은 한 체계만 쓴다: `2xs, xs, sm, md, lg, xl, 2xl…`
  - **색 이름(blue, purple)을 의미 토큰에 넣지 않는다.** 나중에 브랜드 색이 바뀌면 이름이 거짓말이 된다.

### 3.3 Tailwind CSS 4 구현 패턴

```css
@import "tailwindcss";

/* 1) 기본 팔레트 제거: indigo-500 같은 "AI 기본값"이 아예 컴파일되지 않게 */
@theme {
  --color-*: initial;
  --font-*: initial;
  --shadow-*: initial;
  --radius-*: initial;

  /* primitive */
  --color-gray-50: oklch(0.985 0.003 80);
  /* … */
  --radius-sm: 6px;  --radius-md: 10px;  --radius-lg: 16px;  --radius-full: 9999px;
  --ease-standard: cubic-bezier(0.2, 0, 0.38, 0.9);
  --ease-expressive: cubic-bezier(0.4, 0.14, 0.3, 1);
  --text-base: 1rem; --text-base--line-height: 1.375rem;
}

/* 2) semantic: 런타임 변수. 테마와 사이트에 따라 교체 */
:root {
  --fg-default: var(--color-gray-900);
  --bg-surface: var(--color-gray-0);
  --accent-solid: var(--color-coral-600);      /* PlayGround (예시) */
}
[data-site="makers"] { --accent-solid: var(--color-teal-600); }   /* MakersGround (예시) */
[data-theme="dark"] { --fg-default: var(--color-gray-50); --bg-surface: var(--color-gray-900); }

/* 3) semantic을 유틸리티로 노출: 다른 변수를 참조하므로 inline */
@theme inline {
  --color-fg-default: var(--fg-default);
  --color-surface: var(--bg-surface);
  --color-accent-solid: var(--accent-solid);
}

@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```

- Tailwind 4는 `@theme` 변수 하나가 유틸리티와 CSS 변수를 함께 생성한다. `--color-*: initial`로 기본 네임스페이스를 지울 수 있다. 다른 변수를 참조하는 토큰은 `@theme inline`으로 선언해야 예상치 못한 폴백이 생기지 않는다.
- **공유**: 토큰과 테마 CSS를 `packages/design-tokens/theme.css` 같은 독립 파일로 두고, 두 사이트 모두 `@import "tailwindcss";` 뒤에서 import한다(공식 문서가 권장하는 모노레포 공유 방식).
- **[규칙]** 원본 소스는 JSON 하나(W3C Design Tokens 포맷 호환)로 두고, CSS를 생성할지 CSS를 원본으로 둘지 **한 가지만** 고른다. 이중 관리는 금지다.
- **[규칙]** 임의값 유틸리티(`bg-[#…]`, `p-[13px]`, `text-[17px]`)는 lint로 금지하고, 예외는 주석으로 사유를 남긴다.

### 3.4 사이트별 테마(PlayGround / MakersGround)

- **공유하는 것**: 중립색, 상태색, 타입 스케일, 간격, 반경, 포커스 링, 모션 토큰, 아이콘 세트, 컴포넌트 API.
- **사이트별로 다른 것**: `accent-*` 의미 토큰 세트, 밀도 기본값(PlayGround는 comfortable, MakersGround는 compact), 디스플레이 서체 사용 빈도(PlayGround가 더 많이), 브랜드 캐릭터의 등장 맥락.
- **[규칙]** 두 accent 모두 라이트와 다크 각각에서 `fg-on-accent` 대비 4.5:1을 만족해야 한다.
- **[권장]** accent 색은 "트렌디해 보여서"가 아니라 **이유가 있는 색**으로 고른다(aDmD 로고나 마스코트에서 유래, 경쟁 플랫폼과 구분 등). 보라~인디고 계열은 AI 기본값과 겹치므로 쓰려면 강한 근거가 필요하다(4장).

### 3.5 컴포넌트 API 원칙 (Svelte)

- **[규칙] variant는 의미로 짓는다.** `variant="primary | secondary | ghost | danger"`, `size="sm | md | lg"`. `color="blue"` 같은 시각 속성 prop은 없다.
- **[규칙] 스타일 탈출구를 제한한다.** `class` 병합은 레이아웃(margin, grid 위치)에만 허용하고, 색과 타이포를 덮어쓰는 것은 리뷰에서 반려한다.
- **[규칙] 조합(composition) 우선.** `Card` / `Card.Media` / `Card.Body` 같은 슬롯과 스니펫 구조로 두고, boolean prop을 계속 늘리지 않는다(`showIcon`, `isLarge`, `hasBorder` … 금지).
- **[규칙] 접근성을 컴포넌트 안에 넣는다.** 포커스 관리, ARIA, 키보드 조작은 컴포넌트 기본값으로 제공한다. 사용처에서 매번 챙기지 않게 한다.
- **[규칙] 상태 완비.** 모든 컴포넌트 문서에 1.9의 상태 표를 채운다. loading과 error가 없는 데이터 컴포넌트는 머지하지 않는다.

### 3.6 문서화

- 컴포넌트마다 문서에 담을 것: **언제 쓰는지 / 언제 쓰지 않는지**, 변형(variant)별 예시, 상태 표, 접근성 메모, 문구 가이드, Do/Don't 실제 화면 예시.
- 토큰 페이지: 라이트와 다크 스와치, 대비 수치, 사용 예.
- SEED처럼 `llms.txt` 형태의 기계 판독용 문서를 함께 두면, AI 코딩 도구가 **우리 토큰을 기본값으로** 쓰게 유도할 수 있다. AI 기본값 회귀를 막는 실용적인 방법이다.

### 3.7 일관성은 유지하되 단조롭지 않게: 표현 영역(Expression Zones)

Google의 Material 3 Expressive 연구(46개 연구, 1.8만 명 이상 참여)에서 표현적인 디자인은 "활기차다, 친근하다, 재미있다" 평가가 높았고, 과업 핵심 요소를 찾는 속도도 빨랐다(48명 대상 연구에서 33% 빠름). 동시에 Google은 기본 인터랙션 패러다임을 깨면 사용성이 떨어진다고 경고한다. 결론은 **표현은 허가된 곳에서, 기본기는 어디서나**다.

| 영역 | 화면 예 | 고정(불변) | 허용 변주 |
|---|---|---|---|
| **Z0 코어** | 로그인, 설정, 결제, 폼, 표, 업로드 | 모든 토큰, 레이아웃 템플릿, 문구 톤 | 거의 없음 |
| **Z1 콘텐츠** | 카탈로그, 게임 상세, 메이커 프로필, 검색 | 토큰, 카드 구조, CTA 위치 | 섹션 레이아웃 템플릿 선택(아래 목록), 아트에서 추출한 배경 틴트 |
| **Z2 시그니처** | 홈 상단, 신작 런칭, 빈 상태, 404, 첫 방문, 업적, 메이커 첫 게시 축하 | 접근성, 포커스, 대비, reduced motion | 디스플레이 서체, 비대칭 레이아웃, 캐릭터, 표현적 모션, 손그림 요소 |

**변주 규칙**

1. **섹션 템플릿 풀(pool)**: 홈과 카탈로그는 미리 정의한 4–6개 섹션 템플릿만 조합한다. 예: (A) 대형 피처 1 + 보조 2 비대칭, (B) 가로 스크롤 선반, (C) 에디토리얼(큰 이미지 + 글), (D) 촘촘한 리스트/랭킹, (E) 메이커 스포트라이트, (F) 한 줄 공지/배너.
2. **같은 템플릿을 연속으로 쓰지 않는다**(A-B-B 금지). 밀도 리듬은 촘촘 → 여유 → 촘촘으로 교차시킨다.
3. **배경 리듬**: 섹션 간격을 전부 같게 두지 않는다. 두세 섹션마다 표면 톤 전환이나 전폭(full-bleed) 섹션으로 장을 나눈다.
4. **시그니처는 희소하게.** 화면당 시그니처 요소는 최대 1개다. 시그니처가 모든 곳에 있으면 그것이 새로운 단조로움이 된다.
5. **카드 형태를 다양화한다.** 게임 카드, 메이커 카드, 공지 카드, 컬렉션 카드의 형태(비율, 반경, 정보 배치)는 **의도적으로 다르게** 한다. 모든 것이 같은 둥근 사각형이 되지 않게 한다(4장).

**시그니처 순간(후보)**

- 플레이 버튼: 누르면 컨트롤러나 카트리지 은유의 짧은 모션(≤400ms), 이어서 로딩 화면이 게임 아트 대표색으로 물든다.
- 첫 방문: 마스코트가 한 줄로 안내한다(건너뛰기 가능, 한 번만).
- 빈 상태와 404: 캐릭터 + 구체적인 다음 행동.
- MakersGround: 첫 게임 공개 순간의 축하 화면(공유 카드 자동 생성).

---

## 4. "AI 느낌" 진단과 처방

### 4.1 왜 생기나

- 생성 모델은 기존 인터페이스의 통계적 중심, 즉 "평균적인 좋은 UI"로 수렴한다. 그래서 새 SaaS 제품은 제품을 이해하기도 전에 이미 익숙해 보인다(UX Collective).
- Tailwind 제작자 Adam Wathan은 2025년에, Tailwind UI의 모든 버튼을 `bg-indigo-500`으로 만든 것이 모든 AI 인터페이스가 인디고색인 이유라고 농담했다. 원인 분석이라기보다는 기본값이 얼마나 강한지를 보여주는 일화다.
- 사용자는 표면을 보고 제품 전체를 판단한다. UI가 엉성해 보이면 코드도 엉성할 거라고 생각한다(Zurb).
- 실무자들의 결론: **AI 느낌은 AI 문제가 아니라 기본값 문제다.**

### 4.2 진단표: 신호, 왜 뻔해 보이나, 처방

| # | 신호(tell) | 왜 뻔해 보이나 | aDmD 처방 |
|---|---|---|---|
| 1 | **보라→파랑(인디고→바이올렛) 그라데이션** 배경과 버튼 | 2020–21년 드리블 유행 + Tailwind 기본값. 생성물에서 가장 흔한 색 | 기본 팔레트를 `initial`로 제거한다. accent는 단색 솔리드. 그라데이션은 게임 아트 안에서만 허용한다. 색은 기능(주요 행동, 경고, 성공)에 배정한다 |
| 2 | **글래스모피즘 남용**(반투명 + 블러 카드가 모든 곳에) | 깊이에 대한 근거 없이 "현대적" 표면만 흉내 냄. 대비도 불안정 | 블러는 오버레이(모달 배경, 이미지 위 스크림) 1–2곳에만 쓴다. 텍스트 뒤 반투명 배경은 대비를 자동 검사한다 |
| 3 | **"중앙 히어로 + 3개 기능 카드 + 가격 + FAQ"** 순서 | 랜딩 템플릿 그대로. 제품의 실체 없이 형식만 있음 | 홈 첫 화면에 **실제 게임**을 보여준다(플레이 가능한 피처 게임, 신작 선반). 마케팅 섹션이 아니라 콘텐츠로 시작한다 |
| 4 | **이모지 아이콘**(🚀 ✨ 🎮)을 기능 아이콘으로 사용 | 디자인 결정을 회피한 흔적. OS별로 다르게 렌더링됨 | 단일 아이콘 세트 + 브랜드 핵심 아이콘 직접 제작(1.6) |
| 5 | **모든 카드가 똑같은 `rounded-2xl shadow-lg`** | 반경, 패딩, 높이가 전부 같아서 위계가 평평해짐 | 반경 어휘를 3개로 제한한다. 정적 카드는 그림자 없이. 카드 종류별로 형태를 다르게(3.7-5). 주요 항목은 더 크고 무겁게, 부차 항목은 물러나게 |
| 6 | **Inter(한국은 Pretendard)만 기본 굵기로 씀** | 가장 흔한 선택. 타이포 위계 없음 | 본문은 Pretendard로 유지하되 **디스플레이와 숫자 서체를 따로** 두고, 크기와 굵기 대비를 과감하게 한다(2.1) |
| 7 | **모든 것이 가운데 정렬** | 결정을 미룬 정렬. 긴 텍스트 가독성이 떨어짐 | 기본은 왼쪽 정렬. 가운데 정렬은 짧은 빈 상태 메시지와 시그니처 순간에만 쓴다 |
| 8 | **모호한 카피**("혁신적인 경험", "쉽고 빠르게", "Unlock / Empower / Seamless") | 어떤 제품에도 붙일 수 있는 문장 | 구체적인 동사와 명사를 쓴다: "브라우저에서 바로 실행, 설치 없음", "지난주 올라온 게임 12개". aDmD의 목소리 가이드를 만든다(4.4) |
| 9 | **가짜 수치와 사회적 증거**("10,000+ 사용자", 별점 4.9, 가짜 후기) | 검증할 수 없는 숫자는 신뢰를 깎는다. 초기 플랫폼이면 더 그렇다 | 실제 숫자만 쓴다. 숫자가 작으면 숫자 대신 **이름과 이야기**(메이커 인터뷰, 개발 로그)를 보여준다 |
| 10 | **완벽한 대칭과 균일 그리드** | 생성물은 균등 분배를 선호한다. 시선이 머물 곳이 없음 | 12열 위에서 7:5, 8:4 비대칭을 쓰고, 피처 하나를 크게 키운다(템플릿 A) |
| 11 | **스톡풍 3D, 아이소메트릭 일러스트, 범용 AI 일러스트** | 모든 스타트업이 같은 사람과 같은 화분을 씀 | 실제 스크린샷 + aDmD 캐릭터 + 단순 그래픽 모티프(1.7) |
| 12 | **그림자와 글로우 과다**(네온 글로우 버튼, 이중 그림자) | 깊이 체계 없이 "고급스러움"을 덧칠함 | 그림자 3단계 토큰만 쓴다. 글로우 금지(포커스 링 제외) |
| 13 | **섹션 리듬이 전부 같음**(모든 섹션이 제목 + 부제 + 그리드, 간격 96px 동일) | 스크롤해도 장면이 바뀌지 않음 | 섹션 템플릿 풀과 리듬 규칙(3.7) |
| 14 | **스크롤할 때마다 fade-up 애니메이션** | 모든 생성 랜딩의 공통 모션. 내용과 무관함 | 스크롤 연동 장식 모션 금지. 모션은 피드백과 상태 전환에 쓴다 |
| 15 | **배지와 필(pill) 남발**("NEW", "✨ AI-powered", 상단 공지 필) | 정보가 아닌 장식 라벨 | 배지는 상태 정보(신작, 업데이트, 플레이 중)에만. 화면당 종류 2개 이하 |
| 16 | **패널 왼쪽 강조선**(왼쪽 테두리에 색 막대 + 둥근 모서리) | 생성 UI에 자주 나오는 장식 | 알림과 인용에만 쓰고, 일반 카드에는 쓰지 않는다 |
| 17 | **빈 상태, 로딩, 에러가 없음** | 데모는 항상 데이터가 있다는 가정 | 모든 화면에서 불행 경로를 설계한다(1.9, 5.4) |
| 18 | **베이지/크림 배경 + 세리프·이탤릭 혼용**(2025–26년 "고급" 버전의 AI 기본값) | 보라 그라데이션의 반동으로 생긴 새 기본값 | 배경 톤도 근거를 두고 정한다. 이탤릭은 한글에 존재하지 않는 문법이니 한글 UI에서는 쓰지 않는다 |
| 19 | **영어 레이블 장식**("Explore", "Featured", "Trending Now") | 번역 템플릿처럼 보이고 브랜드 목소리가 사라짐 | 한국어 고유 레이블로 쓴다("이번 주 새로 나온", "메이커가 직접 고른") |
| 20 | **모든 기능이 한 번에 노출** | 우선순위 결정이 없음 | 점진적 공개. 플레이어 상태에 따라 보여줄 것을 고른다(5.3) |

**Korean 맥락 추가 신호**

- Pretendard + 토스 블루 계열 + 3D 클레이 이모지 조합은 "국내 핀테크 템플릿" 인상을 준다.
- 모든 문장이 "~하세요!"나 "~해보세요 🙌"로 끝나는 카피.
- 의미 없는 영문 섹션 레이블과 한국어 본문의 혼용.

### 4.3 "누군가 만든 것처럼" 보이게 하는 기법

1. **관점(Point of view)**: aDmD가 무엇을 믿는지 한 문장으로 정하고 화면이 그것을 보여주게 한다. 예: "작은 게임이 주인공인 놀이터". 그러면 대형 AAA식 배너 대신 **메이커의 얼굴과 이름**이 크게 나오는 결정을 내리게 된다.
2. **진짜 콘텐츠로 디자인한다**: Lorem ipsum이나 가짜 게임 카드 대신 실제(또는 실제와 같은 길이와 편차의) 게임 제목, 커버, 설명으로 시안을 만든다. 긴 제목, 아트가 없는 게임, 설명 한 줄짜리 게임도 포함한다.
3. **구체적인 카피와 목소리**: 실제 사람(운영자)의 말투로 쓴다. 숫자, 고유명사, 날짜를 쓴다. "새 게임"보다 "11월 넷째 주, 새로 올라온 게임 7개"가 낫다.
4. **고유 캐릭터와 일러스트**: 마스코트 하나가 빈 상태, 로딩, 404, 이메일, 소셜 카드까지 이어지면 일관성과 개성을 동시에 얻는다.
5. **비대칭과 에디토리얼 레이아웃**: 큰 피처 하나와 작은 것 여럿, 텍스트와 이미지 겹침, 그리드를 의도적으로 깨는 요소 하나.
6. **타이포그래피의 개성**: 디스플레이 서체, 극적인 크기 대비(본문 16 ↔ 디스플레이 56–72), 숫자 전용 서체, 직접 그린 로고타입.
7. **의도된 제약**: 예를 들어 "accent는 1색, 반경은 3종, 그림자는 3단계, 화면당 시그니처 1개". 제약이 스타일을 만든다.
8. **불완전함과 손맛**: 손그림 밑줄, 스티커 같은 배지, 살짝 기울어진 요소 한 개, 픽셀 아트 모티프 등. 단, Z2(시그니처 영역)에서만.
9. **마이크로 인터랙션 수준의 디테일**: 버튼 눌림 깊이, 좋아요 하트의 짧은 탄성, 탭 인디케이터 이동, 복사 완료 피드백. 이런 "보이지 않는 디테일"이 만든 사람의 손길로 읽힌다.
10. **같은 컴포넌트를 여러 번 다시 그린다**: Designlab은 같은 컴포넌트를 여러 방식으로 재설계하는 연습을 크래프트 훈련법으로 권한다. 핵심 컴포넌트(게임 카드, 플레이 버튼, 상세 상단)는 최소 3안을 비교한 뒤 결정한다.
11. **생성과 출시 사이에 사람의 판단을 둔다**: 체크리스트는 증상을 다룰 뿐이다. 실제 사용자가 쓰는 모습을 보는 단계를 프로세스에 넣는다.
12. **기본값 회귀를 기계로 막는다**: 금지 클래스와 패턴(`indigo-*`, `violet-*`, `rounded-2xl shadow-lg` 조합, 임의값)을 lint와 CI로 잡는다.

### 4.4 aDmD 목소리 가이드(초안)

- **말투**: 친구 같은 존댓말("~해요"). 과장된 감탄과 느낌표 연속은 쓰지 않는다.
- **구체성**: 모든 CTA는 동사로 시작하고 결과를 예고한다: "플레이", "이어하기", "게임 올리기", "초안 저장".
- **금지어(예)**: 혁신적인, 차세대, 원활한, 손쉽게, 최고의, 모든 것을, 지금 바로(남발 시).
- **오류**: 사과는 한 번, 원인과 해결을 함께. 사용자를 탓하지 않는다. NN/g도 검색 결과 없음 화면에서 사용자를 놀리는 듯한 어조를 피하라고 한다.

---

## 5. 게임 플랫폼 특화

### 5.1 커버 아트와 썸네일

**참고 사례**

- Steam은 2024년 8월부터 더 큰 에셋 크기를 받고 옛 크기를 받지 않는다. 헤더 캡슐은 920×430(약 2.14:1), 스몰 캡슐은 462×174다. 메인 캡슐 1232×706, 세로 캡슐 748×896, 라이브러리 캡슐 600×900(2:3)은 제3자 가이드 기준이다 **[검증 필요]**.
- Steam 캡슐 규칙: 아트 + 게임명 + 공식 부제만 허용하고, 리뷰 점수, 수상 로고, 할인 문구, CTA, 다른 제품 홍보 문구는 금지한다. 라이브러리 히어로는 글자 없이 아트만 쓴다. 모든 캡슐은 제품명이나 로고가 읽혀야 한다.
- itch.io 커버 권장 크기는 630×500(약 1.26:1)이다(커뮤니티와 대시보드 안내 기준).

**aDmD 에셋 규격(제안)**

| 슬롯 | 비율 | 최소 / 권장 업로드 | 필수 여부 | 쓰이는 곳 |
|---|---|---|---|---|
| 가로 커버 | **16:9** | 1280×720 / 1920×1080 | **필수** | 카드, 상세 상단, 소셜 공유(OG는 별도 크롭) |
| 세로 포스터 | **3:4** | 900×1200 / 1200×1600 | 선택 | 선반 세로 카드, 모바일 피처 |
| 아이콘 | 1:1 | 256 / 512 | 선택(없으면 자동 생성) | 이어하기 목록, 검색 자동완성 |
| 로고(투명 PNG/SVG) | 자유 | 폭 800 | 선택 | 상세 히어로에서 아트 위 오버레이 |
| 스크린샷 | 16:9 권장 | 1280×720 | 3장 이상 권장 | 상세 갤러리 |

**규칙**

- **[규칙] 커버 안 텍스트 규칙(Steam 방식)**: 게임명과 부제 외의 텍스트(점수, "무료!", "지금 플레이")를 금지한다. 플랫폼 UI가 배지와 CTA를 담당하므로 중복과 혼란을 막는다.
- **[규칙] 초점(focal point)**: 메이커가 업로드할 때 초점 좌표를 지정하고, `object-position`으로 각 슬롯 크롭에 반영한다. **MakersGround에 모든 슬롯 크롭 미리보기**(카드, 상세, 모바일, 공유 카드)를 제공한다.
- **[규칙] 세로 포스터가 없을 때의 폴백**: 16:9 아트를 흐리게 확장한 배경 위에 원본을 중앙 배치하고 게임명을 디스플레이 서체로 넣는다. 잘라서 늘리는 크롭은 금지한다.
- **[규칙] 아트가 전혀 없을 때**: 게임 ID 기반으로 브랜드 패턴과 색을 결정적(deterministic)으로 생성하고 게임명을 크게 넣는다. 깨진 이미지 아이콘은 절대 노출하지 않는다.

**제각각인 아트를 하나의 화면으로 묶는 법**

1. **틀을 통일한다**: 모든 커버가 같은 비율, 같은 반경(`game-cover-radius`), 같은 1px 내부 테두리(`border-subtle`, 아트 가장자리가 배경에 녹는 것 방지)를 쓴다.
2. **메타데이터 타이포를 통일한다**: 카드 아래 제목, 메이커, 태그의 위치와 스타일을 고정한다. 아트가 다양할수록 틀은 단순하게 한다.
3. **텍스트를 아트 위에 올리지 않는다**: 카드 제목은 아트 밖에 둔다. 상세 히어로처럼 꼭 겹쳐야 하면 하단 그라데이션 스크림(검정 0→70%)을 깔고 대비를 검사한다.
4. **대표색 추출**: 업로드 시 주조색(dominant color)을 추출해 저장하고 (a) 로딩 플레이스홀더, (b) 상세 페이지 배경 틴트(낮은 채도로), (c) 플레이 로딩 화면에 쓴다. 다양한 아트가 각자 맥락을 가지면서도 UI 토큰은 그대로 유지된다.
5. **LQIP와 반응형 이미지**: AVIF/WebP, `srcset`, `sizes`, 첫 화면 외 `loading="lazy"`, 첫 피처 이미지는 `fetchpriority="high"`.
6. **대체 텍스트**: 커버의 `alt`는 "게임명 커버 아트"를 기본으로 하고, 메이커가 설명을 덧붙일 수 있게 한다. 같은 카드 안에 제목 텍스트가 있으면 이미지가 중복 정보이므로 링크 전체의 이름을 제목으로 두고 이미지 `alt`는 짧게 한다.

### 5.2 "플레이" CTA

- **[규칙] 게임 상세에서 플레이 버튼이 화면 최상위 위계다.** 첫 화면(above the fold) 안에 둔다. 모바일에서는 하단 고정 바에 둔다(안전 영역 패딩 포함). Fitts의 법칙에 따라 크고 가까워야 한다: 높이 48–56, 모바일 전폭.
- **[규칙] 화면당 accent 솔리드 버튼은 플레이 하나뿐이다.** 찜, 공유, 신고는 ghost나 아이콘 버튼으로 둔다.
- **[규칙] 버튼 문구가 상태를 반영한다**: `플레이` → (진행 기록이 있으면) `이어하기` → (새 버전이면) `플레이 · 업데이트됨` → (로딩 중) `불러오는 중 42%` → (실패 시) `다시 시도`. 문구가 바뀌어도 버튼 폭은 유지한다.
- **[권장] 카드에서 바로 플레이**: 데스크톱 호버나 포커스 시 카드에 플레이 아이콘 버튼을 띄운다. 터치에서는 카드 탭이 상세로 가는 것을 기본으로 한다(실수로 실행하는 것 방지).
- **[규칙] 플레이 전 필요 정보는 버튼 근처에 둔다**: 플랫폼(브라우저/다운로드), 조작 방식(키보드, 마우스, 터치, 게임패드), 예상 플레이 시간, 용량, 연령과 콘텐츠 경고, 섬광 경고.
- **[규칙] 시그니처 모션**: 누름 → 70ms 눌림 → 표현적 진입 모션으로 로딩 화면. reduced motion에서는 즉시 전환 + 페이드.

### 5.3 플레이어 상태 인식(신규 vs 재방문)

- **신규(비로그인 또는 플레이 기록 없음)**
  - 홈 첫 섹션: 큐레이션된 "처음이라면 이 게임부터" 3–5개(짧은 플레이 시간, 넓은 조작 지원 위주).
  - 빈 "최근 플레이" 섹션을 **아예 보여주지 않는다**(빈 껍데기 노출 금지).
  - 가입 강요 없이 플레이 가능하게 한다. 진행을 저장해야 할 시점에 가입을 제안한다.
- **재방문**
  - 홈 첫 섹션: **이어하기 선반**(마지막 플레이 순, 진행도 표시)과 "업데이트된 게임"(찜하거나 플레이한 게임의 새 버전).
  - 마지막 방문 이후 새로 올라온 게임을 "지난 방문 이후 새로 올라온 6개"처럼 구체적으로 표시한다.
- **[규칙]** 개인화 섹션은 왜 보이는지 알려준다("○○를 플레이해서 추천").
- **메이커(MakersGround)**: 첫 게임 등록 전에는 대시보드 대신 **"첫 게임 올리기" 단계 가이드**를 보여준다. 게임을 공개한 뒤에는 지표 중심으로 전환한다.

### 5.4 콘텐츠가 적은 카탈로그를 품위 있게 다루기

출시 초기에는 게임 수가 적다. Netflix식 무한 선반을 그대로 쓰면 빈약함이 드러난다.

- **[규칙] 개수에 따라 레이아웃을 바꾼다.** 선반에 항목이 4개 미만이면 가로 스크롤 선반 대신 큰 카드 그리드나 에디토리얼 템플릿으로 바꾼다. 아이템이 1–2개인 섹션은 합치거나 숨긴다.
- **[규칙] 결과가 0인 필터나 카테고리는 노출하지 않거나 비활성 + 개수 표시를 한다.** 결과 0건 화면에 도달하게 만들지 않는다.
- **[규칙] 가짜로 채우지 않는다.** 더미 게임, 부풀린 숫자, "곧 공개" 남발 금지.
- **[권장] 깊이로 채운다**: 게임 하나하나를 크게 보여주고, 메이커 소개, 개발 로그, 패치 노트, 플레이 영상(GIF/짧은 클립), 메이커 코멘트로 상세 페이지를 풍부하게 한다. "적지만 진짜"를 콘셉트로 삼는다.
- **[권장] 앞으로의 흐름을 보여준다**: "개발 중인 게임"(메이커가 공개를 허용한 것), 다음 업데이트 일정, 메이커 모집 CTA(PlayGround → MakersGround 연결).
- **빈 상태 공식**(NN/g 3원칙): (1) 지금 상태를 알린다(로딩 중인지, 실패했는지, 정말 없는지 구분), (2) 이 기능이 무엇이고 어떻게 시작하는지 그 자리에서 가르친다, (3) 바로 행동할 경로(버튼)를 준다. 로딩 중에 "결과 없음"을 먼저 보여주지 않는다.
  - 예: 찜 목록이 비었을 때, "아직 찜한 게임이 없어요. 게임 카드의 ♡를 누르면 여기에 모여요." + `[이번 주 새 게임 보기]`

### 5.5 게임 콘텐츠 접근성

- **[규칙] 섬광 경고**: WCAG 2.3.1(초당 3회 초과 섬광 금지)은 플랫폼 UI에 적용된다. 게임 자체는 메이커가 제출 시 **섬광과 빠른 깜빡임 포함 여부**를 신고하게 하고, 해당 게임은 플레이 전 경고를 표시한다. Game Accessibility Guidelines도 기본(Basic) 단계에서 섬광과 반복 패턴을 피하라고 권한다.
- **[규칙] 접근성 기능 태그**: 메이커가 게임 등록 시 체크리스트로 선언한다. 항목은 Game Accessibility Guidelines와 Xbox Accessibility Guidelines를 참고한다: 자막, 키 재배치, 색각 이상 모드, 난이도 조절(플레이 중 변경 가능), 텍스트 크기 조절, 일시정지 가능, 한 손 플레이, 시간 제한 없음, 튜토리얼 제공, 스킵 가능한 컷신. 이 태그로 필터링할 수 있게 한다.
- **[규칙] 조작 방식 명시**: 키보드, 마우스, 터치, 게임패드 지원 여부를 아이콘 + 텍스트로 표기한다. 모바일에서 터치를 지원하지 않는 게임은 플레이 전에 명확히 알린다.
- **[규칙] 플레이어(iframe/캔버스) 프레임**:
  - 게임 프레임에 들어가고 나오는 포커스 이동이 키보드로 가능해야 한다(포커스 트랩 탈출 방법을 화면에 표시, 예: `Esc` 두 번 또는 단축키 안내).
  - 전체 화면 진입과 종료, 음소거, 일시정지 컨트롤을 플랫폼 레벨에서 제공한다.
  - 소리 자동 재생 금지. 첫 상호작용 후에 재생한다.
  - 게임 로딩 진행률을 스크린리더에 `aria-live="polite"`로 알린다(10–25% 단위로 묶어서).
- **[규칙] 미리보기 영상**: 호버 자동 재생 미리보기는 `prefers-reduced-motion`에서 끈다. 데이터 절약 모드(`Save-Data`)에서도 끈다.
- **[규칙] 연령과 콘텐츠 설명**: 폭력, 공포, 선정성 등 콘텐츠 설명어를 메이커가 선언하게 하고, 상세 페이지 플레이 버튼 근처에 표시한다.
- **[권장]** 텍스트 기반 게임 정보(조작법, 줄거리)를 이미지가 아닌 HTML 텍스트로 제공한다.

---

## 6. aDmD 디자인 체크리스트 (리뷰어용, 화면마다 적용)

> 사용법: PR이나 시안 리뷰 때 해당 화면에 적용되는 항목을 확인한다. ✗가 하나라도 있으면 사유를 기록하거나 고친다.

### A. 위계와 레이아웃

1. [ ] 이 화면의 1순위 행동이 하나이고, 흐리게 봐도(blur) 식별된다.
2. [ ] accent 솔리드 버튼이 화면에 1개 이하다.
3. [ ] 모든 간격이 간격 토큰(4px 단위 목록) 안에 있다. 임의값이 없다.
4. [ ] 묶음 안 간격이 묶음 사이 간격의 절반 이하다(근접성).
5. [ ] 긴 텍스트의 줄 길이가 한글 기준 약 45자 이내다.
6. [ ] 기본 정렬이 왼쪽이고, 가운데 정렬은 짧은 메시지와 시그니처 영역에만 쓰였다.
7. [ ] 360px 폭에서 가로 스크롤과 넘침이 없다(긴 게임명, 긴 닉네임, URL 픽스처로 확인).

### B. 타이포그래피(한글)

8. [ ] 글자 크기, 행간, 굵기가 모두 타입 토큰이다. 한 블록 안 굵기는 3단계 이하다.
9. [ ] 본문 읽기 행간이 1.6 이상이고, UI 한 줄 텍스트는 짝 행간 토큰을 쓴다.
10. [ ] `word-break: keep-all` + `overflow-wrap` 안전장치가 적용돼 어절이 중간에서 끊기지 않는다.
11. [ ] 제목에 `text-wrap: balance`가 적용돼 한 어절만 남는 줄이 없다.
12. [ ] 점수, 순위, 통계 숫자가 `tabular-nums`이고, 큰 수는 한국식 단위나 쉼표를 쓴다.
13. [ ] 디스플레이 서체가 Z2(시그니처) 또는 지정된 헤드라인에만 쓰였고, 사용자 입력 텍스트에는 쓰이지 않았다.
14. [ ] 장식용 영어 레이블이 없다(고유명사 제외).

### C. 색과 테마

15. [ ] 화면 코드에 원시(primitive) 색 토큰이나 HEX를 직접 쓰지 않았다(의미 토큰만).
16. [ ] 라이트와 다크 양쪽에서 텍스트 4.5:1(큰 글자 3:1), 비텍스트 UI 3:1을 통과한다.
17. [ ] 색만으로 상태를 전달하지 않는다(아이콘이나 텍스트 병기).
18. [ ] PlayGround와 MakersGround의 `data-site`를 바꿔도 깨지지 않는다(accent 토큰만 교체됨).
19. [ ] 보라~인디고 그라데이션, 장식용 그라데이션, 글로우가 없다(게임 아트 내부 제외).

### D. 컴포넌트와 상태

20. [ ] 모든 인터랙티브 요소에 hover, focus-visible, active, disabled 상태가 있다.
21. [ ] 포커스 링이 2px 이상, 대비 3:1 이상이고, 스티키 헤더나 하단 바에 가려지지 않는다.
22. [ ] 타깃 크기가 최소 24×24이고, 모바일 주요 타깃은 44px 이상이다.
23. [ ] 비활성 요소는 비활성 이유를 알려준다.
24. [ ] 데이터 영역에 loading, empty, error 상태가 모두 설계돼 있다.
25. [ ] 로딩 중에 "결과 없음"이 먼저 깜빡이지 않는다.
26. [ ] 빈 상태가 상태 설명 + 기능 안내 + 행동 버튼, 이 세 가지를 갖췄다.
27. [ ] 오류 메시지가 원인과 해결 방법을 구체적으로 말하고, 재시도 경로가 있다.
28. [ ] 폼 라벨이 항상 보이고, 오류가 필드 아래에 `aria-describedby`로 연결된다.
29. [ ] 아이콘만 있는 버튼에 `aria-label`이 있고, 이모지를 UI 아이콘으로 쓰지 않았다.

### E. 모션

30. [ ] 모든 전환이 duration과 easing 토큰을 쓴다. 퇴장이 진입보다 짧다.
31. [ ] `prefers-reduced-motion`에서 이동, 확대, 시차, 자동 재생 미리보기가 페이드나 정지로 대체된다.
32. [ ] 스크롤 연동 장식 애니메이션(섹션 fade-up)이 없다.
33. [ ] 사용자가 애니메이션 종료를 기다리지 않고 바로 조작할 수 있다.

### F. 이미지와 게임 콘텐츠

34. [ ] 모든 이미지에 고정 `aspect-ratio`와 플레이스홀더(대표색 또는 LQIP)가 있다(CLS 없음).
35. [ ] 커버 아트가 규격 비율과 초점에 맞게 크롭되고, 아트 누락 시 브랜드 폴백이 나온다(깨진 이미지 없음).
36. [ ] 카드 제목이 아트 위가 아닌 아트 밖에 있다. 겹칠 경우 스크림과 대비 검사를 했다.
37. [ ] 게임 상세에서 플레이 버튼이 첫 화면 안에 있고(모바일은 하단 고정), 상태별 문구(플레이/이어하기/로딩/재시도)가 있다.
38. [ ] 플레이 버튼 근처에 조작 방식, 플랫폼, 콘텐츠와 섬광 경고, 접근성 기능 태그가 있다.
39. [ ] 신규 사용자에게 빈 개인화 섹션(최근 플레이 등)이 노출되지 않는다.
40. [ ] 항목이 4개 미만인 선반이 가로 스크롤로 표시되지 않는다. 결과 0건 필터가 노출되지 않는다.
41. [ ] 게임 프레임에 키보드로 들어가고 나올 수 있고, 소리가 자동 재생되지 않는다.

### G. "AI 느낌"과 작가성

42. [ ] 이 화면에서 **다른 사이트로 그대로 옮겨도 말이 되는 문장**이 없다(카피 구체성 테스트).
43. [ ] 가짜이거나 검증할 수 없는 숫자, 후기, 별점이 없다.
44. [ ] 모든 카드가 같은 반경, 같은 그림자, 같은 높이가 아니다. 종류별 형태 차이가 의도돼 있다.
45. [ ] 섹션 템플릿이 연속으로 반복되지 않고, 밀도 리듬이 교차한다.
46. [ ] 스톡풍 3D나 아이소메트릭 일러스트, 범용 AI 일러스트가 없다. 이미지는 실제 게임, aDmD 캐릭터, 브랜드 모티프다.
47. [ ] 화면당 시그니처 요소가 최대 1개이고, Z0(코어) 화면에는 없다.
48. [ ] 실제 콘텐츠(가장 긴, 가장 짧은, 아트 없는 게임 포함)로 검증한 스크린샷이 PR에 첨부돼 있다.

---

## 출처

**디자인 시스템과 공식 가이드**

- [Atlassian Design: Design tokens](https://atlassian.design/foundations/tokens/design-tokens)
- [GitHub Primer: Token names](https://primer.style/foundations/primitives/token-names)
- [GitHub Primer: @primer/primitives DESIGN_TOKENS_SPEC](https://unpkg.com/@primer/primitives@11.10.0/DESIGN_TOKENS_SPEC.md)
- [IBM Carbon: Spacing overview](https://carbondesignsystem.com/elements/spacing/overview/)
- [IBM Carbon: Motion overview](https://carbondesignsystem.com/elements/motion/overview/)
- [IBM Carbon: Empty states pattern](https://carbondesignsystem.com/patterns/empty-states-pattern/)
- [IBM Carbon: Loading pattern](https://carbondesignsystem.com/patterns/loading-pattern)
- [Material Design blog: Tone-based surface color in M3](https://material.io/blog/tone-based-surface-color-m3)
- [Android Developers: Color roles and tokens](https://developer.android.com/design/ui/wear/guides/styles/color/roles-tokens)
- [Flutter: New ColorScheme roles for Material 3](https://docs.flutter.dev/release/breaking-changes/new-color-scheme-roles)
- [Google Design: Expressive Material Design research](https://design.google/library/expressive-material-design-google-research)
- [Google Research: Usability Hasn't Peaked (expressive design)](https://research.google/pubs/usability-hasnt-peaked-exploring-how-expressive-design-overcomes-the-usability-plateau/)
- [Dezeen: Google ushers in age of expressive interfaces (2025-05-28)](https://dezeen.com/2025/05/28/google-ushers-in-age-of-expressive-interfaces-with-material-design-update/)
- [Apple HIG: Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
- [Apple App Store Connect: Reduced motion evaluation criteria](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria)
- [당근 SEED Design: GitHub](https://github.com/daangn/seed-design)
- [당근 SEED Design: Color foundation (llms.txt)](https://seed-design.io/llms/foundations/color.txt)
- [당근 SEED Design: Typography foundation (llms.txt)](https://seed-design.io/llms/foundations/typography.txt)
- [@seed-design/design-token 패키지 개요 (socket.dev)](https://socket.dev/npm/package/@seed-design/design-token/overview/1.0.0)
- [토스피드: 서체 고민 없이 본질에만 집중할 수 있도록 (Toss Product Sans)](https://toss.im/tossfeed/article/beginning-of-tps)
- [Apps in Toss: TDS 컴포넌트](https://developers-apps-in-toss.toss.im/design/components)
- [Tailwind CSS: Theme variables](https://tailwindcss.com/docs/theme)
- [Tailwind CSS v4.0 발표](https://tailwindcss.com/blog/tailwindcss-v4)

**접근성**

- [W3C: What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)
- [W3C: Understanding Target Size (Minimum) 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum)
- [WebAIM: WCAG 2.2 overview](https://webaim.org/standards/wcag/wcag22)
- [web.dev: Animation and motion (accessibility)](https://web.dev/learn/accessibility/motion)
- [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/)
- [Microsoft: Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/guidelines)

**UX 리서치와 원칙**

- [Nielsen Norman Group: Designing Empty States in Complex Applications](https://www.nngroup.com/articles/empty-state-interface-design/)
- [Nielsen Norman Group: Skeleton Screens 101](https://nngroup.com/articles/skeleton-screens/)
- [Nielsen Norman Group: Skeleton Screens vs. Progress Bars vs. Spinners (video)](https://www.nngroup.com/videos/skeleton-screens-vs-progress-bars-vs-spinners/)
- [Baymard Institute: Line length readability](https://baymard.com/blog/line-length-readability)
- [Laws of UX](https://lawsofux.com/)
- [Refactoring UI (Adam Wathan & Steve Schoger)](https://www.refactoringui.com/)
- [Rauno Freiberg: Invisible Details of Interaction Design](https://rauno.me/craft/interaction-design)

**한글 서체, 라이선스, 웹 타이포그래피**

- [Pretendard GitHub](https://github.com/orioncactus/pretendard)
- [Pretendard README (English, v1.3.9)](https://cdn.jsdelivr.net/npm/pretendard@1.3.9/docs/en/README.md)
- [SUIT GitHub (sun-typeface)](https://github.com/sun-typeface/SUIT)
- [Wanted Sans GitHub](https://github.com/wanteddev/wanted-sans)
- [Design Compass: Wanted Sans](https://designcompass.org/en/2023/11/14/wanted-sans/)
- [Spoqa Han Sans GitHub](https://github.com/spoqa/spoqa-han-sans)
- [Spoqa Han Sans: cdnjs (라이선스 표기)](https://cdnjs.com/libraries/spoqa-han-sans)
- [산돌구름: Paperlogy](https://www.sandollcloud.com/free-font/21071/Paperlogy)
- [산돌구름: Gmarket Sans](https://www.sandollcloud.com/free-font/15744/Gmarket-Sans)
- [산돌구름: 여기어때 잘난체](https://www.sandollcloud.com/free-font/772/Jalnan)
- [Fontsource: Black Han Sans](https://fontsource.org/fonts/black-han-sans/about)
- [SIL Open Font License FAQ](https://openfontlicense.org/ofl-faq/)
- [Google Developers Blog: Google Fonts launches Korean support](https://developers.googleblog.com/en/google-fonts-launches-korean-support/)
- [Google Developers Blog: Google Fonts launches Japanese support (한국어 슬라이싱 방식 설명 포함)](https://developers.googleblog.com/google-fonts-launches-japanese-support/)
- [web.dev: Reduce web font size](https://web.dev/articles/reduce-webfont-size)
- [W3C: Requirements for Hangul Text Layout and Typography (klreq)](https://www.w3.org/TR/klreq/)
- [MDN: word-break](https://developer.mozilla.org/docs/Web/CSS/Reference/Properties/word-break)
- [MDN: text-wrap-style](https://developer.mozilla.org/docs/Web/CSS/Reference/Properties/text-wrap-style)
- [Chrome for Developers: CSS text-wrap: balance](https://developer.chrome.com/docs/css-ui/css-text-wrap-balance)
- [WebKit: Better typography with text-wrap pretty](https://webkit.org/?p=16547)
- [Dale Seo: 어색하게 끊기는 한국어 줄바꿈 다듬는 법](https://daleseo.com/css-text-wrap/)
- [velog: 있어보는 Web을 위한 타이포그라피 10](https://velog.io/@hyounglee/typography-for-web-10)

**"AI 느낌"과 크래프트**

- [Kosta Canatselis: Spot the slop, a UI designer's guide to fixing AI defaults](https://world.hey.com/kostac/spot-the-slop-a-ui-designer-s-guide-to-fixing-ai-defaults-4c448c9c)
- [DEV: How to fix the AI-generated look in your frontend](https://dev.to/alanwest/how-to-fix-the-ai-generated-look-in-your-frontend-1ahh)
- [DEV: Why every AI-built website looks the same (Tailwind indigo-500)](https://dev.to/alanwest/why-every-ai-built-website-looks-the-same-blame-tailwinds-indigo-500-3h2p)
- [Brafton: We've seen this website before](https://www.brafton.com/blog/graphics/weve-seen-this-website-before-ai-design-and-development/)
- [UX Collective: AI-generated UI is fast design, not UX](https://uxdesign.cc/ai-generated-ui-is-fast-design-not-ux-855ca8abcd28)
- [Built In: AI makes bad design look good enough](https://builtin.com/articles/ai-design-slop-era)
- [Designlab: Design craft in an AI-powered world (2025)](https://designlab.com/blog/design-craft-in-an-ai-powered-world)
- [ZURB Radar: Your AI ships fast, it can't tell you what's worth shipping](https://radar.zurb.com/article/your-ai-ships-fast-it-cant-tell-you-whats-worth-shipping)

**게임 플랫폼 에셋**

- [Steamworks: Store graphical assets](https://partner.steamgames.com/doc/store/assets)
- [Steamworks: Standard assets](https://partner.steamgames.com/doc/store/assets/standard)
- [Steamworks: Graphical asset rules](https://partner.steamgames.com/doc/store/assets/rules)
- [Steamworks: Library assets](https://partner.steamgames.com/doc/store/assets/libraryassets)
- [Steam Page Analyzer: Steam capsule sizes (제3자)](https://www.steampageanalyzer.com/blog/steam-capsule-sizes)
- [itch.io 커뮤니티: 커버 이미지 권장 크기 630×500](https://itch.io/post/2289750)
- [itch.io: Itch page image guide and templates (제3자)](https://hedgiespresso.itch.io/itch-page-image-templates)
