# L1 마무리 시안: 내 게임(MG-GAMES) · 리뷰·피드백함(MG-FEEDBACK) · 메이커 프로필 만들기(MG-NEWMAKER)
#                리뷰 전체(PG-REVIEWS) · 신고(SH-REPORT) · 고객센터·약관(SH-HELP · SH-LEGAL)
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + [OUT]
import importlib.util
def load(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(HERE, n + ".py")); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
mc, p3, p4, p5 = (load(n) for n in ("mg_c", "pages3", "pages4", "pages5"))
dt, mg = p5.dt, p5.mg
ic, face, logo, EAR, status = mg.ic, mg.face, mg.logo, mg.EAR, mg.status
BASE_CSS = mc.CSS + p3.CSS + p4.CSS + p5.CSS

CSS = r'''
.split3{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:44px;align-items:start}
.panel2{padding:20px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line);display:flex;flex-direction:column;gap:12px}
.panel2 h3{margin:0;font-size:16px;font-weight:800}
/* 피드백함 */
.fb-sel{display:flex;gap:8px;align-items:center;margin-top:18px}
.rvi{display:grid;grid-template-columns:auto minmax(0,1fr);gap:14px;padding:18px 4px;border-top:1px solid var(--line)}
.rvi:first-child{border-top:0}
.rvi .hd{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--ink-3)}
.rvi .hd b{color:var(--ink-1);font-size:14px}
.rvi p{margin:6px 0 10px;font-size:15px;line-height:1.65}
.rvi.new{background:var(--accent-tint);border-radius:14px;border-top-color:transparent;padding:18px 16px}
.reply-ed{display:flex;flex-direction:column;gap:8px;padding:12px;border-radius:12px;background:var(--bg);box-shadow:inset 0 0 0 2px var(--accent)}
.reply-ed .ta{min-height:64px;font-size:15px;line-height:1.6;color:var(--ink-1)}
.reply-ed .row{display:flex;align-items:center;gap:8px}
.reply-ed .row .m{margin-right:auto}
.bug{display:grid;grid-template-columns:minmax(0,1fr);gap:8px;padding:14px 4px;border-top:1px solid var(--line)}
.bug:first-child{border-top:0}
.bug b{font-size:15px}
.bug .seg{justify-self:start}
.bug .env{font-family:ui-monospace,Consolas,monospace;font-size:12.5px;color:var(--ink-3)}
/* 메이커 프로필 만들기 */
.nm-grid{display:grid;grid-template-columns:minmax(0,1fr) 420px;gap:48px;align-items:start;margin-top:28px}
.nm-form{display:flex;flex-direction:column;gap:20px}
.fld2{display:flex;flex-direction:column;gap:8px}
.fld2 > label{font-size:14px;font-weight:800}
.fld2 .help{font-size:13px;color:var(--ink-3)}
.inp{display:flex;align-items:center;height:46px;padding:0 14px;border-radius:var(--radius-md);background:var(--sunken);font-size:15px}
.inp.focus{background:var(--bg);box-shadow:inset 0 0 0 2px var(--accent)}
.inp.ta{height:auto;min-height:84px;align-items:flex-start;padding:12px 14px;line-height:1.6}
.inp .ph{color:var(--ink-3)}
.kind{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.kind > div{padding:14px 16px;border-radius:14px;box-shadow:inset 0 0 0 1px var(--line);font-size:14px;color:var(--ink-2)}
.kind > div.on{box-shadow:inset 0 0 0 2px var(--accent);background:var(--accent-tint)}
.kind > div b{display:block;font-size:15px;color:var(--ink-1);margin-bottom:2px}
.kind > div.off{opacity:.55}
.mkprev{position:sticky;top:90px;padding:20px;border-radius:var(--radius-2xl);background:var(--sunken)}
.mkprev .cap{font-size:13px;font-weight:700;color:var(--ink-3);margin-bottom:12px}
.mkprev .hero{display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:22px;border-radius:16px;background:var(--accent-tint)}
.mkprev .hero .jf{width:84px;height:84px;font-size:30px}
.mkprev .hero b{font-size:24px;font-weight:800}
.mkprev .hero p{margin:0;font-size:14px;color:var(--ink-2);line-height:1.6}
/* 리뷰 전체 */
.rv-head{display:flex;align-items:center;gap:14px;margin-top:24px}
.rv-head .art{width:120px;border-radius:10px}
.rv-head h1{margin:0;font-size:26px;font-weight:800}
.compose{display:flex;flex-direction:column;gap:12px;padding:20px;border-radius:var(--radius-xl);box-shadow:inset 0 0 0 2px var(--accent)}
.compose .yn2{display:flex;gap:8px}
.compose .yn2 span{display:flex;align-items:center;gap:6px;height:44px;padding:0 18px;border-radius:12px;background:var(--sunken);font-weight:800}
.compose .yn2 span.on{background:var(--accent);color:#FFFFFF}
.rvlist .rv{border-top:1px solid var(--line);padding-top:18px;display:flex;flex-direction:column;gap:10px}
.rvlist .rv .hd{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--ink-3)}
.rvlist .rv .hd b{color:var(--ink-1);font-size:14px}
.rvlist .rv .yes{color:var(--accent-text);font-weight:800}
.rvlist .rv .no{color:var(--ink-2);font-weight:800}
.rvlist .rv p{margin:0;font-size:15px;line-height:1.65}
.rvlist .rv .reply{display:flex;gap:8px;padding:12px;border-radius:12px;background:var(--sunken);font-size:14px;line-height:1.55;color:var(--ink-2)}
.rvlist .rv .reply b{color:var(--ink-1);font-size:13px;display:block}
.rvlist .rv .foot{display:flex;gap:12px;font-size:12.5px;color:var(--ink-3)}
.rvlist{display:flex;flex-direction:column;gap:20px}
/* 신고 */
.rep-dlg{width:480px;padding:28px;border-radius:var(--radius-2xl);background:var(--bg);box-shadow:var(--shadow-pop);display:flex;flex-direction:column;gap:14px}
[data-theme="dark"] .rep-dlg{background:var(--raised)}
.rep-dlg h2{margin:0;font-size:22px;font-weight:800}
.rep-dlg .tgt{display:flex;gap:10px;align-items:center;padding:10px;border-radius:12px;background:var(--sunken);font-size:14px}
.rep-dlg .tgt .art{width:72px;border-radius:7px}
.opts{display:flex;flex-direction:column}
.opts label{display:grid;grid-template-columns:22px minmax(0,1fr);gap:10px;align-items:start;padding:10px 4px;font-size:15px;border-top:1px solid var(--line)}
.opts label:first-child{border-top:0}
.opts .rd{width:20px;height:20px;border-radius:999px;box-shadow:inset 0 0 0 1.5px var(--ink-4);margin-top:1px}
.opts .rd.on{box-shadow:inset 0 0 0 6px var(--accent)}
.opts .m{display:block;font-size:13px}
.acts2{display:flex;justify-content:flex-end;gap:8px}
.dimstage{position:relative;padding:40px;border-radius:14px;background:rgb(16 19 22/.5);display:flex;justify-content:center;gap:40px;align-items:flex-start}
/* 고객센터 */
.help-hero{padding:44px 0 36px;text-align:center}
.help-hero h1{margin:0;font-size:30px;font-weight:800}
.help-hero .search{width:560px;height:52px;margin:18px auto 0;font-size:16px}
.cats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.cats > div{padding:20px;border-radius:var(--radius-lg);background:var(--sunken);display:flex;flex-direction:column;gap:6px}
.cats b{font-size:16px}
.cats span{font-size:13.5px;color:var(--ink-3)}
.acc > div{border-top:1px solid var(--line)}
.acc > div:first-child{border-top:0}
.acc .q{display:flex;flex-direction:row;gap:0;align-items:center;justify-content:space-between;min-height:56px;font-size:16px;font-weight:700}
.acc .a{padding:0 0 16px;font-size:15px;line-height:1.7;color:var(--ink-2)}
.legal{display:grid;grid-template-columns:220px minmax(0,1fr);gap:40px}
.toc{position:sticky;top:90px;display:flex;flex-direction:column;gap:2px;font-size:14px}
.toc a{padding:8px 12px;border-radius:8px;color:var(--ink-2)}
.toc a.on{background:var(--sunken);color:var(--ink-1);font-weight:800}
.doc h2{margin:0;font-size:24px;font-weight:800}
.doc .ver{margin:6px 0 18px;font-size:13px;color:var(--ink-3)}
.doc h3{margin:22px 0 8px;font-size:17px;font-weight:800}
.doc p,.doc li{font-size:15px;line-height:1.8;color:var(--ink-2)}
.doc .sum{padding:16px 18px;border-radius:var(--radius-lg);background:var(--accent-tint);font-size:14.5px;line-height:1.7;color:var(--ink-1)}
'''

