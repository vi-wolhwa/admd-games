# 03. 게임 카드 컴포넌트 리서치와 aDmD 카드 세트 제안

- 작성일: 2026-11-26
- 대상: PlayGround(PC 우선) 게임 카드, 게임 목록 행, 방 카드 등 "게임 하나를 가리키는 모든 작은 단위"
- 전제(이미 확정된 것, [02-concept-ground.md](../02-concept-ground.md) §3.3·§6.3)
  - 카드 정보는 4층: **아트 / 제목 / 만든 사람(자모 얼굴 + 이름) / 한 줄 문맥**(큐레이션 이유 또는 "장르 · 한 판 시간 · 실행").
  - 평점은 리뷰 10개 이상일 때만. 저장·이어하기는 아트 위 상태 표시.
  - 메이커 얼굴은 아트 왼쪽 아래, 플랫폼 칩은 아트 오른쪽 위, 호버 시 빠른 플레이 버튼.
  - 아이콘만으로 뜻을 전하지 않는다. 호버 전용 정보 금지. 허영 지표(누적 플레이 수)는 첫 화면에서 뺀다.
  - 에셋 규격 초안은 [02-craft-principles.md](02-craft-principles.md) §5.1(16:9 필수, 3:4·1:1 선택).
- 방법: 공식 개발자 문서(Steamworks, Poki, CrazyGames, Playdate), 플랫폼 공지와 개발자 포럼(Roblox DevForum, itch.io 포럼, GOG 포럼, Spotify 커뮤니티), 언론 보도, 접근성 표준(W3C)과 실무 글을 웹 검색과 본문 확인으로 읽었다. 출처는 맨 끝.
- 표기
  - 판정: **good**(그대로 가져온다) / **adapt**(바꿔서 가져온다) / **avoid**(쓰지 않는다).
  - **[관찰]**: 문서 근거를 찾지 못했고 서비스 화면에서 널리 알려진 패턴을 정리한 것. 세부는 바뀌었을 수 있다.
  - **[검증 필요]**: 2차 출처나 사용자 보고뿐인 것.
- 한계: STOVE, 카카오페이지, 넥슨의 카드 UI는 공개 문서나 기사로 확인하지 못했다. Game Jolt, Epic, PlayStation의 카드 세부도 공식 문서를 찾지 못해 [관찰]로만 다뤘다. Reddit 스레드는 검색 도구로 잡히지 않아 사용자 불만은 공식 포럼과 기사에서 가져왔다.

---

## 0. 핵심 요약

1. **카드 아트에는 아무 글자도 얹지 않게 한다.** Steam, CrazyGames, Poki 세 곳 모두 메이커에게 같은 규칙을 강제한다: 아트에는 제목만, "NEW·무료·지금 플레이·점수"는 금지. 상태와 배지는 플랫폼이 일관된 자리에 그린다. aDmD도 업로드 가이드와 심사 항목으로 넣는다.
2. **플레이어 수를 카드에서 빼는 것은 근거가 있다.** Roblox는 2024년 4월 큰 16:9 타일에서 동시 접속자 수를 없앴고, 실험에서 처음 보는 게임 발견이 6.79%, 추천 참여가 8.24% 늘었다고 밝혔다. 다만 이어하기·즐겨찾기 타일에는 남겼다. aDmD의 "허영 지표 금지"와 같은 방향이고, **행동을 돕는 숫자(대기 인원, 진행률, 한 판 시간)만** 남기는 규칙의 근거가 된다.
3. **호버 미리보기는 이제 기본기다. 다만 끌 수 있어야 한다.** Poki는 1:1, 4–6초, 무음 애니메이션 썸네일을 출시 필수로 정했고, Steam은 2026년 홈 개편에서 호버 마이크로 트레일러를 넣으면서 **설정에서 끄면 정적 스크린샷으로 바뀌는** 선택지를 같이 냈다. aDmD는 "짧고(6초) 무음이고 첫 프레임이 커버와 같고, 400ms 머문 뒤 시작하고, 끌 수 있는" 미리보기로 간다.
4. **"왜 이 게임이 여기 있나"를 카드가 말해야 한다.** Steam도 2026년 개편에서 추천 이유를 카드에 더 드러냈고, Roblox는 타일 부제에 장르나 "급상승" 같은 설명어를 넣는 실험을 했다. aDmD의 한 줄 문맥 슬롯은 이 흐름의 정답에 가깝다. 차이는 **이유를 쓴 사람이 보인다**는 것(큐레이터 얼굴 + 말풍선).
5. **평점은 표본이 쌓일 때까지 숨긴다.** Kongregate는 최소 평가 수 전엔 평점을 숨기고, itch.io 잼은 평가가 적은 출품작 점수를 중앙값 기준으로 깎는다. aDmD의 "리뷰 10개 이상" 규칙과 일치하고, 잼에서는 조정 점수와 평가 수를 함께 보여준다.
6. **카드 접근성의 정답은 이미 정리돼 있다.** 카드 전체를 `<a>`로 감싸지 말고, 제목 링크를 `::after`로 카드 전체에 늘리고(stretched link), 보조 버튼(저장, 빠른 플레이, 메이커 링크)은 그 위에 따로 둔다. 목록은 `ul/li`. 호버로 나타나는 내용은 WCAG 1.4.13(해제 가능, 호버 가능, 지속)을 지킨다.
7. **카드는 8종이면 모든 상황을 덮는다**(§3): 표준 게임 카드, 픽 카드, 순위 행, 이어하기 카드, 작은 행, 라이브러리 행, 방 카드, 시간 자 핀. 잼은 표준 카드의 모드로 처리한다.

---

## 1. 플랫폼별 메모 (아이디어 목록의 배경)

| 플랫폼 | 카드에서 눈여겨볼 점 | 근거 |
|---|---|---|
| Steam | 위치마다 비율이 다른 캡슐 4종(헤더 920×430, 스몰 462×174, 메인 1232×706, 세로 748×896). 캡슐에 리뷰 점수·수상·할인·CTA 금지, 시즌 이벤트 글자는 14일짜리 아트워크 오버라이드로만. 2026년 홈 개편: 호버 시 마이크로 트레일러 + 짧은 설명, 추천 이유와 리뷰 요약 강화, 캐러셀 양옆 미리보기, 디스커버리 큐를 페이지 이동 없이, 모션 끄기 설정. 주간 판매 차트는 빌보드처럼 등락 표시. Steam Deck 호환 배지 4단계. | Steamworks 문서, GamingOnLinux, PCGamesN, PC Gamer |
| itch.io | 셀 = 커버(630×500 권장) + 제목 + 한 줄 소개 + 작가(인증 표시) + 장르 + "Play in browser" 글자. GIF 커버는 목록에서 호버할 때만 움직인다는 사용자 보고. 잼 결과는 기준별 순위 표, 평가 수, 조정 점수와 원점수, 제출 목록 기본 정렬은 무작위, "평가 적은 순" 정렬. | itch.io 화면, 포럼 |
| Poki | 1:1 full-bleed 정적 썸네일(628px 이상), 글자 없는 썸네일이 테스트에서 우세, 전경 하나, 사이트 배경색과 겹치지 않게. 애니메이션 썸네일 필수: 1:1, 1080px, 4–6초, 50fps, mp4, 무음, 2–3장면, 정적 아트에서 시작, 커서 제거, 호버 때 재생. 홈은 크기가 섞인 타일. | Poki 개발자 가이드, poki.com |
| CrazyGames | 커버 3종(16:9 1920×1080, 2:3 800×1200, 1:1 800×800), 셋이 같은 비주얼. 커버에 제목 외 글자·테두리·아이콘 금지. 미리보기 영상 15–20초, 50MB, 무음, 첫 프레임 = 정적 커버, 빨리감기·검은 화면·커서 금지. 홈 섹션에 "5-minute fun", "With friends", "Just relax" 같은 무드·시간 섹션. | CrazyGames 문서, crazygames.com |
| Roblox | 16:9 타일에서 동시 접속자 수 제거(2024-04), 친구 접속과 평점은 유지, 1:1 이어하기 타일엔 접속자 수 유지. 2025-08 타일 부제에 장르·사회적 증거 설명어 실험. 개발자들은 자기가 정하는 라벨(이벤트 등)을 원함. | Roblox DevForum |
| Kongregate | 평가 수가 최소치에 못 미치면 평점 미표시, 3.5 미만은 "최고 평점" 목록 제외. 배지(업적)로 게임 재방문 유도. | Kongregate 문서·FAQ |
| GOG | "In library" 라벨과 "가진 게임 숨기기" 옵션. 사용자들이 가진 게임을 흐리게 하는 스크립트까지 만듦 = 소유 표시 수요가 큼. | GOG 포럼 |
| Epic | 호버 시 + 아이콘으로 위시리스트 추가, 체크로 해제. 주간 무료 게임 카드, "미스터리 게임" 예고. | Epic 도움말, VGC |
| Xbox | 클라우드로 할 수 있는 게임에 구름 배지와 필터. 기기 간 플레이 기록. 게임 타일에서 빠르게 플레이 진입. | Xbox Wire |
| Nintendo eShop(Switch 2) | 더 빠른 스토어, 정렬 확대, 영상 미리보기, "For You"·위시리스트 메뉴. | Nintendo World Report 외 |
| Apple Games 앱 | 라이브러리 + 친구가 하는 게임 기반 추천 + 친구끼리 점수 챌린지 + 초대 링크·파티 코드. tvOS 락업은 포커스 때 커지므로 간격 확보 권고. | Apple 뉴스룸, HIG |
| Netflix | Top 10 행(국가별 일일, 큰 숫자, 행 위치는 개인 관련도에 따라). 호버 시 카드 확장 + 미리보기 재생, 이웃 카드가 밀림. 확장 지연에 대한 사용자 불만. TV 게임은 폰이 컨트롤러. | Netflix, CSS-Tricks, MacRumors, Tudum |
| Newgrounds | 사람 투표 + 스태프로 매일 Daily Feature ~ Daily 5th 수상. | Wikigrounds |
| Playdate Catalog | 큐레이션 스토어, 헤더 + 정적 이미지 1장 + GIF 1개 필수, 메이커가 페이지 색 몇 개를 지정하되 가독성 요구. | Playdate 도움말 |
| 카카오페이지 | 시계 아이콘 하나로 "기다리면 무료" 상태를 표시. 2022 개편에서 썸네일 확대. | 카카오, 바이라인네트워크 |
| YouTube | 호버 인라인 재생(설정으로 끄기), 썸네일 하단 시청 진행 막대. 빨간 막대가 색약 사용자에게 잘 안 보인다는 지적. | 9to5Google, Android Police |
| Spotify | 호버 시 나타나는 큰 재생 버튼이 실수 재생을 부른다는 사용자 불만. | Spotify 커뮤니티 |
| Letterboxd | 포스터에서 바로 "봤음(눈)", 좋아요, 평점. 포스터 그리드가 사이트의 얼굴. | Letterboxd 안내 |

