/**
 * 가짜 게임 미리보기 영상 만들기 — static/sample/<slug>-video.webm (4초, 소리 없음).
 * 내려받기 없이 Playwright 의 Chromium 에서 캔버스 그림을 녹화한다(MediaRecorder).
 * 사용: node scripts/sample-video.ts  (apps/web 에서) — 결과는 저장소에 커밋한다
 */
import { writeFileSync } from 'node:fs';
import path from 'node:path';

import { chromium } from 'playwright';

import { SAMPLE_VIDEO_SLUGS } from '#lib/fixtures/games.ts';

const OUT = path.join(import.meta.dirname, '../static/sample');
const SECONDS = 4;

function hueOf(slug: string): number {
	let h = 2166136261;
	for (const ch of slug) h = Math.imul(h ^ (ch.codePointAt(0) ?? 0), 16777619);
	return (h >>> 0) % 360;
}

const browser = await chromium.launch();
const page = await browser.newPage();
for (const slug of SAMPLE_VIDEO_SLUGS) {
	const base64 = await page.evaluate(
		async ({ hue, seconds }) => {
			const canvas = document.createElement('canvas');
			canvas.width = 480;
			canvas.height = 270;
			const ctx = canvas.getContext('2d');
			if (!ctx) throw new Error('canvas');
			const recorder = new MediaRecorder(canvas.captureStream(30), {
				mimeType: 'video/webm',
				videoBitsPerSecond: 250_000
			});
			const chunks: Blob[] = [];
			recorder.ondataavailable = (e) => chunks.push(e.data);
			const stopped = new Promise((r) => (recorder.onstop = r));
			recorder.start();
			const t0 = performance.now();
			await new Promise<void>((done) => {
				const frame = () => {
					const t = (performance.now() - t0) / 1000;
					const g = ctx.createLinearGradient(0, 0, 480, 270);
					g.addColorStop(0, `hsl(${hue} 55% 22%)`);
					g.addColorStop(1, `hsl(${(hue + 60) % 360} 60% 48%)`);
					ctx.fillStyle = g;
					ctx.fillRect(0, 0, 480, 270);
					// 굴러가는 공과 튀는 블록 — 움직임이 분명해야 영상인 게 보인다
					for (let i = 0; i < 5; i++) {
						const x = ((t * (60 + i * 25) + i * 90) % 560) - 40;
						const y = 200 - Math.abs(Math.sin(t * 3 + i)) * (60 + i * 15);
						ctx.fillStyle = `hsl(${(hue + 150 + i * 30) % 360} 70% 60%)`;
						ctx.beginPath();
						ctx.arc(x, y, 14 + i * 3, 0, Math.PI * 2);
						ctx.fill();
					}
					ctx.fillStyle = 'rgb(255 255 255 / 0.85)';
					ctx.fillRect(0, 262, (t / seconds) * 480, 8);
					if (t < seconds) requestAnimationFrame(frame);
					else done();
				};
				frame();
			});
			recorder.stop();
			await stopped;
			const bytes = new Uint8Array(await new Blob(chunks, { type: 'video/webm' }).arrayBuffer());
			let s = '';
			for (const b of bytes) s += String.fromCharCode(b);
			return btoa(s);
		},
		{ hue: hueOf(slug), seconds: SECONDS }
	);
	const file = path.join(OUT, `${slug}-video.webm`);
	writeFileSync(file, Buffer.from(base64, 'base64'));
	console.log(`${slug}-video.webm ${String(Math.round((base64.length * 0.75) / 1024))}KB`);
}
await browser.close();
