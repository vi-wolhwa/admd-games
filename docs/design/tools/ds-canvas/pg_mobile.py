# PlayGround 모바일 시안 — 홈·탐색 / 게임(상세·불가·가로 플레이·라이브러리)
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + [OUT]
import importlib.util
spec = importlib.util.spec_from_file_location("mgm", os.path.join(HERE, "mg_mobile.py"))
mgm = importlib.util.module_from_spec(spec); spec.loader.exec_module(mgm)
spec2 = importlib.util.spec_from_file_location("detail", os.path.join(HERE, "detail.py"))
dt = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(dt)
mg = dt.mg
ic, face, logo, EAR, status = mg.ic, mg.face, mg.logo, mg.EAR, mg.status

CSS = r'''
.mtop .word{color:var(--ink-2)}
.mbanner{position:relative;margin:4px 18px 0;border-radius:16px;overflow:hidden;aspect-ratio:4/3;color:#FFFFFF}
.mbanner .art{position:absolute;inset:0;border-radius:0;aspect-ratio:auto}
.mbanner .scrim{position:absolute;inset:auto 0 0 0;height:62%;background:linear-gradient(transparent,rgb(10 18 30/.92))}
.mbanner .t{position:absolute;left:16px;right:16px;bottom:14px;display:flex;flex-direction:column;gap:6px}
.mbanner .t b{font-family:var(--font-display);font-weight:400;font-size:28px;line-height:1.15}
.mbanner .t .m{color:rgb(255 255 255/.8)}
.mbanner .pg{position:absolute;right:12px;top:12px;height:26px;padding:0 10px;border-radius:999px;background:rgb(16 19 22/.6);font-size:12px;font-weight:800;display:flex;align-items:center}
.mdots{display:flex;justify-content:center;gap:5px;margin-top:10px}
.mdots i{width:5px;height:5px;border-radius:999px;background:var(--sunken-hover)}
.mdots i.on{width:18px;background:var(--accent)}
.mrail{display:flex;gap:12px;overflow:hidden;padding:0 18px;margin:0 -18px}
.mcard{flex:0 0 200px;display:flex;flex-direction:column;gap:5px;min-width:0}
.mcard .art{border-radius:12px;--overlay-inset:7px}
.mcard b{font-size:15px;line-height:1.35}
.mcard .m{font-size:12.5px}
.mcard.cont .bar{height:4px;margin-top:2px}
.mcard .go{display:flex;align-items:center;justify-content:center;gap:4px;height:36px;border-radius:10px;background:var(--accent);color:#FFFFFF;font-size:13.5px;font-weight:800;margin-top:4px}
.pcflag{position:absolute;right:7px;top:7px;z-index:3;display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px;border-radius:999px;background:var(--scrim-strong);color:#FFFFFF;font-size:11.5px;font-weight:800}
.mrank{display:flex;flex-direction:column}
.mrank > div{display:grid;grid-template-columns:28px 88px minmax(0,1fr) auto;gap:10px;align-items:center;padding:7px 0}
.mrank .n{font-family:var(--font-display);font-size:22px;text-align:center;color:var(--ink-2)}
.mrank > div:nth-child(-n+3) .n{color:var(--accent-text)}
.mrank .art{border-radius:8px}
.mrank b{display:block;font-size:14.5px}
.mrank .m{display:block;font-size:12.5px}
.mrank .k{font-size:12px;font-weight:800;color:var(--rank-up)}
.mband{margin:0 18px;padding:16px;border-radius:16px;background:var(--accent-tint)}
.m2{display:grid;grid-template-columns:1fr 1fr;gap:16px 12px}
.m2 .mcard{flex:none}
.mchips2{display:flex;gap:6px;overflow:hidden;margin:0 -18px 10px;padding:0 18px}
.mchips2 .chip{height:34px;font-size:13.5px;padding:0 12px;flex:none}
.mlogin{margin:0 18px;padding:18px;border-radius:18px;background:var(--accent);color:#FFFFFF;display:flex;flex-direction:column;gap:10px}
.mlogin .faces{display:flex;gap:6px}
.mlogin b{font-size:17px}
.mlogin .btn{align-self:flex-start}
.devtoggle{display:flex;align-items:center;gap:10px;margin:0 18px 12px;padding:10px 12px;border-radius:12px;background:var(--sunken);font-size:13.5px}
.devtoggle b{font-size:14px}
.devtoggle .switch{margin-left:auto}
.switch{width:40px;height:24px;border-radius:999px;background:var(--sunken-hover);position:relative;flex:none;display:inline-block}
.switch::after{content:"";position:absolute;left:2px;top:2px;width:20px;height:20px;border-radius:999px;background:#FFFFFF;box-shadow:var(--shadow-hairline)}
.switch.on{background:var(--accent)}
.switch.on::after{transform:translateX(16px)}
.sheet{position:absolute;left:0;right:0;bottom:0;z-index:20;padding:10px 18px 28px;border-radius:22px 22px 0 0;background:var(--bg);box-shadow:0 -20px 40px -10px rgb(0 0 0/.35)}
[data-theme="dark"] .sheet{background:var(--raised)}
.sheet .grab{width:40px;height:5px;border-radius:999px;background:var(--sunken-hover);margin:0 auto 12px}
.sheet h3{margin:0 0 12px;font-size:18px;font-weight:800}
.sheet .grp{margin-bottom:14px}
.sheet .grp > b{display:block;font-size:13px;color:var(--ink-3);margin-bottom:8px}
.sheet .chips .chip{height:36px;font-size:14px}
.dimmer{position:absolute;inset:0;z-index:19;background:rgb(16 19 22/.45)}
/* 상세 */
.dmedia{position:relative}
.dmedia .art{border-radius:0}
.dmedia .cnt3{position:absolute;right:12px;bottom:10px;height:24px;padding:0 9px;border-radius:999px;background:rgb(16 19 22/.6);color:#FFFFFF;font-size:12px;font-weight:800;display:flex;align-items:center}
.dmedia .back{position:absolute;left:10px;top:10px;width:38px;height:38px;border-radius:999px;background:rgb(16 19 22/.5);color:#FFFFFF;display:grid;place-items:center}
.dhead{padding:14px 18px 0}
.dhead h1{margin:0;font-size:24px;font-weight:800;letter-spacing:-.02em}
.dhead .by{display:flex;align-items:center;gap:8px;margin-top:8px;font-size:14px;color:var(--ink-2);font-weight:700}
.dhead .by .btn{margin-left:auto;height:32px}
.dchips{display:flex;flex-wrap:wrap;gap:6px;padding:12px 18px 0}
.dchips span{display:inline-flex;align-items:center;gap:5px;height:28px;padding:0 10px;border-radius:999px;background:var(--sunken);font-size:12.5px;font-weight:700;color:var(--ink-2)}
.dchips .okc{color:var(--ok-text);background:var(--ok-tint)}
.dchips .noc{color:var(--accent-text);background:var(--accent-tint)}
.dtabs{display:flex;gap:2px;padding:0 10px;margin-top:14px;border-bottom:1px solid var(--line)}
.dtabs a{height:44px;display:flex;align-items:center;padding:0 10px;font-size:14.5px;font-weight:700;color:var(--ink-3)}
.dtabs a.on{color:var(--ink-1);box-shadow:inset 0 -3px 0 var(--accent)}
.dbody{padding:14px 18px;font-size:15px;line-height:1.7}
.cta-bar{position:absolute;left:0;right:0;bottom:0;z-index:8;display:grid;grid-template-columns:48px 48px minmax(0,1fr);gap:8px;padding:10px 14px 30px;background:color-mix(in srgb,var(--bg) 96%,transparent);backdrop-filter:blur(12px);border-top:1px solid var(--line)}
.cta-bar .sq{display:grid;place-items:center;height:52px;border-radius:14px;background:var(--sunken);color:var(--ink-1)}
.cta-bar .main{display:flex;align-items:center;justify-content:center;gap:6px;height:52px;border-radius:14px;background:var(--accent);color:#FFFFFF;font-size:16px;font-weight:800}
.cta-bar .main.alt{background:var(--sunken);color:var(--ink-1)}
.cta-bar .note{grid-column:1 / -1;font-size:12.5px;color:var(--ink-3);text-align:center;margin-top:-2px}
.nodev{margin:12px 18px 0;padding:14px;border-radius:14px;background:var(--accent-tint);font-size:14px;line-height:1.55}
.nodev b{display:flex;align-items:center;gap:6px;color:var(--accent-text);margin-bottom:2px}
/* 가로 플레이 */
.land{position:relative;width:812px;height:375px;border-radius:40px;overflow:hidden;background:#0B0D10;box-shadow:0 0 0 10px #0C0E11,0 30px 60px -20px rgb(0 0 0/.45)}
.land .canvas{position:absolute;inset:0 44px;}
.land .ov{position:absolute;top:12px;display:flex;gap:8px;z-index:3}
.land .ov.l{left:56px}.land .ov.r{right:56px}
.land .ov span{display:grid;place-items:center;width:40px;height:40px;border-radius:999px;background:rgb(16 19 22/.55);backdrop-filter:blur(6px);color:#FFFFFF}
.land .pad{position:absolute;left:70px;bottom:28px;width:120px;height:120px;border-radius:999px;background:rgb(255 255 255/.10);box-shadow:inset 0 0 0 2px rgb(255 255 255/.25)}
.land .pad::after{content:"";position:absolute;left:38px;top:38px;width:44px;height:44px;border-radius:999px;background:rgb(255 255 255/.35)}
.land .btns{position:absolute;right:70px;bottom:36px;display:flex;gap:14px}
.land .btns span{width:64px;height:64px;border-radius:999px;background:rgb(255 255 255/.12);box-shadow:inset 0 0 0 2px rgb(255 255 255/.25);display:grid;place-items:center;color:#FFFFFF;font-weight:800}
.land .hint{position:absolute;left:50%;top:14px;transform:translateX(-50%);z-index:3;height:34px;padding:0 14px;border-radius:999px;background:rgb(16 19 22/.75);color:#FFFFFF;font-size:12.5px;font-weight:700;display:flex;align-items:center;gap:8px}
.rotate{position:absolute;inset:44px 0 0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;background:#101316;color:#FFFFFF;text-align:center}
.rotate .ph{width:56px;height:90px;border-radius:12px;box-shadow:inset 0 0 0 3px #FFFFFF;transform:rotate(-90deg);margin:20px 0}
.rotate b{font-size:18px}
.rotate .m{color:rgb(255 255 255/.65)}
.lrow{display:grid;grid-template-columns:96px minmax(0,1fr) auto;gap:12px;align-items:center;padding:10px 0;border-top:1px solid var(--line)}
.lrow:first-child{border-top:0}
.lrow .art{border-radius:9px}
.lrow b{display:block;font-size:15px}
.lrow .m{display:block;font-size:12.5px;margin-top:2px}
.lrow .bar{height:4px;margin-top:6px;width:120px}
.lrow .go{height:36px;padding:0 12px;border-radius:10px;background:var(--accent);color:#FFFFFF;font-size:13px;font-weight:800;display:flex;align-items:center;gap:4px}
.lrow .go.sec{background:var(--sunken);color:var(--ink-1)}
.wide-cols{display:flex;gap:48px;align-items:flex-start;justify-content:center;padding:48px 40px 72px;background:var(--sunken);flex-wrap:wrap}
'''