---

## 2. 아이디어 목록 (98개)

각 행: 무엇 / 어디서 / 어떤 문제를 푸나 / aDmD 판정과 한 줄 이유.

### 2.1 아트·썸네일·비율 (14)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| A1 | 위치별로 비율이 다른 캡슐 세트(가로 헤더, 납작한 스몰, 큰 메인, 세로) | Steam | 자리마다 최적 구도 | **adapt** — 메이커 부담을 줄이려 **16:9 하나 필수 + 1:1 선택**만 받고 나머지는 초점 기준 자동 크롭. PC 사이트엔 세로 카드 상황이 거의 없다. |
| A2 | 스몰 캡슐은 로고가 칸을 거의 채워야 최소 크기(120×45)에서도 읽힌다 | Steam | 작은 목록 행에서 판독성 | **adapt** — 순위 행·검색 드롭다운용 1:1 아이콘은 "캐릭터나 로고 하나"로 채우라고 안내. |
| A3 | 아트에 리뷰 점수·수상·할인·CTA·기타 글자 금지 | Steam | 아트가 광고판이 되는 것, 정보 중복 | **good** — 업로드 가이드 + 심사 체크 항목. 상태는 플랫폼이 그린다. |
| A4 | 이벤트·업데이트 글자는 14일짜리 임시 아트(오버라이드)로만, 지금 받을 수 있는 내용만 | Steam | 오래된 "업데이트!" 문구 방치 | **adapt** — 아트 교체 대신 **플랫폼이 14일 "업데이트" 배지**를 자동으로 붙였다 떼게 한다. |
| A5 | 커버 3종(16:9, 2:3, 1:1)을 같은 비주얼로 | CrazyGames | 크기가 달라도 같은 게임으로 인식 | **adapt** — 16:9와 1:1만. 1:1은 16:9에서 초점 크롭을 기본값으로 제안하고 메이커가 바꿀 수 있게. |
| A6 | 커버에 제목만, 테두리·아이콘·"New/Updated/Play" 금지, 흐린 이미지·단순 스크린샷 금지 | CrazyGames | 지저분한 그리드 | **good** — A3과 합쳐 하나의 "커버 규칙" 문서로. |
| A7 | 글자 없는 썸네일이 테스트에서 더 선호됨 | Poki | 작은 타일에서 글자 뭉개짐 | **adapt** — aDmD 카드는 제목을 아트 밖 텍스트로 이미 가지므로 **아트 속 제목은 선택**. 1:1 아이콘에는 글자 넣지 말라고 권장. |
| A8 | 전경 하나(주인공이나 핵심 오브젝트), 콜라주 금지, 역동적인 포즈 | Poki | 한눈에 무슨 게임인지 | **good** — 메이커 가이드 문장으로. |
| A9 | 사이트 배경색과 비슷한 썸네일은 묻히니 대비 확보 | Poki | 아트 경계 소실 | **good** — 흰 배경 aDmD에선 흰 바탕 아트가 사라진다. **아트 안쪽 1px 반투명 테두리**를 모든 카드에. |
| A10 | 큰 크기와 작은 크기 둘 다에서 구도 확인 | Poki | 축소 시 디테일 뭉개짐 | **good** — MakersGround 업로드 화면에 실제 카드 크기(표준·행·아이콘) 미리보기. |
| A11 | 비율이 안 맞으면 늘어나 찌그러짐(사용자 보고) | itch.io | 왜곡 | **avoid**(그 동작을) — 항상 `object-fit: cover` + 메이커가 지정한 초점 좌표. |
| A12 | 스크린샷은 실제 게임플레이만, 콘셉트 아트·시네마틱 금지 | Steam | 기대와 실제의 차이 | **good** — 호버 미리보기 소스에도 같은 규칙. Poki도 썸네일이 실제와 다르면 플레이 전 이탈이 는다고 봄. |
| A13 | 메이커가 페이지 색 몇 개를 지정, 글자 대비 요구 | Playdate | 메이커 개성 + 가독성 | **adapt** — 대표색은 자동 추출, 메이커가 후보 중 고르게 하고 대비는 자동 검사(게임색 필드와 연결). |
| A14 | AI 생성 캡슐 아트가 스팸처럼 보여 둘러보기가 재미없어졌다는 비판 | PC Gamer(2026) | "아무나 찍어낸" 인상 | **adapt** — 카드엔 AI 배지를 달지 않되(낙인 방지), AI 사용 공개는 상세 필수 항목, 필터로 제외 가능. 큐레이션 카드엔 사람 손으로 만든 아트를 우선. |

