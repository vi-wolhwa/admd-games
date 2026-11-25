# PlayGround 게임 상세 시안 A(결정 패널) · B(무대) 생성기
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + [OUT]
import importlib.util
spec = importlib.util.spec_from_file_location("mg", os.path.join(HERE, "mg.py"))
mg = importlib.util.module_from_spec(spec); spec.loader.exec_module(mg)
ic, face, logo, EAR = mg.ic, mg.face, mg.logo, mg.EAR

CSS = r'''
.crumb2{display:flex;gap:6px;align-items:center;margin-top:24px;font-size:13px;font-weight:600;color:var(--ink-3)}
.crumb2 .ic{width:12px;height:12px}
.gtitle{display:flex;align-items:flex-end;gap:16px;margin-top:10px}
.gtitle h1{margin:0;font-size:34px;line-height:1.2;font-weight:800;letter-spacing:-.025em}
.gtitle .by{display:flex;align-items:center;gap:8px;font-size:15px;font-weight:700;color:var(--ink-2);padding-bottom:4px}
.gtitle .tags{margin-left:auto;display:flex;gap:6px;padding-bottom:6px}
.hero2{display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:32px;margin-top:20px;align-items:start}
.media .art{border-radius:var(--radius-lg)}
.media .main{--overlay-inset:12px}
.media .main .plat{height:28px;padding:0 10px;font-size:12.5px;gap:7px}
.thumbs{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:8px;margin-top:10px}
.thumbs .art{border-radius:8px;opacity:.72}
.thumbs .art.on{opacity:1;box-shadow:0 0 0 2px var(--bg),0 0 0 4px var(--accent)}
.thumbs .vid{display:grid;place-items:center;color:#FFFFFF}
.panel{display:flex;flex-direction:column;gap:18px}
.cta{display:flex;flex-direction:column;gap:8px}
.cta .big{height:56px;border-radius:14px;font-size:17px;font-weight:800}
.cta .pair{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.prog-box{display:flex;flex-direction:column;gap:8px;padding:14px 16px;border-radius:var(--radius-lg);background:var(--sunken)}
.prog-box .row{display:flex;justify-content:space-between;font-size:13px;color:var(--ink-3);font-weight:600}
.prog-box .row b{color:var(--ink-1);font-size:14px}
.cond{display:flex;flex-direction:column}
.cond > div{display:grid;grid-template-columns:20px 64px minmax(0,1fr);gap:10px;align-items:center;min-height:40px;border-top:1px solid var(--line);font-size:14px}
.cond > div:first-child{border-top:0}
.cond .ic{color:var(--ink-3)}
.cond span.k{color:var(--ink-3);font-weight:600;font-size:13px}
.cond b{font-weight:700}
.cond .okt{color:var(--ok-text);font-weight:700}
.rate-line{display:flex;align-items:center;gap:10px;font-size:14px;color:var(--ink-2)}
.rate-line b{font-size:22px;font-weight:800;color:var(--ink-1)}
.mk-mini{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center;padding-top:16px;border-top:1px solid var(--line)}
.mk-mini b{display:block;font-size:15px}
.mk-mini .m{display:block}
.notice{display:flex;gap:12px;padding:16px;border-radius:var(--radius-lg);background:var(--sunken);font-size:14px;line-height:1.55;color:var(--ink-2)}
.notice b{display:block;color:var(--ink-1);font-size:15px;margin-bottom:2px}
.qr{width:88px;height:88px;flex:none;border-radius:10px;background:conic-gradient(var(--ink-1) 0 25%,transparent 0 50%,var(--ink-1) 0 75%,transparent 0) 0 0/22px 22px,var(--bg);box-shadow:inset 0 0 0 6px var(--bg),0 0 0 1px var(--line)}
.files{display:flex;flex-direction:column;gap:6px}
.file{display:grid;grid-template-columns:20px minmax(0,1fr) auto;gap:10px;align-items:center;padding:10px 12px;border-radius:12px;box-shadow:inset 0 0 0 1px var(--line);font-size:14px}
.file.on{box-shadow:inset 0 0 0 2px var(--accent)}
.file b{display:block;font-size:14px}
.file .m{display:block;font-size:12.5px}
.scan{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:12px;background:var(--ok-tint);color:var(--ok-text);font-size:13.5px;font-weight:700}
.scan .ic{width:18px;height:18px}
.scan a{margin-left:auto;color:var(--ok-text);text-decoration:underline;text-underline-offset:3px;font-weight:700}
.stabs{position:sticky;top:68px;z-index:10;margin-top:48px;background:color-mix(in srgb,var(--bg) 94%,transparent);backdrop-filter:blur(12px)}
.stabs .utabs{width:1200px;margin:0 auto}
.stabs .mini-cta{margin-left:auto;display:flex;align-items:center;gap:10px}
.about{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:56px;align-items:start}
.about p{margin:0 0 14px;font-size:16px;line-height:1.8;color:var(--ink-1)}
.about .feat{display:flex;flex-direction:column;gap:10px;margin-top:8px}
.about .feat span{display:flex;gap:10px;font-size:15px;color:var(--ink-2)}
.about .feat .ic{color:var(--accent-text);margin-top:4px}
.facts2{display:flex;flex-direction:column;gap:0;font-size:14px}
.facts2 > div{display:grid;grid-template-columns:96px minmax(0,1fr);gap:12px;padding:10px 0;border-top:1px solid var(--line)}
.facts2 > div:first-child{border-top:0}
.facts2 span:first-child{color:var(--ink-3);font-weight:600}
.rv-top{display:grid;grid-template-columns:260px minmax(0,1fr);gap:48px;align-items:start}
.rv-score .disp{font-size:56px;line-height:1;color:var(--accent-text)}
.rv-score b{display:block;margin-top:10px;font-size:16px}
.rv-score .bar2{display:flex;height:8px;border-radius:999px;overflow:hidden;margin-top:14px;background:var(--sunken-hover)}
.rv-score .bar2 i{background:var(--accent)}
.rv-tags{display:flex;flex-wrap:wrap;gap:8px}
.rvs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:28px}
.rv{display:flex;flex-direction:column;gap:10px;padding-top:16px;border-top:2px solid var(--ink-1)}
.rv .hd{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--ink-3)}
.rv .hd b{color:var(--ink-1);font-size:14px}
.rv .yes{display:inline-flex;align-items:center;gap:4px;color:var(--accent-text);font-weight:800;font-size:13px}
.rv .no{display:inline-flex;align-items:center;gap:4px;color:var(--ink-2);font-weight:800;font-size:13px}
.rv p{margin:0;font-size:15px;line-height:1.65}
.rv .reply{display:flex;gap:8px;padding:12px;border-radius:12px;background:var(--sunken);font-size:14px;line-height:1.55;color:var(--ink-2)}
.rv .reply b{color:var(--ink-1);font-size:13px;display:block}
.rv .foot{display:flex;gap:12px;font-size:12.5px;color:var(--ink-3)}
.maker-band{padding:44px 0 48px;background:var(--accent-tint)}
.mkb{display:grid;grid-template-columns:auto minmax(0,1fr) 420px;gap:32px;align-items:start}
.mkb h3{margin:0;font-size:24px;font-weight:800}
.mkb p{margin:8px 0 0;font-size:15px;line-height:1.65;color:var(--ink-2)}
.mkb .acts{display:flex;gap:8px;margin-top:16px}
.mkb .stat{display:flex;gap:18px;margin-top:14px;font-size:13px;color:var(--ink-3)}
.mkb .stat b{color:var(--ink-1)}
.mkb .lglink{display:grid;grid-template-columns:140px minmax(0,1fr);gap:14px;align-items:center;padding:12px;border-radius:var(--radius-lg);background:var(--raised)}
.mkb .lglink .art{border-radius:10px}
.mkb .lglink b{font-size:15px;line-height:1.45}
.mkb .others{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:10px}
.mkb .others .art{border-radius:9px}
.upd{display:flex;flex-direction:column}
.up-row{display:grid;grid-template-columns:120px minmax(0,1fr);gap:24px;padding:18px 0;border-top:1px solid var(--line)}
.up-row:first-child{border-top:0}
.up-row .v{font-size:15px;font-weight:800}
.up-row .v span{display:block;font-size:13px;color:var(--ink-3);font-weight:600;margin-top:2px}
.up-row ul{margin:0;padding-left:18px;font-size:15px;line-height:1.7;color:var(--ink-2)}
.report{display:flex;justify-content:space-between;align-items:center;margin-top:40px;padding:18px 0;border-top:1px solid var(--line);font-size:13px;color:var(--ink-3)}
.report a{display:inline-flex;align-items:center;gap:6px;font-weight:700;color:var(--ink-2)}
/* B 무대 */
.stage{position:relative;background:#132A44;color:#FFFFFF;padding:40px 0 44px}
.stage .in{width:1200px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1fr) 680px;gap:48px;align-items:center}
.stage .crumb2{color:rgb(255 255 255 / .6);margin-top:0}
.stage h1{margin:16px 0 0;font-family:var(--font-display);font-weight:400;font-size:52px;line-height:1.1}
.stage .lede{margin:16px 0 0;font-size:16px;line-height:1.7;color:rgb(255 255 255 / .82)}
.stage .by{display:flex;align-items:center;gap:10px;margin-top:20px;font-size:15px;font-weight:700}
.stage .by .m{color:rgb(255 255 255 / .6)}
.stage .chips2{display:flex;flex-wrap:wrap;gap:6px;margin-top:22px}
.stage .chips2 span{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 12px;border-radius:999px;background:rgb(255 255 255 / .12);font-size:13px;font-weight:700}
.stage .chips2 .ok{color:#7EE2A8}
.stage .acts{display:flex;gap:8px;margin-top:26px}
.stage .acts .big{height:56px;padding:0 28px;border-radius:14px;font-size:17px;font-weight:800}
.stage .art{border-radius:var(--radius-xl);box-shadow:0 30px 60px -30px rgb(0 0 0 / .8)}
.stage .thumbs .art{box-shadow:none}
.stage .thumbs .art.on{box-shadow:0 0 0 2px #132A44,0 0 0 4px #FFFFFF}
.subbar{position:sticky;top:68px;z-index:10;background:color-mix(in srgb,var(--bg) 94%,transparent);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.subbar .in{width:1200px;margin:0 auto;display:flex;align-items:center;gap:20px;height:60px}
.subbar .gt{display:flex;align-items:center;gap:10px;font-weight:800}
.subbar .gt .art{width:64px;border-radius:6px}
.subbar .utabs{border:0;margin-left:12px}
.subbar .utabs a{height:60px;font-size:15px}
'''

