import path from 'node:path';

import js from '@eslint/js';
import { defineConfig, includeIgnoreFile } from 'eslint/config';
import prettier from 'eslint-config-prettier';
import betterTailwind from 'eslint-plugin-better-tailwindcss';
import simpleImportSort from 'eslint-plugin-simple-import-sort';
import svelte from 'eslint-plugin-svelte';
import globals from 'globals';
import ts from 'typescript-eslint';

const gitignorePath = path.resolve(import.meta.dirname, '../../.gitignore');

// 원시 팔레트 · 임의 색 클래스 금지 — 화면 코드는 의미 토큰만 (docs/design/system/README.md)
const PALETTE = '(jjok|inju|bichwi|dahong|graphite|face)';
const COLOR_UTIL =
	'(bg|text|border|ring|outline|fill|stroke|from|via|to|decoration|shadow|accent|caret|divide|placeholder)';

export default defineConfig(
	includeIgnoreFile(gitignorePath),
	{
		ignores: [
			'.svelte-kit/**',
			'build/**',
			'storybook-static/**',
			'worker-configuration.d.ts',
			'migrations/**'
		]
	},
	js.configs.recommended,
	ts.configs.strictTypeChecked,
	ts.configs.stylisticTypeChecked,
	svelte.configs.recommended,
	prettier,
	svelte.configs.prettier,
	{
		languageOptions: {
			globals: { ...globals.browser, ...globals.node },
			parserOptions: {
				projectService: true,
				tsconfigRootDir: import.meta.dirname,
				extraFileExtensions: ['.svelte']
			}
		},
		plugins: { 'simple-import-sort': simpleImportSort },
		rules: {
			// typescript-eslint 는 TS 프로젝트에서 no-undef 를 끄라고 권장
			'no-undef': 'off',
			'simple-import-sort/imports': 'error',
			'simple-import-sort/exports': 'error',
			'@typescript-eslint/restrict-template-expressions': ['error', { allowNumber: true }],
			'@typescript-eslint/no-unused-vars': [
				'error',
				{ argsIgnorePattern: '^_', varsIgnorePattern: '^_' }
			],
			// DB 라이브러리는 어댑터 안에서만 (포트/어댑터 경계 — docs/architecture.md)
			'no-restricted-imports': [
				'error',
				{
					patterns: [
						{
							group: ['drizzle-orm', 'drizzle-orm/*'],
							message: 'drizzle 은 lib/server/adapters 안에서만 씁니다.'
						}
					]
				}
			]
		}
	},
	{
		files: ['src/lib/server/adapters/**', 'drizzle.config.ts'],
		rules: { 'no-restricted-imports': 'off' }
	},
	{
		files: ['**/*.svelte', '**/*.svelte.ts', '**/*.svelte.js'],
		languageOptions: {
			parserOptions: { parser: ts.parser, svelteConfig: { compilerOptions: { runes: true } } }
		}
	},
	{
		files: ['**/*.svelte'],
		plugins: { 'better-tailwindcss': betterTailwind },
		settings: {
			'better-tailwindcss': { entryPoint: 'src/routes/layout.css' }
		},
		rules: {
			'svelte/button-has-type': 'error',
			'svelte/require-each-key': 'error',
			'svelte/block-lang': ['error', { script: 'ts', style: [null] }],
			'svelte/no-useless-mustaches': 'error',
			'svelte/prefer-writable-derived': 'error',
			'svelte/no-unused-svelte-ignore': 'error',
			'better-tailwindcss/no-unknown-classes': 'error',
			'better-tailwindcss/no-duplicate-classes': 'error',
			'better-tailwindcss/no-conflicting-classes': 'error',
			'better-tailwindcss/no-restricted-classes': [
				'error',
				{
					restrict: [
						{
							pattern: `^${COLOR_UTIL}-${PALETTE}-`,
							message: '원시 색 대신 의미 토큰을 쓰세요 (예: bg-accent, text-ink-3).'
						},
						{
							pattern: String.raw`^${COLOR_UTIL}-\[`,
							message: '임의 색 값 대신 의미 토큰을 쓰세요.'
						}
					]
				}
			]
		}
	},
	{
		// 설정 파일 · 스크립트는 타입 검사 규칙을 느슨하게
		files: ['*.config.{js,ts}', 'scripts/**'],
		extends: [ts.configs.disableTypeChecked]
	}
);
