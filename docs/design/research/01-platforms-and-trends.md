# 01. 게임 플랫폼 경쟁 분석 & 2025–2026 웹 디자인 트렌드

- 작성일: 2026-11-26
- 대상: aDmD Games (PlayGround = 플레이어용, MakersGround = 메이커용) 디자인 방향 수립
- 방법: 2025–2026년 기사, 공식 블로그/문서, 개발자 포럼, 리뷰 사이트(Trustpilot, Common Sense Media 등) 웹 검색 및 본문 확인. 모든 사실 근거는 마지막 "출처" 섹션에 링크.
- 주의
  - 각 사이트의 화면 구조(홈, 상세 페이지 구성 요소) 설명 중 일부는 이 분야에서 널리 알려진 구조를 정리한 것이고, 숫자, 날짜, 정책처럼 시간에 따라 바뀌는 사실은 출처가 있는 것만 적었다.
  - 회사가 직접 의뢰한 설문(예: Poki 리포트)이나 마케팅 블로그 성격의 트렌드 글은 편향 가능성을 본문에 표시했다.
  - Reddit 스레드는 이번 검색 도구로 거의 잡히지 않아, 사용자 불만은 itch.io 포럼, Roblox DevForum, Trustpilot, Common Sense Media, 언론 보도에서 가져왔다.

---

## 0. 핵심 요약 (먼저 읽을 것)

1. **카탈로그 경쟁은 이미 끝났다.** Poki는 손으로 심사한 약 1,700개 게임, itch.io는 약 177만 개 페이지, Steam은 2025년 한 해 2만 개 이상 출시. aDmD가 이길 수 있는 축은 "양"이 아니라 **신뢰(사람이 고른다), 마찰 없는 플레이, 메이커의 얼굴, 한국어 맥락**이다.
2. **2026년 하반기 최대 이슈는 AI 생성 게임 범람.** itch.io의 하루 신규 페이지가 2개월 만에 3천 → 6천으로 두 배가 됐지만 다운로드와 구매는 늘지 않았다. 자발적 AI 표시 필터는 오래된 게임까지 숨겨 사실상 작동하지 않는다. "사람이 만들었고, 사람이 골랐다"를 증명하는 UI가 차별점이 된다.
3. **브라우저 게임 포털(Poki, CrazyGames)의 최대 불만은 광고.** 플레이어 리뷰에서 반복되는 1순위 불만이다. aDmD는 광고 없는 플레이를 기본값으로 두고 메이커 후원을 붙이면, 그것만으로 포지셔닝이 분명해진다.
4. **한국 내 실질 경쟁자는 STOVE가 아니라 "앱인토스(토스 미니앱 게임)"일 수 있다.** HTML5 게임 메이커를 적극 모집하고 있고, 신작 2주 노출 구좌와 또래 기반 추천을 이미 운영한다. 다만 메이커 정체성과 커뮤니티는 없다. aDmD가 들어갈 자리가 바로 여기다.
5. **잼 생태계에 빈자리가 생긴다.** Ludum Dare는 2028년 10월 LD64를 끝으로 이름을 내린다. 한국어 상시 잼 플랫폼은 사실상 없다. MakersGround의 잼은 핵심 무기가 될 수 있다.
6. **디자인은 "사람 손맛 + 살아있는 마스코트 + 플랫폼 기술(View Transitions / 스크롤 기반 애니메이션)" 조합을 권장한다.** Linear풍 다크+보라 그라데이션, 히어로 벤토 그리드, Y2K 크롬/픽셀 클리셰, 글래스모피즘은 피한다. 지금은 너무 흔해서 어디서 본 듯한 사이트가 된다.

---

# Part A. 경쟁 플랫폼 분석

## A-0. 분석 프레임

각 플랫폼은 아래 8개 항목으로 본다.

| 항목 | 질문 |
|---|---|
| 대상 | 누구를 위한 곳인가 (플레이어 / 메이커 / 둘 다) |
| 홈·발견 구조 | 첫 화면과 탐색 동선은 어떻게 짜여 있나 |
| 상세 페이지 | 게임 페이지에 무엇이 어떤 순서로 있나 |
| 플레이 방식 | "지금 플레이"를 누르면 무슨 일이 일어나나 |
| 메이커 혜택 | 수익, 도구, 노출, 데이터 |
| 정체성·톤 | 시각적 인상과 브랜드 성격 |
| 강점 | 배울 것 |
| 약점·불만 | 실제 사용자/개발자 불만 |

---

## A-1. itch.io

- **대상**: 인디 메이커 중심, 플레이어는 그다음. 사실상 인디/실험 게임의 기본 저장소.
- **홈·발견 구조**: 피처드 게임, 인기/신작 목록, 태그와 장르, 가격(무료/유료), 플랫폼(웹/Windows 등) 필터로 된 그리드. 로그인 사용자용 추천 영역이 있지만 눈에 잘 띄지 않는다는 포럼 의견이 있다. 잼, 데브로그, 컬렉션이 별도 축으로 존재.
- **상세 페이지**: 메이커가 CSS 수준까지 색과 배경을 커스터마이즈할 수 있는 단일 컬럼 페이지. 스크린샷, 설명, 다운로드/웹 플레이 영역, "More information"(상태, 플랫폼, 평점, 작성자, 태그, 사용 도구) 접이식 테이블, 데브로그, 댓글. 페이지마다 생김새가 크게 달라 일관성은 낮지만 메이커 개성은 최대.
- **플레이 방식**: HTML5 빌드(ZIP)를 올리면 페이지 안 iframe에 임베드되고, "Run game" 클릭 후 실행. 전체화면 버튼 제공. 심사 없이 공개 가능.
- **메이커 혜택**: 가격 자유 설정(무료, 최소가, 원하는 만큼 지불), 플랫폼 수수료 비율도 메이커가 정할 수 있음, 잼 개최, 데브로그, 번들, 분석. 트래픽은 메이커가 직접 끌어와야 한다는 점이 단점으로 자주 지적된다.
- **정체성·톤**: 기능 위주의 담백한 회색/흰 UI, 빨간 로고. 플랫폼은 조용하고 게임 페이지가 각자 떠드는 구조.
- **강점**: 진입 장벽이 가장 낮음, 메이커 커스터마이징, 잼 인프라의 사실상 표준(수천 개 잼, GMTK 같은 초대형 잼 운영).
- **약점·불만 (2025–2026)**
  - 2026년 8월에서 10월 사이 하루 신규 페이지가 약 3천에서 6천 이상으로 늘었지만 다운로드와 구매는 늘지 않았다고 itch.io가 직접 밝혔다. 원인은 생성형 AI로 추정된다.
  - 전체 약 177만 개 리스팅 중 "AI 생성" 자진 표시는 약 7.5%뿐. "No AI" 필터를 켜면 약 43만 개만 남아, AI 질문이 생기기 전 게임까지 130만 개 넘게 숨겨진다. 필터가 사실상 망가진 셈이다. 2026-11-03에는 AI 공개 필터를 검색 결과까지 확대하고 대량의 스팸을 삭제했다.
  - 2025년 7월 결제사 압력으로 성인 콘텐츠를 탐색/검색에서 내렸다가(deindex) 무료 콘텐츠부터 다시 올렸다. 소통 부족과 "항소 불가" 규정이 신뢰를 흔들었다는 비판이 있다.
  - 포럼 불만: 검색이 제목만 찾고 태그는 못 찾음, 탐색이 인기순이라 개인화된 느낌이 없음, 지원 티켓에 약 50일 무응답 사례.
- **aDmD 시사점**: itch.io의 "누구나 올림"은 AI 시대에 발견을 망가뜨린다. 반대로 aDmD는 **적게, 확인해서, 사람이 보증하는** 쪽으로 가야 한다. AI 사용 공개는 선택이 아니라 필수 입력 필드로.

## A-2. Steam 스토어 (웹)

- **대상**: PC 게이머 대중 + 모든 규모의 개발사.
- **홈·발견 구조**: 대형 캐러셀(피처드 & 추천), 할인/이벤트, 카테고리, 큐레이터, 디스커버리 큐, 위시리스트 기반 추천. 2026년 홈 리프레시(4월 1일 베타 공개, 6월 무렵 정식 확산)로 디스커버리 큐가 별도 화면이 아니라 홈 안에 들어오고, 하단 무한 스크롤 추천, 더 큰 아트워크, 마우스오버 상세 정보, 트레일러 컨트롤이 추가됐다. 더 넓고 반응형이 되었고 Steam Deck/Big Picture에도 반영.
- **상세 페이지**: 트레일러+스크린샷 캐러셀, 짧은 설명, 리뷰 요약(긍정 비율 라벨), 출시일, 개발/배급사, 사용자 태그, 구매 박스, 긴 설명, 시스템 사양, 큐레이터/리뷰 목록. 사실상 업계 표준 해부도.
- **플레이 방식**: 웹에서는 플레이 불가. 구매/설치 후 클라이언트에서 실행. 데모는 Next Fest를 통해 대량 노출.
- **메이커 혜택**: 압도적 트래픽, 위시리스트, Next Fest, 업적/트레이딩카드/클라우드 저장 등 플랫폼 기능.
- **정체성·톤**: 짙은 남색/청회색 다크 UI, 정보 밀도 높음. 상점이자 데이터베이스.
- **강점**: 리뷰 요약 라벨, 사용자 태그, 위시리스트라는 "나중에" 장치, 페이지 구조의 예측 가능성.
- **약점·불만**
  - 홈 리프레시에서 "인기 예정작" 섹션이 인디 노출을 오히려 줄일 수 있다는 비판(PCGamesN).
  - Next Fest는 이미 위시리스트가 많은 게임만 더 키운다는 개발자 설문 결과(2025년 2월, 208명). 2026년 10월 Next Fest에는 데모 약 7천 개, 그중 34.4%가 생성형 AI 사용을 공개. Valve도 저품질 게임이 너무 많이 노출된다는 점을 인정했다(2026년 Steam Indie Connect, 한국).
  - 2025년 출시작 2만 개 이상이라는 2차 자료도 있다(검증 필요).
- **aDmD 시사점**: 상세 페이지 해부도(미디어 → 한 줄 요약 → 평판 → 태그 → 행동 버튼)는 표준으로 차용한다. 다만 "인기가 인기를 부르는" 구조는 의도적으로 깨야 한다.

## A-3. Poki