def phone(inner, active=0, extra=""):
    tabs = [("home", "홈"), ("box", "게임"), ("bm", "라이브러리"), ("bell", "알림"), ("user", "나")]
    tb = "".join(f'<a href="#"{" aria-current=\"page\"" if i == active else ""}>{ic(t)}{n}</a>' for i, (t, n) in enumerate(tabs))
    return f'<div class="phone"><div class="sbar"><span>9:41</span><span>5G</span></div><div class="pscroll">{inner}</div>{extra}<nav class="tabbar">{tb}</nav></div>'

def top(signed=True):
    right = mg.THEME_BTN + f'<button class="icon-btn" aria-label="검색">{ic("search","ic ic20")}</button>'
    right += (f'<button class="icon-btn" aria-label="알림">{ic("bell","ic ic20")}<span class="dot-new"></span></button>' if signed else '<span class="btn btn-primary btn-sm" style="height:34px;margin-left:4px">로그인</span>')
    return f'<div class="mtop"><span class="logo" style="font-size:19px">{logo()}</span><span class="word">PlayGround</span><span class="sp">{right}</span></div>'

def card(art, t, who, ch, col, meta, mobile=True, cls=""):
    flag = "" if mobile else f'<span class="pcflag">{ic("pc","ic ic12")}PC 에서</span>'
    return f'<div class="mcard {cls}"><span class="art {art}"><span class="shots"></span>{flag}<span class="jf maker" style="background:var(--color-face-{col})">{ch}<i>ㅅ</i>{ch}</span></span><b>{t}</b><span class="m">{who} · {meta}</span></div>'

