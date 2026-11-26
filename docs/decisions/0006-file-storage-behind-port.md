# 0006. 설치 파일 저장: Cloudflare R2, 파일 저장 포트 뒤에 격리

- 상태: 승인 (2026-11-26, 사용자 승인)
- 등급: A
- 근거 조사: [`docs/product/research-scan-storage.md`](../product/research-scan-storage.md)

## 배경

설치형 게임(.exe · .dmg · .apk · zip)을 무료로 저장하고 내려받게 해야 한다. Worker 는 요청 본문 100MB · 메모리 128MB · CPU 10ms 라서 파일을 직접 받거나 해시할 수 없다.

사용자 요구: **"개발할 때 언제든지 교체할 수 있도록 구조를 설계하라. 극단적으로는 구글 드라이브로 교체할 수도 있어야 한다."**

## 선택지

| 후보 | 무료 | 장점 | 단점 |
| --- | --- | --- | --- |
| **Cloudflare R2** | 10GB · 쓰기 100만/월 · 읽기 1천만/월 · 전송 무료 | 스택 일치, 서명된 업로드·다운로드 주소, 분할 업로드 | 활성화 때 결제수단 등록을 요구할 수 있음 |
| Backblaze B2 | 10GB, 카드 없음 | 카드 불필요 | 공급자 추가 |
| Google Drive | 15GB(개인 계정) | 사용자가 이미 가진 공간 | 서명된 주소 대신 업로드 세션·공유 권한 모델, 직접 다운로드 대역폭 제한 |
| GitHub Releases | 무료 | — | 남의 바이너리 배포 → 약관·권리 위험 |

## 결정

- 운영 저장소: **Cloudflare R2**. 결제수단 등록이 필요하면 **사용자가 직접** 한다(무료 범위 안에서 운영).
- 설치 파일 한 개당 **최대 500MB**.
- **모든 파일 저장 접근은 `FileStorage` 포트 뒤의 어댑터에서만** 한다. 라우트·도메인은 R2 API 를 모른다.

### 포트 설계 — 가장 약한 저장소(구글 드라이브)도 구현할 수 있는 최소 공통분모

```ts
// src/lib/server/ports/file-storage.ts (구현 단계에서 작성)
export type StoredFileKey = string;            // 우리 쪽 키(uuid). 저장소의 내부 id 와 분리
export type UploadTarget =
  | { kind: 'presigned-multipart'; uploadId: string; partUrls: string[]; partSize: number } // R2 · S3 · B2
  | { kind: 'resumable-session'; sessionUrl: string };                                       // Google Drive
export interface FileStorage {
  createUpload(input: { key: StoredFileKey; zone: 'quarantine'; size: number; contentType: string }): Promise<UploadTarget>;
  completeUpload(key: StoredFileKey, proof: unknown): Promise<{ size: number }>;
  promote(key: StoredFileKey, from: 'quarantine', to: 'public'): Promise<void>; // 검사·승인 후에만
  downloadUrl(key: StoredFileKey, ttlSeconds: number): Promise<string>;        // 'public' 만
  remove(key: StoredFileKey): Promise<void>;
  stat(key: StoredFileKey): Promise<{ zone: 'quarantine' | 'public'; size: number } | null>;
}
```

- 키 ↔ 저장소 내부 id 매핑, 상태(`quarantine` · `public`), SHA-256 은 **D1(DB 포트)에 둔다** — 저장소를 바꿔도 메타데이터는 그대로.
- 업로드 방식은 `UploadTarget` 의 `kind` 로 갈라 브라우저 쪽 업로더가 둘 다 처리한다.
- 다운로드는 항상 Worker 를 거쳐 상태를 확인한 뒤 짧은 수명의 주소로 넘긴다(302).
- 어댑터: `adapters/r2/`(운영) · `adapters/memory/`(테스트) — 같은 `file-storage.contract.ts` 를 통과해야 한다. B2 · Google Drive 어댑터는 필요해질 때 추가.

## 결과

- 저장소 교체 = 어댑터 하나 추가 + `container.ts` 한 줄 + 파일 이관 스크립트.
- R2 무료 10GB 를 넘기 전에 경고(관리자 화면) — 오래된 보관 버전부터 정리.
