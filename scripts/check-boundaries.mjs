#!/usr/bin/env node
// 구조 경계 검사 — import 가 정해진 방향(아래로만)으로만 흐르는지 확인한다.
// 규칙의 근거: docs/dev/component-architecture.md 4절, docs/architecture.md(포트 · 어댑터)
// 사용: node scripts/check-boundaries.mjs [파일 …]  (인자가 없으면 apps/web/src 전체)
import { readdirSync, readFileSync, statSync } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const SRC = path.join(ROOT, 'apps/web/src');
const rel = (p) => path.relative(SRC, p).split(path.sep).join('/');

/** 파일이 속한 층과(있다면) 묶음 이름을 돌려준다. */
export function classify(file) {
	const r = rel(file);
	if (r.startsWith('..')) return null;
	const seg = r.split('/');
	if (seg[0] === 'routes') return { layer: 'routes' };
	if (/^hooks(\.server|\.client)?\.(ts|js)$/.test(r)) return { layer: 'hooks' };
	if (seg[0] !== 'lib') return { layer: 'other' };
	if (seg[1] === 'ui') {
		if (seg[2] === 'primitives') return { layer: 'ui-primitives' };
		if (seg[2] === 'patterns') return { layer: 'ui-patterns' };
		if (seg[2] === 'entities') return { layer: 'ui-entities', group: seg[3] };
		if (seg[2] === 'features') return { layer: 'ui-features', group: seg[3] };
		if (seg[2] === 'widgets') return { layer: 'ui-widgets' };
		return { layer: 'ui-unknown' };
	}
	if (seg[1] === 'domain') return { layer: 'domain' };
	if (seg[1] === 'fixtures') return { layer: 'fixtures' };
	if (seg[1] === 'server') {
		if (seg[2] === 'ports') return { layer: 'ports' };
		if (seg[2] === 'adapters') return { layer: 'adapters', group: seg[3] };
		if (seg[2] === 'container.ts') return { layer: 'container' };
		return { layer: 'server' };
	}
	return { layer: 'lib-shared' };
}

// from → 가도 되는 층. 'same' = 같은 층이면 같은 묶음(group)끼리만.
const ALLOW = {
	'ui-primitives': ['ui-primitives', 'lib-shared'],
	'ui-patterns': ['ui-primitives', 'ui-patterns', 'lib-shared'],
	'ui-entities': ['ui-primitives', 'ui-patterns', 'same', 'domain', 'lib-shared'],
	'ui-features': ['ui-primitives', 'ui-patterns', 'ui-entities', 'same', 'domain', 'lib-shared'],
	'ui-widgets': ['ui-primitives', 'ui-patterns', 'ui-entities', 'ui-features', 'domain', 'lib-shared'],
	routes: ['ui-primitives', 'ui-patterns', 'ui-entities', 'ui-features', 'ui-widgets', 'domain', 'server', 'ports', 'routes', 'lib-shared'],
	hooks: ['container', 'server', 'ports', 'domain', 'lib-shared'],
	domain: ['domain', 'lib-shared'],
	ports: ['ports', 'domain'],
	adapters: ['ports', 'same', 'domain'],
	container: ['adapters', 'ports', 'server', 'domain'],
	server: ['ports', 'server', 'domain', 'lib-shared'],
	fixtures: ['fixtures', 'domain', 'ports'],
	'lib-shared': ['lib-shared'],
	'ui-unknown': [],
	other: ['lib-shared', 'domain']
};

const WHY = {
	'ui-unknown': 'lib/ui 바로 아래에는 primitives · patterns · entities · features · widgets 폴더만 둡니다',
	fixtures: '가짜 데이터(fixtures)는 이야기 · 테스트 · 시드에서만 씁니다',
	adapters: '어댑터는 container.ts 에서만 연결합니다(라우트 · 도메인은 locals.services 를 씀)',
	container: 'container 는 hooks 에서만 부릅니다'
};

const isTestOrStory = (f) => /\.(spec|test)\.[jt]s$|\.stories\.(svelte|[jt]s)$/.test(f);

function* walk(dir) {
	for (const name of readdirSync(dir)) {
		const p = path.join(dir, name);
		if (statSync(p).isDirectory()) yield* walk(p);
		else if (/\.(ts|js|svelte)$/.test(name) && !name.endsWith('.d.ts')) yield p;
	}
}

const IMPORT_RE = /(?:import|export)\s[^'"`;]*?from\s*['"]([^'"]+)['"]|import\s*\(\s*['"]([^'"]+)['"]\s*\)|import\s+['"]([^'"]+)['"]/g;

function resolveSpec(file, spec) {
	if (spec.startsWith('#lib/')) return path.join(SRC, 'lib', spec.slice(5));
	if (spec === '#lib') return path.join(SRC, 'lib/index.ts');
	if (spec.startsWith('$lib/')) return path.join(SRC, 'lib', spec.slice(5));
	if (spec.startsWith('./$types')) return null;
	if (spec.startsWith('.')) return path.resolve(path.dirname(file), spec);
	return null; // 패키지 · $app · $env 등
}

export function check(files) {
	const errors = [];
	for (const file of files) {
		const from = classify(file);
		if (!from) continue;
		const text = readFileSync(file, 'utf8');
		for (const m of text.matchAll(IMPORT_RE)) {
			const spec = m[1] ?? m[2] ?? m[3];
			const target = resolveSpec(file, spec);
			if (!target) continue;
			const to = classify(target);
			if (!to) continue;
			const line = text.slice(0, m.index).split('\n').length;
			const where = `${path.relative(ROOT, file).split(path.sep).join('/')}:${line}`;
			if (to.layer === 'fixtures' && from.layer !== 'fixtures' && !isTestOrStory(file)) {
				errors.push(`${where}  ${from.layer} → fixtures: ${WHY.fixtures}`);
				continue;
			}
			if (isTestOrStory(file) && to.layer !== 'routes') continue;
			const allowed = ALLOW[from.layer] ?? [];
			const sameGroupOk = allowed.includes('same') && from.layer === to.layer && from.group === to.group;
			if (allowed.includes(to.layer) || sameGroupOk) continue;
			const reason =
				from.layer === to.layer
					? `같은 층의 다른 묶음(${from.group} → ${to.group})은 import 하지 않습니다 — 위층에서 조합하세요`
					: (WHY[to.layer] ?? WHY[from.layer] ?? `${from.layer} 는 ${to.layer} 를 import 할 수 없습니다(import 는 아래 층으로만)`);
			errors.push(`${where}  ${from.layer} → ${to.layer} (${spec}): ${reason}`);
		}
	}
	return errors;
}

if (import.meta.url === `file://${process.argv[1].split(path.sep).join('/')}` || process.argv[1]?.endsWith('check-boundaries.mjs')) {
	const args = process.argv.slice(2).map((a) => path.resolve(a)).filter((a) => /\.(ts|js|svelte)$/.test(a) && !a.endsWith('.d.ts')); // 타입 선언 파일은 검사하지 않음(전체 검사와 같게)
	const files = args.length ? args : [...walk(SRC)];
	const errors = check(files);
	if (errors.length) {
		console.error(`구조 경계 위반 ${errors.length}건:\n` + errors.map((e) => '  ' + e).join('\n'));
		process.exit(1);
	}
	console.log(`구조 경계 확인: ${files.length}개 파일 OK`);
}
