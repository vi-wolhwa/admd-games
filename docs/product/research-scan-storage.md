# 조사: 무료 보안 검사 · 설치 파일 저장 (D4, 2026-11-26)

설치형 게임(.exe · .dmg · .apk · zip, 50MB~2GB)을 **완전 무료 · 약관 준수**로 검사하고 내려받게 할 방법. 사용자 결정 전 조사 자료다 — 결정은 [feedback-queue.md](../design/feedback-queue.md) D4.

## 확인한 사실 (공식 문서 기준, 일부 2차 출처 표시)

| 옵션 | 비용 · 카드 | 2GB 파일 | 약관 | 메모 |
| --- | --- | --- | --- | --- |
| VirusTotal 공개 API — 해시 조회만 | 무료 · 카드 없음 | 무관 | **회색**: "상업 제품·서비스에 쓰지 말 것", 비상업·학술만 | 하루 500회 · 분당 4회. 새로 만든 게임 파일은 대부분 "처음 보는 파일"로 나와 의미가 적음 |
| VirusTotal 공개 API — 파일 업로드 | 무료 | 650MB 까지 | 회색 + **올린 파일이 VT 파트너에게 공유됨** | 메이커의 미공개 빌드가 외부로 나감 → 비추천 |
| ClamAV + GitHub 제공 러너 | 무료 | 가능 | **위반 소지**: 호스팅 러너를 프로젝트와 무관한 작업에 쓰지 말 것 | 계정 정지 위험 |
| ClamAV(+ Windows Defender) + **셀프 호스트 러너**(본인 PC · VM) | 무료 | 가능 | 적합 | ClamAV 메모리 3GB+, 큰 파일은 제한값 올려야 함. PC 가 켜져 있어야 검사됨 |
| MetaDefender Cloud · Hybrid Analysis 무료 키 | 무료 | 제한 | 부적합(데모 · 연구 전용) | — |
| Cloudflare Containers | 유료(월 $5 플랜) | — | — | 무료 플랜 아님 |
| Cloudflare R2 | 무료 범위: 10GB · 쓰기 100만 · 읽기 1천만 /월 · 전송 무료 | 객체 5TiB · 분할 업로드 | 적합 | **활성화 때 결제수단 등록이 필요하다는 보고(2차 출처, 미확정)** |
| Backblaze B2 | 10GB 무료 · 카드 없음 | 가능 | 적합 | 공급자가 하나 늘어남 |
| GitHub Releases | 무료 | 2GiB 미만 | 남의 바이너리를 우리 저장소에서 배포 → 권리·약관 위험 | 주 저장소로 비추천 |

Workers 제한: 요청 본문 100MB · 메모리 128MB · CPU 10ms → **Worker 가 파일을 받거나 해시하지 않는다.** 브라우저가 저장소로 직접 올린다(서명된 업로드 주소).

## 추천 MVP 흐름 (무료 · 약관 준수)

1. Worker 가 서명된 분할 업로드 주소 발급 → 브라우저가 저장소 `quarantine/` 에 직접 업로드 → D1 상태 `scanning`.
2. 업로드 완료 → Worker 가 GitHub `repository_dispatch` 로 검사 작업 시작(`runs-on: self-hosted`).
3. 셀프 호스트 러너(전용 계정 또는 VM): 내려받기 → SHA-256 → ClamAV(+ Windows 면 Defender `MpCmdRun -Scan`) → 결과를 HMAC 서명 콜백으로 Worker 에 → D1 기록 → 통과 시 `public/` 으로 이동.
4. 다운로드: Worker 가 D1 에서 `clean` 확인 → 서명된 다운로드 주소로 302.
5. 화면 문구는 "문제를 찾지 못했어요"(안전 보장 단언 금지) — 이미 [보안 검사 리포트 시안](../design/05-playground-pages.md)에 반영.

## 위험

- 10GB 는 1~2GB 게임 10~20개면 찬다 → 초기엔 설치형 용량 상한(예: 500MB)을 두는 것을 검토.
- 본인 PC 가 꺼져 있으면 검사가 밀린다 → 화면에 "보통 10분, 길면 하루" 로 안내.
- 악성 파일이 러너로 내려온다 → 실행 금지 전용 계정 · VM 에서 돌린다.
- ClamAV · Defender 통과가 안전 보장은 아니다 → 신고 → 운영자 확인 흐름 필수.
- VirusTotal 은 수익화하는 순간 약관 위반 → 쓰더라도 해시 조회만, 비상업 동안만.

## 사용자 결정 (2026-11-26) → ADR 0006 · 0007

R2(파일 저장 포트 뒤 격리 — 구글 드라이브까지 교체 가능하게) · 셀프 호스트 러너 · **검사 통과 + 운영자 승인 두 관문 없이는 공개 안 됨** · VirusTotal 안 씀 · 설치 파일 500MB 상한.

### 당시 질문

1. **저장소**: R2(추천 — 스택 일치, 전송 무료, 단 결제수단 등록 필요할 수 있음 → 등록은 사용자가 직접) / Backblaze B2(카드 없음, 공급자 추가).
2. **검사 실행 위치**: 셀프 호스트 러너(추천 — 약관 안전, 본인 PC 또는 VM 필요) / GitHub 제공 러너(편하지만 약관 위반 소지).
3. **VirusTotal 해시 조회**: 쓰지 않음(추천 — 새 파일엔 효과가 적고 약관 회색) / 비상업 기간만 사용.
4. **MVP 에 설치형을 넣을지**: 넣음(킥오프 요구) / 브라우저 게임만 먼저 출시하고 설치형은 L2.

## 출처

- VirusTotal: https://docs.virustotal.com/reference/public-vs-premium-api · https://docs.virustotal.com/docs/difference-public-private · https://docs.virustotal.com/reference/files-scan
- Cloudflare: https://developers.cloudflare.com/workers/platform/limits/ · https://developers.cloudflare.com/r2/pricing/ · https://developers.cloudflare.com/r2/platform/limits/ · https://developers.cloudflare.com/r2/get-started/ · https://developers.cloudflare.com/containers/pricing/
- GitHub: https://docs.github.com/en/billing/concepts/product-billing/github-actions · https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features · https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- ClamAV: https://docs.clamav.net
- 기타: https://www.opswat.com/docs/mdcloud/integrations/public-apis · https://www.backblaze.com/blog/free-isnt-always-free-a-guide-to-free-cloud-tiers/ · https://tech-insider.org/how-to-set-up-cloudflare-r2-2026/ (R2 카드, 2차 출처)