### 2.2 모션·호버·미리보기 (15)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| M1 | 호버 애니메이션 썸네일: 4–6초, 무음, 2–3장면, 정적 아트에서 시작, 커서 숨김 | Poki | 정지 이미지로는 손맛이 안 보임 | **good** — aDmD 미리보기 사양의 기준. 길이 6초 이하. |
| M2 | 미리보기 15–20초, 첫 프레임 = 정적 커버, 빨리감기·검은 화면·로고 전환 금지 | CrazyGames | 어색한 전환, 과장 | **adapt** — 금지 목록만 가져오고 길이는 Poki처럼 짧게. |
| M3 | 호버 시 마이크로 트레일러 + 짧은 설명 + 추천 이유 + 리뷰 요약 | Steam(2026) | 상세 페이지 안 가고 판단 | **adapt** — 영상은 가져오되 **호버 때만 나타나는 글자 정보는 금지**(설명은 이미 카드에 있는 한 줄 문맥으로). |
| M4 | 트레일러 여러 지점에서 짧은 클립을 자동으로 뽑아 미리보기 생성 | Steam(2026, 2차 출처) | 메이커 추가 작업 없음 | **avoid** — 의도와 다른 장면이 첫인상이 된다. 메이커가 고른 6초를 쓰고, 없으면 정적. |
| M5 | 설정에서 호버 트레일러·움직이는 에셋을 끄면 정적 스크린샷으로 대체 | Steam(2026) | 멀미·주의 분산 | **good** — "움직이는 미리보기" 설정 + `prefers-reduced-motion`이면 기본 꺼짐. |
| M6 | GIF 커버는 목록에서 호버할 때만 움직이고, 첫 프레임을 정적 커버로 | itch.io(사용자 보고) | 그리드가 한꺼번에 움직이는 소음 | **good** — 자동 재생 그리드는 금지, 한 번에 한 카드만 재생. |
| M7 | 썸네일 위 "GIF" 라벨 | itch.io | 움직이는 카드 예고 | **avoid** — 플레이어에게 의미 없는 기술 용어. |
| M8 | 호버하면 카드가 커지고 이웃이 밀려나는 확장 + 1초 뒤 영상 | Netflix | 더 많은 정보 | **avoid** — 촘촘한 5열 그리드에서 레이아웃이 흔들리고, 확장 지연에 대한 사용자 불만도 있다. 크기는 고정, 아트 안에서만 영상 교체. |
| M9 | 호버 인라인 재생 + 설정으로 끄기, 예전엔 무음 루프 GIF | YouTube | 클릭 전 미리보기 | **adapt** — 끄기 설정을 사이트 설정 한 곳에 모은다(M5와 동일). |
| M10 | 호버 의도 지연 300–500ms(지나가는 커서는 무시) | Baymard, NN/g | 커서가 지나갈 때마다 재생되는 소음과 낭비 | **good** — 약 400ms 머문 뒤 로드·재생, 떠나면 즉시 멈추고 첫 프레임으로. |
| M11 | `preload="none"`, 호버(mouseenter) 때 로드 시작, 화면 밖은 IntersectionObserver로 지연 | web.dev, Chrome 문서 | 그리드 수십 개 영상의 데이터 낭비 | **good** — 영상 URL은 hover-intent 이후에만 붙인다. 포스터는 이미 있는 커버 이미지 재사용. |
| M12 | 포커스된 항목이 커지므로 항목 사이 간격을 확보, 깊이감(시차) | Apple tvOS HIG | 포커스 확대 시 겹침 | **adapt** — 키보드 포커스·호버 때 2–4px 들어올림 정도만, 그만큼 간격 확보. 시차 효과는 **avoid**. |
| M13 | 호버 시 커다란 재생 버튼 → 열려고 눌렀다가 재생돼 버림 | Spotify(사용자 불만) | 실수 실행 | **adapt** — aDmD 빠른 플레이 버튼은 **아트 오른쪽 아래 작은 원형(40px)**, 가운데 큰 버튼 금지. 브라우저 게임에만. |
| M14 | 캐러셀에서 양옆 다음 항목이 살짝 보이게 | Steam(2026) | 더 있다는 신호 | **good** — 이미 v6 배너에 반영. 레일에도 마지막 카드를 반쯤 잘라 보여준다. |
| M15 | 화면 안 여러 움직임은 한 곳에서 멈출 수 있게, 5초 넘는 자동 움직임은 정지 수단 필요 | WCAG 2.2.2 | 주의 분산, 전정 장애 | **good** — 호버 미리보기는 사용자가 시작한 것이라 대상 밖이지만, 배너 자동 재생은 금지(이미 원칙). |

### 2.3 보여줄 정보 (메타, 평점, 배지, 플랫폼, 가격 대체) (14)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| I1 | 셀 = 제목 + 한 줄 소개 + 작가 + 장르 + "Play in browser"(아이콘 아닌 글자) | itch.io | 최소 정보로 판단 | **good** — aDmD 4층 구조와 거의 같다. 실행 방식도 글자로. |
| I2 | 리뷰 요약을 단어로("매우 긍정적") | Steam | 숫자보다 빠른 판단 | **adapt** — 단어 등급은 과장처럼 읽힐 수 있다. "추천 92% · 리뷰 38"처럼 **비율 + 표본 수**, 10개 미만이면 생략. |
| I3 | 최소 평가 수 전엔 평점 숨김, 낮은 평점은 상위 목록 제외 | Kongregate | 적은 표본의 극단값 | **good** — 이미 "10개 이상" 규칙. 목록 정렬에도 같은 하한을 쓴다. |
| I4 | 타일 부제에 장르 또는 "급상승·떠오르는" 같은 설명어 | Roblox(2025 실험) | 숫자 없이 맥락 | **adapt** — 한 줄 문맥 슬롯에 **우선순위대로 하나만**: 큐레이션 이유 > 친구 활동 > "장르 · 한 판 시간 · 실행". |
| I5 | 동시 접속자 수를 큰 타일에서 제거(발견 6.79%↑), 이어하기 작은 타일엔 유지 | Roblox | 인기 게임 쏠림 | **good** — 카드에서 누적·동시 플레이 수 제외. 단 **방 목록·멀티 게임에서는 "지금 대기 n명"**이 행동 정보이므로 표시. |
| I6 | 사용자가 호버하면 숫자를 보여주자는 절충안(개발자 제안) | Roblox DevForum | 숨김에 대한 반발 | **avoid** — 호버 전용 정보 금지 원칙. 숫자는 상세 페이지에. |
| I7 | 기기별 호환 배지(Verified/Playable/Unsupported/Unknown), 호환 게임만 모은 탭 | Steam Deck | 내 기기에서 되나? | **adapt** — 단계는 2개로 줄이고(된다 / 이 기기에선 안 된다), **안 될 때만 카드에 글자로** 표시. |
| I8 | 클라우드 가능 게임에 배지 + 같은 조건 필터 | Xbox | 실행 방식 탐색 | **good** — v6의 "칩 아이콘 = 필터 범례" 원칙과 같다. |
| I9 | 추천 이유를 카드에 드러냄 | Steam(2026), PC Gamer | 알고리즘 불신 | **good** — aDmD는 알고리즘 이유 대신 **큐레이터가 쓴 이유**. 개인화 섹션은 "○○를 해서" 문구. |
| I10 | 무드·시간 섹션("5-minute fun", "With friends", "Just relax") | CrazyGames | 상황별 고르기 | **good**(방향) — 경쟁자도 섹션 단위로만 한다. aDmD는 **카드마다 "한 판 5분" 글자 표기 + 시간 자**로 한 단계 더 간다. |
| I11 | 아이콘 하나(시계)로 이용 조건 표시 | 카카오페이지 | 작은 공간 | **adapt** — 아이콘 + 짧은 글자. 아이콘만은 금지. |
| I12 | 다운로드 게임: 바이러스 다중 엔진 검사 결과 | VirusTotal 문서 | 설치 불안 | **adapt** — 카드엔 "설치 · 검사 통과"(방패, 비취색) 한 칩만. 엔진 수·검사일·버전·용량은 상세와 라이브러리 행에. |
| I13 | 가격 자리 | Steam, Epic 등 [관찰] | 구매 판단 | **adapt** — aDmD는 무료라 가격 자리가 비어 있다. 그 자리를 **한 판 시간**이 차지한다. "무료" 배지는 쓰지 않는다(전부 무료라 소음). |
| I14 | 인증 계정 표시 | itch.io | 사칭, 신뢰 | **avoid**(카드에서) — 초기 플랫폼에 등급 표식은 소음. 심사 통과가 이미 신뢰 장치. |

