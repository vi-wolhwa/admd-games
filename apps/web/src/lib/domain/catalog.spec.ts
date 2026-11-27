import { describe, expect, it } from 'vitest';

import {
	catalogSearchParams,
	decodeCursor,
	DEFAULT_QUERY,
	encodeCursor,
	parseCatalogQuery,
	parseLoaded,
	searchKey
} from './catalog';

const params = (s: string) => new URLSearchParams(s);

describe('parseCatalogQuery', () => {
	it('아무것도 없으면 기본값(플레이 많은 순, 필터 없음)', () => {
		expect(parseCatalogQuery(params(''))).toEqual(DEFAULT_QUERY);
	});

	it('주소의 필터 · 정렬을 읽는다', () => {
		expect(
			parseCatalogQuery(params('q=러너&tag=퍼즐&tag=액션&len=30m&run=web&ppl=duo&sort=new'))
		).toEqual({
			q: '러너',
			tags: ['퍼즐', '액션'],
			length: 2,
			launch: 'web',
			players: 'duo',
			sort: 'new'
		});
	});

	it('모르는 값은 버리고 기본값으로 — 잘못된 주소도 페이지는 열린다', () => {
		expect(parseCatalogQuery(params('len=7m&run=cd&ppl=x&sort=short'))).toEqual(DEFAULT_QUERY);
		// 예전 주소(5구간 · 같이)는 필터 없음으로
		expect(parseCatalogQuery(params('len=1h&ppl=group'))).toEqual(DEFAULT_QUERY);
	});

	it('검색어는 앞뒤 공백을 지우고 40자까지', () => {
		expect(parseCatalogQuery(params('q=  러너  ')).q).toBe('러너');
		expect(parseCatalogQuery(params(`q=${'가'.repeat(50)}`)).q).toHaveLength(40);
	});

	it('같은 태그가 겹치거나 빈 태그면 한 번만, 최대 10개', () => {
		const many = Array.from({ length: 12 }, (_, i) => `tag=t${String(i)}`).join('&');
		expect(parseCatalogQuery(params('tag=퍼즐&tag=퍼즐&tag=')).tags).toEqual(['퍼즐']);
		expect(parseCatalogQuery(params(many)).tags).toHaveLength(10);
	});
});

describe('catalogSearchParams', () => {
	it('기본값은 주소에 남기지 않는다', () => {
		expect(catalogSearchParams(DEFAULT_QUERY).toString()).toBe('');
	});

	it('읽은 것을 다시 쓰면 같은 질의가 된다', () => {
		const q = parseCatalogQuery(
			params('q=고양이&tag=퍼즐&len=daily&run=download&ppl=online&sort=reviews')
		);
		expect(parseCatalogQuery(catalogSearchParams(q))).toEqual(q);
	});

	it('불러온 개수는 첫 묶음보다 많을 때만 남긴다', () => {
		expect(catalogSearchParams(DEFAULT_QUERY, 12).has('n')).toBe(false);
		expect(catalogSearchParams(DEFAULT_QUERY, 36).get('n')).toBe('36');
	});
});

describe('searchKey', () => {
	it('공백은 모두 무시한다', () => {
		expect(searchKey(' A  BC ')).toBe('ABC');
		expect(searchKey('고양이 우편')).toBe('고양이우편');
	});

	it('끝의 조합되지 않은 한글 자모는 빼고, 남는 것이 없으면 빈 검색어', () => {
		expect(searchKey('게임ㅇ')).toBe('게임');
		expect(searchKey('러너ㄴㅓ')).toBe('러너');
		expect(searchKey('ㄱ')).toBe('');
		// 가운데 자모는 그대로(입력 중인 끝 글자만 문제)
		expect(searchKey('ㅋ게임')).toBe('ㅋ게임');
	});
});

describe('parseLoaded', () => {
	it('12개 단위로 맞추고 12~96 안으로', () => {
		expect(parseLoaded(params(''))).toBe(12);
		expect(parseLoaded(params('n=30'))).toBe(36);
		expect(parseLoaded(params('n=9999'))).toBe(96);
		expect(parseLoaded(params('n=abc'))).toBe(12);
	});
});

describe('커서', () => {
	it('정렬마다 값을 담아 되돌린다', () => {
		const c = { sort: 'played', values: [980, 140], id: 'g-1' } as const;
		expect(decodeCursor(encodeCursor(c), 'played')).toEqual(c);
	});

	it('다른 정렬의 커서나 망가진 값은 무시한다', () => {
		const c = encodeCursor({ sort: 'new', values: [1700000000000], id: 'g-1' });
		expect(decodeCursor(c, 'recommended')).toBeNull();
		expect(decodeCursor('not-base64!', 'new')).toBeNull();
		expect(decodeCursor(encodeCursor({ sort: 'new', values: [], id: 'g-1' }), 'new')).toBeNull();
	});
});