def mypage(title, body, h, memo, make=False):
    html = (mg.page if make else dt.page)(title, body, h, memo)
    return html.replace("</style>", BASE_CSS + CSS + "\n</style>", 1)

def todo_rows():
    return '<div class="todo">' + "".join(f'<div class="td"><span class="ico{" acc" if acc else ""}">{ic(icn,"ic ic16")}</span><span><b>{t}</b><span class="m">{m}</span></span><span class="btn btn-{k} btn-sm">{lab}</span></div>' for icn, acc, t, m, (k, lab) in mg.TODOS) + "</div>"

def games_page():
    body = mg.header2(True, "내 게임") + f'''<main class="wrap">
<div class="pg-title"><h1>내 게임</h1><span class="m">픽셀상점 · 4개</span><div class="r"><span class="btn btn-secondary">{ic("pen","ic ic16")}메이커 페이지 고치기</span><span class="btn btn-primary">{ic("up2","ic ic16")}새 게임 올리기</span></div></div>
<aside class="panel2" style="margin-top:24px"><h3>처리할 일 <span class="cnt">3</span></h3>{todo_rows()}</aside>
<nav class="utabs" style="margin-top:28px"><a href="#" aria-current="page">전체 4</a><a href="#">공개 1</a><a href="#">심사 중 1</a><a href="#">보완 요청 1</a><a href="#">작성 중 1</a></nav>
<div class="mg-rows" style="margin-top:14px">{"".join(mg.game_row(g) for g in mg.GAMES)}{mg.draft_row()}</div>
<p class="m" style="margin-top:28px">통계 숫자는 나에게만 보여요. 게임을 누르면 관리 · 통계로 가요.</p>
</main>''' + mg.footer()
    memo = "MG-GAMES. 메이커 홈에서 뺀 ‘내 게임’ 이 오는 곳(M1). 상태 탭(전체 · 공개 · 심사 중 · 보완 요청 · 작성 중) + MakerGameRow 목록 + 오른쪽 처리할 일(TodoRow). → 컴포넌트 2 의 ‘후보’ 두 개가 여기서 채택."
    return mypage("내 게임", body, 1300, memo, make=True)