def pg_header(signed=True):
    right = '<div class="ground"><a class="play" href="#" aria-current="true">플레이</a><a class="make" href="#">메이커스</a></div>'
    right += f'<div class="search">{ic("search")}게임, 메이커 검색</div>' + mg.THEME_BTN
    right += (f'<button class="icon-btn" aria-label="알림">{ic("bell","ic ic20")}</button>{face("ㅇ","olive","md")}' if signed else '<span class="btn btn-primary btn-sm">로그인</span>')
    return f'''<header class="hdr"><div class="in">
<a class="brand" href="#"><span class="logo" style="font-size:22px">{logo()}</span><span class="word">PlayGround</span></a>
<nav class="gnb"><a href="#">홈</a><a href="#" aria-current="page">게임</a><a href="#">랭킹</a><a href="#">같이</a><a href="#">잼</a></nav>
<div class="right">{right}</div></div></header>'''

def sif(var, html, hint=False):
    return f'<sc-if value="{{{{ {var} }}}}" hint-placeholder-val="{{{{ {"true" if hint else "false"} }}}}">{html}</sc-if>'

def media(dl_hint=False):
    plat_web = f'<span class="plat">{ic("web","ic ic12")}브라우저 {ic("phone","ic ic12")}휴대폰</span>'
    plat_dl = f'<span class="plat">{ic("dl","ic ic12")}설치형 <svg class="ic ic12 ok"><use href="#i-shield"></use></svg>검사 통과</span>'
    thumbs = '<span class="art a-loop on"></span>' + "".join(f'<span class="art {a}"></span>' for a in ("a-tess", "a-grid", "a-halcyon", "a-paper")) + f'<span class="art vid" style="background:#151A20">{ic("play","ic ic16")}</span>'
    return f'''<div class="media"><span class="art main a-loop"><span class="shots"></span><span class="badge">{ic("crown","ic ic12")}이번 주 PICK</span>{sif("isWeb", plat_web, True)}{sif("isDl", plat_dl)}<span class="frames"><b></b><b></b><b></b><b></b><b></b><b></b></span></span>
<div class="thumbs">{thumbs}</div></div>'''

