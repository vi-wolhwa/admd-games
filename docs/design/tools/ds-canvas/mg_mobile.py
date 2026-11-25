# MakersGround 모바일 시안 — mg.py 의 데이터·헬퍼를 재사용
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + ([OUT])
import importlib.util
spec = importlib.util.spec_from_file_location("mg", os.path.join(HERE, "mg.py"))
mg = importlib.util.module_from_spec(spec); spec.loader.exec_module(mg)
ic, face, logo, status, EAR = mg.ic, mg.face, mg.logo, mg.status, mg.EAR

M_CSS = r'''
body{min-width:0}
.phones{display:flex;gap:48px;align-items:flex-start;justify-content:center;padding:48px 40px 72px;background:var(--sunken)}
.pcol{display:flex;flex-direction:column;gap:14px;width:375px}
.pcol > b{font-size:15px;font-weight:800}
.pcol > span{font-size:13px;color:var(--ink-3);line-height:1.5;margin-top:-8px;min-height:40px}
.phone{position:relative;width:375px;height:812px;border-radius:40px;overflow:hidden;background:var(--bg);box-shadow:0 0 0 10px #0C0E11,0 30px 60px -20px rgb(0 0 0/.45)}
.pscroll{position:absolute;inset:0;overflow:hidden;padding:44px 0 84px}
.sbar{position:absolute;top:0;left:0;right:0;height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 26px;font-size:14px;font-weight:700;z-index:5;background:var(--bg)}
.mtop{display:flex;align-items:center;gap:6px;height:52px;padding:0 10px 0 18px}
.mtop .word{font-size:13px;font-weight:800;color:var(--ink-2);margin-top:6px}
.mtop .sp{margin-left:auto;display:flex;align-items:center;gap:2px}
.mtop .icon-btn{width:44px;height:44px}
.msec{padding:0 18px;margin-top:28px}
.msh{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.msh h2{margin:0;font-size:19px;line-height:1.3;font-weight:800;letter-spacing:-.02em}
.msh .r{margin-left:auto;font-size:13px;font-weight:700;color:var(--ink-3)}
.msh .ear{width:18px;height:10px;margin-top:4px}
.mtd{display:grid;grid-template-columns:36px minmax(0,1fr) 16px;gap:12px;align-items:center;min-height:64px;padding:10px 0;border-top:1px solid var(--line)}
.mtd:first-child{border-top:0}
.mtd b{display:block;font-size:15px;line-height:1.4}
.mtd .m{display:block;font-size:13px}
.mtd .ico{display:grid;place-items:center;width:36px;height:36px;border-radius:10px;background:var(--sunken);color:var(--ink-2)}
.mtd .ico.acc{background:var(--accent-tint);color:var(--accent-text)}
.mtd > .ic{color:var(--ink-4)}
.hs{display:flex;gap:12px;overflow:hidden;padding:0 18px;margin:0 -18px}
.mgc{flex:0 0 228px;display:flex;flex-direction:column;gap:6px;min-width:0}
.mgc .art{border-radius:12px}
.mgc b{font-size:15px}
.mgc .row{display:flex;align-items:center;gap:6px;font-size:12.5px;color:var(--ink-3);min-width:0}
.mlog{display:grid;grid-template-columns:minmax(0,1fr) 104px;gap:14px;align-items:center;padding:12px 0;border-top:1px solid var(--line)}
.mlog:first-child{border-top:0}
.mlog b{font-size:15px;line-height:1.45;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.mlog .by{display:flex;align-items:center;gap:6px;margin-top:6px;font-size:12.5px;color:var(--ink-3)}
.mlog .art{border-radius:10px}
.tabbar{position:absolute;left:0;right:0;bottom:0;height:84px;padding:6px 6px 26px;display:grid;grid-template-columns:repeat(5,1fr);background:color-mix(in srgb,var(--bg) 94%,transparent);backdrop-filter:blur(12px);border-top:1px solid var(--line);z-index:6}
.tabbar a{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:11px;font-weight:700;color:var(--ink-3)}
.tabbar a .ic{width:22px;height:22px}
.tabbar a[aria-current]{color:var(--ink-1)}
.tabbar a[aria-current] .ic{color:var(--accent)}
.tabbar .up{width:52px;height:52px;margin:-4px auto 0;border-radius:18px;background:var(--accent);display:grid;place-items:center;box-shadow:var(--shadow-float)}
.tabbar .up .ic{width:24px;height:24px;color:#FFFFFF}
.mintro{padding:8px 18px 0}
.mintro h1{margin:8px 0 0;font-family:var(--font-display);font-weight:400;font-size:30px;line-height:1.25}
.mintro p{margin:12px 0 0;font-size:15px;line-height:1.65;color:var(--ink-2)}
.msteps{list-style:none;margin:20px 0 0;padding:0;display:flex;flex-direction:column;counter-reset:h}
.msteps li{display:grid;grid-template-columns:28px minmax(0,1fr);gap:12px;padding:12px 0;border-top:1px solid var(--line);font-size:14px;color:var(--ink-2);line-height:1.5}
.msteps li::before{counter-increment:h;content:counter(h);display:grid;place-items:center;width:28px;height:28px;border-radius:999px;background:var(--accent-tint);color:var(--accent-text);font-weight:800;font-size:13px}
.msteps b{display:block;color:var(--ink-1);font-size:15px}
.mbtn{display:flex;height:52px;border-radius:14px;align-items:center;justify-content:center;gap:6px;font-size:16px;font-weight:800}
.mback{display:flex;align-items:center;gap:4px;height:52px;padding:0 14px 0 4px}
.mback .t{font-size:17px;font-weight:800;margin-left:2px}
.vsteps{display:flex;flex-direction:column;margin-top:6px}
.vs{display:grid;grid-template-columns:20px minmax(0,1fr);gap:12px;position:relative;padding-bottom:16px}
.vs::before{content:"";position:absolute;left:9px;top:20px;bottom:0;width:2px;background:var(--sunken-hover)}
.vs:last-child::before{display:none}
.vs > i{width:20px;height:20px;border-radius:999px;box-shadow:inset 0 0 0 2px var(--ink-4);background:var(--bg);display:grid;place-items:center;color:#FFFFFF;position:relative;z-index:1}
.vs.done > i{background:var(--ink-2);box-shadow:none}
.vs.now > i{background:var(--accent);box-shadow:0 0 0 4px var(--accent-tint)}
.vs b{font-size:15px;display:block}
.vs .m{font-size:13px;display:block}
.fixbox{margin-top:8px;padding:12px 14px;border-radius:14px;background:var(--accent-tint);font-size:14px;line-height:1.55}
.fixbox b{display:flex;align-items:center;gap:6px;color:var(--accent-text);font-size:14px;margin-bottom:2px}
.shots-row{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.shots-row .art{border-radius:9px}
.shots-row .add{display:grid;place-items:center;aspect-ratio:16/9;border-radius:9px;background:var(--accent-tint);color:var(--accent-text)}
.kv{display:flex;flex-direction:column}
.kv > div{display:grid;grid-template-columns:84px minmax(0,1fr) 16px;gap:10px;align-items:center;min-height:52px;border-top:1px solid var(--line);font-size:14px}
.kv > div:first-child{border-top:0}
.kv > div > span:first-child{color:var(--ink-3);font-weight:600}
.kv .ic{color:var(--ink-4)}
'''

