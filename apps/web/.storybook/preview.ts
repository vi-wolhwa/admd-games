import 'pretendard/dist/web/variable/pretendardvariable-dynamic-subset.css';
import '../src/routes/layout.css';

import type { Preview } from '@storybook/sveltekit';

/**
 * 모든 이야기를 테마(라이트 · 다크) × 그라운드(Play · Make)로 볼 수 있게 한다.
 * 앱과 같은 방식으로 <html data-theme data-ground> 를 바꾼다(hooks.server.ts 의 appearance 와 같은 규칙).
 */
const preview: Preview = {
	globalTypes: {
		theme: {
			description: '테마',
			toolbar: {
				title: '테마',
				items: [
					{ value: 'light', title: '라이트' },
					{ value: 'dark', title: '다크' }
				],
				dynamicTitle: true
			}
		},
		ground: {
			description: '그라운드',
			toolbar: {
				title: '그라운드',
				items: [
					{ value: 'play', title: 'PlayGround' },
					{ value: 'make', title: 'MakersGround' }
				],
				dynamicTitle: true
			}
		}
	},
	// 화면 크기 'pc' — 이야기 테스트도 이 크기로 찍는다(addon-vitest 가 viewport 전역값을 따름).
	// 높이를 넉넉히: 화면 밖은 캡처에 안 찍혀서 페이지 이야기가 잘린다
	initialGlobals: { theme: 'light', ground: 'play', viewport: { value: 'pc', isRotated: false } },
	decorators: [
		(story, context) => {
			const root = document.documentElement;
			root.lang = 'ko';
			root.dataset.theme = String(context.globals.theme ?? 'light');
			root.dataset.ground = String(context.globals.ground ?? 'play');
			return story();
		}
	],
	parameters: {
		layout: 'padded',
		viewport: {
			options: {
				pc: { name: 'PC 1440', styles: { width: '1440px', height: '1800px' }, type: 'desktop' }
			}
		},
		// 접근성(axe) 위반은 테스트 실패로 (setup-agenda 4-1)
		a11y: { test: 'error' },
		controls: { expanded: true }
	}
};

export default preview;