COND_WEB = [("web", "실행", '<b>브라우저에서 바로</b> · 설치 없음'), ("pc", "기기", "PC · 휴대폰(가로)"), ("pad", "조작", "키보드 또는 터치"), ("clock", "한 판", "5분 안팎 · 전체 40스테이지"), ("duo", "인원", "혼자"), ("cmt", "언어", "한국어 · 영어")]
COND_DL = [("dl", "실행", "<b>설치형</b> · Windows · macOS"), ("shield", "검사", '<span class="okt">보안 검사 통과</span> · 11/24'), ("pc", "사양", "Windows 10 이상 · 4GB RAM"), ("clock", "한 판", "40분 · 저장 가능"), ("duo", "인원", "혼자"), ("cmt", "언어", "한국어")]
COND_NO = [("phone", "실행", "<b>휴대폰 · 패드 전용</b> · 터치 조작"), ("pc", "PC", "지원하지 않아요"), ("clock", "한 판", "3분"), ("duo", "인원", "혼자"), ("cmt", "언어", "한국어")]
def cond(rows):
    return '<div class="cond">' + "".join(f'<div>{ic(i)}<span class="k">{k}</span><span>{v}</span></div>' for i, k, v in rows) + "</div>"

def panel():
    first = f'''<div class="cta"><span class="btn btn-primary big" data-play>{ic("play","ic ic16")}지금 플레이</span><div class="pair"><span class="btn btn-secondary">{ic("bm","ic ic16")}저장</span><span class="btn btn-secondary">친구에게 도전장</span></div></div>'''
    prog = f'''<div class="cta"><span class="btn btn-primary big" data-play>{ic("play","ic ic16")}이어하기 · 23스테이지</span>
<div class="prog-box"><div class="row"><span><b>진행 45%</b> · 18 / 40</span><span>어제 · 1시간 12분</span></div><div class="bar"><i style="width:45%"></i></div><div class="row"><span>도전과제 7 / 12</span><span>{ic("bmf","ic ic12")} 저장함</span></div></div></div>'''
    done = f'''<div class="cta"><span class="btn btn-primary big" data-play>{ic("play","ic ic16")}다시 하기</span>
<div class="prog-box"><div class="row"><span><b>완주</b> · 11/20</span><span>총 2시간 14분</span></div><div class="row"><span>최고 기록</span><b class="num">03:42.18</b></div><div class="row"><span>도전과제</span><b>12 / 12</b></div></div>
<span class="btn btn-secondary">내 기록으로 친구에게 도전장</span></div>'''
    dl = f'''<div class="cta"><div class="files"><div class="file on">{ic("pc")}<span><b>Windows</b><span class="m">v1.2 · 312MB · 설치 파일(.exe)</span></span>{ic("check","ic ic16")}</div><div class="file">{ic("pc")}<span><b>macOS</b><span class="m">v1.2 · 298MB · .dmg · Apple 서명 없음</span></span><span></span></div></div>
<span class="btn btn-primary big">{ic("dl","ic ic16")}다운로드 · Windows</span>
<div class="scan">{ic("shield")}<span>보안 검사 통과 · 엔진 3종 · 11/24</span><a href="#">리포트</a></div>
<a class="link" href="#" style="font-size:13px">Windows 가 경고를 띄우나요? 설치 안내 보기 ›</a></div>'''
    no = f'''<div class="notice"><span class="qr" aria-hidden="true"></span><span><b>휴대폰에서 열어 주세요</b>이 게임은 터치 전용이라 PC 에서는 플레이할 수 없어요. QR 을 찍거나 링크를 보내 보세요.</span></div>
<div class="pair" style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><span class="btn btn-secondary">내 휴대폰으로 링크 보내기</span><span class="btn btn-secondary">{ic("bm","ic ic16")}저장</span></div>'''
    states = sif("sFirst", first, True) + sif("sProg", prog) + sif("sDone", done) + sif("sDl", dl) + sif("sNo", no)
    conds = sif("isWebOk", cond(COND_WEB), True) + sif("isDl", cond(COND_DL)) + sif("sNo", cond(COND_NO))
    return f'''<aside class="panel" aria-label="플레이 정보">{states}
{conds}
<div class="rate-line"><b>추천 92%</b><span>리뷰 38개 · <a class="link" href="#reviews" style="font-size:14px">리뷰 보기</a></span></div>
<div class="mk-mini">{face("ㅍ","jjok","md")}<span><b>픽셀상점</b><span class="m">퍼즐만 만드는 1인 메이커 · 게임 4개</span></span><span class="btn btn-secondary btn-sm">팔로우</span></div></aside>'''