def feedback_page():
    rv = f'''<div class="rvi new">{face("ㅁ","bora","md")}<span><span class="hd"><b>모래시계</b><span style="color:var(--ink-2);font-weight:800">비추천</span>· 플레이 1.1시간 · 2시간 전 <span class="st st-fix st-sm" style="margin-left:6px">답글 없음</span></span><p>튜토리얼이 너무 길어요. 처음 세 스테이지는 건너뛰기가 있으면 좋겠어요.</p>
<div class="reply-ed"><span class="ta">v1.2 에서 튜토리얼을 한 스테이지로 줄였어요. 다시 한 번 봐 주세요!<span class="caret" style="display:inline-block;width:2px;height:1.1em;background:var(--accent);vertical-align:-3px"></span></span><div class="row"><span class="m">답글은 모두에게 보이고, 리뷰 쓴 사람에게 알림이 가요</span><span class="btn btn-secondary btn-sm">취소</span><span class="btn btn-primary btn-sm">답글 달기</span></div></div></span></div>
<div class="rvi">{face("ㄱ","gyul","md")}<span><span class="hd"><b>귤껍질</b><span style="color:var(--accent-text);font-weight:800">추천</span>· 플레이 48분 · 어제</span><p>출퇴근길에 한 판씩 하기 딱 좋아요.</p><span class="btn btn-secondary btn-sm">답글 달기</span></span></div>
<div class="rvi">{face("ㅅ","hong","md")}<span><span class="hd"><b>새벽코딩</b><span style="color:var(--accent-text);font-weight:800">추천</span>· 3.2시간 · 3일 전 <span class="st st-live st-sm" style="margin-left:6px">{ic("check")}답글 함</span></span><p>15스테이지 이후로 난이도가 확 오르는데 힌트가 잘 잡아줘요.</p></span></div>'''
    bugs = f'''<div class="bug"><b>3단계에서 소리가 안 나요</b><span class="seg" style="justify-self:end"><span class="on">새로</span><span>확인 중</span><span>고침</span></span><span class="env">Windows 11 · Chrome 131 · 1920×1080 · v1.2 · 오류 없음</span></div>
<div class="bug"><b>세로 모드에서 블록이 잘려요</b><span class="seg" style="justify-self:end"><span>새로</span><span>확인 중</span><span class="on">고침</span></span><span class="env">iOS 18 · Safari · 390×844 · v1.1</span></div>'''
    body = mg.header2(True, "내 게임") + f'''<main class="wrap">
<div class="crumb2"><a href="#">내 게임</a>{ic("chev")}<a href="#">루프 디버거</a></div>
<div class="pg-title" style="margin-top:10px"><h1>리뷰 · 피드백</h1></div>
<nav class="utabs" style="margin-top:16px"><a href="#" aria-current="page">리뷰 38 <span class="cnt" style="height:18px;min-width:18px;font-size:11px;padding:0 5px">2</span></a><a href="#">버그 제보 3</a><a href="#">응원 · 출시 후</a></nav>
<div class="split3" style="margin-top:18px"><div><div class="chips" style="margin-bottom:6px"><button class="chip" aria-pressed="true">답글 안 단 것 2</button><button class="chip">비추천 3</button><button class="chip">최신순</button></div>{rv}</div>
<aside class="panel2"><h3>버그 제보</h3>{bugs}<a class="link" href="#" style="font-size:14px">전체 3개 ›</a></aside></div>
</main>''' + mg.footer()
    memo = "MG-FEEDBACK. 리뷰(답글 안 단 것 먼저 · 그 자리에서 답글 편집 · 답글은 공개되고 알림) + 버그 제보(환경 정보 · 새로/확인 중/고침 상태 — 바꾸면 제보한 사람에게 알림). 응원함은 출시 후(L2)."
    return mypage("리뷰 · 피드백함", body, 1400, memo, make=True)