### 2.4 상태 (13)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| S1 | "In library" 라벨 + "가진 것 숨기기" 옵션, 사용자 스크립트로 흐리게까지 | GOG | 이미 아는 게임이 자리 차지 | **good** — "해본 게임" 작은 표시 + 그리드 필터 "해본 게임 숨기기". 흐리게 하진 않는다(대비 저하). |
| S2 | 썸네일 하단 시청 진행 막대 | YouTube | 이어보기 위치 | **adapt** — 막대 + 글자("3/8 스테이지" 또는 "42%"), 메이커가 진행률 API를 쓸 때만. |
| S3 | 진행 막대 빨강이 아트와 섞이거나 색약에게 안 보임 | YouTube(확장 프로그램 설명) | 색 의존 | **good**(교훈) — 막대는 아트 **밖**(아트 아래 경계선)에, 트랙 대비 3:1 이상. |
| S4 | 부분 시청 막대, 완료 체크, 끝나면 다음 회차가 이어보기에 | Apple TV | 다음 행동 제시 | **adapt** — "완료" 대신 "엔딩 봄", 업데이트된 게임은 이어하기 줄 앞으로. |
| S5 | 호버 시 + 아이콘으로 위시리스트, 체크로 해제 | Epic | 빠른 저장 | **adapt** — 저장 버튼은 카드 안 보조 버튼, **저장된 상태는 항상 표시**, 저장 전 버튼은 호버·포커스·터치 기기에서 보임. |
| S6 | 기간제 업데이트 표기(14일) | Steam | 오래된 "NEW" | **good** — "새로 나옴"·"업데이트" 배지 둘 다 14일 자동 만료. |
| S7 | 썸네일은 큰 업데이트 때만 교체(승인 필요) | Poki | 잦은 교체로 인한 혼란 | **adapt** — 커버 교체는 자유, 다만 교체 후 큐레이션 카드는 큐레이터 확인. |
| S8 | 커버 교체가 재방문을 부른다 | CrazyGames | 오래된 게임 재발견 | **adapt** — 메이커 대시보드 팁으로. |
| S9 | TV 게임 / 모바일 게임 구분, 폰이 컨트롤러 | Netflix Games | 장치 요구 | **adapt** — 특수 입력("휴대폰이 컨트롤러", "게임패드 필요")은 칩이 아니라 한 줄 문맥 끝에 글자로. |
| S10 | 친구가 하는 게임 기반 추천, 친구와 점수 챌린지 | Apple Games | 함께 하기 동기 | **good** — "친구 3명이 이번 주에 함" + 얼굴 스택(최대 3). |
| S11 | 타일 위 친구 접속 표시 유지 | Roblox | 지금 같이 할 사람 | **good** — "지금 ㅍㅅㅍ 님이 하는 중"(초록 점 + 글자). 공개 설정한 친구만. |
| S12 | 매주 무료 게임 카드, 다음 게임을 "미스터리"로 예고 | Epic | 기대감, 재방문 | **adapt** — "다음 주 픽" 예고 카드 1장까지만. "곧 공개" 남발은 금지(리서치 02 §5.4). |
| S13 | 게임이 내려가거나 점검 중 | [관찰] 여러 스토어 | 라이브러리 깨짐 | **good** — 라이브러리 행에 "점검 중"·"메이커가 내림" 상태, 진행 기록은 남김. |

### 2.5 사회적 증거 (가짜 통계 없이) (8)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| P1 | 국가별·일일 Top 10 행, 큰 숫자, 행 위치는 개인 관련도 | Netflix | 인기를 한눈에 | **good** — 순위 숫자는 Gasoek One 28px 이상(이미 규칙). |
| P2 | 주간 차트 등락 표시(빌보드식), 매출 기준 | Steam Charts | 흐름 | **good** — 한국식 ▲빨강 ▼파랑 + "NEW". 기준(무엇으로 매긴 순위인지)을 탭 이름에 명시. |
| P3 | 사람 투표 + 스태프로 매일 수상(Daily Feature, 2~5위) | Newgrounds | 사람이 고른 증거 | **adapt** — "오늘의 픽" 배지에 날짜와 큐레이터 이름. |
| P4 | 평가 수가 적으면 점수를 중앙값 기준 비례 감점, 원점수와 조정 점수 병기 | itch.io 잼 | 소수 평가 왜곡 | **adapt** — 잼 결과 카드에 "조정 점수 · 평가 n개"를 함께. 원점수는 상세에. |
| P5 | 잼 제출 목록 기본 정렬 무작위, "평가 적은 순" 정렬 | itch.io 잼 | 평가 쏠림 | **good** — 잼 아케이드 기본 셔플 + 평가 기간엔 "아직 평가 n개" 표시. |
| P6 | 친구 범위 기록(친한 친구 평점은 통계에서 제외 같은 세분화) | Letterboxd | 사적 공유 | **adapt**(후속) — 친구 활동 공개 범위는 계정 설정 단계에서. |
| P7 | 평점을 숨긴 실험에 대해 "낮은 평점 숨김은 오해를 부른다"는 개발자 우려 | Roblox DevForum | 신뢰 | **good**(교훈) — 숨기는 조건(10개 미만)을 툴팁이 아니라 상세 페이지에 공개 문장으로. |
| P8 | 친구 데려오기를 좋은 게임의 신호로 사용(랭킹 신호, 표시 아님) | Roblox 뉴스룸(2026) | 질 좋은 인기 | **adapt** — "같이 한 판 많이 한 게임" 랭킹 탭 후보(B등급 결정). |

### 2.6 메이커 존재감 (5)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| K1 | 모든 셀에 작가 이름(링크) | itch.io | 만든 사람이 보임 | **good** — 자모 얼굴 + 이름. 팀이면 얼굴 겹침 최대 3 + "외 2". |
| K2 | 개발자가 직접 정하는 라벨(이벤트 등) 요구 | Roblox DevForum | 메이커의 목소리 | **adapt** — "메이커 한마디"(20자) 를 한 줄 문맥 후보로, 큐레이션 이유보다 낮은 우선순위. |
| K3 | 작가 링크 같은 보조 링크는 꼭 필요할 때만, 누르기 쉽게 패딩 | Inclusive Components | 탭 정지 과다 | **good** — 카드 안 보조 링크는 메이커 하나뿐. 얼굴과 이름은 한 링크로 묶는다. |
| K4 | 메이커가 페이지 색 지정 | Playdate | 개성 | **adapt** — A13과 동일. |
| K5 | 메이커 얼굴을 아트 위 모서리에 | aDmD v6 | 사람이 보이게 | **adapt** — 아트 위 얼굴 + 아트 아래 이름이 중복된다. **아트 위 얼굴은 큰 카드(픽·표준)만**, 작은 행에선 이름 옆 16px 얼굴로. |

### 2.7 순위·목록 행 (5)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| R1 | 스몰 캡슐(462×174 → 184×69, 120×45)로 만든 목록 행 | Steam | 많은 항목을 촘촘히 | **adapt** — aDmD 행은 1:1 아이콘(48–64px)을 쓴다. 납작한 별도 아트를 또 받지 않는다. |
| R2 | 행 전체를 링크로 만드는 것은 안티패턴, 다른 칸 글자 복사도 막힘 | Adrian Roselli | 접근성 | **good** — 제목 링크를 행 전체로 늘리되, 행 안 버튼(참가·설치) 주변에 여백. |
| R3 | 기준별 순위 표(재미, 완성도, 혁신 등) | itch.io 잼 | 여러 잣대 | **adapt** — 잼 결과 페이지는 기준 탭 + 순위 행 재사용. |
| R4 | 순위 행의 큰 숫자 + 등락 | Netflix, Steam | 순서가 정보 | **good** — RankRow의 핵심. |
| R5 | 같은 게임이 여러 구역에 반복 노출 | Poki 홈 | 노출 극대화 | **avoid** — 한 화면에 같은 게임은 두 번까지만. 적은 카탈로그가 반복으로 더 빈약해 보인다. |

### 2.8 레이아웃 변형 (6)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| L1 | 크기가 섞인 타일 그리드(작은 94px, 큰 204·314px) | Poki | 시선 리듬 | **adapt** — 큰 타일은 **사람이 고른 픽에만**. 인기순으로 크기를 키우면 부익부. |
| L2 | 락업 = 헤더·콘텐츠·푸터 3영역 | Apple HIG | 카드 구조 일관성 | **good** — 모든 변형이 "아트 / 본문 / 하단 메타" 같은 뼈대를 공유. |
| L3 | 세로 2:3 커버 | CrazyGames, Steam 라이브러리 | 모바일·책장 | **avoid**(PC) — PC PlayGround엔 세로 카드 상황이 없다. 모바일 별도 디자인 때 재검토. |
| L4 | 세일용 세로 캡슐(748×896) | Steam | 시즌 페이지 | **avoid** — 세일이 없다. |
| L5 | 개수가 적으면 레일 대신 큰 카드 그리드 | 리서치 02 §5.4 | 빈약해 보임 | **good** — 레일 항목 4개 미만이면 픽 카드 2–3열로. |
| L6 | 디스커버리 큐를 페이지 이동 없이 오버레이로 | Steam(2026) | 연속 탐색 | **adapt**(후속) — "한 판 5분짜리 다음 거" 같은 연속 추천은 플레이 종료 화면에서. 카드 변형은 추가하지 않는다. |

