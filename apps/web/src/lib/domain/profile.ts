/**
 * 사람 프로필 규칙 — 닉네임 · 멘션(@닉네임).
 * 닉네임: 한글(완성형) · 영문만, 최대 15자, 겹치지 않음(사용자 결정 2026-11-28).
 */
const NICKNAME = /^[가-힣A-Za-z]{1,15}$/;

export function isValidNickname(name: string): boolean {
	return NICKNAME.test(name);
}

/** 멘션 후보 — '@' 뒤에 붙은 한글 · 영문(최대 15자) */
const MENTION = /@([가-힣A-Za-z]{1,15})/g;

export type MentionPart = { text: string } | { mention: string };

/**
 * 글을 일반 글과 멘션으로 나눈다. '@새벽배송님'처럼 조사가 붙어도 아는 닉네임 중 **가장 긴 앞부분**을 멘션으로 본다.
 * 아는 닉네임이 아니면 그냥 글. (닉네임이 겹치지 않으므로 앞부분 맞추기로 충분)
 */
export function splitMentions(text: string, isKnown: (name: string) => boolean): MentionPart[] {
	const parts: MentionPart[] = [];
	let last = 0;
	for (const m of text.matchAll(MENTION)) {
		const word = m[1] ?? '';
		let name = '';
		for (let n = word.length; n > 0; n--) {
			if (isKnown(word.slice(0, n))) {
				name = word.slice(0, n);
				break;
			}
		}
		if (!name) continue;
		const at = m.index;
		if (at > last) parts.push({ text: text.slice(last, at) });
		parts.push({ mention: name });
		last = at + 1 + name.length;
	}
	if (last < text.length) parts.push({ text: text.slice(last) });
	return parts;
}

/** 멘션일 수 있는 이름 후보 전부(저장소에서 한 번에 찾으려고) — 각 '@단어'의 모든 앞부분 */
export function mentionCandidates(text: string): string[] {
	const out = new Set<string>();
	for (const m of text.matchAll(MENTION)) {
		const word = m[1] ?? '';
		for (let n = 1; n <= word.length; n++) out.add(word.slice(0, n));
	}
	return [...out];
}