def newmaker_page():
    eyes = "".join(f'<span class="{"on" if c == "ㅍ" else ""}">{c}</span>' for c in "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ")
    body = mg.header2(True, "내 게임") + f'''<main class="wrap">
<div class="pg-title"><h1>메이커 프로필 만들기</h1><span class="m">게임을 올리기 전에 한 번만</span></div>
<div class="nm-grid"><div class="nm-form">
<div class="fld2"><label>어떤 메이커인가요?</label><div class="kind"><div class="on"><b>혼자 만들어요</b>개인 메이커</div><div class="off"><b>팀으로 만들어요</b>팀원 초대 · 출시 후</div></div></div>
<div class="fld2"><label>메이커 이름</label><div class="inp focus">픽셀상점|</div><span class="help">게임 카드와 메이커 페이지에 나와요. 2~20자, 나중에 바꿀 수 있어요.</span></div>
<div class="fld2"><label>메이커 얼굴</label><div class="pick-grid">{eyes}</div><span class="help">플레이어 얼굴과 따로 정할 수 있어요. 색은 대표 게임의 색에서 자동으로 골라요.</span></div>
<div class="fld2"><label>한 줄 소개</label><div class="inp ta">퍼즐만 만드는 1인 메이커예요. 회사 다니면서 주말에 만들어요.</div></div>
<div class="fld2"><label>링크 <span class="m" style="font-weight:600">· 선택</span></label><div class="inp"><span class="ph">pixelshop.dev · 다른 스토어 · SNS</span></div><span class="help">외부 판매 링크는 여기에만 둘 수 있어요.</span></div>
<div style="display:flex;gap:8px"><span class="btn btn-primary">만들고 첫 게임 올리기</span><span class="btn btn-secondary">나중에</span></div></div>
<aside class="mkprev"><div class="cap">메이커 페이지 미리보기</div><div class="hero"><span class="jf" style="background:var(--color-face-jjok)">ㅍ<i>ㅅ</i>ㅍ</span><b>픽셀상점</b><p>퍼즐만 만드는 1인 메이커예요. 회사 다니면서 주말에 만들어요.</p><span class="btn btn-primary btn-sm">팔로우</span></div></aside></div>
</main>''' + mg.footer()
    memo = "MG-NEWMAKER. 게임 올리기 전 한 번. 개인/팀(팀은 L2) · 이름 · 메이커 얼굴(고양이 실루엣, 색은 대표 게임색) · 한 줄 소개 · 링크(외부 판매 링크는 여기만). 오른쪽에 메이커 페이지가 어떻게 보일지 바로 미리보기."
    return mypage("메이커 프로필 만들기", body, 1300, memo, make=True).replace(".pick-grid{display:grid;grid-template-columns:repeat(14,minmax(0,1fr));gap:6px}", ".pick-grid{display:grid;grid-template-columns:repeat(14,minmax(0,1fr));gap:6px}")