def tabs(active=0):
    names = ["소개", "리뷰 38", "개발일지 3", "업데이트"]
    return '<nav class="utabs">' + "".join(f'<a href="#"{" aria-current=\"page\"" if i == active else ""}>{n}</a>' for i, n in enumerate(names)) + "</nav>"

def about():
    return f'''<section class="sec wrap"><div class="about"><div>
<div class="sh">{EAR}<h2>소개</h2></div>
<p>모든 방이 하나의 함수인 프로그래밍 퍼즐. 손으로 쓴 코드 블록을 옮겨 루프를 고치면, 갇힌 로봇이 다음 방으로 넘어가요.</p>
<p>문법을 몰라도 괜찮아요. 블록은 그림으로 되어 있고, 틀리면 로봇이 어디서 멈췄는지 바로 보여 줘요. 진행은 브라우저에 저장되고, 로그인하면 다른 기기에서도 이어서 할 수 있어요.</p>
<div class="feat"><span>{ic("check")}40개 스테이지 · 스테이지당 3~8분</span><span>{ic("check")}힌트는 세 단계 — 답을 바로 알려 주지 않아요</span><span>{ic("check")}스테이지 편집기로 만든 문제를 링크로 공유</span></div></div>
<div><div class="sh">{EAR}<h2 style="font-size:18px">정보</h2></div><div class="facts2">
<div><span>장르</span><span>퍼즐 · 프로그래밍</span></div><div><span>공개</span><span>2026.10.02 · v1.2(11/23)</span></div><div><span>콘텐츠</span><span>표시할 내용 없음</span></div><div><span>엔진</span><span>Godot 4</span></div><div><span>저장</span><span>브라우저 · 로그인 시 계정</span></div><div><span>태그</span><span style="display:flex;gap:6px;flex-wrap:wrap"><span class="tag">퍼즐</span><span class="tag">짧게</span><span class="tag">두뇌</span><span class="tag">한 손</span></span></div>
</div></div></div></section>'''

