# 운영 시안: 신고 처리(AD-REPORTS) · 큐레이션 편집(AD-CURATE) · 공지·사용자(AD-NOTICE · AD-USERS)
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + [OUT]
import importlib.util
s7 = importlib.util.spec_from_file_location("p7", os.path.join(HERE, "pages7.py")); p7 = importlib.util.module_from_spec(s7); s7.loader.exec_module(p7)
mg, dt = p7.mg, p7.dt
ic, face, logo, EAR, status = mg.ic, mg.face, mg.logo, mg.EAR, mg.status

ADMIN_NAV = ["심사 14", "신고 3", "큐레이션", "공지", "사용자"]
def adh(active):
    return mg.header2(True, active, ADMIN_NAV).replace('MakersGround</span>', '운영</span>', 1)

CSS = r'''
.ad-h2{display:flex;align-items:center;gap:12px;margin-top:24px}
.ad-h2 h1{margin:0;font-size:26px;font-weight:800}
.ad-h2 .tag2{height:24px;padding:0 9px;border-radius:999px;background:var(--surface-ink);color:#FFFFFF;font-size:12px;font-weight:800;display:inline-flex;align-items:center}
.ad-h2 .r{margin-left:auto;display:flex;gap:8px;align-items:center}
.ad2{display:grid;grid-template-columns:400px minmax(0,1fr);gap:28px;margin-top:20px;align-items:start}
.rq{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:10px;align-items:center;padding:12px;border-radius:12px}
.rq.on{background:var(--accent-tint);box-shadow:inset 0 0 0 2px var(--accent)}
.rq b{display:block;font-size:14.5px}
.rq .m{display:block;font-size:12.5px}
.rq .n{font-size:12px;font-weight:800;color:var(--ink-3);text-align:right}
.rq .n.hot{color:var(--danger-text)}
.kindt{display:grid;place-items:center;width:36px;height:36px;border-radius:10px;background:var(--sunken);color:var(--ink-2)}
.pane{display:flex;flex-direction:column;gap:16px;padding:24px;border-radius:var(--radius-xl);box-shadow:inset 0 0 0 1px var(--line)}
.quote{padding:16px;border-radius:12px;background:var(--sunken);font-size:15px;line-height:1.7}
.quote .hd{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--ink-3);margin-bottom:6px}
.quote .hd b{color:var(--ink-1)}
.reasons{display:flex;flex-direction:column;gap:6px}
.reasons div{display:flex;justify-content:space-between;font-size:14px;padding:8px 12px;border-radius:10px;background:var(--sunken)}
.hist{font-size:13.5px;color:var(--ink-3);line-height:1.8}
.decide2{display:flex;gap:8px;justify-content:flex-end;padding-top:14px;border-top:1px solid var(--line)}
.kbd2{display:inline-grid;place-items:center;min-width:20px;height:18px;padding:0 5px;border-radius:5px;background:var(--sunken-hover);font-size:11px;font-weight:800;margin-left:6px;color:var(--ink-2)}
/* 큐레이션 */
.cur{display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:32px;margin-top:20px;align-items:start}
.slot4{display:flex;flex-direction:column;gap:10px}
.slot{display:grid;grid-template-columns:20px 150px minmax(0,1fr) auto;gap:14px;align-items:center;padding:12px;border-radius:14px;box-shadow:inset 0 0 0 1px var(--line);background:var(--bg)}
.slot .grip{color:var(--ink-4);font-weight:900;letter-spacing:-2px;cursor:grab}
.slot .art{border-radius:9px}
.slot b{display:block;font-size:15px}
.slot .why2{display:flex;align-items:center;gap:8px;margin-top:6px;height:38px;padding:0 12px;border-radius:10px;background:var(--sunken);font-size:14px}
.slot .why2.warn{box-shadow:inset 0 0 0 2px var(--accent);background:var(--bg)}
.slot .why2 .cnt3{margin-left:auto;font-size:12px;color:var(--ink-3)}
.lint{font-size:12.5px;color:var(--accent-text);font-weight:700;margin-top:4px}
.slot.empty{grid-template-columns:20px minmax(0,1fr);border-style:dashed;box-shadow:inset 0 0 0 1.5px var(--sunken-hover);color:var(--ink-3);font-size:14px;min-height:72px}
.cands{display:flex;flex-direction:column;gap:2px}
.cand2{display:grid;grid-template-columns:88px minmax(0,1fr) auto;gap:10px;align-items:center;padding:8px;border-radius:10px}
.cand2:hover{background:var(--sunken)}
.cand2 .art{border-radius:7px}
.cand2 b{display:block;font-size:14px}
.cand2 .m{display:block;font-size:12px}
.sched{display:flex;align-items:center;gap:10px;padding:14px 16px;border-radius:14px;background:var(--sunken);font-size:14px}
.sched b{font-size:15px}
.sched .btn{margin-left:auto}
/* 공지 · 사용자 */
.two2{display:grid;grid-template-columns:1fr 1fr;gap:32px;margin-top:20px;align-items:start}
.nrow{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center;padding:12px 4px;border-top:1px solid var(--line);font-size:14.5px}
.nrow:first-child{border-top:0}
.nrow b{display:block}
.banner-pv{display:flex;align-items:center;gap:10px;height:40px;padding:0 16px;border-radius:10px;background:var(--surface-ink);color:#FFFFFF;font-size:13.5px;font-weight:700}
.banner-pv .x{margin-left:auto;opacity:.7}
.utable{width:100%;border-collapse:collapse;font-size:14px}
.utable th{text-align:left;font-size:12.5px;color:var(--ink-3);font-weight:700;padding:0 10px 8px}
.utable td{padding:10px;border-top:1px solid var(--line);vertical-align:middle}
.utable td .who2{display:flex;align-items:center;gap:8px;font-weight:700}
.log2{font-family:ui-monospace,Consolas,monospace;font-size:12.5px;color:var(--ink-2);line-height:1.9;padding:14px 16px;border-radius:12px;background:var(--sunken)}
'''