### 2.9 빈 상태·로딩·대체 아트 (5)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| E1 | ThumbHash/BlurHash(대표색 포함, 투명도·비율까지) | evanw/thumbhash | 이미지 로딩 전 빈칸 | **good** — 업로드 때 ThumbHash 저장, 대표색은 최후 폴백. 수십 바이트라 D1 행에 넣어도 부담 없음. |
| E2 | 배경 이미지가 없으면 마지막 스크린샷으로 자동 생성 | Steam | 메이커 누락 | **good** — 1:1 아이콘이 없으면 16:9에서 크롭, 16:9도 없으면 E3. |
| E3 | 아트 없을 때 게임 ID 기반 결정적 패턴 + 큰 제목 | 리서치 02 §5.1 | 깨진 이미지 | **good** — 여기에 메이커 자모 얼굴을 크게 넣어 "사람"이 보이게. |
| E4 | 졸린 DmD 표정을 빈 상태에 | aDmD v6 | 빈 목록의 냉랭함 | **good** — 빈 라이브러리, 빈 방 목록. |
| E5 | 스켈레톤은 실제 카드와 같은 비율·같은 줄 수 | [관찰] YouTube 등 | 로딩 후 레이아웃 점프 | **good** — 스켈레톤에 반짝이는 쉬머는 `prefers-reduced-motion`에서 멈춤. |

### 2.10 접근성 (8)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| X1 | 카드 목록은 `ul/li`, 카드 제목은 같은 단계의 제목 요소 안 링크 | Inclusive Components | 개수 안내, 제목 탐색 | **good** |
| X2 | 카드 전체를 `<a>`로 감싸지 않는다(링크 이름이 수십 초짜리가 됨) | Adrian Roselli, Inclusive Components | 장황한 링크 | **good** |
| X3 | 제목 링크의 `::after`를 카드 전체로 늘리는 stretched link, 보조 버튼은 그 위 레이어 | Inclusive Components, Roselli | 전체 클릭 + 중첩 없음 | **good** — 단점(글자 선택 불가)은 카드 글자가 짧아 수용. |
| X4 | 이미지는 DOM상 제목 뒤, 화면에선 CSS `order`로 위 | Inclusive Components, Roselli | 제목 탐색 시 이미지 건너뜀 | **good** — 장식 아트는 `alt=""`(제목이 이미 이름). |
| X5 | 카드 단위 포커스 표시는 `:focus-within`, 호버와 같은 규칙에 묶지 않기 | Inclusive Components | 키보드 사용자 | **good** — 포커스 링 2px 3:1(이미 기준). |
| X6 | 기본 행동 영역에 다른 인터랙티브 요소 두지 않기, 카드당 주 행동 하나 | Material, Aetna 디자인 시스템 | 오클릭 | **good** — 카드 안 버튼은 최대 2개(저장, 빠른 플레이) + 메이커 링크. |
| X7 | 호버·포커스로 나타난 내용은 Esc로 닫을 수 있고, 그 위로 커서를 옮겨도 안 사라지고, 스스로 사라지지 않게 | WCAG 1.4.13 | 확대 사용자, 손떨림 | **good** — 플랫폼 칩 툴팁, 얼굴 스택 툴팁에 적용. |
| X8 | 상태를 색으로만 구분하지 않기(진행 막대, 접속 점) | YouTube 사례, WCAG 1.4.1 | 색약 | **good** — 초록 점 옆 "하는 중", 막대 옆 숫자. |

### 2.11 모바일·터치 (5)

| # | 아이디어 | 출처 | 푸는 문제 | 판정 |
|---|---|---|---|---|
| T1 | 터치에선 카드 탭 = 상세, 바로 실행 안 함 | 리서치 02 §5.2, Spotify 불만 | 실수 실행 | **good** |
| T2 | 모바일에선 클릭 후 게임 시작 전에 썸네일이 다시 보이므로 실제와 같아야 | Poki | 기대 불일치 | **good** — 로딩 화면 = 같은 커버 + 대표색. |
| T3 | 작은 화면에선 카드 사이 간격을 넓혀 오탭 방지 | Inclusive Components | 오탭 | **good** — 모바일 디자인 때 적용. |
| T4 | 호버가 없으니 미리보기는 상세에서 탭으로 | [관찰] 대부분 앱 | 데이터·배터리 | **good** — 모바일 카드에서 자동 재생 금지. |
| T5 | 초대 링크·파티 코드를 아무 메신저로 공유 | Apple Games | 같이 하기 진입 | **adapt** — 방 카드에 "초대 링크 복사" 보조 버튼(카톡 공유는 후속). |

> 합계: 아트 14 + 모션 15 + 정보 14 + 상태 13 + 사회적 증거 8 + 메이커 5 + 행 5 + 레이아웃 6 + 빈 상태 5 + 접근성 8 + 터치 5 = **98개**(중복 성격 제외 시 약 85개).

---

## 3. aDmD 카드 컴포넌트 세트 제안 (8종)

### 3.0 모든 카드가 공유하는 규칙

**뼈대(락업 3영역)**: 아트 → 본문(제목, 만든 사람) → 하단 메타(한 줄 문맥). 아트 위 글자는 배지·칩뿐이고 제목은 항상 아트 밖.

**아트 위 오버레이 자리(최대 3개, 서로 겹치지 않음)**

| 자리 | 들어가는 것 | 우선순위(한 자리에 하나) |
|---|---|---|
| 왼쪽 위 | 문맥 배지(아이콘 + 글자) | 오늘의 픽 > 새로 나옴(14일) > 업데이트(14일) > 친구가 하는 중 |
| 오른쪽 위 | 실행 칩 | 이 기기에서 안 됨(경고) > 설치·검사 통과 > 브라우저 / 같이(인원) |
| 왼쪽 아래 | 메이커 자모 얼굴(24px) | 큰 카드만 |
| 오른쪽 아래 | 호버·포커스 때 빠른 플레이(40px 원) | 브라우저 게임만 |
| 아트 아래 경계 | 진행 막대(3px, 아트 밖) | 이어하기 카드만 |

**한 줄 문맥 슬롯 우선순위**: 큐레이터 이유(픽 문맥일 때) > 친구 활동("친구 2명이 이번 주에 함") > 메이커 한마디 > 기본형 "장르 · 한 판 5분 · 브라우저".

**호버·포커스 공통**
- 카드 크기 고정, 2–4px 들어올림 + 아트 테두리 진하게. 포커스는 `:focus-within` 2px 링.
- 미리보기 영상: 약 400ms 머문 뒤 로드 시작, 첫 프레임 = 커버, 무음, 6초 이하 반복, 떠나면 즉시 정지. 페이지 전체에서 한 번에 하나. "움직이는 미리보기" 설정 꺼짐이나 `prefers-reduced-motion`이면 영상 없음.
- 호버로만 보이는 **정보**는 없다. 호버로 나타나는 것은 빠른 플레이 버튼(키보드 포커스로도 나타남, 상세 페이지에 같은 행동이 있음)뿐.

**마크업 공통**: `ul > li > article`, 제목 `h3 > a`(stretched `::after`), 아트는 DOM상 제목 뒤 + CSS `order`, 아트 `alt=""`, 보조 버튼(저장·빠른 플레이)과 메이커 링크는 `position: relative; z-index` 로 링크 레이어 위. 보조 버튼 이름은 "○○ 저장", "○○ 바로 플레이"처럼 게임명 포함.

**미리보기 영상 사양(메이커용, B등급 제안)**: 16:9, 640×360 이상, 6초 이하, 무음, mp4(H.264) 또는 webm, 1.5MB 이하, 실제 플레이만, 첫 프레임 = 커버, 커서·검은 화면·홍보 문구 금지. 저장 위치·용량 비용은 §4 열린 질문.

### 3.1 GameCard — 표준 게임 카드