def reviews_page():
    revs = "".join(f'<article class="rv"><div class="hd">{face(ch,col,"xs")}<b>{who}</b><span class="{"yes" if yes else "no"}">{"추천" if yes else "비추천"}</span><span>· 플레이 {tm} · {d}</span></div><p>{t}</p>{rep}<div class="foot"><span>도움이 됐어요 {h}</span><span>신고</span></div></article>' for ch, col, who, yes, tm, d, t, rep, h in [
        ("ㅅ", "hong", "새벽코딩", True, "3.2시간", "11/24", "회사에서 하는 일이랑 너무 똑같아서 웃겼어요. 그런데 이건 고치면 칭찬을 해 주네요.", f'<div class="reply">{face("ㅍ","jjok","xs")}<span><b>픽셀상점 · 메이커 답글</b>다음 업데이트에서 단계를 하나 더 넣을게요!</span></div>', 12),
        ("ㄱ", "gyul", "귤껍질", True, "48분", "11/23", "출퇴근길에 한 판씩 하기 딱 좋아요. 휴대폰 가로 모드에서도 블록이 안 작아서 좋았어요.", "", 8),
        ("ㅁ", "bora", "모래시계", False, "1.1시간", "11/22", "튜토리얼이 너무 길어요. 처음 세 스테이지는 건너뛰기가 있으면 좋겠어요.", f'<div class="reply">{face("ㅍ","jjok","xs")}<span><b>픽셀상점 · 메이커 답글</b>v1.2 에서 튜토리얼을 한 스테이지로 줄였어요.</span></div>', 21)])
    tags = "".join(f'<button class="chip">{t} <span class="c">{n}</span></button>' for t, n in [("짧고 굵음", 21), ("퍼즐 좋아하면", 18), ("한 손으로", 9), ("튜토리얼이 길어요", 4)])
    body = p5.pgh("게임") + f'''<main class="wrap" style="width:900px">
<div class="crumb2"><a href="#">게임</a>{ic("chev")}<a href="#">루프 디버거</a></div>
<div class="rv-head"><span class="art a-loop"></span><span><h1>루프 디버거 리뷰</h1><span class="m">추천 92% · 38개 · 플레이한 사람만 쓸 수 있어요</span></span></div>
<section class="sec" style="margin-top:28px"><div class="compose"><b style="font-size:16px">내 리뷰 쓰기 <span class="m" style="font-weight:600">· 플레이 48분</span></b><div class="yn2"><span class="on">{ic("up","ic ic16")}추천</span><span><svg class="ic ic16" style="transform:rotate(180deg)"><use href="#i-up"></use></svg>별로</span></div><div class="chips"><button class="chip" aria-pressed="true">짧고 굵음</button><button class="chip">퍼즐 좋아하면</button><button class="chip">한 손으로</button><button class="chip">어려워요</button></div><div class="inp ta"><span class="ph">한 줄이면 충분해요 (선택)</span></div><div class="acts2"><span class="btn btn-primary btn-sm">올리기</span></div></div></section>
<section class="sec" style="margin-top:36px"><div class="sh">{EAR}<h2>38개</h2><div class="r"><span class="sort cm-sort"><span class="on">도움 많은</span><span>최신</span><span>추천만</span><span>비추천만</span></span></div></div><div class="chips" style="margin-bottom:14px">{tags}</div><div class="rvlist">{revs}</div>
<div class="pager2"><span>‹</span><span class="on">1</span><span>2</span><span>3</span><span>›</span></div></section>
</main>''' + dt.footer()
    memo = "PG-REVIEWS. 위에 내 리뷰 쓰기(플레이 기록 있을 때만: 추천/별로 한 번 + 태그 + 한 줄 선택). 정렬(도움 많은 · 최신 · 추천만 · 비추천만), 태그로 거르기, 리뷰마다 플레이 시간 · 메이커 답글 · 신고."
    return mypage("리뷰 전체", body, 1700, memo)