def home_top():
    cont = "".join(f'<div class="mcard cont"><span class="art {a}"><span class="shots"></span></span><b>{t}</b><span class="bar"><i style="width:{p}%"></i></span><span class="m">진행 {p}% · {w}</span><span class="go">{ic("play","ic ic12")}이어하기</span></div>' for a, t, p, w in [("a-loop", "루프 디버거", 45, "어제"), ("a-tess", "테셀레이트", 70, "3일 전")])
    picks = "".join(card(*c) for c in [("a-ash", "애쉬폴 러너", "잿빛토끼", "ㅈ", "ju", "스피드런 6분"), ("a-refac", "리팩터 러시", "리팩터클럽", "ㄹ", "gyul", "아케이드 3분"), ("a-tilt", "틸트 이론", "기울기연구소", "ㄱ", "hwang", "퍼즐 8분")])
    inner = f'''{top()}
<div class="mbanner"><span class="art a-loop"></span><span class="scrim"></span><span class="pg">1 / 5</span><div class="t"><span class="badge static" style="align-self:flex-start">에디터 추천</span><b>루프를 벗어나려면,<br>코드를 고쳐라.</b><span class="m">퍼즐 · 한 판 15분 · 휴대폰 가로</span></div></div>
<div class="mdots"><i class="on"></i><i></i><i></i><i></i><i></i></div>
<div class="msec" style="margin-top:20px"><div class="msh">{EAR}<h2>이어하기</h2><span class="r">라이브러리</span></div><div class="mrail">{cont}</div></div>
<div class="msec"><div class="msh">{EAR}<h2>이번 주 PICK</h2></div><div class="mrail">{picks}</div></div>'''
    return phone(inner, 0)