def page(title, body, h, memo):
    html = mg.page(title, body, h, memo)
    return html.replace("</style>", p7.BASE_CSS + p7.CSS + CSS + "\n</style>", 1)

def reports_page():
    q = [("cmt", "댓글", "“이것도 게임이라고…” 외 2개 문장", "커뮤니티 · 피드백 글", 3, True, True), ("box", "게임", "격자 탈출 — 작동하지 않아요", "환경: Android · Chrome", 2, False, False), ("pen", "글", "무료 효과음 사이트 정리 — 광고 의심", "자유 · 정보", 1, False, False)]
    rows = "".join(f'<div class="rq{" on" if on else ""}"><span class="kindt">{ic(k,"ic ic16")}</span><span><b>{kind} · {t}</b><span class="m">{w}</span></span><span class="n{" hot" if hot else ""}">신고 {n}</span></div>' for k, kind, t, w, n, hot, on in q)
    pane = f'''<div class="pane"><div style="display:flex;align-items:center;gap:10px"><span class="kindt">{ic("cmt","ic ic16")}</span><span><b style="font-size:18px">댓글 신고 3건</b><span class="m" style="display:block">커뮤니티 › 피드백 › 타이틀 화면 두 가지 중 뭐가 나아요?</span></span><a class="link" href="#" style="margin-left:auto">원문에서 보기 ›</a></div>
<div class="quote"><div class="hd">{face("ㅋ","gyul","xs")}<b>크림빵</b>· 가입 2일 · 이전 신고 0 · 20분 전</div>이것도 게임이라고 올린 건가요? 시간 낭비네요. 그냥 접으세요.</div>
<div class="reasons"><div><span>욕설 · 괴롭힘</span><b>2</b></div><div><span>기타 — “글쓴이를 공격해요”</span><b>1</b></div></div>
<div class="hist">처리 기준(운영정책 4조): 작품 비판은 허용, 사람을 향한 공격은 숨김. 처음이면 숨김 + 안내, 반복되면 7일 글쓰기 제한.</div>
<div class="decide2"><span class="btn btn-secondary">문제없음<span class="kbd2">N</span></span><span class="btn btn-secondary">숨기고 안내 보내기<span class="kbd2">H</span></span><span class="btn btn-danger">숨기고 7일 제한<span class="kbd2">B</span></span></div></div>'''
    body = adh("신고 3") + f'''<main class="wrap"><div class="ad-h2"><h1>신고 처리</h1><span class="tag2">운영자</span><span class="m">대기 3 · 오늘 처리 5</span><div class="r"><div class="chips"><button class="chip" aria-pressed="true">전체</button><button class="chip">게임</button><button class="chip">글 · 댓글</button><button class="chip">리뷰</button></div></div></div>
<div class="ad2"><div style="display:flex;flex-direction:column;gap:6px">{rows}</div>{pane}</div></main>'''
    memo = "AD-REPORTS. 같은 대상의 신고는 하나로 묶어(신고 n) 많은 순. 오른쪽: 원문 그대로 · 쓴 사람 정보(가입일 · 이전 신고) · 이유별 개수 · 처리 기준 요약 · 행동 3개(키보드 N/H/B). 게임 ‘작동 안 함’ 은 메이커에게 전달."
    return page("운영 · 신고 처리", body, 1000, memo)

