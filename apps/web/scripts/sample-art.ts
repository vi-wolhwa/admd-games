/**
 * 가짜 게임 그림 만들기 — static/sample/<slug>-<0~5>.svg (0 = 대표 그림, 1~5 = 호버 순환).
 * 게임마다 색이 다르고, 같은 게임 안에서는 같은 색으로 구도만 바뀐다. 저작권 · 다운로드 없음(결정 2026-11-28).
 * 사용: node scripts/sample-art.ts  (apps/web 에서) — 결과는 저장소에 커밋한다(캡처 비교가 늘 같은 그림을 보도록)
 */
import { mkdirSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import path from 'node:path';

import { SAMPLE_SHOTS, sampleGames } from '#lib/fixtures/games.ts';

const OUT = path.join(import.meta.dirname, '../static/sample');
const W = 480;
const H = 270;

function hash(s: string): number {
	let h = 2166136261;
	for (const ch of s) h = Math.imul(h ^ (ch.codePointAt(0) ?? 0), 16777619);
	return h >>> 0;
}

function rng(seed: number) {
	let a = seed;
	return () => {
		a = (a + 0x6d2b79f5) >>> 0;
		let t = a;
		t = Math.imul(t ^ (t >>> 15), t | 1);
		t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
		return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
	};
}

const r1 = (n: number) => Math.round(n * 10) / 10;

function art(slug: string, shot: number): string {
	const base = hash(slug) % 360;
	const rand = rng(hash(`${slug}#${String(shot)}`));
	const hsl = (dh: number, s: number, l: number) =>
		`hsl(${String((base + dh + 360) % 360)} ${String(s)}% ${String(Math.round(l))}%)`;
	const shapes: string[] = [];

	// 바닥 띠(지평선)
	const horizon = H * (0.55 + rand() * 0.25);
	shapes.push(
		`<rect x="0" y="${r1(horizon)}" width="${String(W)}" height="${r1(H - horizon)}" fill="${hsl(-20, 45, 18)}" opacity="0.55"/>`
	);

	// 큰 원(해 · 행성)
	const big = shot === 0 ? 70 : 40 + rand() * 50;
	shapes.push(
		`<circle cx="${r1(60 + rand() * (W - 120))}" cy="${r1(40 + rand() * (horizon - 40))}" r="${r1(big)}" fill="${hsl(40, 85, 70)}" opacity="0.9"/>`
	);

	// 기울어진 블록들
	const blocks = 3 + Math.floor(rand() * 4);
	for (let i = 0; i < blocks; i++) {
		const w = 30 + rand() * 90;
		const h = 20 + rand() * 70;
		const x = rand() * (W - w);
		const y = horizon - h * (0.4 + rand() * 0.6);
		const rot = (rand() - 0.5) * 30;
		shapes.push(
			`<rect x="${r1(x)}" y="${r1(y)}" width="${r1(w)}" height="${r1(h)}" rx="${r1(4 + rand() * 10)}" fill="${hsl(160 + i * 25, 55, 45 + rand() * 20)}" transform="rotate(${r1(rot)} ${r1(x + w / 2)} ${r1(y + h / 2)})"/>`
		);
	}

	// 작은 점(별 · 불씨)
	const dots = 12 + Math.floor(rand() * 18);
	for (let i = 0; i < dots; i++) {
		shapes.push(
			`<circle cx="${r1(rand() * W)}" cy="${r1(rand() * horizon)}" r="${r1(1 + rand() * 2.5)}" fill="${hsl(60, 90, 92)}" opacity="${r1(0.4 + rand() * 0.6)}"/>`
		);
	}

	return `<svg xmlns="http://www.w3.org/2000/svg" width="${String(W)}" height="${String(H)}" viewBox="0 0 ${String(W)} ${String(H)}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${hsl(0, 55, 26)}"/><stop offset="1" stop-color="${hsl(50 + shot * 12, 60, 52)}"/></linearGradient></defs>
<rect width="${String(W)}" height="${String(H)}" fill="url(#g)"/>
${shapes.join('\n')}
</svg>
`;
}

mkdirSync(OUT, { recursive: true });
for (const f of readdirSync(OUT)) rmSync(path.join(OUT, f));
let n = 0;
for (const g of sampleGames()) {
	for (let shot = 0; shot <= SAMPLE_SHOTS; shot++) {
		writeFileSync(path.join(OUT, `${g.slug}-${String(shot)}.svg`), art(g.slug, shot));
		n++;
	}
}
console.log(`그림 ${String(n)}장 → static/sample`);