def home_bottom():
    ranks = "".join(f'<div><span class="n">{i}</span><span class="art {a}"></span><span><b>{t}</b><span class="m">{who}</span></span><span class="k"{" style=\"color:var(--rank-down)\"" if k.startswith("▼") else ""}>{k}</span></div>' for i, a, t, who, k in [(1, "a-ash", "애쉬폴 러너", "잿빛토끼", "▲3"), (2, "a-paper", "페이퍼 벡터", "벡터공방", "▲1"), (3, "a-loop", "루프 디버거", "픽셀상점", "–"), (4, "a-grid", "그리드락", "보라네", "▼1")])
    grid = "".join(card(*c) for c in [("a-refac", "리팩터 러시", "리팩터클럽", "ㄹ", "gyul", "3분"), ("a-bazaar", "바이트 바자", "바이트마켓", "ㅂ", "bora", "4분"), ("a-grid", "그리드 러너", "보라네", "ㅂ", "bora", "3분", False), ("a-tilt", "틸트 이론", "기울기연구소", "ㄱ", "hwang", "8분")])
    inner = f'''{top(False)}
<div class="msec" style="margin-top:6px"><div class="mband"><div class="msh">{EAR}<h2>주간 랭킹</h2></div><div class="mchips2" style="margin:0 0 6px;padding:0"><button class="chip" aria-pressed="true">전체</button><button class="chip">퍼즐</button><button class="chip">액션</button><button class="chip">같이</button></div><div class="mrank">{ranks}</div></div></div>
<div class="msec" style="margin-top:22px"><div class="msh">{EAR}<h2>몇 분 있어요?</h2></div><div class="mchips2"><button class="chip" aria-pressed="true">5분 이하</button><button class="chip">15분 이하</button><button class="chip">30분 이하</button><button class="chip">여유 있다</button></div><div class="m2">{grid}</div></div>
<div class="msec"><div class="mlogin"><span class="faces">{face("ㅎ","hong","lg")}{face("ㅇ","olive","lg")}{face("ㅁ","bora","lg")}</span><b>로그인하면 내 얼굴이 생겨요</b><span class="m" style="color:rgb(255 255 255/.82)">진행이 어느 기기에서나 이어져요.</span><span class="btn btn-on-color btn-sm">로그인</span></div></div>'''
    return phone(inner, 0)