- **대상**: 설치 없이 바로 노는 캐주얼 플레이어(학생 비중 큼), HTML5 게임 스튜디오.
- **홈·발견 구조**: 크기가 다른 정사각 타일이 빽빽한 모자이크 그리드. 마우스오버 시 짧은 영상 미리보기. 카테고리 태그, 최근 플레이, 추천. 에디토리얼 판단과 개인화 추천을 함께 쓴다.
- **상세 페이지**: 게임이 곧 페이지. 큰 iframe 플레이 영역이 첫 화면을 차지하고, 아래로 설명, 조작법, 관련 게임 타일이 이어진다.
- **플레이 방식**: 다운로드, 설치, 계정 없이 시작. 로그인은 선택. 몇 초 안에 플레이 가능해야 한다는 원칙. 점진적 로딩과 작은 용량을 중시하고 SDK가 이를 지원. 기기 간 저장(선택).
- **메이커 혜택**: 광고 수익 공유(타이틀별 협상, 공개된 고정 비율 없음), 비독점 라이선스 일시금 옵션, 광고 미디에이션, 플레이어 인사이트, 기술 최적화 지원. 2025년에 손으로 심사해 최종 출시한 게임은 227개뿐이라 진입이 어렵다. 2025년에 1백만 플레이를 넘긴 게임은 1,018개.
- **정체성·톤**: 밝은 하늘색 배경, 둥근 타일, 장난스러운 로고. 아이들이 쓰기 쉬운 "놀이터" 톤. 월 1억 플레이어, 600곳 이상 개발 파트너. 2025 Dutch Game Awards 수상.
- **강점**: 무마찰 플레이의 기준점. 타일 호버 영상. 엄격한 큐레이션으로 지켜지는 평균 품질.
- **약점·불만**
  - Trustpilot(2025년 말 – 2026년 초)과 Common Sense Media 부모/아이 리뷰에서 1순위 불만은 과도한 광고. 그다음은 렉, 연령에 맞지 않는 콘텐츠, 엉뚱한 검색 결과.
  - 개발자 포럼에서도 "Poki에 올리면서 광고가 많이 들어갔다"는 이야기가 나온다. Poki 측은 광고가 무료 플레이와 개발자 수익을 떠받친다는 입장이고, 광고 없는 kids.poki.com을 따로 운영한다.
- **참고 데이터 (Poki 의뢰 설문, 2026년 5월, 미국/영국 게이머 2,000명)**: 가장 흔한 웹 게이머는 하루 여러 번, 한 번에 11–20분, 한 세션에 2–3개 게임을 한다. 90%가 다른 일을 하며 플레이. 46%가 로딩이 느려서 모바일 게임을 그만둔 적이 있다. 62%가 웹에서 먼저 해보고 게임을 사거나 내려받은 경험이 있다. (회사 의뢰 조사라 편향 가능성 있음)
- **aDmD 시사점**: 무마찰 플레이(계정 없이 3초 안에 시작)는 따라 해야 할 기준. 반대로 광고는 aDmD가 이길 수 있는 지점이다.

## A-4. CrazyGames

- **대상**: Poki와 비슷한 캐주얼 웹 플레이어, 웹 게임 개발자. 소셜/멀티플레이 쪽으로 이동 중.
- **홈·발견 구조**: 왼쪽 세로 카테고리 사이드바 + 가로 스크롤 줄(신작, 인기, 장르별)로 된 다크 테마 그리드. 썸네일 호버 영상.
- **상세 페이지**: 큰 플레이 프레임, 그 아래 설명, 조작법, 출시일, 기술(엔진), 평가(좋아요/싫어요), 관련 게임.
- **플레이 방식**: 즉시 iframe 플레이. 친구 기능(Friends Connect)으로 친구를 찾아 추가하고, "Playing Right Now"에서 친구가 무엇을 하는지 보고, 한 번 클릭으로 친구 게임에 합류. 프로필에 이름, 게임 통계, 연속 플레이(스트릭).
- **메이커 혜택**: 개발자 포털에서 직접 제출 → Basic Launch(제한된 초기 노출로 데이터 검증) → Full Launch(SDK 완전 연동, QA 통과 후 수익 배분 시작). Full Launch 선정은 CrazyGames의 편집/품질/성과 판단에 달려 있음. 광고는 CrazyGames SDK를 통한 것만 허용. 일반 수익 배분율은 공개 문서에 명시되지 않음(2026 GameMaker 웹 잼 조건으로 광고 60%, 인앱결제 70%라는 3차 자료가 있음).
- **정체성·톤**: 어두운 보라/남색 배경에 네온 포인트. 게이머스러운 "아케이드" 톤.
- **강점**: Basic → Full 단계형 출시(작게 시험하고 데이터로 승격)는 메이커에게 공정해 보이는 구조. 친구 합류 1클릭.
- **약점·불만**: Trustpilot(2025년 4월 – 2026년 3월)에서 광고가 게임보다 많다, 1분도 못 하고 광고가 뜬다는 불만이 반복된다. 회사도 항상 맞는 균형은 아니라고 인정. itch.io의 한 개발자는 CrazyGames 연동이 전체화면을 막고 게임을 방해하는 광고를 넣었다고 썼다. 개발자 쪽에서는 광고 수익이 기대보다 적다는 불만.
- **aDmD 시사점**: "단계형 출시"(작은 테스트 노출 → 데이터 기반 승격)는 MakersGround 릴리스 파이프라인에 그대로 응용 가능하다. 친구 합류는 PlayGround 2차 기능 후보.

## A-5. Game Jolt

- **대상**: 10대 중심의 인디 플레이어/크리에이터 커뮤니티(팬게임, 공포게임, FNaF 계열 문화가 강함).
- **홈·발견 구조**: 게임 스토어보다 SNS 피드에 가깝다. 포스트, 커뮤니티, 크리에이터 중심 피드에 게임이 섞여 있음.
- **상세 페이지**: 게임 페이지 + 데브로그성 포스트 피드 + 커뮤니티. 다운로드형이 많고 웹 빌드도 지원.
- **플레이 방식**: 다운로드 또는 브라우저 플레이. 게임 API로 트로피(업적), 점수표, 데이터 저장 제공. 트로피는 사용자 경험치(EXP)를 준다.
- **메이커 혜택**: 크리에이터 프로그램. 사용자가 일일 퀘스트로 충전한 "차지드 스티커"를 크리에이터 포스트에 붙이면 광고 수익 일부가 크리에이터에게 간다. 퀘스트 코인으로 스티커 팩 구매.
- **정체성·톤**: 검정 바탕에 형광 초록/분홍, 스티커와 이모트를 마구 붙이는 장난스러운 10대 감성.
- **강점**: 플레이어 행동(퀘스트, 스티커)이 곧 크리에이터 후원이 되는 경제 구조. 플랫폼 공통 트로피.
- **약점·불만**: 2022년 성인 콘텐츠 금지 때 성적 내용이 없는 게임까지 내려갔고, 회사도 개발자에게 이전할 기회를 주지 않았다고 인정했다. 라이브 기능 Firesides는 2023년 10월 종료. 2025–2026년 이용 지표에 대한 신뢰할 만한 보도는 찾지 못했다(정체 상태로 추정만 가능).
- **aDmD 시사점**: "플레이어의 가벼운 행동이 메이커에게 실질적 보상이 되는" 고리는 강력하다. 다만 스티커 남발 같은 시각적 소음은 피하고, 정책 변경 시 이전 기간을 보장하는 원칙을 처음부터 문서화해야 한다.

## A-6. Newgrounds

- **대상**: 1995년부터 이어진 게임/애니메이션/음악/아트 창작 커뮤니티. 플래시 시대의 상징.
- **홈·발견 구조**: 포털별(게임, 영상, 오디오, 아트) 프론트 페이지, 운영자/커뮤니티 추천, 주간/일간 상위작, 시즌 이벤트(Madness Day, Halloween Spooktacular 등 연례 행사).
- **상세 페이지**: 플레이 영역, 작가 정보, 5점 별점, 리뷰(작성자 코멘트), 메달/점수표, 관련 작품.
- **플레이 방식**: 브라우저 임베드(플래시 이후 HTML5와 Ruffle 에뮬레이션). 메달(업적)과 점수표 API.
- **메이커 혜택**: 커뮤니티 심사(새 제출물을 사용자들이 투표로 살리거나 내리는 "Judgment" 문화), 광고 수익 일부 공유, 연례 이벤트 노출.
- **정체성·톤**: 진한 주황, 탱크 로고, 거칠고 소란스러운 2000년대 웹 감성. 25년 넘게 유지된 "모든 것을, 모두가" 정신.
- **강점**: 강한 정체성과 역사, 연례 이벤트 문화, 커뮤니티가 직접 품질을 거르는 구조.
- **약점·불만**: 오래된 UI, 광고 수익 감소와 트래픽 정체 속 재정 압박(서포터 연간 구독으로 광고 제거). 2025–2026년 포털 구조 개편에 대한 보도는 찾지 못했다.
- **aDmD 시사점**: 연례/시즌 이벤트(예: "DmD의 날")와 커뮤니티 판정 같은 의식(ritual)이 정체성을 만든다.

## A-7. Kongregate / Armor Games (참고용, 현재는 레거시)

- **Kongregate**: 2020년 7월 플래시 종료와 함께 신규 게임 접수와 신규 배지 추가를 중단하고 포럼/채팅을 축소했다. 기존 약 12.8만 개 게임은 유지. 2024년 Monumental이 인수. 사실상 아카이브 모드.
  - 배울 점: 전성기 Kongregate의 핵심은 **플랫폼 공통 배지(업적)와 계정 레벨**이었다. 게임 사이를 오가게 만드는 메타 진행이 있었고, 이 계층은 지금 웹 포털에서 사라졌다.
- **Armor Games**: 포털은 큐레이션된 HTML5/브라우저 게임을 계속 호스팅하지만, 회사 무게중심은 Steam/콘솔 퍼블리싱(Armor Games Studios)으로 이동. 2026년에도 Steam 신작과 GemCraft 컬렉션 출시. 2025–2026년 포털 신규작에 대한 보도는 찾지 못했다.
- **aDmD 시사점**: "플랫폼 공통 업적/레벨"이라는 빈자리. 웹 포털 중 지금 이걸 제대로 하는 곳이 거의 없다.

## A-8. Playdate Catalog (Panic)