def report_page():
    dlg = f'''<div class="rep-dlg" role="dialog" aria-modal="true"><h2>게임 신고</h2><div class="tgt"><span class="art a-grid"></span><span><b>그리드 러너</b><span class="m" style="display:block">보라네</span></span></div>
<div class="opts"><label><span class="rd on"></span><span>작동하지 않아요<span class="m">로딩이 안 되거나 멈춰요 — 환경 정보가 함께 가요</span></span></label><label><span class="rd"></span><span>악성 · 의심 파일<span class="m">설치 파일이 이상하게 동작해요</span></span></label><label><span class="rd"></span><span>저작권 침해<span class="m">권리자라면 저작권 신고 양식이 더 빨라요</span></span></label><label><span class="rd"></span><span>부적절한 내용<span class="m">콘텐츠 표시와 다른 폭력 · 선정 등</span></span></label><label><span class="rd"></span><span>설명과 달라요</span></label></div>
<div class="inp ta"><span class="ph">무슨 일이 있었는지 적어 주세요 (선택)</span></div><p class="m" style="margin:0">신고한 사람은 메이커에게 알리지 않아요. 결과는 알림으로 알려 드려요.</p>
<div class="acts2"><span class="btn btn-secondary">취소</span><span class="btn btn-danger">신고하기</span></div></div>'''
    small = f'''<div class="rep-dlg" role="dialog" style="width:380px"><h2 style="font-size:19px">댓글 신고</h2><div class="opts"><label><span class="rd on"></span><span>욕설 · 괴롭힘</span></label><label><span class="rd"></span><span>광고 · 도배</span></label><label><span class="rd"></span><span>개인정보 노출</span></label><label><span class="rd"></span><span>기타</span></label></div><div class="acts2"><span class="btn btn-secondary btn-sm">취소</span><span class="btn btn-danger btn-sm">신고하기</span></div></div>'''
    toast = f'<span class="toast" style="display:inline-flex;align-items:center;gap:10px;height:44px;padding:0 18px 0 14px;border-radius:999px;background:var(--surface-ink);color:#FFFFFF;font-size:14px;font-weight:600;box-shadow:var(--shadow-pop)">{ic("check","ic ic16")}신고를 받았어요 · 결과는 알림으로 알려 드려요</span>'
    body = p5.pgh("게임") + f'''<main class="wrap"><div class="pg-title"><h1>신고</h1><span class="m">게임 · 리뷰 · 글 · 댓글 공통</span></div>
<div class="dimstage" style="margin-top:24px">{dlg}<div style="display:flex;flex-direction:column;gap:24px">{small}{toast}</div></div></main>''' + dt.footer()
    memo = "SH-REPORT. 대상 미리보기 + 이유(한 개, 설명 한 줄씩) + 선택 설명 + 익명 안내 + 다홍 ‘신고하기’(대화상자 안에서만). 게임 ‘작동하지 않아요’ 는 환경 정보 첨부. 끝나면 토스트, 결과는 알림."
    return mypage("신고", body, 1100, memo)