REVIEWS = [
    ("ㅅ", "hong", "새벽코딩", True, "3.2시간", "회사에서 하는 일이랑 너무 똑같아서 웃겼어요. 그런데 이건 고치면 칭찬을 해 주네요. 15스테이지 이후로 난이도가 확 오르는데 힌트가 잘 잡아줘요.", "15스테이지 구간은 다음 업데이트에서 단계를 하나 더 넣을게요. 고마워요!"),
    ("ㄱ", "gyul", "귤껍질", True, "48분", "출퇴근길에 한 판씩 하기 딱 좋아요. 휴대폰 가로 모드에서도 블록이 안 작아서 좋았어요.", None),
    ("ㅁ", "bora", "모래시계", False, "1.1시간", "튜토리얼이 너무 길어요. 처음 세 스테이지는 건너뛰기가 있으면 좋겠어요.", "v1.2 에서 튜토리얼을 한 스테이지로 줄였어요. 다시 한 번 봐 주세요!"),
]
def reviews():
    cards = ""
    for ch, col, who, yes, time, text, reply in REVIEWS:
        verdict = f'<span class="yes">{ic("up","ic ic12")}추천</span>' if yes else f'<span class="no"><svg class="ic ic12" style="transform:rotate(180deg)"><use href="#i-up"></use></svg>비추천</span>'
        rep = f'<div class="reply">{face("ㅍ","jjok","xs")}<span><b>픽셀상점 · 메이커 답글</b>{reply}</span></div>' if reply else ""
        cards += f'<article class="rv"><div class="hd">{face(ch,col,"xs")}<b>{who}</b>{verdict}<span>· 플레이 {time}</span></div><p>{text}</p>{rep}<div class="foot"><span>11/2{len(who)}</span><span>도움이 됐어요 12</span><span>신고</span></div></article>'
    tags = "".join(f'<button class="chip">{t} <span class="c">{n}</span></button>' for t, n in [("짧고 굵음", 21), ("퍼즐 좋아하면", 18), ("한 손으로", 9), ("힌트가 친절해요", 8), ("튜토리얼이 길어요", 4)])
    return f'''<section class="sec wrap" id="reviews"><div class="sh">{EAR}<h2>리뷰</h2><span class="sub">플레이한 사람만 쓸 수 있어요</span><div class="r"><span class="btn btn-secondary btn-sm">{ic("pen")}리뷰 쓰기</span></div></div>
<div class="rv-top"><div class="rv-score"><span class="disp">92%</span><b>38명 중 35명이 추천</b><span class="bar2"><i style="width:92%"></i></span></div>
<div><p class="m" style="margin:0 0 10px">자주 고른 말</p><div class="rv-tags">{tags}</div></div></div>
<div class="rvs">{cards}</div></section>'''