- **대상**: Playdate 소유자. 매우 작은 시장이지만 디자인적으로 가장 참고할 만하다.
- **홈·발견 구조**: 웹(play.date/games)과 기기 내 스토어 두 버전. 웹은 All Games, Staff Picks, Quick Plays, 장르 탭, 시즌 섹션으로 구성. 격주로 새 게임 "드롭". Season Two는 2025년 5월 29일 시작, 몇 달에 걸쳐 12개 게임을 주 단위로 공개.
- **상세 페이지**: 웹은 기기의 1비트 제약이 없어서, 게임마다 더 풍부한 페이지(설명, 이미지, 제작자)를 갖는다. 기기 화면 해상도를 존중한 흑백 그래픽과 웹의 넓은 레이아웃이 공존.
- **플레이 방식**: 구매 후 기기로 무선 전송. 웹 플레이 없음.
- **메이커 혜택**: Panic의 손 큐레이션, 시즌/드롭 형태의 이벤트성 노출. 출시 첫해 15만 개 이상 판매, 개발자 매출 50만 달러 이상(Panic 공개).
- **정체성·톤**: 노란 기기색 + 1비트 흑백, 손글씨 같은 장난기, 출시 크레딧에 디자이너 이름까지 표기하는 장인 정신.
- **강점**: "작고, 사람이 고르고, 정기적으로 도착한다"는 리듬. 시즌제는 기다림 자체를 이벤트로 만든다. Quick Plays처럼 플레이 길이로 묶는 분류.
- **약점**: 카탈로그가 작고 검색/필터가 단순. 플랫폼이 Playdate에 묶여 있음.
- **aDmD 시사점**: 1인 운영 플랫폼에 가장 잘 맞는 모델. "매주 목요일 N개 드롭", "플레이 시간별 분류(5분 / 20분 / 저녁 하나)"를 그대로 차용할 만하다.

## A-9. GOG

- **대상**: DRM 없는 소유, 고전 게임 보존을 중시하는 PC 게이머.
- **홈·발견 구조**: 할인/신작/추천 캐러셀, 장르, "Good Old Games" 고전 큐레이션, 보존 프로그램 배지.
- **상세 페이지**: Steam과 비슷한 해부도 + DRM-free 표시, 보존 상태 같은 GOG 고유 속성.
- **플레이 방식**: 오프라인 설치 파일 직접 다운로드 또는 GOG Galaxy 런처. 웹 플레이 없음.
- **메이커 혜택**: 큐레이션 입점, 보존 프로그램.
- **정체성·톤**: 진한 보라 + 흰색, "소유"와 "보존"이라는 명확한 가치.
- **최근 변화**: 2025년 12월 29일 공동창업자 Michał Kiciński가 CD Projekt로부터 GOG를 약 2,500만 달러에 인수해 독립. DRM-free와 보존을 유지하고 2026–2027년 보존 이니셔티브를 확대하겠다고 밝혔다. 새 오너는 Steam이 사용 편의성으로 이기고 있다고 인정하면서도 정면 대결 대신 GOG의 핵심 가치를 강화하겠다는 입장.
- **aDmD 시사점**: 작은 플랫폼은 **가치 한 줄**(GOG = DRM-free 소유)로 기억된다. aDmD도 한 줄 가치가 필요하다(예: "광고 없이, 사람이 만든 게임을, 바로").

## A-10. Epic Games Store (웹)

- **대상**: PC 게이머, 대형/중형 개발사. 매주 무료 게임으로 사용자 확보.
- **홈·발견 구조**: 대형 히어로 캐러셀, 무료 게임 섹션, 할인, 장르 줄. 큰 키 아트 중심.
- **상세 페이지**: 키 아트, 트레일러, 평점, 태그, 가격 박스. Steam보다 정보 밀도가 낮고 시각 비중이 크다.
- **플레이 방식**: 런처 설치 필요. 웹 플레이 없음.
- **메이커 혜택**: 2025년 6월부터 앱당 연 매출 첫 100만 달러까지 수수료 0%, 이후 12%. 개발자가 직접 운영하는 웹숍(Epic이 호스팅) 지원, 웹숍 구매에도 Epic 리워드 5% 적립.
- **정체성·톤**: 검정 바탕 + 대형 아트, 극장형 쇼케이스.
- **약점**: 커뮤니티/소셜 기능 부족, "무료 게임 받으러만 가는 곳"이라는 인식이 오래 이어짐(일반적으로 알려진 평가).
- **aDmD 시사점**: 수수료 경쟁은 aDmD가 이길 판이 아니다. 대신 Epic처럼 "메이커에게 무엇을 남겨주나"를 첫 화면에 숫자로 명시하는 투명성은 차용할 만하다.

## A-11. Netflix Games

- **대상**: Netflix 구독자. 2025년 10월부터 TV에서 바로 하는 파티 게임 도입.
- **홈·발견 구조**: Netflix 홈 안의 게임 줄(row). 영상과 같은 문법(가로 썸네일 줄)으로 게임을 배치.
- **플레이 방식**: TV에서 게임을 고르면 QR 코드가 뜨고, 휴대폰 카메라로 찍으면 휴대폰이 컨트롤러가 된다. 웹 브라우저에서도 플레이 가능. LEGO Party, Boggle Party, Pictionary 등.
- **전략**: 2025년 4분기 실적 발표에서 클라우드 우선 게임 전략을 공식화. 회원 약 1/3이 TV 게임에 접근 가능하나, 파티 게임 이용은 대상 회원의 약 10% 수준이라는 보도.
- **aDmD 시사점**: **QR로 휴대폰을 컨트롤러/참가자로 붙이는 방식**은 웹 게임 플랫폼이 바로 쓸 수 있는 "같이 하기" 패턴이다. 거실 화면(PC/TV)과 휴대폰을 잇는 파티형 게임 섹션 후보.

## A-12. Apple Arcade / Apple Games

- **대상**: Apple 기기 사용자, 구독형 큐레이션 게임 200개 이상.
- **구조 변화**: 2025년 WWDC에서 Apple Games 앱을 발표(iOS 26 등과 함께 가을 출시). Arcade 전용 탭, 내려받은 게임을 모은 Library 탭, Game Center 리더보드 위에 만든 "챌린지"(혼자 하는 게임을 친구끼리 겨루는 경쟁으로 바꿈)를 제공.
- **웹 페이지**: apple.com의 Arcade 페이지는 마케팅 페이지(대형 아트, 스크롤 연출, 구독 유도)이고 웹 플레이는 없다.
- **비판**: 비구독자에게도 Arcade 추천이 노출되는 데 대한 사용자 불만이 일부 있다(사용자 댓글 수준).
- **aDmD 시사점**: "챌린지" 개념, 즉 **싱글 게임의 기록을 친구에게 도전장으로 보내는 비동기 경쟁**은 서버 부담이 적고 한국 메신저 공유 문화와 잘 맞는다.

## A-13. Roblox Discover

- **대상**: 아동/청소년 플레이어, Roblox 경험(experience) 제작자.
- **홈·발견 구조**: 개인화 홈(추천 피드, "계속하기", 즐겨찾기)과 비개인화 Discover/Charts 페이지로 분리. Charts에는 Top Trending, Top Revisited, Fun with Friends 같은 정렬 줄과, 2025년 4월 29일 전 세계 공개된 동시접속 기반 "Top Playing Now". 국가/기기 필터, 장르 필터는 추후 예정. 2025년 4월 "Recommended for You" 알고리즘 기준을 공개.
- **플레이 방식**: 클라이언트 실행(웹에서 "플레이" → 앱 실행).
- **메이커 혜택**: 거대한 트래픽, 알고리즘 투명성 문서, 수익화.
- **약점·불만 (DevForum)**: 예고 없는 알고리즘 변경, 카테고리 이름과 실제 내용 불일치, 봇으로 순위를 조작하기 쉬움, 복제 게임이 차트를 점령, 장르 필터 복원 요구. Roblox도 이전 Discover 페이지는 새 콘텐츠 부족으로 트래픽 5% 미만이었다고 밝혔다.
- **aDmD 시사점**: **차트 정렬 이름이 곧 큐레이션의 성격**을 드러낸다("다시 찾는 게임", "친구랑 하기 좋은"). 랭킹은 조작 가능성 때문에 규모가 작을 때는 오히려 숨기는 편이 낫다.

## A-14. STOVE / 스토브인디 (스마일게이트)

- **대상**: 한국 PC 게이머, 특히 비주얼노벨, 서브컬처, 미스터리 취향층. 한국 인디 개발사.
- **홈·발견 구조**: 웹 스토어 + PC 런처. 메인 배너 캐러셀, 할인, 장르, 인디 섹션. 2015년 출범, 3,500개 이상 게임 등록(2026년 1월 보도).
- **상세 페이지**: 한국어 상점 표준 구조(미디어, 소개, 평가, 가격, 사양) + 한국어 커뮤니티 연결.
- **플레이 방식**: 구매 후 STOVE 런처로 설치/실행. 웹 플레이 없음.
- **메이커 혜택**: Indie Boost Lab(개발 중 플레이어 피드백 수집), STOVE INDIE Alliance, 펀딩 프로그램, 글로벌 퍼블리싱 계약, 스토브인디 어워즈(2025년 어워즈는 후보 21종에 각각 15% 할인 쿠폰, 일부 부문은 사용자 투표, 2026-02-11 발표, 올해의 게임 Clair Obscur: Expedition 33). BIC(부산인디커넥트) 등 오프라인 행사 스폰서. 2025년 중국/대만/베트남 등 아시아 확장.
- **정체성·톤**: 기업형 상점 톤. 서브컬처 공유 세계관("두근두근 유니버스") 같은 취향 기반 생태계를 키우는 중.
- **강점**: 한국어 커뮤니티, 취향 기반 큐레이션, 어워즈/행사 같은 의식.
- **약점**: 런처 설치 필요, Steam 대비 작은 사용자층. 이번 검색에서 구체적 사용자 불만은 찾지 못했다(커뮤니티 검색 추가 필요).
- **aDmD 시사점**: 한국 인디 메이커에게 STOVE는 "PC 패키지 판매처", aDmD는 "웹에서 바로 노는 첫 무대"로 역할이 다르다. 충돌보다 보완 관계로 포지셔닝 가능(예: aDmD에서 데모 → STOVE/Steam 위시리스트 링크).

## A-15. 네이버 게임

- **대상**: 한국 대형 온라인/모바일 게임 이용자, 게임사.
- **구조**: 게임 정보 + 게임사가 직접 여는 공식 커뮤니티 "라운지"(2021년 출범). 이용자층이 국내에 한정되어 있어 주로 한국 시장용 MMORPG, 한국 서버를 따로 둔 외산 게임이 라운지를 연다.
- **흐름**: 2025년 보도에 따르면 국내 게임업계는 공식 커뮤니티를 네이버 카페/라운지 대신 디스코드로 옮기는 추세다(비용과 기능 이유). 네이버는 2026년 1월 28일 주제별 오픈 커뮤니티 "라운지"(게시판 + 댓글 + 오픈톡)를 별도 출시했다.
- **플레이 방식**: 게임 플레이 플랫폼이 아님(정보/커뮤니티 허브).
- **aDmD 시사점**: 한국에서 "게임 커뮤니티 = 대형 게임의 공식 게시판"이라는 공백. 작은 게임이 커뮤니티를 갖기 어렵다. aDmD는 **게임 하나하나에 작은 방명록/커뮤니티**를 기본 제공하는 것으로 이 틈을 메울 수 있다.