def browse():
    grid = "".join(card(*c) for c in [("a-loop", "루프 디버거", "픽셀상점", "ㅍ", "jjok", "퍼즐 5분"), ("a-grid", "그리드 러너", "보라네", "ㅂ", "bora", "액션 3분", False), ("a-tess", "테셀레이트", "노을공방", "ㄴ", "haneul", "퍼즐 10분"), ("a-null", "널 포인터", "레몬게임즈", "ㄹ", "olive", "퍼즐 15분", False)])
    inner = f'''<div class="mtop"><span style="font-size:19px;font-weight:800">게임</span><span class="sp">{mg.THEME_BTN}<button class="icon-btn" aria-label="검색">{ic("search","ic ic20")}</button></span></div>
<div class="devtoggle">{ic("phone","ic ic16")}<span><b>이 휴대폰에서 되는 게임만 보기</b><span class="m" style="display:block">지금은 전부 보여요 · ‘PC 에서’ 게임은 링크를 PC 로 보낼 수 있어요</span></span><span class="switch"></span></div>
<div class="msec" style="margin-top:4px"><div class="mchips2"><button class="chip" aria-pressed="true">필터 2</button><button class="chip">퍼즐</button><button class="chip">15분 이하</button><button class="chip">추천 많은</button></div><div class="m2">{grid}</div></div>'''
    sheet = f'''<div class="dimmer"></div><div class="sheet"><div class="grab"></div><h3>필터</h3>
<div class="grp"><b>장르</b><div class="chips"><button class="chip" aria-pressed="true">퍼즐</button><button class="chip">액션</button><button class="chip">탐험</button><button class="chip">전략</button></div></div>
<div class="grp"><b>한 판</b><div class="chips"><button class="chip">5분 이하</button><button class="chip" aria-pressed="true">15분 이하</button><button class="chip">30분 이하</button></div></div>
<div style="display:grid;grid-template-columns:1fr 2fr;gap:8px"><span class="mbtn" style="background:var(--sunken);font-size:15px">초기화</span><span class="mbtn btn-primary" style="font-size:15px">32개 보기</span></div></div>'''
    return phone(inner, 1, sheet)

