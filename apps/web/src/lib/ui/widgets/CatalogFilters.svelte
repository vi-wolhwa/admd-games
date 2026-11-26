<script lang="ts">
	import {
		type CatalogQuery,
		DEFAULT_QUERY,
		type Players,
		PLAYERS_LABEL,
		SORT_LABEL
	} from '#lib/domain/catalog.ts';
	import {
		type Launch,
		LENGTH_BUCKETS,
		LENGTH_LABEL,
		type LengthBucket
	} from '#lib/domain/game.ts';
	import Button from '#lib/ui/primitives/Button.svelte';
	import Chip from '#lib/ui/primitives/Chip.svelte';
	import Select from '#lib/ui/primitives/Select.svelte';

	/**
	 * 전체 게임 필터 띠(PG03): 태그 칩 줄 + 요약 · 한 판 · 실행 · 인원 · 정렬.
	 * 태그는 공개 게임이 있는 것만 게임 수 순(ADR 0010), 여러 개 고르면 '하나라도 해당'.
	 */
	interface Props {
		tags: { slug: string; name: string; count: number }[];
		query: CatalogQuery;
		/** 지금 조건의 게임 수 */
		total: number;
		onchange: (query: CatalogQuery) => void;
	}

	let { tags, query, total, onchange }: Props = $props();

	const set = (patch: Partial<CatalogQuery>) => {
		onchange({ ...query, ...patch });
	};
	const toggleTag = (slug: string) => {
		set({
			tags: query.tags.includes(slug) ? query.tags.filter((t) => t !== slug) : [...query.tags, slug]
		});
	};
	const hasFilter = $derived(
		query.q !== '' ||
			query.tags.length > 0 ||
			query.length !== null ||
			query.launch !== null ||
			query.players !== null
	);

	const ALL = { value: '', label: '전체' };
	const lengthItems = [
		ALL,
		...LENGTH_BUCKETS.map((b) => ({ value: String(b), label: LENGTH_LABEL[b] }))
	];
	const launchItems = [
		ALL,
		...(['web', 'download'] as const).map((v) => ({
			value: v,
			label: v === 'web' ? '바로 플레이' : '설치형'
		}))
	];
	const playerItems = [
		ALL,
		...(['solo', 'group'] as const).map((v) => ({ value: v, label: PLAYERS_LABEL[v] }))
	];
	const sortItems = (['recommended', 'new', 'short'] as const).map((v) => ({
		value: v,
		label: SORT_LABEL[v]
	}));
</script>

<div role="group" aria-label="태그 — 여러 개 고를 수 있어요" class="mt-5 flex flex-wrap gap-2">
	<Chip
		pressed={query.tags.length === 0}
		onclick={() => {
			set({ tags: [] });
		}}
	>
		전체
	</Chip>
	{#each tags as tag (tag.slug)}
		<Chip
			pressed={query.tags.includes(tag.slug)}
			count={tag.count}
			onclick={() => {
				toggleTag(tag.slug);
			}}
		>
			{tag.name}
		</Chip>
	{/each}
</div>

<div class="mt-3.5 flex items-center gap-2 border-t border-line-strong pt-3.5">
	<p class="text-label text-ink-2" aria-live="polite">
		<b class="text-ink-1">{total.toLocaleString('ko-KR')}</b>개
	</p>
	{#if hasFilter}
		<Button
			variant="link"
			onclick={() => {
				onchange({ ...DEFAULT_QUERY, sort: query.sort });
			}}
		>
			모두 지우기
		</Button>
	{/if}
	<div class="ml-auto flex items-center gap-2">
		<Select
			label="한 판"
			value={query.length ? String(query.length) : ''}
			items={lengthItems}
			onchange={(v) => {
				set({ length: v ? (Number(v) as LengthBucket) : null });
			}}
		/>
		<Select
			label="실행"
			value={query.launch ?? ''}
			items={launchItems}
			onchange={(v) => {
				set({ launch: v ? (v as Launch) : null });
			}}
		/>
		<Select
			label="인원"
			value={query.players ?? ''}
			items={playerItems}
			onchange={(v) => {
				set({ players: v ? (v as Players) : null });
			}}
		/>
		<Select
			label="정렬"
			value={query.sort}
			items={sortItems}
			highlightWhenSet={false}
			onchange={(v) => {
				set({ sort: v as CatalogQuery['sort'] });
			}}
		/>
	</div>
</div>