## A-16. 앱인토스 (토스 미니앱 게임) — 한국 웹 게임의 실질적 신흥 채널

- **대상**: 토스 앱 사용자(대중), HTML5/WebGL 게임 개발자.
- **규모**: 출시 약 10개월 만에 미니앱 약 4,000개, 그중 약 20%가 게임(보도). 위메이드, NHN, 넵튠 같은 게임사부터 1인 개발자까지 입점. AI로 게임 미니앱 20개를 낸 1인 개발자 사례, 출시 70일 만에 100만 사용자를 모은 방치형 게임 사례를 공식 블로그가 홍보.
- **홈·발견 구조 (2025년 12월 게임 홈 개편)**: 카테고리 확장, 카테고리별 인기, 실시간 인기 게임, 꾸준히 사랑받는 게임, 따끈따끈 신작, "내 또래가 많이 플레이한 게임"(연령/성별 기반). **출시 2주 이내 신규 미니앱 전용 노출 구좌 강화.**
- **플레이 방식**: 토스 앱 안 웹뷰에서 즉시 실행. SDK 필수 기능 5가지(게임 로그인 등), 풀스크린 대응은 심사 필수.
- **메이커 혜택**: 인앱 광고, 인앱결제, Unity → WebGL 전환 가이드, 공모전(넵튠과 HTML5 게임 챌린지), AI 게임 제작 웨비나(2026년 1월).
- **정체성·톤**: 토스의 깔끔한 금융 앱 UI 안에 게임이 들어감. 게임 자체의 개성은 아이콘 하나로 축소된다.
- **약점(분석)**: 메이커 프로필, 데브로그, 커뮤니티가 없다. 게임은 "미니앱"이라는 상품 단위로 취급되고, 만든 사람의 얼굴은 보이지 않는다. AI 대량 제작을 오히려 장려하는 메시지.
- **aDmD 시사점**: 한국 HTML5 메이커를 두고 사실상 경쟁한다. 트래픽으로는 이길 수 없으므로 **"토스에는 없는 것": 메이커 정체성, 데브로그, 잼, 동료 커뮤니티, 사람의 큐레이션**으로 차별화해야 한다. 신작 2주 보호 노출 같은 공정성 장치는 차용할 가치가 있다.

## A-17. 국내 인디 커뮤니티 기타

- **디시인사이드 인디게임 마이너 갤러리**: 인디게임 이야기와 개발자 홍보 글이 오가는 익명 커뮤니티. 개발자 홍보 공지가 따로 있을 정도로 메이커 유입이 있지만, 게임을 올리고 바로 플레이하는 기능은 없다.
- **행사 중심 생태계**: 인디크래프트(2026년 대상 1HP 스튜디오 "이나리"), 대한민국 인디게임포럼(2026-04-03), BIC, BEAVEROCKS(스마일게이트, 2025년 서울 DDP 1만 5천 명 방문). 오프라인 행사는 활발하지만 **상시 온라인 거점은 비어 있다.**
- **쯔꾸르/비주얼노벨 창작층**: 포스타입 같은 블로그나 itch.io 컬렉션에 흩어져 있다. 한국어로 웹 플레이까지 되는 전용 거점은 이번 검색에서 찾지 못했다.
- **aDmD 시사점**: "한국어로 올리고, 바로 플레이되고, 메이커끼리 모이는 곳"이라는 조합은 비어 있다. 이 문장이 aDmD의 시장 정의가 될 수 있다.

---

## A-18. 한눈에 비교

| 플랫폼 | 웹 즉시 플레이 | 큐레이션 | 메이커 얼굴 노출 | 광고 부담 | 공통 업적/메타 | 잼 | 한국어 |
|---|---|---|---|---|---|---|---|
| itch.io | O | 약함(개방) | 강함 | 없음 | 없음 | 매우 강함 | 약함 |
| Steam | X | 알고리즘 | 중간 | 없음 | 게임별 업적 | X | O |
| Poki | O(무계정) | 매우 강함 | 약함 | 높음 | 약함 | X | 일부 |
| CrazyGames | O | 단계형 | 약함 | 높음 | 스트릭/통계 | 제휴 잼 | 일부 |
| Game Jolt | O/다운로드 | 약함 | 강함(SNS형) | 중간 | 트로피/EXP | 일부 | 약함 |
| Newgrounds | O | 커뮤니티 판정 | 강함 | 중간 | 메달 | 이벤트형 | X |
| Playdate | X | 매우 강함(손) | 중간 | 없음 | X | X | X |
| STOVE | X | 취향형 | 중간 | 없음 | 약함 | 행사형 | O |
| 앱인토스 | O(앱 내) | 심사+알고리즘 | 거의 없음 | 있음 | 없음 | 공모전 | O |
| **aDmD 목표** | **O(무계정)** | **사람+공정 노출** | **강함** | **없음** | **강함** | **상시** | **O** |

---

## A-19. 게임잼 사이트의 페이지 구조

### itch.io Jams (사실상 표준 인프라)
- **잼 페이지 구성**: 상단 배너(호스트가 꾸밈), 카운트다운(시작/제출 마감/투표 마감), 참가 버튼과 참가자 수, 개요/규칙/테마 본문, 탭(Overview, Submissions, Results, Community, Screenshots, Feed).
- **제출**: 기존 itch.io 게임 페이지를 잼에 연결하는 방식. 제출물마다 자동 댓글 스레드. 잼 전용 게시판(Community)은 선택.
- **평가**: 투표는 제출 마감 후 시작해 투표 마감까지. 심사위원만 또는 itch 계정 보유자 전체 공개 투표 선택. 공개 투표는 부정 위험이 있어 "Rating Queue"(투표할 게임을 배정해 쏠림 방지) 사용을 권장. 평가 기준은 호스트가 정하며 투표 시작 후엔 수정 불가. 기준별 평균으로 순위를 매기고 기준이 여럿이면 종합 순위 계산. 심사위원 수동 순위도 가능.
- **규모 사례**: GMTK Game Jam 2025(테마 "Loop", 2025-07-30 – 08-03) 약 9,500개 제출, 평가 약 19.7만 건. 평가 기준 5개(창의성, 재미, 서사, 아트, 오디오). 주최자가 창의성과 재미에 가중치를 두고 상위 일부를 직접 플레이해 영상으로 발표. AI 사용은 자제를 요청.

### Ludum Dare (ldjam.com)
- **구조**: 정보 사이트(ludumdare.com)와 이벤트 사이트(ldjam.com) 분리. 커뮤니티 투표로 테마를 여러 라운드에 걸쳐 정하고, 개발 과정 기록(포스트)을 공유하고, 공개 플레이와 투표로 평가. 혼자 48시간 하는 Compo와 팀/완화 규칙의 Jam 부문이 있다. 다른 사람 게임을 평가할수록 내 게임이 더 노출되는 상호 평가 구조가 핵심.
- **현황**: 2025년 예정 행사(LD57, LD58)를 취소. 2026년 4월 LD59(테마 "Signal") 개최 후, 주최자가 6회만 더 열고 2028년 10월 LD64로 이름을 마무리하겠다고 발표(2029년 4월 1회성 앙코르 예정). 후계 행사는 새 이름으로 이어가길 희망.
- **커뮤니티 반응**: 문제는 웹사이트가 아니며 다른 잼이 참가자를 흡수하겠지만 Ludum Dare와 같지는 않을 것이라는 의견. 참가자가 가치 있게 여긴 것은 커뮤니티 테마 투표, 개발 과정 기록, 공개 평가, 기부 기반 무료 운영, Inscryption, Mini Metro, Hollow Knight 같은 게임의 출발점이라는 역사.