def maker_band():
    others = "".join(f'<span class="art {a}"></span>' for a in ("a-paper", "a-grid", "a-tess"))
    return f'''<section class="sec maker-band"><div class="wrap"><div class="sh">{EAR}<h2>만든 사람</h2></div>
<div class="mkb">{face("ㅍ","jjok","lg")}
<div><h3>픽셀상점</h3><p>퍼즐만 만드는 1인 메이커예요. 회사 다니면서 주말에 만들어요. 작은 아이디어를 끝까지 다듬는 걸 좋아해요.</p>
<div class="stat"><span><b>게임 4</b></span><span><b>개발일지 12</b></span><span>2025년부터</span></div>
<div class="acts"><span class="btn btn-primary btn-sm">팔로우</span><span class="btn btn-secondary btn-sm">메이커 페이지</span></div></div>
<div><a class="lglink" href="#"><span class="art a-loop"></span><span><span class="m">최근 개발일지 · 3일 전</span><b style="display:block">첫 리뷰 38개를 읽고 바꾼 것들</b></span></a>
<p class="m" style="margin:14px 0 0">다른 게임</p><div class="others">{others}</div></div>
</div></div></section>'''

def updates():
    rows = [("v1.2", "11/23", ["튜토리얼을 세 스테이지에서 한 스테이지로 줄였어요", "15스테이지 힌트 두 번째 단계를 고쳤어요", "휴대폰 가로 모드에서 블록 크기를 키웠어요"]), ("v1.1", "10/20", ["스테이지 편집기 공유 링크", "효과음 볼륨을 따로 조절할 수 있어요"])]
    r = "".join(f'<div class="up-row"><span class="v">{v}<span>{d}</span></span><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>' for v, d, xs in rows)
    return f'<section class="sec wrap"><div class="sh">{EAR}<h2>업데이트</h2><div class="r"><a class="link" href="#">전체 내역</a></div></div><div class="upd">{r}</div></section>'

