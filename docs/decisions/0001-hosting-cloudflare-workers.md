# 0001. 호스팅: Cloudflare Workers 무료 플랜

- 상태: 승인 (2026-11-26, 사용자 승인)
- 등급: A

## 배경

비용은 반드시 0원이어야 한다. 트래픽이 적은 개인 프로젝트라도 "오래 안 쓰면 잠드는" 서비스는 첫 진입 3초 목표와 맞지 않는다. 나중에 수익화 가능성도 열어 두고 싶다.

## 선택지

| 후보 | 장점 | 단점 |
| --- | --- | --- |
| **Cloudflare Workers (Free)** | 상업 이용 가능, 잠들지 않음, 정적 에셋 요청 무료·무제한, D1·Durable Objects·R2 가 같은 계정에 | 요청당 CPU 10ms, 코드 3MB, 요청 10만/일 |
| Vercel Hobby | SvelteKit 지원 좋음 | **비상업 개인 용도로만 허용** |
| Netlify Free | 상업 이용 가능 | 2025-09 부터 크레딧제(월 300 크레딧, 초과 시 정지) |
| Supabase / Firebase 호스팅 | BaaS 일체형 | Supabase 무료 프로젝트는 7일 비활성 시 일시정지 |

## 결정

Cloudflare Workers 무료 플랜에 Worker 하나로 배포한다. 커스텀 도메인은 유료라 당분간 `*.workers.dev` 를 쓴다.

## 이유

무료이면서 상업 이용이 가능하고, 잠들지 않으며, 이후 필요한 DB(D1)·실시간(Durable Objects)·파일(R2)이 같은 플랫폼 무료 한도 안에 있다.

## 결과

- 서버 코드에 CPU 10ms 제약 → 비밀번호 해싱 같은 무거운 연산을 피하고 OAuth·익명 로그인 위주로 설계 (0004).
- 배포 전 사용자가 Cloudflare 무료 계정을 만들고 API 토큰을 GitHub 시크릿에 넣어야 한다.

## 출처

- [Workers 한도](https://developers.cloudflare.com/workers/platform/limits/) · [Workers 요금](https://developers.cloudflare.com/workers/platform/pricing/)
- [정적 에셋 과금·한도](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations)
- [D1 요금](https://developers.cloudflare.com/d1/platform/pricing/) · [D1 무료 한도 강제 (2026-09-01)](https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/)
- [Vercel Hobby 플랜](https://vercel.com/docs/plans/hobby) · [Vercel 공정 사용 가이드](https://vercel.com/docs/limits/fair-use-guidelines)
- [Neon vs Supabase 무료 플랜](https://neon.com/guides/neon-vs-supabase-free-plan)
