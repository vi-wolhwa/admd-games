# 페이지 목록 (설계·디자인 대상)

[scenarios.md](../product/scenarios.md) 의 요구사항에서 도출. 기존 캔버스에 있던 페이지는 "기존" 열에 표시 — 있어도 새로 설계한다(감사 결과: [00-audit.md](00-audit.md)).

- 기기: **D** 데스크톱 우선 설계, **M** 모바일 우선 설계, **D+M** 둘 다 1급
- 출시: L1 / L2 (PRD 에서 확정)

## PlayGround (플레이어) — `play.` 경로

| ID | 페이지 | 주요 요구사항 | 기기 | 출시 | 기존 |
| --- | --- | --- | --- | --- | --- |
| PG-HOME | 홈 (이번 호 · 이어하기 · 팔로우 소식) | R-HOME-01~02, R-CURA-01 | D+M | L1 | 홈 v2 |
| PG-ISSUE | 지난 호 보관함 / 호 상세 | R-CURA-01 | D+M | L1 | — |
| PG-COLL | 컬렉션 목록 · 컬렉션 상세 | R-CURA-02 | D+M | L1 | — |
| PG-CAT | 전체 게임(카탈로그 · 필터) | R-DISC-01~04 | D+M | L1 | 홈 섹션 |
| PG-SRCH | 검색 결과 | R-SRCH-01~02 | D+M | L1 | — |
| PG-GAME | 게임 상세 (상태별 변형: 처음 / 진행 중 / 완료 / 다운로드 / 멀티 / 이 기기 불가 / 리뷰 0) | R-DETAIL-*, R-MAKER-01 | D+M | L1 | 기획 문서만 |
| PG-PLAY | 플레이 셸 (로딩 · 플레이 · 일시정지 · 오류) | R-PLAY-01~07 | D (+M 터치 게임) | L1 | — |
| PG-END | 플레이 종료 화면 | R-PLAY-03, R-SOCIAL-05 | D+M | L1 | — |
| PG-DL | 다운로드 (플랫폼 선택 · 설치 안내) | R-DL-01~02 | D | L1 | — |
| PG-SCAN | 보안 검사 리포트 | R-TRUST-01~03 | D+M | L1 | — |
| PG-REVIEWS | 리뷰 전체 | R-REVIEW-* | D+M | L1 | — |
| PG-RANK | 리더보드 | R-RANK-01 | D+M | L2 | — |
| PG-ROOM | 같이 하기 대기실 | R-SOCIAL-03 | D | L2 | — |
| PG-MAKER | 메이커 페이지 (개인 / 팀) | R-MAKER-02~03 | D+M | L1 | — |
| PG-LIB | 내 라이브러리 (이어하기 · 저장 · 다운로드 · 기록) | R-LIB-* | D+M | L1 | 홈 섹션 |
| PG-PROFILE | 공개 프로필 | R-PROF-01 | D+M | L1 | — |
| PG-FRIENDS | 친구 | R-SOCIAL-02, 04 | D+M | L2 | — |

## MakersGround (메이커) — `make.` 경로

| ID | 페이지 | 주요 요구사항 | 기기 | 출시 | 기존 |
| --- | --- | --- | --- | --- | --- |
| MG-HOME | 홈 (게스트: 안내·쇼케이스 / 메이커: 내 작업 요약·할 일) | R-MK-01, R-COMM-05 | M+D | L1 | 홈 v2 |
| MG-START | 처음 올리는 분 안내 (규칙 · 형식 · 심사 시간) | R-MK-01 | M+D | L1 | — |
| MG-NEWMAKER | 메이커 프로필 만들기 | R-MK-02 | M+D | L1 | — |
| MG-UPLOAD | 업로드 마법사 (8단계, 임시저장) | R-MK-03~05 | D+M | L1 | — |
| MG-GAMES | 내 게임 목록 | R-MK-10 | M+D | L1 | 홈 패널 |
| MG-GAME | 게임 관리 (개요 · 상태 · 버전 · 스토어 정보 · 공개 설정) | R-MK-06~09 | M+D | L1 | — |
| MG-STATS | 게임 통계 | R-MK-11 | M+D | L1 | 홈 패널 |
| MG-FEEDBACK | 리뷰 · 피드백 · 응원함 | R-MK-12~13 | M+D | L1 | — |
| MG-LOG | 개발일지 목록 · 글 · 작성 | R-COMM-01, 04, 05 | M+D | L1 | 홈 패널 |
| MG-QA | 질문·답변 | R-COMM-02 | M+D | L2 | 홈 패널 |
| MG-RECRUIT | 팀원 모집 | R-COMM-03 | M+D | L2 | 홈 패널 |
| MG-JAMS | 잼 목록 · 잼 상세 · 제출 · 투표 · 결과 | R-JAM-* | M+D | L2 | 홈 패널 |
| MG-TEAM | 팀 관리 (팀원 초대 · 권한) | R-MK-02 | D | L2 | — |

## 공통

| ID | 페이지 | 요구사항 | 기기 | 출시 |
| --- | --- | --- | --- | --- |
| SH-NAV | 헤더 · 사이트 전환 · 모바일 탭바 · 푸터 | R-SYS-07 | D+M | L1 |
| SH-LOGIN | 로그인 / 계정 연결 모달 | R-ACCT-01~03 | D+M | L1 |
| SH-ONBOARD | 첫 로그인: 닉네임 · 얼굴 아바타 만들기 | R-ACCT-04 | D+M | L1 |
| SH-SETTINGS | 설정 (프로필 · 연결 계정 · 알림 · 공개 범위 · 데이터 · 탈퇴) | R-ACCT-05, R-NOTI-02 | D+M | L1 |
| SH-NOTI | 알림 센터 (패널 + 전체 페이지) | R-NOTI-01 | D+M | L1 |
| SH-REPORT | 신고 모달 | R-SAFE-* | D+M | L1 |
| SH-HELP | 고객센터 · FAQ · 문의 | R-SYS-06 | D+M | L1 |
| SH-LEGAL | 약관 · 개인정보 · 운영정책 · 저작권 신고 | R-SYS-05 | D+M | L1 |
| SH-ERR | 404 · 오류 · 점검 | R-SYS-01 | D+M | L1 |

## 운영자

| ID | 페이지 | 요구사항 | 기기 | 출시 |
| --- | --- | --- | --- | --- |
| AD-REVIEW | 심사 대기열 · 심사 상세 | R-ADMIN-01 | D (+M 승인) | L1 |
| AD-REPORTS | 신고 처리 | R-ADMIN-02 | D (+M) | L1 |
| AD-CURATE | 큐레이션 편집기 (이번 호 · 컬렉션) | R-ADMIN-03 | D | L1 |
| AD-NOTICE | 공지 · 점검 띠 | R-ADMIN-04 | D | L1 |
| AD-USERS | 사용자 · 운영 로그 | R-ADMIN-05 | D | L1 |

## 합계

PlayGround 17 · MakersGround 13 · 공통 9 · 운영 5 = **44 페이지** (상태 변형 제외). 템플릿은 디자인 시스템 단계에서 묶는다.