- **쓰는 곳**: 카탈로그 그리드(5열), 홈 레일(새로 나온 게임, 업데이트된 게임), 검색 결과 페이지, 게임 상세의 "비슷한 게임", 메이커 프로필의 게임 목록, 다운로드 게임 목록, **잼 아케이드(잼 모드)**.
- **비율**: 아트 16:9. 카드 폭 220–260px(1280 컨테이너 5열).
- **정보 층(우선순위 순)**: ① 아트 ② 제목(15px, 2줄까지) ③ 만든 사람(16px 얼굴 + 이름 13px, 팀은 얼굴 겹침) ④ 한 줄 문맥(13px, 기본형 "퍼즐 · 한 판 5분 · 브라우저") ⑤ 평점(리뷰 10개 이상일 때만, "추천 92% · 38") ⑥ 아트 위 배지·칩.
- **호버·포커스**: 공통 규칙 + 미리보기 영상 + 빠른 플레이. 저장 버튼은 호버·포커스 때 아트 오른쪽 위 칩 아래에 나타나고, 저장된 뒤엔 항상 보임(터치 기기에선 항상 보임).
- **상태**: 새로 나옴, 업데이트, 저장됨, 해봄, 이 기기에서 안 됨, 설치형(검사 통과), 친구가 하는 중, 점검 중(아트 흐리게 + "점검 중" 글자). **잼 모드**: 평가 기간엔 "아직 평가 n개"를 문맥 슬롯에, 결과 후엔 "3위 · 조정 4.12 · 평가 21", 기본 셔플 정렬, 순위 배지는 결과 발표 후에만.
- **보여주지 않을 것**: 누적 플레이 수, 다운로드 수, 태그 3개 이상, "무료", 리뷰 10개 미만 평점, 설명 문단, 호버 때만 나타나는 글자 정보, 아트 위 제목.

### 3.2 PickCard — 큐레이션 픽 카드

- **쓰는 곳**: 홈 "오늘의 픽", 테마 컬렉션 상단, 시간 자 섹션의 대표 게임, 카탈로그가 적을 때 레일 대체(L5), 메이커 프로필의 대표작 1개.
- **비율**: 아트 16:9를 크게(카드 폭 380–600px, 2–3열). 카드 바탕은 **게임색 필드**(대표색, 대비 자동 검사).
- **정보 층**: ① 아트 ② 큐레이션 문맥 배지(아트 왼쪽 위, 아이콘 + 글자, 그라운드 색) ③ 제목(18–20px) ④ **큐레이터 말풍선**: 큐레이터 자모 얼굴 + 고른 이유 1–2문장 + 이름·날짜 ⑤ 만든 사람 ⑥ "한 판 15분 · 브라우저 · 2인".
- **호버·포커스**: 공통 규칙. 미리보기는 큰 카드일수록 효과가 크므로 우선 적용. 빠른 플레이 버튼은 말풍선 아래 글자 버튼("바로 플레이")으로 바꿔도 된다(큰 카드라 공간 있음).
- **상태**: 저장됨, 해봄("해본 게임이에요" 작은 글자), 이 기기에서 안 됨, 다음 주 픽 예고(아트 흐림 + "다음 수요일 공개", 화면에 1장까지).
- **보여주지 않을 것**: 평점·리뷰 수(큐레이터의 말과 숫자가 경쟁), 순위, 여러 개의 배지, 큐레이터 없는 "추천" 문구(알고리즘 추천엔 픽 카드를 쓰지 않는다).

### 3.3 RankRow — 순위 행

- **쓰는 곳**: 홈 탭 랭킹 격자(이번 주 / 새 게임 / 같이 하기 등), 랭킹 페이지, 잼 결과(기준별 탭).
- **비율**: 1:1 아이콘 56px(랭킹 페이지 64px). 행 높이 72px 안팎.
- **정보 층**: ① 순위 숫자(Gasoek One 28px, 1–3위는 그라운드 색) ② 등락(▲3 빨강 / ▼1 파랑 / NEW / −) ③ 아이콘 ④ 제목 ⑤ 만든 사람(16px 얼굴 + 이름) ⑥ 한 줄 문맥(장르 · 한 판 시간) ⑦ 잼 모드: 조정 점수 · 평가 수.
- **호버·포커스**: 행 배경 옅게(neutral), 제목 밑줄. 미리보기 영상 없음(아이콘이 작아 효과 없음, 데이터 낭비). 빠른 플레이 없음.
- **상태**: 해봄(제목 옆 작은 체크 + "해봄" 숨김 텍스트), 저장됨은 표시 안 함(순위 맥락에 소음).
- **보여주지 않을 것**: 순위 산정 숫자 자체(플레이 수 등) — 기준은 탭 이름과 섹션 설명에 글로. 배지·칩 전부(행이 아니라 표가 됨).

### 3.4 ContinueCard — 이어하기 카드

- **쓰는 곳**: 홈 이어하기 한 줄(회원), 라이브러리 상단 "최근 플레이", 플레이 종료 화면의 "이어서 할 것".
- **비율**: 아트 16:9, GameCard보다 작게(180–200px, 한 줄 6개). 가로 레일.
- **정보 층**: ① 아트 ② 진행 막대(아트 바로 아래 3px) + 진행 글자("3/8 스테이지", 메이커가 진행률을 보낼 때만) ③ 제목 ④ "어제 플레이 · 브라우저" ⑤ 업데이트 배지(마지막 플레이 이후 새 버전이면).
- **호버·포커스**: 빠른 플레이 = 이 카드의 주 행동. 그래서 이 카드는 **카드 전체가 "이어하기" 링크**(상세가 아니라 플레이 화면으로)이고, 보조 링크로 "상세"만 둔다. 미리보기 영상 없음(이미 아는 게임).
- **상태**: 진행 중, 엔딩 봄, 업데이트 있음, 설치형이면 "설치됨 / 업데이트 필요", 이 기기에서 안 됨(다른 기기에서 하던 게임, "PC에서 이어하기" 글자), 점검 중.
- **보여주지 않을 것**: 메이커 얼굴(이미 아는 게임, 공간 절약 — 이름은 상세에서), 평점, 문맥 배지, 플레이 시간 누적("10h" 같은 약어 — 기존 감사 E-5에서 지적).
- **빈 상태**: 기록이 없으면 줄 자체를 숨긴다(리서치 02 §5.3).

### 3.5 MiniRow — 작은 게임 행

- **쓰는 곳**: 헤더 검색 드롭다운(자동완성), 데브로그·게시글 안 게임 언급, 메이커 소식 목록, 멀티 방 만들기의 게임 선택, 알림 목록.
- **비율**: 1:1 아이콘 32–40px, 행 높이 44px 이상(터치 목표).
- **정보 층**: ① 아이콘 ② 제목(검색어 일치 부분 굵게) ③ 만든 사람 이름(얼굴 없이 또는 16px) ④ 실행 방식 글자("브라우저"/"설치") — 검색 드롭다운에서만.
- **호버·포커스**: 검색 드롭다운에선 `aria-activedescendant`로 방향키 이동, 행 배경 옅게. 영상·버튼 없음.
- **상태**: 없음(최대 "해봄" 정도). 
- **보여주지 않을 것**: 배지, 평점, 한 줄 문맥(드롭다운은 빨리 훑는 곳).

### 3.6 LibraryRow — 라이브러리 행 (설치형 포함)

- **쓰는 곳**: 내 라이브러리(해본 게임, 저장한 게임, 설치한 게임 탭), 다운로드 관리, 메이커가 내린 게임 보관.
- **비율**: 1:1 아이콘 64px 또는 16:9 썸네일 112px. 표처럼 열이 맞는 넓은 행.
- **정보 층**: ① 아이콘 ② 제목 + 만든 사람 ③ 실행 방식과 상태("브라우저" / "Windows · v1.2.0 · 312MB · 검사 통과 11월 20일") ④ 마지막 플레이 시각 ⑤ 행 끝 행동 버튼 1개(상태에 따라 "플레이" / "이어하기" / "설치 파일 받기" / "업데이트 받기") ⑥ 더보기 메뉴(저장 해제, 기록 지우기).
- **호버·포커스**: 행 배경 옅게. 제목 링크(상세) stretched, 행 끝 버튼은 위 레이어 + 주변 여백(R2). 영상 없음.
- **상태**: 저장됨, 해봄, 진행률, 설치형: 받을 수 있음 / 새 버전 있음 / 검사 중 / 검사 통과 / 검사 경고(받기 버튼 비활성 + 이유 글자), 이 기기에서 안 됨, 점검 중, 메이커가 내림(기록은 남음, 행동 버튼 없음).
- **보여주지 않을 것**: 미리보기, 큐레이션 배지, 평점, 친구 활동. "설치됨"은 웹이 확인할 수 없으니 **표시하지 않는다**(받은 기록만 "받음 11월 20일"). 
- **비고**: 웹 사이트는 사용자 PC에 실제로 설치됐는지 알 수 없다. 그래서 "설치됨" 대신 "받은 버전 v1.1 → 새 버전 v1.2" 처럼 **받은 기록 기준**으로 말한다.

### 3.7 RoomCard — 멀티플레이 방 카드

