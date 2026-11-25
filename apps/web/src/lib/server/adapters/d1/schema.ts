/**
 * D1(SQLite) 테이블 정의. 이 파일은 D1 어댑터 내부 구현이다 —
 * 어댑터 밖(ports, 도메인, 라우트)에서 import 하지 않는다.
 *
 * 다른 DB로 옮기기 쉽게 하는 규칙 (docs/architecture.md 참고):
 * - ID 는 text (UUID), 시각은 integer (epoch ms)
 * - SQLite 전용 기능(JSON1 함수, 동적 타입)에 기대지 않는다
 *
 * 변경 후: npm run db:generate → npm run db:migrate:local
 */
export {};
