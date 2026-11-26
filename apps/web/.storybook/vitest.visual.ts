/**
 * 화면 캡처 비교(setup-agenda 4-1): 이야기마다 라이트 · 다크 두 장을 기준 그림과 비교한다.
 * 테마는 CSS 만 바뀌므로 같은 화면에서 html[data-theme] 만 바꿔 찍는다.
 * 기준 그림은 CI(리눅스)에서 만든 것만 저장소에 둔다 — 글꼴 렌더링이 OS 마다 달라서.
 *   새로 만들기 · 갱신: GitHub Actions 의 'update-screenshots' 를 브랜치를 골라 실행.
 */
import { afterEach, expect } from 'vitest';
import { page } from 'vitest/browser';

/**
 * 한 파일에 이야기가 여럿이어도 그림이 겹치지 않게 이야기마다 다른 이름.
 * 파일 이름에 한글이 지워지므로(vitest 가 ASCII 만 남김) 이야기 이름의 짧은 해시를 쓴다.
 */
function storyKey(name: string): string {
	let h = 2166136261;
	for (const ch of name) h = Math.imul(h ^ (ch.codePointAt(0) ?? 0), 16777619);
	return (h >>> 0).toString(36);
}

afterEach(async (context) => {
	if (context.task.result?.state === 'fail') return;
	// 글꼴 조각(Pretendard 글자 범위별)이 다 받아진 뒤에 찍는다 — 덜 받아진 채 찍히면 그림이 흔들린다
	await document.fonts.ready;
	const root = document.querySelector('#storybook-root') ?? document.body;
	const locator = page.elementLocator(root);
	for (const theme of ['light', 'dark'] as const) {
		document.documentElement.dataset.theme = theme;
		await expect.element(locator).toMatchScreenshot(`${storyKey(context.task.name)}-${theme}`);
	}
	document.documentElement.dataset.theme = 'light';
});