def detail(ok=True):
    if ok:
        chips = f'<span class="okc">{ic("phone","ic ic12")}이 휴대폰에서 돼요 · 가로</span><span>{ic("clock","ic ic12")}한 판 5분</span><span>{ic("duo","ic ic12")}혼자</span><span>{ic("thumb","ic ic12")}추천 214 · 리뷰 38</span>'
        bar = f'<div class="cta-bar"><span class="sq" aria-label="저장">{ic("bm","ic ic20")}</span><span class="sq" aria-label="공유">{ic("up2","ic ic20")}</span><span class="main" data-play>{ic("play","ic ic16")}지금 플레이</span></div>'
        extra = ""
        art = "a-loop"; title = "루프 디버거"; who = ("ㅍ", "jjok", "픽셀상점")
    else:
        chips = f'<span class="noc">{ic("pc","ic ic12")}PC 전용 · 키보드</span><span>{ic("clock","ic ic12")}한 판 3분</span><span>{ic("thumb","ic ic12")}추천 135 · 리뷰 22</span>'
        bar = f'<div class="cta-bar"><span class="sq" aria-label="저장">{ic("bm","ic ic20")}</span><span class="sq" aria-label="공유">{ic("up2","ic ic20")}</span><span class="main alt">{ic("pc","ic ic16")}PC 로 링크 보내기</span><span class="note">내 다른 기기 알림으로 보내요 · 로그인 필요</span></div>'
        extra = f'<div class="nodev"><b>{ic("alert")}이 휴대폰에서는 할 수 없어요</b>키보드가 필요한 게임이에요. 저장해 두면 PC 라이브러리에 바로 보여요.</div>'
        art = "a-grid"; title = "그리드 러너"; who = ("ㅂ", "bora", "보라네")
    inner = f'''<div class="dmedia"><span class="art {art}" style="display:block"></span><span class="back">{ic("chev","ic ic16")}</span><span class="cnt3">1 / 6</span></div>
<div class="dhead"><h1>{title}</h1><div class="by">{face(who[0], who[1], "")}{who[2]}<span class="btn btn-secondary btn-sm">팔로우</span></div></div>
<div class="dchips">{chips}</div>{extra}
<nav class="dtabs"><a class="on">소개</a><a>리뷰 38</a><a>개발일지</a><a>업데이트</a></nav>
<div class="dbody">모든 방이 하나의 함수인 프로그래밍 퍼즐. 손으로 쓴 코드 블록을 옮겨 루프를 고치면, 갇힌 로봇이 다음 방으로 넘어가요.</div>'''
    return f'<div class="phone"><div class="sbar" style="background:transparent;color:#FFFFFF;z-index:9"><span>9:41</span><span>5G</span></div><div class="pscroll" style="padding-top:0">{inner}</div>{bar}</div>'

def play_land():
    return f'''<div class="land"><span class="canvas art a-loop" style="display:block;border-radius:0"></span>
<div class="ov l"><span aria-label="일시정지"><svg class="ic ic16" viewBox="0 0 16 16"><path d="M5.5 3.5v9M10.5 3.5v9"></path></svg></span></div>
<div class="ov r"><span aria-label="나가기"><svg class="ic ic16" viewBox="0 0 16 16"><path d="M4 4l8 8M12 4l-8 8"></path></svg></span></div>
<div class="hint">{ic("check","ic ic12")}화면 왼쪽은 이동 · 오른쪽은 버튼 · 일시정지는 왼쪽 위</div>
<span class="pad"></span><div class="btns"><span>B</span><span>A</span></div></div>'''

def rotate_prompt():
    return f'<div class="phone"><div class="sbar"><span>9:41</span><span>5G</span></div><div class="rotate"><span class="ph"></span><b>휴대폰을 가로로 돌려 주세요</b><span class="m">이 게임은 가로 화면에서 해요</span><span class="btn btn-glass btn-sm" style="margin-top:10px">세로로 그냥 하기</span></div></div>'

def library():
    rows = "".join(f'<div class="lrow"><span class="art {a}"></span><span><b>{t}</b><span class="m">{m}</span>{"<span class=\"bar\"><i style=\"width:%d%%\"></i></span>" % p if p else ""}</span><span class="go{" sec" if sec else ""}">{lab}</span></div>' for a, t, m, p, lab, sec in [("a-loop", "루프 디버거", "진행 45% · 어제", 45, "이어하기", False), ("a-tess", "테셀레이트", "완주 · 최고 03:42", 0, "다시 하기", True), ("a-grid", "그리드 러너", "PC 전용 · 저장함", 0, "PC 로", True), ("a-ash", "재의 도시", "설치형 · PC 에서 받기", 0, "PC 로", True), ("a-halcyon", "할시온 바다", "진행 8% · 1주 전", 8, "이어하기", False)])
    inner = f'''<div class="mtop"><span style="font-size:19px;font-weight:800">라이브러리</span><span class="sp">{mg.THEME_BTN}</span></div>
<div class="mchips2" style="margin:0 0 6px;padding:0 18px"><button class="chip" aria-pressed="true">이어하기 5</button><button class="chip">저장함 7</button><button class="chip">설치형 2</button><button class="chip">기록</button></div>
<div class="msec" style="margin-top:6px">{rows}</div>'''
    return phone(inner, 2)