def similar():
    return f'''<section class="sec wrap"><div class="sh">{EAR}<h2>비슷한 게임</h2><div class="r"><span class="arw" style="opacity:.4">{ic("chev","ic")}</span><span class="arw">{ic("chev","ic")}</span></div></div>
<div class="rail">{"".join(mg.game_card(a) for a in mg.NEWG)}</div>
<div class="report"><span>문제가 있나요? 작동하지 않거나, 저작권을 침해하거나, 설명과 다른 게임은 알려 주세요.</span><a href="#">{ic("alert")}게임 신고</a></div></section>'''

def footer():
    return f'''<footer class="ft"><div class="wrap" style="display:flex;flex-direction:column;gap:14px">
<div class="links"><a href="#">이용약관</a><a href="#"><b>개인정보처리방침</b></a><a href="#">운영정책</a><a href="#">저작권 신고</a><a href="#">고객센터</a><a href="#" style="color:var(--make-strong)">게임 올리기</a></div>
<div style="display:flex;align-items:flex-end;gap:10px"><span class="logo" style="font-size:18px;color:var(--ink-3);--ears:var(--ink-4)">{logo()}</span><span>aDmD Games · 광고 없는 인디 게임 플랫폼</span></div></div></footer>'''

STATES = ["처음", "진행 중", "완료", "다운로드", "이 기기 불가"]
def page(title, body, height, memo):
    props = '{"$preview":{"width":1440,"height":%d},"state":{"editor":"enum","default":"처음","options":["처음","진행 중","완료","다운로드","이 기기 불가"],"tsType":"string"},"theme":{"editor":"enum","default":"light","options":["light","dark"],"tsType":"string"},"showMemo":{"editor":"boolean","default":true,"tsType":"boolean"}}' % height
    return f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Gasoek+One&display=swap" rel="stylesheet">
<style>
{mg.TOK}
{mg.COMMON}
{mg.MG_CSS}
{CSS}
</style>
</helmet>
<div class="ds" data-theme="{{{{ theme }}}}" data-ground="play">
{mg.SPRITE}
{mg.EXTRA_ICONS}
{body}
<sc-if value="{{{{ showMemo }}}}" hint-placeholder-val="{{{{ true }}}}"><aside class="memo" style="--x:0"><b style="color:#3A96FE">{title}</b>{memo}</aside></sc-if>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{props}'>
class Component extends DCLogic {{
  renderVals() {{
    const s = this.props.state ?? '처음';
    const th = this.state.theme ?? (this.props.theme ?? 'light');
    return {{ theme: th, toggleTheme: () => this.setState({{ theme: th === 'dark' ? 'light' : 'dark' }}), showMemo: this.props.showMemo ?? true,
      sFirst: s === '처음', sProg: s === '진행 중', sDone: s === '완료', sDl: s === '다운로드', sNo: s === '이 기기 불가',
      isWeb: s !== '다운로드', isWebOk: s !== '다운로드' && s !== '이 기기 불가', isDl: s === '다운로드' }};
  }}
}}
</script>
</body>
</html>'''

def page_a():
    body = pg_header() + f'''<main class="wrap">
