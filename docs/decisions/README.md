# 결정 기록

- A등급 결정은 `NNNN-제목.md` ADR(Architecture Decision Record: 배경 · 선택지 · 결정 · 이유 · 결과)로 남긴다.
- B등급 결정은 [log.md](log.md) 에 한 줄씩 남긴다. 사용자가 언제든 뒤집을 수 있다.
- 결정을 뒤집을 때는 기존 ADR 을 지우지 않고 상태를 `대체됨 → NNNN` 으로 바꾼 뒤 새 ADR 을 쓴다.

| 번호 | 제목 | 상태 |
| --- | --- | --- |
| [0001](0001-hosting-cloudflare-workers.md) | 호스팅: Cloudflare Workers 무료 플랜 | 승인 |
| [0002](0002-framework-sveltekit.md) | 프레임워크: SvelteKit | 승인 |
| [0003](0003-database-d1-behind-ports.md) | DB: D1 + Drizzle, 포트/어댑터 뒤에 격리 | 승인 |
| [0004](0004-auth-better-auth.md) | 인증: better-auth (게스트 → OAuth) | 승인 (미구현) |
| [0005](0005-repository-and-workflow.md) | 저장소·모노레포·브랜치·커밋 규칙 | 승인 |
| [0006](0006-file-storage-behind-port.md) | 설치 파일 저장: R2, 파일 저장 포트 뒤에 격리 | 승인 (미구현) |
| [0007](0007-scan-and-approval-gate.md) | 보안 검사(셀프 호스트 러너) + 운영자 승인 필수 | 승인 (미구현) |
| [0008](0008-mvp-product-defaults.md) | MVP 기본값: 라이트·다크(개정) · 스크린샷 미리보기 · 활동 기본 공개 | 승인 |
| [0009](0009-positive-feedback-and-card-media.md) | 추천은 개수만(싫어요 없음) · 카드 호버 미디어 · 미디어 5개 이상 | 승인 (2026-11-27) |
| [0010](0010-tags-and-catalog-loading.md) | 태그는 공개된 게임에서 생김(빈 태그 숨김) · 전체 게임은 무한 스크롤(커서) | 승인 (2026-11-27) |
| [0011](0011-play-states-favorites-and-control-borders.md) | 플랫폼이 아는 것만 약속(이어하기 · 다시 하기) · 추천/리뷰 로그인만 · 즐겨찾기(별) · 누를 수 있는 것은 테두리 · 문제 알리기 | 승인 (2026-11-27) |