def page(title, cols, memo, height):
    body = '<div class="phones" style="flex-wrap:wrap">' + "".join(f'<div class="pcol"{" style=\"width:812px\"" if w else ""}><b>{t}</b><span>{d}</span>{p}</div>' for t, d, p, w in cols) + "</div>"
    html = dt.page(title, body, height, memo)
    return html.replace("</style>", mgm.M_CSS + CSS + "\n</style>", 1)

def page_home():
    cols = [("홈 · 위", "배너(4:3, 아래 가림막 위 글자 — 아트를 가리지 않음) → 이어하기(진행 + 버튼) → 이번 주 PICK 가로 넘김", home_top(), False),
            ("홈 · 아래", "랭킹은 옅은 쪽빛 상자 안 4줄 · 시간 칩 + 2열 카드(PC 전용은 ‘PC 에서’ 표시) · 게스트 로그인 띠", home_bottom(), False),
            ("게임 탐색 + 필터 시트", "PC 전용 게임도 기본으로 보이고 ‘PC 에서’ 표시만(PM2). ‘이 휴대폰에서 되는 게임만 보기’ 는 켤 수 있음. 필터는 아래에서 올라오는 시트", browse(), False)]
    memo = "PlayGround 모바일 · 홈과 탐색. 탭바 = 홈 · 게임 · 라이브러리 · 알림 · 나(MakersGround 와 같은 자리 규칙). 상단: 로고 · 테마 · 검색 · 알림. v10 의 순서(배너 → 이어하기 → PICK → 랭킹 → 시간 → 로그인 띠 → 전체)를 한 열로."
    return page("PlayGround 모바일 · 홈", cols, memo, 1000)

def page_game():
    cols = [("게임 상세 · 이 휴대폰에서 됨", "위 미디어(넘김) · 제목 · 메이커 · 실행 조건 칩(되는지 맨 앞, 비취) · 탭. 아래 고정: 저장 · 공유 · 지금 플레이", detail(True), False),
            ("게임 상세 · 이 기기에서 불가", "PC 전용이면 칩과 안내 상자로 먼저 알리고, 주 버튼은 ‘PC 로 링크 보내기’", detail(False), False),
            ("라이브러리", "이어하기 · 저장함 · 설치형 · 기록. 휴대폰에서 못 하는 건 ‘PC 로’", library(), False),
            ("세로로 들고 있을 때", "가로 게임은 돌려 달라고 안내(세로로 그냥 하기 선택 가능)", rotate_prompt(), False),
            ("플레이 · 가로 터치", "플랫폼 UI 는 반투명 버튼 두 개(일시정지 · 나가기)뿐. 처음 4초 조작 안내. 가상 패드는 게임이 SDK 로 요청할 때만", play_land(), True)]
    memo = "PlayGround 모바일 · 게임. 핵심은 ‘이 휴대폰에서 되나’를 숨기지 않는 것 — PC 전용도 보이되 카드에 ‘PC 에서’ 표시(PM2), 원하면 ‘되는 게임만 보기’, 상세의 비취/쪽빛 칩, 불가 시 ‘PC 로 링크 보내기’. 플레이는 전체 화면 · 가로 우선."
    return page("PlayGround 모바일 · 게임", cols, memo, 1900)

if __name__ == "__main__":
    for name, fn in [("PG91-mobile-home.dc.html", page_home), ("PG92-mobile-games.dc.html", page_game)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