def curate_page():
    slots = [("a-loop", "루프 디버거", "픽셀상점", "이번 주 플레이 수 · 완주율 모두 1위", False, ""), ("a-refac", "리팩터 러시", "리팩터클럽", "오늘 공개된 3분짜리 아케이드", False, ""), ("a-tilt", "틸트 이론", "기울기연구소", "제가 제일 좋아하는 퍼즐이에요", True, "이유는 사실로 — ‘제가’ · 감상 표현을 빼 주세요")]
    sh = "".join(f'''<div class="slot"><span class="grip">⋮⋮</span><span class="art {a}"></span><span><b>{t}</b><span class="m">{w}</span><span class="why2{" warn" if warn else ""}">{y}<span class="cnt3">{len(y)} / 30</span></span>{f'<span class="lint">{lint}</span>' if lint else ""}</span><span class="btn btn-secondary btn-sm">빼기</span></div>''' for a, t, w, y, warn, lint in slots)
    sh += f'<div class="slot empty"><span>4</span><span>오른쪽 후보에서 끌어다 놓기</span></div>'
    cands = "".join(f'<div class="cand2"><span class="art {a}"></span><span><b>{t}</b><span class="m">{m}</span></span><span class="btn btn-secondary btn-sm">{ic("plus")}</span></div>' for a, t, m in [("a-bazaar", "바이트 바자", "플레이 ▲ 140% · 완주 22% · 리뷰 9"), ("a-solvent", "솔벤트", "추천 88% · 리뷰 17 · 같이"), ("a-halcyon", "할시온 바다", "공개 5일 · 완주 31%"), ("a-null", "널 포인터", "설치형 · 검사 통과 · 리뷰 11")])
    body = adh("큐레이션") + f'''<main class="wrap"><div class="ad-h2"><h1>큐레이션 편집</h1><span class="tag2">운영자</span><div class="r"><nav class="utabs" style="border:0"><a href="#" aria-current="page">이번 주 PICK</a><a href="#">배너 5</a><a href="#">컬렉션</a></nav></div></div>
<div class="cur"><div><div class="sched"><span>{ic("clock","ic ic16")}</span><span><b>12월 첫째 주 PICK</b><span class="m" style="display:block">12/1(월) 00:00 자동 공개 · 3 / 4 채움</span></span><span class="btn btn-secondary btn-sm">미리보기</span><span class="btn btn-primary btn-sm" style="margin-left:0">예약</span></div>
<div class="slot4" style="margin-top:14px">{sh}</div>
<p class="m" style="margin-top:14px">이유 한 줄은 사실만(숫자 · 특징). ‘누가 골랐다’ · 1인칭 · 감상은 자동으로 표시돼요(문구 규칙).</p></div>
<aside class="panel2"><h3>후보</h3><div class="search" style="width:100%">{ic("search")}게임 찾기</div><div class="chips"><button class="chip" aria-pressed="true">이번 주 급상승</button><button class="chip">새로 공개</button><button class="chip">아직 PICK 안 됨</button></div><div class="cands">{cands}</div></aside></div></main>'''
    memo = "AD-CURATE. 이번 주 PICK 4칸(끌어서 순서 · 이유 한 줄 30자, 문구 규칙 위반은 강조색 경고) · 월요일 자동 공개 예약 · 미리보기. 오른쪽 후보(급상승 · 새로 공개 · 아직 안 됨) — 숫자로 판단. 배너 5장 · 컬렉션은 같은 틀의 다른 탭."
    return page("운영 · 큐레이션 편집", body, 1100, memo)