- **쓰는 곳**: "같이 하기" 페이지의 열린 방 목록, 게임 상세의 방 목록, 친구가 만든 방 알림, 홈 "지금 같이 할 사람" 모듈.
- **비율**: 가로 카드, 1:1 게임 아이콘 48px + 본문. 아트가 주인공이 아니다(방 정보가 주인공).
- **정보 층**: ① 방 이름 ② 상태 + 인원("대기 중 · 3/4명", 숫자가 행동 정보라 크게) ③ 방장 자모 얼굴 + 참가자 얼굴 겹침 ④ 게임 아이콘 + 게임 제목(게임 상세 안에선 생략) ⑤ 조건("초보 환영 · 한 판 10분 · 음성 없음") ⑥ "참가" 버튼 + "초대 링크 복사".
- **호버·포커스**: 카드 전체 클릭은 하지 않는다 — 참가는 되돌리기 어려운 행동이라 **명시적 "참가" 버튼만**. 방 이름은 방 상세(참가 전 미리보기) 링크.
- **상태**: 대기 중, 시작 직전(카운트다운 글자), 진행 중(관전 가능 여부), 가득 참(버튼 비활성 + "가득 참"), 친구가 있음(친구 얼굴을 앞에), 비밀번호 방(자물쇠 + "비공개").
- **보여주지 않을 것**: 게임 커버 큰 아트, 게임 평점, 누적 플레이 수, 방장 레벨·등급(감사 M-4).
- **빈 상태**: 졸린 DmD + "지금 열린 방이 없어요" + "방 만들기" 버튼.

### 3.8 TimePin — 시간 자 핀

- **쓰는 곳**: 홈·카탈로그의 "시간으로 고르기" 눈금자(0분 → 60분+) 위에 꽂힌 게임들. aDmD에만 있는 화면.
- **비율**: 1:1 아이콘 40–48px, 눈금 위치 = 한 판 시간.
- **정보 층**: ① 아이콘 ② 자 위 위치(그 자체가 "한 판 시간" 정보) ③ 포커스·호버 때 붙는 작은 라벨: 제목 + "한 판 7분" ④ 선택하면 자 아래에 GameCard 하나가 펼쳐짐.
- **호버·포커스**: 라벨은 WCAG 1.4.13을 지킨다(Esc로 닫기, 라벨 위로 커서 이동 가능, 스스로 사라지지 않음). 키보드는 좌우 방향키로 핀 사이 이동(`role="listbox"` 또는 핀 목록 + 로빙 탭인덱스). **위치 정보만으로 전하지 않도록** 각 핀의 접근성 이름에 "한 판 7분"을 넣고, 같은 내용을 일반 목록으로도 볼 수 있는 "목록으로 보기" 전환을 둔다.
- **상태**: 해봄(아이콘 테두리), 선택됨.
- **보여주지 않을 것**: 메이커, 평점, 배지 전부 — 선택 후 펼쳐지는 GameCard가 맡는다.

### 3.9 상황 → 변형 매핑

| 상황 | 변형 |
|---|---|
| 홈 메인 배너 | (카드 아님 — 배너 컴포넌트) |
| 홈 오늘의 픽 / 큐레이션 레일 | PickCard |
| 홈 이어하기 | ContinueCard |
| 홈 시간으로 고르기 | TimePin → GameCard |
| 홈 새로 나온 게임 · 업데이트된 게임 레일 | GameCard |
| 홈 랭킹 탭 격자 · 랭킹 페이지 | RankRow |
| 카탈로그 그리드 · 검색 결과 페이지 | GameCard |
| 헤더 검색 드롭다운 | MiniRow |
| 게임 상세 "비슷한 게임" | GameCard(4개, 미리보기 끔 — 상세에서 또 영상이 뜨면 산만) |
| 게임 상세 방 목록 · 같이 하기 페이지 | RoomCard |
| 라이브러리 · 다운로드 관리 | LibraryRow (+ 상단 ContinueCard 한 줄) |
| 메이커 프로필 | PickCard(대표작 1) + GameCard |
| 잼 아케이드(출품작) | GameCard 잼 모드 |
| 잼 결과 | RankRow 잼 모드 |
| 데브로그·게시글 속 게임 언급, 알림 | MiniRow |
| 다운로드 게임 둘러보기 | GameCard(실행 칩 "설치 · 검사 통과") |

### 3.10 상태 × 변형 매트릭스

| 상태 | GameCard | PickCard | RankRow | ContinueCard | MiniRow | LibraryRow | RoomCard | TimePin |
|---|---|---|---|---|---|---|---|---|
| 새로 나옴(14일) | 배지 | 배지 | NEW(등락 자리) | — | — | — | — | — |
| 업데이트(14일) | 배지 | — | — | 배지 | — | 글자 | — | — |
| 저장됨 | 아이콘 | 아이콘 | — | — | — | 탭 | — | — |
| 해봄 | 작은 표시 | 글자 | 체크 | (전제) | 선택 | 탭 | — | 테두리 |
| 진행률 | — | — | — | 막대+글자 | — | 글자 | — | — |
| 설치형 · 검사 통과 | 칩 | 칩 | — | 칩 | 글자 | 상세 글자 | — | — |
| 새 버전 받기 | — | — | — | 글자 | — | 버튼 | — | — |
| 이 기기에서 안 됨 | 칩(경고) | 칩 | — | 글자 | — | 글자 | 글자 | — |
| 친구가 하는 중 | 배지/문맥 | — | — | — | — | — | 얼굴 앞에 | — |
| 지금 대기 n명 | — | — | — | — | — | — | 핵심 | — |
| 점검 중 · 내려감 | 흐림+글자 | 숨김 | 숨김 | 흐림+글자 | 숨김 | 글자 | 숨김 | 숨김 |
| 잼 평가 중 / 결과 | 잼 모드 | — | 잼 모드 | — | — | — | — | — |

---

## 4. 결정이 필요한 것 (aDmD 결정 등급)

| 질문 | 등급 | 추천 |
|---|---|---|
| 호버 미리보기 영상을 받을지, 받으면 어디 저장할지(Cloudflare R2 무료 한도 10GB 저장·외부 전송 무료 [검증 필요]) | **A**(비용·호스팅) | (추천) MVP는 영상 없이 **정적 커버 + 스크린샷 2장 교차 페이드**로 시작, 영상은 저장 비용 확인 후 — 무료 원칙과 충돌 위험이 없다. |
| 1:1 아이콘을 필수로 할지 | B | (추천) 선택 + 16:9에서 자동 크롭 기본값 — 메이커 부담 최소화. |
| 평점 표기 방식 | B | (추천) "추천 92% · 38"(비율 + 표본) — 별점 소수점보다 정직하다. |
| 카드에 "해봄" 표시와 "해본 게임 숨기기" 필터 | B | (추천) 둘 다 — GOG 사용자 수요가 증명. |
| 친구 활동 공개 기본값 | **A**(개인정보·핵심 UX) | (추천) 기본 비공개, 첫 친구 추가 때 묻기. |

---

## 5. 하지 말 것 요약

- 아트 위 제목·설명·평점·"무료"·"NEW" 글자(메이커가 넣는 것도, 플랫폼이 넣는 것도 배지 자리 밖에서는 금지).
- 누적 플레이 수, 다운로드 수, 레벨·등급을 카드에.
- 호버 때만 나타나는 정보, 호버 확장으로 이웃 카드 밀기, 그리드 자동 재생, 커서가 지나가기만 해도 재생.
- 카드 전체를 `<a>`로 감싸기, 카드 안 버튼 3개 이상, 가운데 큰 재생 버튼.
- 인기순으로 카드 크기 키우기, 같은 게임을 한 화면에 세 번 이상.
- 진행·접속 상태를 색으로만.
- 웹이 확인할 수 없는 "설치됨" 표시.

---

## 출처

