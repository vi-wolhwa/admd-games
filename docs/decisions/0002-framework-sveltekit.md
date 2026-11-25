# 0002. 프레임워크: SvelteKit

- 상태: 승인 (2026-11-26, 사용자 승인)
- 등급: A

## 배경

웹 플랫폼(카탈로그·상세·플레이 셸·마이페이지)과 서버 API 를 한 코드베이스에서 만들고, Cloudflare Workers 무료 플랜(코드 3MB, CPU 10ms)에서 돌아가야 한다. 첫 화면에서 플레이까지 빠른 진입이 핵심 경험이다.

## 선택지

| 후보 | 장점 | 단점 |
| --- | --- | --- |
| **SvelteKit 3 + Svelte 5** | 런타임이 작아 번들·Worker 크기가 가장 작음, 공식 Cloudflare 어댑터, 풀스택(SSR·API·폼) 일체 | React 대비 생태계가 작음 |
| React Router v7 (Remix) | React 생태계, Cloudflare 공식 템플릿 | 번들이 더 큼 |
| Next.js (OpenNext) | 가장 큰 생태계 | Workers 무료 3MB 한도에 걸리기 쉬움, 어댑터 계층이 무거움 |
| Astro | 콘텐츠 페이지에 최적 | 앱 성격(로그인·상태·플레이 셸)에는 부가 설정이 많음 |

## 결정

SvelteKit 3 + Svelte 5(runes) + `@sveltejs/adapter-cloudflare`, TypeScript strict.

## 이유

무료 플랜의 크기·CPU 제약과 "빠른 첫 진입" 목표에 가장 유리하고, Cloudflare 바인딩(D1 등) 로컬 에뮬레이션이 어댑터에 내장되어 Docker 없이 개발 환경이 재현된다.

## 결과

- 스캐폴드: `sv@1.3.0 create` (minimal, ts, prettier, eslint, vitest, tailwindcss, adapter-cloudflare/workers, drizzle d1).
- SvelteKit 3 관례: `#lib/...` import(+ `.ts` 확장자), 훅 타입은 `@sveltejs/kit/hooks`, 바인딩은 `cloudflare:workers`.
- 스타일링은 Tailwind CSS 4 로 시작(B등급) — 디자인 토큰은 Phase 2 에서 설계.