def help_page():
    cats = "".join(f'<div><b>{t}</b><span>{d}</span></div>' for t, d in [("계정 · 로그인", "Google · GitHub 연결, 얼굴 바꾸기"), ("플레이", "안 될 때, 저장, 휴대폰"), ("다운로드 · 보안", "설치 안내, 검사 결과"), ("게임 올리기", "심사, 보완 요청, 파일 형식")])
    faq = "".join(f'<div><div class="q">{q}<span>{ic("chev","ic ic16")}</span></div>{("<div class=\"a\">" + a + "</div>") if a else ""}</div>' for q, a in [("게임이 검은 화면에서 멈춰요", "새로고침 후에도 같으면 플레이 화면의 ‘문제 알리기’ 를 눌러 주세요. 브라우저 · 기기 정보가 함께 가서 메이커가 빨리 고칠 수 있어요."), ("다른 기기에서 이어 할 수 있나요?", ""), ("Windows 가 ‘PC 보호’ 창을 띄워요", ""), ("탈퇴하면 리뷰도 지워지나요?", "")])
    body = p5.pgh("") + f'''<main class="wrap">
<div class="help-hero"><h1>무엇을 도와드릴까요?</h1><div class="search">{ic("search")}궁금한 걸 적어 보세요 — 예: 저장, 설치, 심사</div></div>
<div class="cats">{cats}</div>
<section class="sec"><div class="split3"><div><div class="sh">{EAR}<h2>자주 묻는 것</h2></div><div class="acc">{faq}</div></div>
<aside class="panel2"><h3>찾는 답이 없나요?</h3><p class="m" style="margin:0">로그인한 계정으로 문의를 남기면 보통 이틀 안에 답을 드려요.</p><span class="btn btn-primary btn-sm" style="align-self:flex-start">문의 남기기</span><p class="m" style="margin:8px 0 0">저작권 신고는 <a class="link" href="#" style="font-size:13px">전용 양식</a>으로</p></aside></div></section>
<section class="sec"><div class="sh">{EAR}<h2>약관 · 정책</h2></div><div class="legal"><nav class="toc"><a class="on" href="#">이용약관</a><a href="#"><b>개인정보처리방침</b></a><a href="#">운영정책</a><a href="#">저작권 신고</a><a href="#">이전 버전</a></nav>
<div class="doc"><h2>이용약관</h2><div class="ver">시행 2026.12.01 · 이전 버전 보기</div><div class="sum"><b>한눈에 보기</b> — aDmD 는 무료예요. 올린 게임의 권리는 메이커에게 있고, aDmD 는 보여 주고 내려받게 하는 데만 써요. 광고용으로 정보를 쓰지 않아요.</div>
<h3>제1조 목적</h3><p>이 약관은 aDmD Games(이하 ‘서비스’)를 이용하는 데 필요한 권리 · 의무와 책임을 정합니다.</p><h3>제2조 게임의 권리</h3><p>메이커가 올린 게임과 자료의 권리는 메이커에게 있습니다. 서비스는 게임을 보여 주고, 실행하고, 내려받게 하는 데 필요한 범위에서만 이용합니다.</p></div></div></section>
</main>''' + dt.footer()
    memo = "SH-HELP · SH-LEGAL. 검색 → 분류 4개 → 자주 묻는 것(펼침) + 문의 남기기(로그인 계정, 보통 이틀). 약관은 왼쪽 목차 + 본문, 맨 위 ‘한눈에 보기’ 요약 상자, 시행일 · 이전 버전. 실제 문구는 법률 검토 필요."
    return mypage("고객센터 · 약관", body, 1900, memo)

if __name__ == "__main__":
    for name, fn in [("내 게임.dc.html", games_page), ("리뷰 · 피드백함.dc.html", feedback_page), ("메이커 프로필 만들기.dc.html", newmaker_page), ("리뷰 전체.dc.html", reviews_page), ("신고.dc.html", report_page), ("고객센터 · 약관.dc.html", help_page)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