### Steam
- [Steamworks: Standard Assets (캡슐 크기·용도)](https://partner.steamgames.com/doc/store/assets/standard)
- [Steamworks: Graphical Asset Rules (캡슐 금지 문구, 아트워크 오버라이드)](https://partner.steamgames.com/doc/store/assets/rules)
- [Steamworks: Steam Deck 호환성 검토](https://partner.steamgames.com/doc/steamdeck/compat)
- [GamingOnLinux: Steam store home page gets a refresh in beta (2026-04)](https://www.gamingonlinux.com/2026/04/steam-store-home-page-gets-a-refresh-in-beta-plus-another-linux-steamrt3-beta-fix)
- [PCGamesN: Steam store refresh (2026-06)](https://www.pcgamesn.com/steam/store-refresh)
- [indiegamejoe: Steam just changed how players see your game](https://indiegamejoe.com/steam-just-changed-how-players-see-your-game-and-most-devs-will-miss-this/)
- [TweakTown: Valve updates Steam with a Store page refresh](https://www.tweaktown.com/news/110831/valve-updates-steam-with-store-page-refresh-designed-to-make-it-easier-find-new-games/index.html)
- [PCGamesN: Steam Discovery Queue Labs update](https://www.pcgamesn.com/steam/discovery-queue-update)
- [PC Gamer: Steam Charts update (빌보드식 차트)](https://pcgamer.com/steam-charts-update)
- [PC Gamer: Steam now tells you why it recommended a game](https://www.pcgamer.com/steam-now-tells-you-why-it-recommended-a-game-to-you)
- [PC Gamer: AI-generated capsule art 비판 (2026)](https://www.pcgamer.com/gaming-industry/steam-week-in-review-spammy-ai-generated-capsule-art-is-a-pox-and-it-makes-browsing-steam-less-fun/)

### itch.io
- [itch.io 브라우저 무료 게임 목록 (셀 구조)](https://itch.io/games/free/platform-web)
- [itch.io 포럼: 커버 권장 크기 630×500](https://itch.io/post/5308783)
- [itch.io 포럼: GIF 커버가 호버 때만 움직임](https://itch.io/post/14408781)
- [itch.io 포럼: 잼 출품작 정렬 (평가 적은 순)](https://itch.io/t/4614305/game-jam-entries-list-sort-by-top-rated)
- [itch.io 포럼: 평가 수 기반 가중 점수 설명](https://itch.io/post/855450)
- [itch.io: GMTK 2024 잼 결과](https://itch.io/jam/gmtk-2024/results)

### Poki / CrazyGames
- [Poki for Developers: Game thumbnail](https://developers.poki.com/guide/game-thumbnail)
- [Poki for Developers: Your game page (애니메이션 썸네일)](https://developers.poki.com/guide/your-game-page)
- [Poki 홈](https://poki.com/)
- [CrazyGames Docs: Game covers (커버·미리보기 영상)](https://docs.crazygames.com/requirements/game-covers/)
- [CrazyGames 홈](https://www.crazygames.com/)

### Roblox / Kongregate / Newgrounds
- [Roblox DevForum: Player Count Changes on Experience Tiles (2024-04)](https://devforum.roblox.com/t/player-count-changes-on-experience-tiles/2914339)
- [Roblox DevForum: Improving Game Discovery With Relevant Information (2025-08)](https://devforum.roblox.com/t/upcoming-tests-improving-game-discovery-with-relevant-information/3907203)
- [Roblox Newsroom: Optimizing discovery (2026-06)](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox)
- [Kongregate Launch 101](https://docs.kongregate.com/docs/kongregate-launch-101)
- [Kongregate FAQ](https://www.kongregate.com/pages/resources%7Cfaq)
- [Wikigrounds: Flash Portal Awards](https://newgrounds.fandom.com/wiki/Flash_Portal_Awards)

### GOG / Epic / Xbox / Nintendo / Playdate
- [GOG 포럼: please show owned games as owned](https://www.gog.com/forum/general/please_show_owned_games_as_owned)
- [GOG 포럼: hide games I already bought](https://www.gog.com/forum/general/hide_games_i_already_bought)
- [Epic 도움말: 위시리스트 추가·제거](https://www.epicgames.com/help/c-41804731/a20128508)
- [Epic 도움말: 주간 무료 게임](https://www.epicgames.com/help/c-41804731/c-39278613/a21954037)
- [VGC: Epic 다음 무료 게임은 미스터리 게임](https://videogameschronicle.com/news/the-epic-games-stores-next-free-title-is-a-mystery-game)
- [Xbox Wire: July 2025 update](https://news.xbox.com/en-us/2025/07/28/xbox-july-update-more-ways-to-play/)
- [Nintendo World Report: Switch 2 리뷰(eShop)](https://www.nintendoworldreport.com/review/71350)
- [Digital Trends: Switch 2 eShop improvements](https://www.digitaltrends.com/gaming/tnintendo-switch-2-eshop-improvements/)
- [Playdate 도움말: Catalog에 게임 올리기](https://help.play.date/ja/developer/publishing-in-catalog)

### Apple / Netflix / YouTube / Spotify / Letterboxd / 카카오페이지
- [Apple Newsroom: Introducing the Apple Games app (2025-06)](https://www.apple.com/newsroom/2025/06/introducing-the-apple-games-app-a-personalized-home-for-games/)
- [Apple HIG: Lockups](https://developer.apple.com/design/human-interface-guidelines/lockups)
- [Apple HIG: Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)
- [Apple 커뮤니티: TV 앱 Up Next 진행 표시](https://discussions.apple.com/thread/252906057)
- [Netflix: See what's popular on Netflix (Top 10)](https://about.netflix.com/news/see-whats-popular-on-netflix)
- [CSS-Tricks: Netflix식 호버 확장 카드](https://css-tricks.com/?p=305681)
- [MacRumors: Netflix TV 앱 재설계 테스트 (2024-06)](https://www.macrumors.com/2024/06/06/netflix-tv-app-redesign/)
- [Netflix Tudum: TV에서 Netflix 게임 하기](https://www.netflix.com/tudum/articles/how-to-play-netflix-games-on-tv)
- [9to5Google: YouTube 데스크톱 미리보기 플레이어 (2021)](https://9to5google.com/2021/01/13/youtube-on-desktop-gains-pop-out-preview-player-on-home-feed/)
- [Android Police: YouTube 썸네일 진행 막대 테스트 (2016)](https://www.androidpolice.com/2016/05/11/youtube-is-testing-a-new-progress-bar-showing-how-far-you-were-in-a-video/)
- [9to5Google: YouTube 진행 막대 색 (2022)](https://9to5google.com/2022/12/20/youtube-progress-bar-red/)
- [Chrome 웹 스토어: YouTube 진행 막대 색 확장(색약 언급)](https://chromewebstore.google.com/detail/gmgldnaadbkmkanlgdhohbfddgkhjfng)
- [Spotify 커뮤니티: 라이브러리 호버 버튼 불만](https://community.spotify.com/t5/Your-Library/I-dislike-the-mouse-over-buttons-in-library/td-p/7078716)
- [Letterboxd: Welcome (포스터에서 기록하기)](https://letterboxd.com/welcome/)
- [카카오: 카카오페이지 서비스 소개](https://www.kakaocorp.com/service/KakaoPage)
- [바이라인네트워크: 카카오페이지가 달라졌다 (2022)](https://byline.network/2022/09/22-202/)

### 접근성
- [Inclusive Components: Cards (Heydon Pickering)](https://inclusive-components.design/cards/)
- [Adrian Roselli: Block Links, Cards, Clickable Regions, Rows, Etc.](https://adrianroselli.com/2020/02/block-links-cards-clickable-regions-etc.html)
- [W3C: Understanding SC 1.4.13 Content on Hover or Focus](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus)
- [W3C: Understanding SC 2.2.2 Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide)
- [W3C: Understanding SC 1.4.1 Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color)
- [Material Design 2: Cards](https://m2.material.io/components/cards)
- [Aetna Design System: Card](https://design.aetna.com/web/card.html)
- [eBay Evo: Card accessibility](https://opensource.ebay.com/evo-web/components/card/accessibility)

### 성능·로딩·호버 의도
- [web.dev: Lazy loading video](https://web.dev/articles/lazy-loading-video)
- [Chrome for Developers: Lazy load video and audio](https://developer.chrome.com/docs/modern-web-guidance/guides/performance/lazy-load-video-and-audio)
- [Baymard: Dropdown menu flickering (호버 지연 300–500ms)](https://baymard.com/blog/dropdown-menu-flickering-issue)
- [NN/g: Timing exposing content](https://www.nngroup.com/articles/timing-exposing-content)
- [GitHub: evanw/thumbhash](https://github.com/evanw/thumbhash)
- [VirusTotal Docs: How it works](https://docs.virustotal.com/docs)

### 내부 문서
- [02-concept-ground.md](../02-concept-ground.md) — 카드 4층, v6 카드 규칙
- [02-craft-principles.md](02-craft-principles.md) — 에셋 규격, 플레이 CTA, 빈 상태
