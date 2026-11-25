import { defineConfig } from 'drizzle-kit';

// drizzle-kit 은 마이그레이션 SQL 생성(generate)에만 쓴다.
// 적용은 wrangler 가 담당한다: npm run db:migrate:local | db:migrate:remote
export default defineConfig({
	schema: './src/lib/server/adapters/d1/schema.ts',
	out: './migrations',
	dialect: 'sqlite',
	verbose: true,
	strict: true
});
