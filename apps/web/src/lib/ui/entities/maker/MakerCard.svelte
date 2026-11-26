<script lang="ts">
	import { faceOf } from '#lib/domain/face.ts';
	import JamoFace from '#lib/ui/primitives/JamoFace.svelte';

	/**
	 * 메이커 카드(게임 상세 소개 탭 맨 위). 팔로우 · 메이커 페이지 버튼은 로그인(SH01) · 메이커 페이지(PG13)가 생기면 붙인다.
	 */
	interface Props {
		name: string;
		gameCount: number;
	}

	let { name, gameCount }: Props = $props();
	const face = $derived(faceOf(name));
</script>

<div
	class="grid grid-cols-[auto_minmax(0,1fr)] items-center gap-3 rounded-lg p-4 inset-ring inset-ring-line"
>
	<JamoFace char={face.char} color={face.color} size="lg" />
	<span>
		<b class="block text-lead font-heavy text-ink-1">{name}</b>
		<span class="mt-0.5 block text-meta text-ink-3">
			메이커 · 게임 {gameCount.toLocaleString('ko-KR')}개
		</span>
	</span>
</div>