def notice_users_page():
    notices = "".join(f'<div class="nrow"><span class="st st-{k}">{lab}</span><span><b>{t}</b><span class="m">{m}</span></span><span class="btn btn-secondary btn-sm">고치기</span></div>' for k, lab, t, m in [("live", "게시 중", "12월 정기 점검 안내 (12/3 02:00~04:00)", "띠 표시 · 12/1 ~ 12/3"), ("wait", "예약", "설치형 게임 보안 검사를 시작했어요", "12/5 09:00"), ("draft", "작성 중", "커뮤니티 운영정책 개정", "어제 저장")])
    users = "".join(f'<tr><td><span class="who2">{face(c,col,"xs")}{n}</span></td><td>{r}</td><td>{d}</td><td>{st}</td><td><span class="btn btn-secondary btn-sm">{a}</span></td></tr>' for c, col, n, r, d, st, a in [("ㅋ", "gyul", "크림빵", "플레이어", "2일", '<span class="st st-fix st-sm">제한 7일</span>', "해제"), ("ㅍ", "jjok", "픽셀상점", "메이커 · 게임 4", "1년", '<span class="st st-live st-sm">정상</span>', "보기"), ("ㄹ", "olive", "레몬게임즈", "메이커 · 게임 1", "3주", '<span class="st st-wait st-sm">심사 중 1</span>', "보기")])
    body = adh("공지") + f'''<main class="wrap"><div class="ad-h2"><h1>공지 · 사용자</h1><span class="tag2">운영자</span></div>
<div class="two2"><section><div class="sh">{EAR}<h2 style="font-size:19px">공지</h2><div class="r"><span class="btn btn-primary btn-sm">{ic("plus")}새 공지</span></div></div>{notices}
<p class="sub" style="font-size:13px;font-weight:800;color:var(--ink-3);margin:18px 0 8px">사이트 맨 위 띠 미리보기</p><div class="banner-pv">{ic("alert","ic ic16")}12/3(수) 02:00~04:00 정기 점검이 있어요<span class="x">✕</span></div></section>
<section><div class="sh">{EAR}<h2 style="font-size:19px">사용자</h2><div class="r"><div class="search" style="width:200px">{ic("search")}닉네임 · 메이커</div></div></div>
<table class="utable"><thead><tr><th>이름</th><th>종류</th><th>가입</th><th>상태</th><th></th></tr></thead><tbody>{users}</tbody></table>
<p class="sub" style="font-size:13px;font-weight:800;color:var(--ink-3);margin:18px 0 8px">운영 기록 (누가 · 언제 · 무엇을 · 왜)</p>
<div class="log2">11/26 14:02 운영자 · 크림빵 · 글쓰기 7일 제한 · 신고 3 (운영정책 4조)<br>11/26 11:40 운영자 · 종이 배 2 · 보완 요청 · 외부 판매 링크<br>11/25 18:11 운영자 · 루프 디버거 v1.2 · 공개 승인</div></section></div></main>'''
    memo = "AD-NOTICE · AD-USERS. 공지(게시 중 · 예약 · 작성 중) + 사이트 맨 위 점검 띠 미리보기. 사용자 표(종류 · 가입 · 상태 · 행동)와 운영 기록(모든 결정은 누가 · 언제 · 왜를 남김 — ADR 0007)."
    return page("운영 · 공지 · 사용자", body, 1000, memo)

if __name__ == "__main__":
    for name, fn in [("AD02-reports.dc.html", reports_page), ("AD03-curation.dc.html", curate_page), ("AD04-notice-users.dc.html", notice_users_page)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