def phone(inner, tab_active=0):
    tabs = [("home", "홈"), ("box", "내 게임"), None, ("pen", "일지"), ("user", "나")]
    tb = []
    for i, t in enumerate(tabs):
        if t is None:
            tb.append(f'<a href="#" aria-label="게임 올리기"><span class="up">{ic("plus")}</span></a>')
            continue
        cur = ' aria-current="page"' if i == tab_active else ""
        tb.append(f'<a href="#"{cur}>{ic(t[0])}{t[1]}</a>')
    return f'<div class="phone"><div class="sbar"><span>9:41</span><span>5G</span></div><div class="pscroll">{inner}</div><nav class="tabbar">{"".join(tb)}</nav></div>'

def mtop(signed=True):
    right = mg.THEME_BTN + f'<button class="icon-btn" aria-label="검색">{ic("search", "ic ic20")}</button>'
    if signed:
        right += f'<button class="icon-btn" aria-label="알림 2개">{ic("bell", "ic ic20")}<span class="dot-new"></span></button>'
    else:
        right += '<span class="btn btn-secondary btn-sm" style="height:36px;margin-left:4px">로그인</span>'
    return f'<div class="mtop"><span class="logo" style="font-size:19px">{logo()}</span><span class="word">MakersGround</span><span class="sp">{right}</span></div>'

def m_home():
    tds = "".join(f'<div class="mtd"><span class="ico{" acc" if acc else ""}">{ic(icn, "ic ic16")}</span><span><b>{t}</b><span class="m clip">{m}</span></span>{ic("chev")}</div>' for icn, acc, t, m, _ in mg.TODOS)
    games = ""
    for g in mg.GAMES:
        sub = f'7일 {g["plays"]} · {g["newr"]}' if g.get("spark") else g["note"]
        games += f'<div class="mgc"><span class="art {g["art"]}"></span><b>{g["t"]}</b><span class="row">{status(*g["st"])}<span class="clip">{sub}</span></span></div>'
    logs = "".join(f'<div class="mlog"><span><b>{l[1]}</b><span class="by">{face(l[3], l[4], "xs")}{l[5]} · {l[7]}명이 좋아해요</span></span><span class="art {l[0]}"></span></div>' for l in mg.LOGS[:4])
    inner = f'''{mtop()}
<div class="msec" style="margin-top:12px"><div class="msh">{EAR}<h2>할 일</h2><span class="cnt">3</span></div>{tds}</div>
<div class="msec"><div class="msh">{EAR}<h2>내 게임</h2><span class="r">전체 4</span></div><div class="hs">{games}</div></div>
<div class="msec"><div class="msh">{EAR}<h2>개발일지</h2><span class="r">전체 보기</span></div>{logs}</div>'''
    return phone(inner, 0)