<div class="crumb2"><a href="#">게임</a>{ic("chev")}<a href="#">퍼즐</a></div>
<div class="gtitle"><h1>루프 디버거</h1><span class="by">{face("ㅍ","jjok","")}픽셀상점</span><span class="tags"><span class="tag">퍼즐</span><span class="tag">한 판 5분</span><span class="tag">혼자</span></span></div>
<div class="hero2">{media()}{panel()}</div></main>
<div class="stabs"><div style="width:1200px;margin:0 auto;display:flex;align-items:center">{tabs()}</div></div>''' + about() + reviews() + maker_band() + updates() + similar() + footer()
    memo = "첫 화면에서 ‘무슨 게임 · 지금 되나 · 누가’를 한 번에. 왼쪽 움직이는 화면, 오른쪽 결정 패널(상태별 버튼 · 실행 조건 · 평가 · 메이커). Tweaks 의 state 로 처음 / 진행 중 / 완료 / 다운로드 / 이 기기 불가를 바꿔 보세요."
    return page("게임 상세 A · 결정 패널", body, 4200, memo)

def page_b():
    stage = f'''<section class="stage"><div class="in"><div>
<div class="crumb2"><a href="#">게임</a>{ic("chev")}<a href="#">퍼즐</a></div>
<span class="badge static" style="margin-top:18px">{ic("crown","ic ic12")}이번 주 PICK</span>
<h1>루프 디버거</h1>
<p class="lede">모든 방이 하나의 함수인 프로그래밍 퍼즐. 루프를 고쳐 갇힌 로봇을 꺼내 주세요.</p>
<div class="by">{face("ㅍ","jjok","md")}<span>픽셀상점 <span class="m">· 1인 메이커 · 게임 4</span></span><span class="btn btn-glass btn-sm" style="margin-left:6px">팔로우</span></div>
<div class="chips2"><span>{ic("web","ic ic12")}브라우저에서 바로</span><span>{ic("pc","ic ic12")}PC · 휴대폰</span><span>{ic("clock","ic ic12")}한 판 5분</span><span>{ic("duo","ic ic12")}혼자</span><span>추천 92% · 38</span></div>
<div class="acts"><span class="btn btn-on-color big" data-play>{ic("play","ic ic16")}지금 플레이</span><span class="btn btn-glass big" style="padding:0 18px">{ic("bm","ic ic16")}</span><span class="btn btn-glass big" style="padding:0 20px;font-size:15px">친구에게 도전장</span></div>
</div>
<div class="media"><span class="art main a-loop"><span class="shots"></span><span class="frames"><b></b><b></b><b></b><b></b><b></b><b></b></span></span><div class="thumbs">{"".join(f'<span class="art {a}{" on" if i==0 else ""}"></span>' for i,a in enumerate(("a-loop","a-tess","a-grid","a-halcyon","a-paper","a-demon")))}</div></div>
</div></section>
<div class="subbar"><div class="in"><span class="gt"><span class="art a-loop"></span>루프 디버거</span>{tabs()}<span style="margin-left:auto" class="btn btn-primary btn-sm" data-play>{ic("play")}지금 플레이</span></div></div>'''
    body = pg_header() + stage + about() + reviews() + maker_band() + updates() + similar() + footer()
    memo = "게임이 주인공인 무대. 게임 대표색 바탕(게임색 필드) 위에 Gasoek 제목 · 실행 조건 칩 · 큰 플레이 버튼. 스크롤하면 얇은 바에 제목 · 탭 · 플레이 버튼이 붙는다. 상태별 버튼 변형은 A 와 같다(여기선 ‘처음’만)."
    return page("게임 상세 B · 무대", body, 3900, memo)

if __name__ == "__main__":
    for name, fn in [("게임 상세 A.dc.html", page_a), ("게임 상세 B.dc.html", page_b)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