### GMTK Game Jam
- itch.io 인프라 위에서 운영되는 초대형 온라인 잼. 유튜브 채널(Game Maker's Toolkit) 테마 공개 영상과 결과 영상이 이벤트의 중심. 2027년 잼 일정도 이미 itch.io에 공지됨.
- 배울 점: **테마 공개와 결과 발표를 "쇼"로 만든다.** 잼 페이지는 인프라이고, 의식(테마 공개 순간, 결과 영상)이 경험의 핵심.

### Global Game Jam
- 2026년 대회는 1월 26일 – 2월 1일, 테마 "Mask"(핀란드 주최 측 선정). 테마 공개 라이브 전에 준비 주간. 보통 100개국 이상, 약 800개 오프라인 사이트, 약 4만 명 규모. 2026년 누적 참가자 50만 명 돌파 목표.
- **구조**: 지역 "사이트"(대학, 커뮤니티 공간)가 단위. 사이트 등록 → 참가자가 사이트 선택 → 같은 테마로 동시에 제작 → 전 세계 게임 아카이브. 경쟁보다 참가와 협업 중심.
- 배울 점: **장소/모임 단위**를 1급 개념으로 둔다(학교, 동아리, 지역 모임).

### MakersGround 잼에 대한 시사점
1. 테마 공개 순간을 페이지 이벤트로(카운트다운이 0이 되면 DmD 얼굴이 테마를 "말한다").
2. 평가 큐 방식으로 쏠림 방지 + 평가에 참여할수록 내 게임 노출 증가(LD식 상호 평가).
3. 잼 종료와 동시에 PlayGround에 **"잼 아케이드"** 자동 개설. 플레이어도 즐길 수 있게 해 잼 작품의 수명을 늘린다(itch.io 잼 작품은 잼이 끝나면 대부분 묻힌다).
4. 팀/모임 단위(GGJ의 사이트 개념)를 지원해 학교/동아리 참여 유도.
5. Ludum Dare 은퇴(2028)로 생기는 공백. 한국어 상시 잼의 "집"이 될 기회.

---

## A-20. 종합: 기본 요건 / 공백 / 차별화 기회

### 기본 요건 (없으면 플랫폼으로 인정받지 못함)
- 썸네일 그리드 + 장르/태그 필터 + 검색(제목과 태그 모두)
- 게임 상세 해부도: 미디어 → 한 줄 소개 → 평판 요약 → 태그 → 행동 버튼 → 상세 설명 → 조작법 → 메이커 정보 → 리뷰/댓글 → 관련 게임
- 계정 없이 몇 초 안에 플레이 시작, 전체화면, 모바일 대응, 점진적 로딩
- 최근 플레이/이어하기, 즐겨찾기(위시리스트), 기본 프로필
- 썸네일 호버(또는 탭) 미리보기 영상/움직임
- 신고와 콘텐츠 정책, AI 사용 공개
- 메이커용: 업로드 → 미리보기 → 공개 흐름, 기본 통계(플레이 수, 평균 플레이 시간), 버전 업데이트

### 아무도 잘 못하는 공백
1. **AI 시대의 신뢰 신호**: itch.io는 자진 표시에 의존해 실패, Steam은 공개율만 오른다. "사람이 만들었다"를 보여주는 UI가 없다.
2. **광고 없는 무료 웹 플레이**: Poki/CrazyGames는 광고가 사업 모델이라 구조적으로 못 한다.
3. **플랫폼 공통 메타 진행**: Kongregate 배지 이후 웹 포털에서 사라짐. CrazyGames는 스트릭/통계 수준.
4. **메이커와 플레이어를 잇는 이야기**: Poki/앱인토스는 메이커 얼굴이 없고, itch.io는 데브로그가 게임 페이지와 따로 논다.
5. **잼 작품의 사후 수명**: 잼이 끝나면 작품이 묻힌다.
6. **공정한 신작 노출**: Steam/Roblox 모두 인기가 인기를 부른다는 불만. 앱인토스만 2주 구좌로 대응.
7. **한국어 웹 인디 거점**: 오프라인 행사는 많은데 상시 온라인 집이 없다.
8. **짧은 세션에 맞춘 발견**: 웹 게이머는 한 번에 11–20분, 2–3개 게임을 한다(Poki 조사). 이 리듬에 맞춘 "오늘의 세트"를 짜주는 곳이 없다.

### aDmD 차별화 기회 12가지 (플레이어가 실제로 보고 하는 것)

1. **"3초 놀이" 카드**: 홈 카드에 마우스를 올리거나 길게 누르면 카드가 그 자리에서 커지며 게임 첫 화면이 무음 미리보기로 돈다. 클릭하면 View Transition으로 카드가 그대로 플레이 화면으로 늘어나고 계정 없이 바로 시작. 페이지 이동을 느끼지 못하게 한다.
2. **살아있는 DmD 얼굴 = 시스템 상태**: 로고의 DmD 얼굴이 장식이 아니라 상태 표시기. 로딩 중에는 눈을 깜빡이며 기다리고, 오류가 나면 당황하고, 업적을 따면 윙크하고, 게임 iframe 위 상단 바에서 플레이 중일 때 조용히 졸고 있다. 빈 화면, 404, 점검 화면도 모두 같은 얼굴의 표정 변주로 처리.
3. **광고 없음 약속 + 메이커 응원**: 모든 게임 페이지 하단에 "이 게임은 광고 없이 무료입니다" 한 줄과 메이커 응원 버튼(후원 링크 또는 응원 스티커). 플레이를 끝내면 "재밌었다면 만든 사람에게 한마디" 프롬프트.
4. **주간 "판"(Issue) 큐레이션**: 매주 정해진 요일에 운영자가 고른 5–8개 게임을 잡지 한 호처럼 묶어 공개("aDmD 판 #12: 비 오는 날의 퍼즐"). 운영자의 짧은 손글씨풍 노트가 붙는다. Playdate 시즌처럼 기다리는 리듬을 만든다.
5. **플레이 시간 기반 탐색**: 장르보다 먼저 "5분 / 15분 / 저녁 하나" 탭. 세션 길이가 짧은 웹 게이머의 실제 리듬에 맞춘 첫 분류(Playdate의 Quick Plays 응용).
6. **"사람이 만든" 증명 배지**: 데브로그 2편 이상, 잼 참가 기록, 제작 과정 스크린샷 같은 공개 이력이 있으면 게임 카드에 "제작 일지 있음" 배지. AI 사용 여부와 범위는 업로드 시 필수 입력으로 상세 페이지에 명시. 필터는 숨기기가 아니라 강조 방식으로.
7. **게임 페이지 = 메이커의 무대**: 상세 페이지 오른쪽에 메이커 카드(얼굴/아바타, 한 줄 소개, 다른 게임), 아래에 데브로그 타임라인이 게임 버전 기록과 겹쳐 보인다("v1.2 — 점프가 더 쫀득해졌어요"). PlayGround와 MakersGround가 한 페이지에서 만나는 지점.
8. **신작 보호 구좌 + "발견자" 기록**: 출시 2주 이내 게임은 정해진 홈 슬롯에 순환 노출. 리뷰 10개 전에 플레이하고 리뷰를 남긴 사람은 그 게임의 "초기 발견자"로 프로필에 남는다. 인기 쏠림을 깨고, 발견하는 행동 자체를 보상한다.
9. **플랫폼 공통 도장판**: 게임별 업적과 별개로 aDmD 전체에 걸친 도장판(예: "공포 게임 3개 완주", "잼 작품 10개 플레이", "처음 리뷰 남기기"). 한국 도장/스탬프 문화와 DmD 얼굴 도장 이미지로 시각화. Kongregate 배지가 남긴 빈자리.
10. **기록 도전장 링크**: 게임이 끝나면 "내 기록 깨봐" 링크와 자동 생성 OG 이미지(DmD 얼굴 + 점수). 카카오톡에 붙이면 친구는 링크 하나로 같은 게임, 같은 목표에서 바로 시작. 실시간 서버 없이 되는 비동기 경쟁(Apple Games 챌린지 응용).
11. **잼 아케이드**: MakersGround 잼이 끝나면 PlayGround에 잼별 아케이드 페이지가 자동 생성. 테마, 수상작, 전 작품 그리드, 플레이어 투표. 플레이어는 "잼 작품 한 판" 도장을 모은다.
12. **게임마다 작은 방명록**: 리뷰(평가)와 별도로 짧은 방명록 벽. 별점 대신 "손맛 / 이야기 / 분위기 / 웃김" 같은 태그 감상과 한 줄. 대형 게임만 공식 커뮤니티를 갖는 한국 상황(네이버 라운지)에 대한 대안.

(보너스 후보) QR 파티 모드: PC 화면에 QR, 친구들이 휴대폰으로 참가하는 파티 게임 섹션(Netflix 패턴). 메이커용 SDK가 필요해 2차 단계로.

---

# Part B. 2025–2026 웹 디자인 트렌드

## B-0. 큰 흐름

- 2026년 트렌드 글 대부분이 공통으로 말하는 것: **AI가 만든 듯한 매끈함이 흔해지면서, 매끈함 자체가 평범함이 됐다.** 차별화는 손맛, 질감, 개성, 사람의 이야기에서 나온다(DesignRush, Bubble, NN/g, Creative Bloq).
- 모션은 표준이 되는 중: GSAP가 2025년 4월부터 무료, Figma가 2026년 6월 Figma Motion 출시(Digidop 정리). 동시에 CSS 스크롤 기반 애니메이션이 2026년 10월 Firefox 159로 3대 브라우저 지원을 갖췄다.
- 성능과 접근성이 "트렌드" 목록에 올라왔다(DesignRush의 성능 우선, 접근성 설계). 무료 인프라 위의 1인 운영 플랫폼에게는 오히려 유리한 흐름.
- 주의: 트렌드 글 대다수가 Webflow, Figma, 에이전시 등 판매자 측 콘텐츠다. 성숙도 판단은 여러 출처의 공통점과 필자의 해석을 결합한 것이다.

## B-1. 트렌드별 정리

성숙도: 상승 / 정점 / 하락. 적합도: 게임 플랫폼(aDmD)에 대한 판단.

| # | 트렌드 | 무엇인가 | 사례 | 성숙도 | aDmD 적합도 |
|---|---|---|---|---|---|
| 1 | 벤토 그리드 | 크기가 다른 사각 타일을 모아 위계를 주는 레이아웃. Apple 키노트/제품 페이지가 대중화 | Apple 제품 페이지, Kneads Bakeshop | **정점 → 포화**. 2025년엔 흔하다고 놀림받는 수준 | **부분 적합.** 프로필 통계, 메이커 대시보드, 잼 결과 요약에는 좋다. 홈 히어로를 벤토로 하면 SaaS 랜딩처럼 보인다. 모바일에서 예쁘게 쌓이지 않는 문제도 있다 |
| 2 | 에디토리얼/매거진 레이아웃 | 큰 제목, 비대칭 단, 인용, 호(issue) 단위 구성. 콘텐츠 우선 설계와 연결 | 콘텐츠 우선 사이트 사례(DesignRush: Pacific Environment), Playdate 웹 스토어의 편집형 페이지 | **상승** | **매우 적합.** "주간 판" 큐레이션, 운영자 노트, 메이커 인터뷰에 딱 맞는다. 1인 운영자의 목소리가 차별점이 된다 |
| 3 | 네오브루탈리즘 | 두꺼운 검은 테두리, 딱딱한 그림자, 원색 충돌 | Gumroad, Diesel | **정점 이후 고원.** shadcn 기반 RetroUI 같은 템플릿까지 나와 기성품화 | **조심.** 장난기와는 맞지만 이제 "템플릿 같다". 버튼 눌림 같은 일부 요소만 빌려 쓰는 정도 |
| 4 | 안티 디자인 / 못생김 | 의도적 불협화음, 규칙 파괴 | Creative Review의 "못생김" 트렌드 리포트 | 니치 상승 | **낮음.** 게임 탐색은 정보 밀도와 가독성이 중요. 잼 테마 페이지나 이벤트 한정으로만 |
| 5 | Y2K / 레트로 퓨처리즘 / 픽셀 | 크롬 그라데이션, 픽셀아트, 로파이 질감 | Figma가 말하는 "도파민" 채도 회귀 흐름 | **하락/과용.** DesignRush는 그 시대와 진짜 연결이 없으면 더 이상 차별점이 아니라고 봄 | **피하기.** 게임 사이트 + 픽셀/아케이드 = 가장 뻔한 조합. 게임 썸네일 자체가 이미 이 역할을 한다 |
| 6 | 촉감형 UI / 클레이모피즘 / 소프트 3D | 말랑한 버튼, 눌리면 찌그러지는 반응, 부드러운 3D 아이콘 | 소프트 3D 아이콘 트렌드(ManyPixels), 온보딩/키즈 앱 | 니치에서 안정. 클레이 단독은 이미 반짝 유행은 지남 | **적합(부분).** DmD 얼굴, 버튼 눌림, 도장 찍힘 같은 "손맛" 상호작용에 좋다. 전체 스타일로 하면 유아적 |
| 7 | 키네틱 타이포그래피 | 글자가 움직이며 내비게이션과 이야기 역할 | Dillinger.tv | **상승**(GSAP 무료화 영향) | **적합(절제해서).** 잼 테마 공개, 주간 판 표지, 업적 획득 순간. 상시 화면에는 쓰지 않는다 |
| 8 | CSS 스크롤 기반 애니메이션 | `animation-timeline`으로 스크롤 위치에 애니메이션을 묶음. JS 없이 가능 | 공식 데모 사이트 scroll-driven-animations.style | **새로 표준 진입.** Chrome 115, Safari 26, Firefox 159(2026년 10월)로 Baseline Newly available | **적합.** 상세 페이지 스크롤에 따라 헤더 축소, 데브로그 타임라인 진행 표시. 미지원 브라우저는 정적 화면으로 자연스럽게 대체되게 |
| 9 | View Transitions API | 화면 간 요소를 모핑하며 전환 | Chrome 팀 사례 모음 | 같은 문서 내 전환: 2025년 10월 Firefox 144로 Baseline. 문서 간 전환: Chromium 지원, Firefox는 미확인 | **매우 적합.** 카드 → 상세 → 플레이 화면 확장, 라이브러리 정렬 전환. "무마찰 플레이" 느낌의 핵심 기술 |
| 10 | 마이크로 인터랙션 | 작은 피드백 애니메이션(좋아요, 저장, 진행) | Maxima Therapy(DesignRush), Duolingo | **기본 요건** | **필수.** 게임 플랫폼에서 반응 없는 버튼은 죽은 느낌. 단, prefers-reduced-motion 존중 |
| 11 | 다크 모드 기본 | 어두운 UI를 기본으로, 사용자 설정 존중 | Linear, Webflow University | **기본 요건** | **적합하지만 함정.** 게임은 어두운 화면과 잘 맞는다. 하지만 "다크 + 보라/파랑 그라데이션 + 글로우"는 Linear식 SaaS 클리셰. aDmD 고유 색으로 다크를 만들고 라이트 모드도 1급으로 |
| 12 | 가변 폰트 | 하나의 파일로 굵기 등을 연속 조절 | Pretendard Variable(한글, OFL, 동적 서브셋) | **성숙** | **적합.** 한글 웹폰트 용량 문제를 동적 서브셋으로 해결. 호버 시 굵기 변화, DmD 표정과 맞춘 타이포 반응 |
| 13 | 사람 손맛 / 핸드메이드 미학 | 리노컷, 수채, 손글씨, 고르지 않은 선. AI의 매끈함에 대한 반작용 | Hermès 2026 홈(리노컷풍 일러스트), Microsoft AI 사이트(구아슈풍), Oatly | **상승.** NN/g가 2026년 4월 "새로운 신뢰 신호"로 정리 | **매우 적합.** "사람이 만든 게임" 포지셔닝과 정확히 일치. 단 AI로 흉내 내기 쉬워 겉모양만으로는 신호가 약해지니, 실제 메이커 이야기와 함께 써야 한다 |
| 14 | 제품 UI 속 마스코트/캐릭터 | 캐릭터가 빈 화면, 로딩, 피드백을 맡음 | Duolingo(Duo를 게임 마스코트처럼 키움, 애니메이션 스튜디오 인수), Discord(빈 친구 요청 화면의 Wumpus) | **성숙, 여전히 강력** | **매우 적합.** DmD 얼굴이 이미 있다. 단순한 형태가 애니메이션 비용을 줄인다(Duo는 "날개 달린 원기둥"). 위험: 2026년 Discord 연령 인증 논란 때 사용자들이 Wumpus를 항의의 표적으로 썼다. 마스코트는 브랜드의 감정 피뢰침이 된다 |
| 15 | 게임 인접 UI (콘솔 스토어/런처) | 큰 아트, 포커스 상태, 컨트롤러 탐색, 빠른 반응 | Switch 2 eShop(빠른 로딩으로 호평), Steam 2026 홈 리프레시(큰 아트, 호버 정보, 홈 안 디스커버리 큐, 무한 스크롤) | **성숙** | **적합(라이브러리 한정).** "내 라이브러리"는 런처처럼(큰 커버, 이어하기, 키보드/패드 포커스). 홈 탐색은 웹답게 |
| 16 | 글래스모피즘 / Liquid Glass | 반투명 흐림 패널. Apple이 2025년 Liquid Glass로 재점화 | Apple iOS 26 | **정점, 논란.** 가독성/접근성 비판이 많다 | **피하기.** 게임 썸네일 위 반투명 텍스트는 가독성 지옥. 플레이 화면 위 일시정지 메뉴 정도만 |
| 17 | 도파민 컬러 | 고채도 네온을 중립 배경 위 포인트로 | Starface | 상승 | **적합(포인트로).** DmD 브랜드 컬러 1–2개를 고채도 포인트로, 나머지는 중립 |
| 18 | 몰입형 3D / WebGL | 브라우저 3D 장면 | Awwwards 2025 올해의 사이트(Lando Norris), Cartier | 성숙 | **피하기(홈).** 무료 인프라와 저사양 기기에서 무겁다. 게임이 주인공이어야 한다 |
| 19 | AI 스타트업 미학 (Linear풍) | 다크 배경 + 보라-마젠타 그라데이션 + 블러 글로우 + 얇은 산세리프 | 수많은 SaaS 랜딩 | **과용.** "다 Linear처럼 생겼다"는 비판이 일반화 | **반드시 피하기** |
| 20 | 게이미피케이션 (스트릭, 진행 바) | 이탈 지점에 작은 보상 | Duolingo | 성숙 | **적합하지만 윤리 주의.** 도장판, 업적은 좋다. 연속 접속 압박 같은 다크 패턴은 금지 |
| 21 | 기계가 읽는 구조 (MX) | AI 검색/에이전트가 읽기 좋은 구조화 | Meltwater(DesignRush) | 상승 | **적합(보이지 않는 곳).** 게임 상세에 구조화 데이터. 디자인 트렌드라기보다 기본 위생 |

## B-2. 이미 과용되어 "어디서 본 듯한 사이트"를 만드는 것

1. **다크 배경 + 보라/마젠타 그라데이션 + 글로우 블롭** (AI/SaaS 클리셰). 게임 사이트에서는 "또 하나의 런처"처럼 보인다.
2. **히어로 벤토 그리드**: Apple, Vercel, Linear 이후 모든 랜딩 페이지가 쓴다.
3. **Y2K 크롬, 픽셀아트, CRT 스캔라인**: 게임 + 레트로는 가장 쉽게 떠오르는 조합이라 개성이 사라진다.
4. **글래스모피즘 / Liquid Glass 따라하기**: 가독성 문제 + 2025–2026년 Apple 흉내로 읽힌다.
5. **AI 생성 일러스트**: 평평한 조명, 이상한 비율, 균일한 광택이 바로 티가 난다. "사람이 만든 게임" 플랫폼에서는 치명적.
6. **템플릿형 네오브루탈리즘**: 두꺼운 테두리 + 하드 섀도 + 원색이 컴포넌트 키트로 상품화됐다.
7. **스톡 사진 히어로, 의미 없는 실험적 내비게이션**: 접근성 비용만 크다.

## B-3. aDmD 권장 조합 (Part A와 연결)

- **기본 골격**: 에디토리얼 레이아웃(주간 판, 운영자 노트) + 정보형 게임 그리드(썸네일이 주인공).
- **성격**: 손맛 있는 선과 질감(핸드메이드), DmD 얼굴 마스코트가 상태와 감정을 맡는다. 손그림 느낌은 장식 일러스트가 아니라 **선, 도장, 손글씨 메모** 같은 작은 단위로.
- **움직임**: View Transitions(카드 → 플레이), 스크롤 기반 애니메이션(상세/데브로그), 말랑한 마이크로 인터랙션(눌림, 도장 찍힘), 키네틱 타이포는 이벤트 순간에만. 모두 점진적 향상 + reduced-motion 대응.
- **색**: 중립 바탕(라이트/다크 둘 다 1급) + DmD 고유 고채도 포인트 1–2색. 보라 그라데이션 금지.
- **타이포**: Pretendard Variable(본문/UI) + 개성 있는 디스플레이 서체 1종(제목/이벤트). 가변 굵기를 상호작용에 활용.
- **라이브러리 화면만** 콘솔/런처 문법(큰 커버, 포커스 링, 이어하기, 키보드/패드 탐색).
- **피할 것**: 히어로 벤토, 글래스, Y2K/픽셀 클리셰, 3D 히어로, AI 일러스트, Linear풍 다크.

---

## 출처

### 플랫폼 — itch.io
- [Inven Global: 새 itch.io 페이지 두 배, 다운로드와 구매는 정체 (2026-11)](https://www.invenglobal.com/articles/28077/6000-new-itchio-game-pages-daily-but-gamers-arent-buying)
- [Aftermath: itch.io AI 게임 범람](https://aftermath.site/itch-ai-games-pc-slop/)
- [GamingOnLinux: itch.io가 AI 슬롭으로 넘쳐난다 (2026-11)](https://www.gamingonlinux.com/2026/11/game-store-itch-io-is-getting-flooded-with-ai-slop/comment_id=302064)
- [Gaming.net: itch.io, AI 공개 필터를 검색 결과로 확대](https://www.gaming.net/itch-io-expands-ai-disclosure-filters-to-search-results/)
- [itch.io 공식: NSFW 콘텐츠 업데이트](https://itch.io/updates/update-on-nsfw-content)
- [GamingOnLinux: itch.io 성인 콘텐츠 deindex (2025-07)](https://gamingonlinux.com/2025/07/game-store-itch-io-has-deindexed-adult-content-due-to-payment-processor-scrutiny)
- [GamingOnLinux: 무료 성인 콘텐츠 재색인 (2025-08)](https://www.gamingonlinux.com/2025/08/itch-io-to-reindex-free-adult-content-as-they-search-for-new-payment-processors)
- [PC Gamer: itch.io, 다른 결제사 접촉 중](https://www.pcgamer.com/gaming-industry/game-development/itch-io-is-actively-reaching-out-to-other-payment-processors-after-pressure-from-credit-card-companies-to-curtail-nsfw-content-and-that-compared-to-valve-it-has-limited-ability-to-push-back/)
- [itch.io 포럼 게시글 (탐색/추천 관련 불만)](https://itch.io/post/9621049)
- [itch.io 포럼 게시글 (개발자 서한, deindex와 소통)](https://itch.io/post/13540035)
- [itch.io 포럼: 새 검색 백엔드](https://itch.io/t/3818776/new-search-backend)
- [Cinevva: 2026년 웹 게임 게시처 가이드 (한국어)](https://app.cinevva.com/ko/guides/publish-web-game)

### 플랫폼 — Steam
- [PCGamesN: Steam 홈 개편 베타](https://www.pcgamesn.com/steam/homepage-update-beta-test)
- [Engadget: Steam 재설계 스토어 테스트](https://www.engadget.com/gaming/pc/steam-is-testing-out-a-redesigned-storefront-that-makes-it-easier-to-find-games-youll-like-165216486.html?src=rss)
- [TweakTown: Steam 스토어 페이지 리프레시](https://www.tweaktown.com/news/110831/valve-updates-steam-with-a-store-page-refresh-designed-to-make-it-easier-to-find-new-games/index.html)
- [Massively OP: Steam 홈 리프레시 (2026-06)](https://massivelyop.com/2026/06/05/steam-puts-out-a-refreshed-store-home-page-with-more-personalization-and-features/)
- [Automaton: Steam Next Fest와 위시리스트](https://automaton-media.com/en/news/steam-next-fest-disappoints-japanese-indie-devs-with-meager-wishlist-gains-but-theres-an-important-catch-to-how-the-algorithm-works/)
- [Outlook Respawn: 인디 발견 문제 악화](https://respawn.outlookindia.com/gaming/gaming-originals/the-indie-game-discovery-problem-is-getting-worse)
- [tbreak: Valve, AI 게임 게이트키핑 안 함](https://tbreak.com/valve-steam-visibility-ai-games-no-gatekeeping/)
- [Aftermath: Next Fest 데모와 AI 공개](https://aftermath.site/steam-next-fest-demos-ai-disclosure-algorithm/)

### 플랫폼 — Poki / CrazyGames
- [PocketGamer.biz: Poki의 브라우저 게임 비전 (2026-07)](https://www.pocketgamer.biz/inside-pokis-vision-for-the-future-of-browser-gaming/)
- [Poki: State of Web Gaming Report 2026](https://poki.com/blog/state-of-web-gaming-report-2026)
- [Poki: 2025 연간 리뷰](https://poki.com/blog/2025-at-poki-a-year-in-review)
- [Poki: Dutch Game Awards 2025 수상](https://poki.com/blog/poki-wins-dutch-game-awards-2025)
- [Mobidictum: Poki 공동창업자 인터뷰](https://mobidictum.com/pokis-web-gaming-interview-michiel-van-amerongen)
- [Playgama: Poki vs CrazyGames vs GameDistribution 수익 배분](https://playgama.com/blog/business-faqs/poki-vs-crazygames-vs-gamedistribution-revenue-share/)
- [Cinevva: Poki 게시 가이드 (2026)](https://app.cinevva.com/guides/publish-game-poki)
- [Trustpilot: Poki 리뷰](https://ca.trustpilot.com/review/poki.com)
- [Common Sense Media: Poki 부모 가이드](https://www.commonsensemedia.org/website-reviews/poki)
- [Common Sense Media: Poki 아이 리뷰](https://www.commonsensemedia.org/website-reviews/poki/user-reviews/child)
- [Poki FAQ](https://poki.com/ua/c/faq)
- [CrazyGames 문서: 요구사항 개요](https://docs.crazygames.com/requirements/intro/)
- [CrazyGames 문서: FAQ](https://docs.crazygames.com/faq/)
- [CrazyGames 개발자 약관 (2025-08-18)](https://files.crazygames.com/documents/developer_terms_20250818.pdf)
- [Cinevva: CrazyGames 개발자 가이드 (2026)](https://app.cinevva.com/guides/publish-game-crazygames)
- [PocketGamer.biz: CrazyGames 소셜 기능 출시](https://pocketgamer.biz/crazygames-launches-new-social-features-for-instant-multiplayer-gaming)
- [GamesBeat: CrazyGames 3,500만 사용자와 소셜 기능](https://gamesbeat.com/crazygames-hits-35m-users-for-browser-games-and-launches-social-multiplayer-features/)
- [Trustpilot: CrazyGames 리뷰](https://www.trustpilot.com/review/www.crazygames.com)
- [itch.io 포럼: CrazyGames 연동과 광고에 대한 개발자 글](https://itch.io/post/12237397)

### 플랫폼 — Game Jolt / Newgrounds / Kongregate / Armor Games
- [PC Gamer: Game Jolt 성인 콘텐츠 금지의 여파](https://pcgamer.com/indie-store-game-jolts-porn-ban-has-hit-games-with-no-sexual-content)
- [Game Developer: Game Jolt 금지 비판](https://gamedeveloper.com/business/indie-game-platform-game-jolt-taken-to-task-for-porn-ban)
- [Game Jolt 도움말: 크리에이터 작동 방식](https://ssr.gamejolt.net/help/creators)
- [Game Jolt 도움말: 스티커와 팩](https://ssr.gamejolt.net/help-docs/Shop/stickers)
- [Wikipedia: Game Jolt](https://www.wikipedia.org/wiki/Game_Jolt)
- [Wikipedia: Newgrounds](https://en.wikipedia.org/wiki/Newgrounds)
- [Zeli: Newgrounds가 25년 넘게 남은 이유 (한국어)](https://zeli.app/ko/story/49940394)
- [Gameranx: Newgrounds 후원 요청](https://gameranx.com/updates/id/9428/article/newgrounds-seeking-support-to-stay-alive)
- [PC Gamer: Kongregate 신규 게임 접수 중단](https://pcgamer.com/browser-game-portal-kongregate-is-no-longer-accepting-new-games)
- [PocketGamer.biz: Kongregate 해고와 접수 중단](https://www.pocketgamer.biz/kongregate-layoffs-no-new-game-submissions)
- [Wikiwand: Kongregate](https://wikiwand.com/en/Kongregate)
- [Wikiwand: Armor Games](https://wikiwand.com/en/articles/Armor_Games)
- [Gamespress: GemCraft Legacy Collection](https://www.gamespress.com/The-Games-You-Played-Between-Classes-Are-Back-GemCraft---Legacy-Collec)
- [PR.com: Obliterator-X 출시일](https://www.pr.com/press-release/956528)

### 플랫폼 — Playdate / GOG / Epic / Netflix / Apple / Roblox
- [play.date/games (Catalog 웹)](https://play.date/games)
- [Playdate 팟캐스트 Episode 25: Catalog](https://podcast.play.date/episodes/s01e25/transcript)
- [Game Developer: Panic, 큐레이션 스토어 Catalog 출시](https://gamedeveloper.com/business/panic-launches-catalog-a-curated-digital-storefront-for-playdate)
- [Engadget: Playdate 개발자 Catalog 매출 50만 달러 돌파](https://engadget.com/playdate-developers-have-made-more-than-500k-in-catalog-sales-120034296.html)
- [Good Game Lobby: Playdate Season Two](https://goodgamelobby.substack.com/p/exploring-playdate-season-two-games-panic-publishing)
- [The Sixth Axis: Playdate 2025 리뷰](https://www.thesixthaxis.com/?p=462340)
- [AlternativeTo: GOG, CD Projekt에서 분리](https://alternativeto.net/news/2025/12/gog-announces-its-separation-from-cd-projekt-as-co-founder-kici-ski-acquires-the-platform)
- [PC Gamer: GOG 새 오너, Steam은 사용 편의성으로 이긴다](https://www.pcgamer.com/games/steam-is-winning-with-its-ease-of-use-gogs-new-owner-says-but-hes-not-interested-in-picking-a-fight-i-think-much-can-be-done-in-gog-without-losing-its-core-values-and-the-way-it-operates)
- [Tech Insider: GOG 독립과 DRM-free (2026)](https://tech-insider.org/gog-independent-drm-free-2026/)
- [Epic Games Store: 웹숍과 수익 배분 업데이트](https://store.epicgames.com/news/new-epic-games-store-webshops-and-revenue-share-update)
- [TechSpot: Epic, 첫 100만 달러 수수료 0%](https://www.techspot.com/news/107797-epic-challenges-steam-zero-percent-fee-first-1.html)
- [Netflix Tudum: TV 파티 게임 안내](https://www.netflix.com/tudum/articles/netflix-party-games-play-on-tv)
- [TechCrunch: Netflix, TV에서 게임 플레이 (2025-10)](https://techcrunch.com/2025/10/09/netflix-is-letting-users-play-games-on-their-tv-screens)
- [PocketGamer.biz: Netflix 클라우드 우선 게임 전략](https://www.pocketgamer.biz/netflix-unveils-new-cloud-first-direction-for-its-games-strategy)
- [Outlook Respawn: Netflix, 2026년 클라우드 TV 게임 우선](https://respawn.outlookindia.com/gaming/gaming-news/netflix-makes-cloud-based-tv-games-a-key-priority-for-2026)
- [Apple Newsroom: Apple Games 앱 소개 (2025-06)](https://www.apple.com/newsroom/2025/06/introducing-the-apple-games-app-a-personalized-home-for-games/)
- [MacRumors: Apple Games 앱](https://www.macrumors.com/2025/06/09/apples-new-games-app/)
- [Roblox DevForum: 강화된 Discover 페이지 테스트](https://devforum.roblox.com/t/testing-an-enhanced-discover-page-top-charts-and-new-sorts/2954676)
- [Roblox DevForum: Charts의 Top Playing Now](https://devforum.roblox.com/t/introducing-top-playing-now-on-charts/3529809)
- [Roblox DevForum: 2025 디스커버리 로드맵](https://devforum.roblox.com/t/roblox%E2%80%99s-2025-discovery-roadmap-and-ways-to-reach-and-engage-your-audience/3557533/39)
- [Roblox DevForum: 개인화 디스커버리](https://devforum.roblox.com/t/building-the-future-of-roblox-home-and-search-introducing-personalized-discovery/3432124/74)
- [Roblox DevForum: 알고리즘 변경 불만 스레드](https://devforum.roblox.com/t/roblox%E2%80%99s-algorithm-changes-are-killing-our-game/2417236/113)

### 플랫폼 — 한국
- [Byline Network: 스마일게이트 스토브 (2026-01)](https://byline.network/2026/01/26-540/)
- [KOCCA Welcon: 스토브, 한국 인디 허브로](https://welcon.kocca.kr/en/support/issue-focus/185)
- [GameMeca: 2025 스토브인디 어워즈 GOTY](https://www.gamemeca.com/en/view.php?gid=1771403)
- [디지털투데이: 2025 스토브인디 어워즈 개최](https://www.digitaltoday.co.kr/en/view/1261/smilegate-to-hold-2025-stove-indie-awards)
- [디지털데일리: 클레르 옵스퀴르, 스토브 올해의 게임](https://www.ddaily.co.kr/page/view/2026021115383952883)
- [Smilegate Newsroom: BEAVEROCKS 2025](https://newsroom.smilegate.com/en/lab/beaverrocks2025)
- [Smilegate Newsroom: PlayX4 2025 스토브 부스](https://newsroom.smilegate.com/en/indiegame/playx420250520)
- [인디게임닷컴: 2025 한국 인디 동향](https://indiegame.com/en/archives/21812)
- [GameMeca: 네이버 게임 첫 화면 개편](https://www.gamemeca.com/view.php?gid=254000)
- [Daum/연합뉴스: 게임업계, 네이버 카페보다 디스코드로 (2025-09)](https://v.daum.net/v/20250906110131633)
- [네이버 보도자료: 오픈 커뮤니티 라운지](https://navercorp.com/media/pressReleasesDetail?seq=34309)
- [Dealsite: 네이버 라운지 분석](https://dealsite.co.kr/articles/154097)
- [앱인토스 블로그: 12월 1주 업데이트, 게임 홈 개편](https://toss.im/apps-in-toss/blog/update-12-1)
- [앱인토스 블로그: 게임 미니앱 필수 SDK](https://toss.im/apps-in-toss/blog/apps-in-toss-game-sdk-guide)
- [앱인토스 블로그: 거지키우기 사례](https://toss.im/apps-in-toss/blog/manababa)
- [앱인토스 블로그: 용사단키우기 100만 사용자](https://toss.im/apps-in-toss/blog/superjoy)
- [앱인토스 블로그: HTML5 게임 챌린지 수상작](https://toss.im/apps-in-toss/blog/gamechallenge)
- [앱인토스 블로그: AI 게임 웨비나](https://toss.im/apps-in-toss/blog/AI-webinar-2601)
- [Daum: 토스, 게임 퍼블리셔로 변신, 앱인토스 4천 개 돌파](https://v.daum.net/v/ZnYH6rIkrB?f=p)
- [디시인사이드 인디게임 마이너 갤러리](https://gall.dcinside.com/indiegame/489093)
- [GameMeca: 2026 인디크래프트 대상](https://www.gamemeca.com/en/mv.php?gid=1782102)
- [GameMeca: 2026 대한민국 인디게임포럼](https://www.gamemeca.com/en/mv.php?gid=1773630)
- [Daum: Poki가 생각하는 웹 게임의 미래 (한국어)](https://v.daum.net/v/z3IPtfDgCY)

### 게임잼
- [itch.io 문서: 게임잼](https://itch.io/docs/creators/game-jams)
- [itch.io: 게임잼 개발자 안내](https://itch.io/developers/game-jams)
- [itch.io 업데이트: 잼 심사 피드백, 수동 순위, 업로드 잠금](https://itch.io/updates/jams-updated-judge-feedback-manual-ranking-locked-uploads)
- [itch.io 업데이트: 잼 주요 평가 기준](https://itch.io/updates/primary-rating-criteria-for-game-jams)
- [itch.io: GMTK Game Jam 2025 제출작](https://itch.io/jam/gmtk-2025/entries)
- [Lenovo Legion 커뮤니티: GMTK Game Jam 2025](https://gaming.lenovo.com/game-dev/post/gmtk-game-jam-2025-YnepPOlWwsSQZ2L)
- [itch.io: GMTK Game Jam 2027 공지](https://itch.io/jam/gmtk-2027)
- [Aftermath: 20년 만에 Ludum Dare 마무리](https://aftermath.site/after-20-years-influential-game-jam-ludum-dare-will-wind-down/)
- [80.lv: Ludum Dare 2028년 10월 종료](https://80.lv/articles/ludum-dare-to-officially-end-in-october-2028)
- [Automaton: Ludum Dare 2028년 종료 (일본어)](https://automaton-media.com/articles/newsjp/ludum-dare-20260418-438298/)
- [Game Developer: Ludum Dare 2025 일정 취소](https://gamedeveloper.com/production/online-game-jam-ludum-dare-scraps-2025-event-schedule)
- [Wikipedia: Ludum Dare](https://en.wikipedia.org/wiki/Ludum_Dare)
- [PocketGamer.biz: Global Game Jam 누적 50만 명 목표](https://www.pocketgamer.biz/global-game-jam-aims-to-surpass-500000-lifetime-participants-ahead-of-2026-event)
- [Goldsmiths: Global Game Jam 2026](https://www.gold.ac.uk/news/2026/global-game-jam-2026/)
- [GamesBeat: Finnish Game Jam 2026](https://gamesbeat.com/?p=317007)

### 디자인 트렌드
- [Webflow: 2026 웹 디자인 트렌드 8가지](https://webflow.com/blog/web-design-trends-2026)
- [Figma 리소스 라이브러리: 웹 디자인 트렌드](https://www.figma.com/resource-library/web-design-trends/)
- [Digidop: 2026 웹 디자인 트렌드 5가지](https://www.digidop.com/blog/5-web-design-trends-2025/index.md)
- [DesignRush: 2026 웹 디자인 트렌드](https://www.designrush.com/agency/website-design-development/trends/web-design-trends)
- [Bubble: 2026 웹 디자인 트렌드](https://bubble.io/blog/web-design-trends/)
- [iTechGuides: 2026 웹 디자인 트렌드 27가지](https://www.itechguides.com/27-web-design-trends-for-2026-with-stunning-examples/)
- [IONOS: 웹 디자인 트렌드](https://www.ionos.com/digitalguide/websites/web-design/webdesign-trends/)
- [NN/g: 핸드메이드 디자인, 새로운 신뢰 신호 (2026-04)](https://nngroup.com/articles/handmade-designs)
- [Creative Bloq: 2026 그래픽 디자인 트렌드](https://www.creativebloq.com/design/graphic-design/texture-warmth-and-tactile-rebellion-the-big-graphic-design-trends-for-2026)
- [Fast Company: AI 공포가 핸드메이드 브랜딩을 키운다](https://www.fastcompany.com/91584397/ai-fears-are-fueling-the-handmade-branding-trend-technology-ai-fear-handmade-design)
- [Creative Review: 못생김을 진지하게](https://www.creativereview.co.uk/design-trend-report-ugliness/)
- [LogRocket: Linear 디자인](https://blog.logrocket.com/ux-design/linear-design)
- [Hacker News: 왜 모든 B2B SaaS가 Linear/Stripe처럼 생겼나](https://hn.svelte.dev/item/46179202)
- [Brainy: 2026년 SaaS가 다 똑같아 보이는 이유](https://brainy.ink/paper/why-every-saas-looks-the-same-2026)
- [Visual Movements: 벤토](https://visual-movements.pages.dev/movements/bento/)
- [Design Styles: 벤토 UI](https://design-styles.enlighten-media.net/pages/bento-ui/)
- [SaaSFrame: 벤토 레이아웃 트렌드](https://www.saasframe.io/blog/the-bento-layout-trend)
- [NN/g: 네오브루탈리즘](https://www.nngroup.com/articles/neobrutalism/)
- [Bejamas: 네오브루탈리즘 웹 디자인 트렌드 (2025-05)](https://bejamas.com/blog/neubrutalism-web-design-trend)
- [RetroUI: 2026년 알아야 할 네오브루탈리즘 사이트 12개](https://retroui.shadcn.io/blogs/12-neobrutalist-websites-you-should-know-in-2026)
- [LogRocket: 클레이모피즘이란](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/)
- [daisyUI Trends: 2026 UI 디자인 트렌드 18가지](https://trends.daisyui.com/ui-design-trends-2026/)
- [ManyPixels: 2026 아이콘 디자인 트렌드](https://www.manypixels.co/blog/post/the-key-trends-in-icon-design-in-2022)
- [Superdesign: 클레이모피즘 스타일](https://www.superdesign.dev/styles/claymorphism)
- [web.dev: 2026년 10월 웹 플랫폼 신기능](https://web.dev/blog/web-platform-10-2026)
- [Mozilla dev-platform: 스크롤 기반 애니메이션 Intent to Ship](https://groups.google.com/a/mozilla.org/g/dev-platform/c/uLZPrpA5Ic0)
- [Can I use: 스크롤 기반 애니메이션](https://caniuse.com/wf-scroll-driven-animations)
- [web.dev: 같은 문서 View Transitions Baseline (2025-10)](https://web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available)
- [Chrome for Developers: 2025년의 View Transitions](https://developer.chrome.com/blog/view-transitions-in-2025.md.txt)
- [Can I use: 문서 간 View Transitions](https://caniuse.com/cross-document-view-transitions)
- [Web Features Explorer: View transitions](https://web-platform-dx.github.io/web-features-explorer/features/view-transitions)
- [Pretendard GitHub](https://github.com/orioncactus/pretendard)
- [Fontsource: Pretendard](https://fontsource.org/fonts/pretendard/about)
- [Duolingo 블로그: 캐릭터 만들기](https://blog.duolingo.com/building-character/)
- [Fast Company: Duo의 다음 무대는 애니메이션 시리즈](https://fastcompany.com/91621113/duo-the-owl-next-big-act-is-an-animated-series)
- [Discord 패치노트 2026-06-04 (빈 화면의 Wumpus)](https://discord.com/blog/discord-patch-notes-june-4-2026)
- [PC Gamer: 인터넷이 Discord 마스코트를 의례적으로 괴롭히는 중](https://www.pcgamer.com/software/platforms/the-internet-is-ritualistically-murdering-discords-cartoon-mascot/)
- [Dot Esports: 연령 인증 항의와 Wumpus 팬아트](https://dotesports.com/general/news/discord-wumpus-torture-art-age-restriction-protest)
- [Atlassian: The Browser Company 인수](https://www.atlassian.com/blog/announcements/atlassian-acquires-the-browser-company)
- [TechCrunch: Atlassian, Arc 개발사 6.1억 달러 인수](https://techcrunch.com/2025/09/04/atlassian-to-buy-arc-developer-the-browser-company-for-610m)
- [TechCrunch: Liquid Glass 엇갈린 평가](https://techcrunch.com/2025/06/10/love-it-or-hate-it-apples-new-liquid-glass-design-is-getting-mixed-reviews)
- [Cult of Mac: Liquid Glass 가독성 우려](https://www.cultofmac.com/news/readability-concerns-take-shine-out-of-apples-new-liquid-glass-aesthetic)
- [UX Collective: Apple이 자기 원칙을 버렸나](https://uxdesign.cc/did-apple-abandoned-its-own-design-heuristics-accessibility-principles-2d616ed7ace5)
- [Creative Bloq: Switch 2의 의외의 업그레이드, eShop 디자인](https://www.creativebloq.com/entertainment/gaming/the-eshop-ui-design-is-the-switch-2s-most-unexpected-significant-upgrade)
- [Galaxus: Switch 2가 eShop 문제를 해결했다](https://www.galaxus.de/en/page/with-the-switch-2-nintendo-has-solved-one-of-the-switch-1s-biggest-problems-its-terrible-eshop-38267)
- [TechRadar: Switch eShop은 여전히 큐레이션 없는 혼돈](https://www.techradar.com/features/the-nintendo-switch-eshop-is-still-an-uncurated-mess-six-years-after-launch)