def m_guest():
    logs = "".join(f'<div class="mlog"><span><b>{l[1]}</b><span class="by">{face(l[3], l[4], "xs")}{l[5]} · {l[6]}</span></span><span class="art {l[0]}"></span></div>' for l in mg.LOGS[:3])
    inner = f'''{mtop(False)}
<div class="mintro"><h1>만든 게임,<br>여기에 올려 보세요</h1><p>웹 빌드는 바로 플레이, 설치 파일은 무료 보안 검사 후 공개. 광고도 수수료도 없어요.</p>
<ol class="msteps"><li><span><b>메이커 프로필 만들기</b>이름과 얼굴만 있으면 돼요</span></li><li><span><b>게임 올리기</b>저장하며 진행 — PC 에서 이어서 해도 돼요</span></li><li><span><b>검사 · 심사 후 공개</b>보통 이틀 안에 끝나요</span></li></ol>
<span class="mbtn btn-primary" style="margin-top:16px">{ic("up2", "ic ic16")}첫 게임 올리기</span>
<span class="mbtn" style="margin-top:4px;color:var(--ink-2);font-size:15px;font-weight:700;height:44px">올리기 전에 읽어 보기 ›</span></div>
<div class="msec"><div class="msh">{EAR}<h2>메이커들의 개발일지</h2></div>{logs}</div>'''
    return phone(inner, 0)

def m_game():
    inner = f'''<div class="mback"><button class="icon-btn" aria-label="뒤로"><svg class="ic ic20" viewBox="0 0 16 16"><path d="M10 3 5 8l5 5"></path></svg></button><span class="t">종이 배 2</span><span style="margin-left:auto">{status("fix", "보완 요청")}</span></div>
<div class="msec" style="margin-top:8px"><div class="vsteps">
<div class="vs done"><i>{ic("check", "ic ic12")}</i><span><b>작성</b><span class="m">11/24 제출</span></span></div>
<div class="vs done"><i>{ic("check", "ic ic12")}</i><span><b>자동 검사 통과</b><span class="m">악성코드 · 용량 · 실행 확인</span></span></div>
<div class="vs now"><i></i><span><b>심사 — 보완 요청</b><span class="m">2시간 전 · 고치면 바로 다시 심사해요</span>
<div class="fixbox"><b>{ic("alert")}고칠 것 1개</b>스크린샷을 3장 이상 올려 주세요. 지금 2장이에요.</div></span></div>
<div class="vs"><i></i><span><b style="color:var(--ink-3)">공개</b></span></div>
</div></div>
<div class="msec" style="margin-top:8px"><div class="msh"><h2 style="font-size:16px">스크린샷 2 / 최소 3</h2></div>
<div class="shots-row"><span class="art a-paper"></span><span class="art a-halcyon"></span><span class="add">{ic("plus", "ic ic20")}</span></div>
<span class="mbtn btn-primary" style="margin-top:14px">고친 내용으로 다시 제출</span></div>
<div class="msec"><div class="msh"><h2 style="font-size:16px">휴대폰에서 바로 고치기</h2></div>
<div class="kv"><div><span>한 줄 소개</span><span class="clip">접은 종이배로 강을 따라 내려가요</span>{ic("chev")}</div><div><span>공개 설정</span><span>심사 통과 후 바로 공개</span>{ic("chev")}</div><div><span>태그</span><span>탐험 · 힐링 · 20분</span>{ic("chev")}</div></div></div>'''
    return phone(inner, 1)

def page_m():
    cols = [("메이커 홈", "할 일 → 내 게임(가로로 넘김) → 일지. 올리기는 탭바 가운데 버튼 하나.", m_home()),
            ("게스트 홈", "지표 없이 올리는 법 3단계와 버튼 하나. 아래는 다른 메이커들의 일지.", m_guest()),
            ("게임 상태 · 보완 요청", "알림을 받고 들어온 화면. 어디까지 왔는지 · 무엇을 고칠지 · 여기서 바로 고치기.", m_game())]
    body = '<div class="phones">' + "".join(f'<div class="pcol"><b>{t}</b><span>{d}</span>{p}</div>' for t, d, p in cols) + "</div>"
    memo = "MakersGround 는 휴대폰도 1급. 탭바(홈 · 내 게임 · 올리기 · 일지 · 나), 누름 영역 44 이상, 큰 버튼 52. 업로드 마법사는 PC 권장이지만 저장하며 진행해 휴대폰에서 이어 쓸 수 있다."
    html = mg.page("MakersGround 모바일", body, 1000, memo, width=1400)
    return html.replace("</style>", M_CSS + "\n</style>", 1)

if __name__ == "__main__":
    # M3 결정 이후 모바일 페이지는 mg_c.py 가 만든다. 이 파일은 헬퍼·CSS 제공용
    raise SystemExit("MakersGround 모바일은 mg_c.py 로 생성하세요")
    html = page_m()
    open(os.path.join(OUT, "MakersGround 모바일.dc.html"), "w", encoding="utf-8").write(html)
    print("MakersGround 모바일.dc.html", len(html))
