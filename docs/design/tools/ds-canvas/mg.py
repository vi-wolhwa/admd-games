# MakersGround 홈 시안 생성기 — 디자인 시스템(tokens.css + common.css) 위에서 페이지를 조립한다
# 실행: python mg.py <출력 폴더>
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.argv_out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
import importlib.util
spec = importlib.util.spec_from_file_location("dsb", os.path.join(HERE, "build.py"))
dsb = importlib.util.module_from_spec(spec); spec.loader.exec_module(dsb)

TOK = dsb.canvas_tokens()
COMMON = open(os.path.join(HERE, "common.css"), encoding="utf-8").read()
SPRITE = open(os.path.join(HERE, "sprite.html"), encoding="utf-8").read()
EAR = '<svg class="ear" viewBox="0 0 22 12" aria-hidden="true"><path d="M0 12 L3 0 L9 7 Z M22 12 L19 0 L13 7 Z"></path></svg>'
def logo(m="m"): return "<span>a</span>" + dsb.cat(m)
def ic(name, cls="ic"): return f'<svg class="{cls}"><use href="#i-{name}"></use></svg>'
def face(ch, color, size=""): return f'<span class="jf {size}" style="background:var(--color-face-{color})">{ch}<i>ㅅ</i>{ch}</span>'
# 추가 아이콘(16 격자, 1.7px 선)
EXTRA_ICONS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="i-plus" viewBox="0 0 16 16"><path d="M8 3v10M3 8h10"></path></symbol>
<symbol id="i-pen" viewBox="0 0 16 16"><path d="M10.5 2.5l3 3L6 13H3v-3z"></path><path d="M9 4l3 3"></path></symbol>
<symbol id="i-bug" viewBox="0 0 16 16"><rect x="5" y="5" width="6" height="8" rx="3"></rect><path d="M8 5V3.5M6 3.2 5 2M10 3.2 11 2M5 8H2.5M13.5 8H11M5 11l-2 1.5M11 11l2 1.5"></path></symbol>
<symbol id="i-star" viewBox="0 0 16 16"><path d="M8 2l1.8 3.8 4.2.5-3.1 2.9.8 4.1L8 11.3l-3.7 2 .8-4.1L2 6.3l4.2-.5z"></path></symbol>
<symbol id="i-alert" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6"></circle><path d="M8 5v3.5M8 11h0"></path></symbol>
<symbol id="i-check" viewBox="0 0 16 16"><path d="M3 8.5l3 3 7-7"></path></symbol>
<symbol id="i-chev" viewBox="0 0 16 16"><path d="M6 3l5 5-5 5"></path></symbol>
<symbol id="i-search" viewBox="0 0 16 16"><circle cx="7" cy="7" r="4.5"></circle><path d="M10.5 10.5 13 13"></path></symbol>
<symbol id="i-bell" viewBox="0 0 16 16"><path d="M4 11V7a4 4 0 0 1 8 0v4l1 1.5H3z"></path><path d="M6.5 14h3"></path></symbol>
<symbol id="i-home" viewBox="0 0 16 16"><path d="M2.5 7.5 8 3l5.5 4.5V13a.5.5 0 0 1-.5.5H10V10H6v3.5H3a.5.5 0 0 1-.5-.5z"></path></symbol>
<symbol id="i-box" viewBox="0 0 16 16"><path d="M2.5 5 8 2.5 13.5 5v6L8 13.5 2.5 11z"></path><path d="M2.5 5 8 7.5 13.5 5M8 7.5v6"></path></symbol>
<symbol id="i-user" viewBox="0 0 16 16"><circle cx="8" cy="5.5" r="2.8"></circle><path d="M2.8 13.5c.6-2.6 2.6-4 5.2-4s4.6 1.4 5.2 4"></path></symbol>
<symbol id="i-heart" viewBox="0 0 16 16"><path d="M8 13.3S2.3 10 2.3 6.1A2.9 2.9 0 0 1 8 4.9a2.9 2.9 0 0 1 5.7 1.2C13.7 10 8 13.3 8 13.3z"></path></symbol>
<symbol id="i-q" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6"></circle><path d="M6.3 6.3a1.8 1.8 0 1 1 2.4 1.7c-.5.2-.7.6-.7 1.1v.3M8 11.3h0"></path></symbol>
<symbol id="i-team" viewBox="0 0 16 16"><circle cx="5.5" cy="5.5" r="2.2"></circle><circle cx="11" cy="6.2" r="1.8"></circle><path d="M1.8 13c.4-2.3 1.9-3.6 3.7-3.6s3.3 1.3 3.7 3.6M10 9.6c1.9 0 3.2 1.1 3.6 3"></path></symbol>
<symbol id="i-up2" viewBox="0 0 16 16"><path d="M8 13V4M4.5 7.5 8 4l3.5 3.5"></path><path d="M3 2.5h10"></path></symbol>
</svg>'''

MG_CSS = r'''
body{min-width:1280px}
.hdr .search{width:220px}
.two-line{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.clip{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}
.ds{font-size:15px}
.wrap{width:1200px;margin:0 auto}
.hdr{position:sticky;top:0;z-index:var(--z-header)}
.sec{margin-top:var(--section-gap)}
.sh{display:flex;align-items:center;gap:10px;margin-bottom:var(--section-head-gap)}
.sh h2{margin:0;font-size:22px;line-height:1.3;font-weight:800;letter-spacing:-.02em}
.sh .sub{font-size:13px;color:var(--ink-3);font-weight:500;margin:0 0 0 2px}
.sh .r{margin-left:auto;display:flex;align-items:center;gap:8px}
.link{font-size:14px;font-weight:700;color:var(--ink-3)}
.link:hover{color:var(--ink-1)}
.cnt{display:inline-grid;place-items:center;min-width:22px;height:22px;padding:0 7px;border-radius:999px;background:var(--accent);color:#FFFFFF;font-size:12px;font-weight:800}
/* 상태 칩 */
.st{display:inline-flex;align-items:center;gap:5px;height:24px;padding:0 9px;border-radius:999px;font-size:12px;font-weight:800;white-space:nowrap}
.st .ic{width:12px;height:12px}
.st-live{background:var(--ok-tint);color:var(--ok-text)}
.st-wait{background:var(--sunken);color:var(--ink-2)}
.st-fix{background:var(--accent-tint);color:var(--accent-text)}
.st-draft{background:var(--sunken);color:var(--ink-3)}
.st-no{background:var(--danger-tint);color:var(--danger-text)}
.pulse{width:6px;height:6px;border-radius:999px;background:currentColor;animation:pl 1.6s var(--ease-soft) infinite}
@keyframes pl{50%{opacity:.25}}
@media (prefers-reduced-motion:reduce){.pulse{animation:none}}
/* 단계 표시 */
.steps{display:flex;align-items:center;gap:0;font-size:12px;font-weight:700;color:var(--ink-3)}
.steps span{display:flex;align-items:center;gap:6px}
.steps span::before{content:"";width:8px;height:8px;border-radius:999px;box-shadow:inset 0 0 0 1.5px var(--ink-4)}
.steps span.done::before{background:var(--ink-2);box-shadow:none}
.steps span.now{color:var(--ink-1)}
.steps span.now::before{background:var(--accent);box-shadow:0 0 0 3px var(--accent-tint)}
.steps i{width:22px;height:1.5px;background:var(--sunken-hover);margin:0 6px}
/* 할 일 */
.todo{display:flex;flex-direction:column}
.td{display:grid;grid-template-columns:36px minmax(0,1fr) auto;align-items:center;gap:14px;padding:14px 4px;border-top:1px solid var(--line)}
.td:first-child{border-top:0}
.td .ico{display:grid;place-items:center;width:36px;height:36px;border-radius:10px;background:var(--sunken);color:var(--ink-2)}
.td .ico.acc{background:var(--accent-tint);color:var(--accent-text)}
.td b{display:block;font-size:15px;font-weight:700}
.td .m{display:block;margin-top:2px}
/* 내 게임 줄 */
.mg-rows{display:flex;flex-direction:column;gap:6px}
.mr{position:relative;display:grid;grid-template-columns:128px minmax(0,1.3fr) minmax(0,1fr) 148px 120px;align-items:center;gap:20px;padding:10px 14px 10px 10px;border-radius:var(--radius-lg);transition:background var(--dur-fast) var(--ease-soft)}
.mr:hover{background:var(--sunken)}
.mr .art{width:128px;border-radius:9px}
.mr .ttl{display:flex;flex-direction:column;gap:6px;min-width:0}
.mr .ttl b{font-size:16px;font-weight:800}
.mr .ttl .row{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.mr .note{font-size:13px;color:var(--ink-2)}
.mr .note.acc{color:var(--accent-text);font-weight:700}
.kpi{display:flex;flex-direction:column;gap:2px;font-size:12px;color:var(--ink-3);font-weight:600}
.kpi b{font-size:18px;font-weight:800;color:var(--ink-1);font-variant-numeric:tabular-nums;letter-spacing:-.01em}
.kpi .up{color:var(--ok-text);font-weight:800}
.spark{display:flex;align-items:flex-end;gap:3px;height:28px}
.spark i{width:8px;border-radius:2px 2px 1px 1px;background:var(--sunken-hover)}
.spark i:last-child{background:var(--accent)}
.mr .act{justify-self:end}
.mr.new{grid-template-columns:128px minmax(0,1fr) auto;color:var(--ink-2)}
.mr.new .art{display:grid;place-items:center;background:var(--sunken);color:var(--ink-3)}
.mr.new b{font-size:15px;color:var(--ink-1)}
/* 개발일지 */
.band{padding:44px 0 48px;background:var(--accent-tint)}
.logs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px 24px}
.logc{position:relative;display:flex;flex-direction:column;gap:8px;min-width:0}
.logc .art{border-radius:var(--radius-lg);transition:transform var(--dur-base) var(--ease-soft),box-shadow var(--dur-base) var(--ease-soft)}
.logc:hover .art{transform:var(--card-lift);box-shadow:var(--shadow-lift)}
.logc:hover b{color:var(--accent-text)}
.logc b{font-size:16px;line-height:1.45;font-weight:800}
.logc p{margin:0;font-size:14px;line-height:1.55;color:var(--ink-2)}
.logc .by{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--ink-3)}
.logc .by .g{color:var(--ink-2);font-weight:700}
.react{display:flex;align-items:center;gap:10px;font-size:13px;color:var(--ink-3);margin-left:auto}
.react span{display:flex;align-items:center;gap:4px}
.react .ic{width:13px;height:13px}
.band .ptabs button[aria-selected="true"]{background:var(--raised-hover)}
/* 질문·모집 */
.qa{display:grid;grid-template-columns:1fr 1fr;gap:48px}
.ql{display:flex;flex-direction:column}
.qi{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 16px;align-items:center;padding:14px 2px;border-top:1px solid var(--line)}
.qi:first-child{border-top:0}
.qi b{font-size:15px;font-weight:700}
.qi .m{grid-column:1}
.qi .ans{grid-row:1 / span 2;grid-column:2;display:flex;flex-direction:column;align-items:center;justify-content:center;width:56px;height:52px;border-radius:12px;background:var(--sunken);font-size:11.5px;font-weight:700;color:var(--ink-3)}
.qi .ans b{font-size:17px;color:var(--ink-1)}
.qi .ans.ok{background:var(--ok-tint);color:var(--ok-text)}
.qi .ans.ok b{color:var(--ok-text)}
.qi .ans.zero{background:var(--accent-tint);color:var(--accent-text)}
.qi .ans.zero b{color:var(--accent-text)}
/* 게임 레일 */
.rail{display:flex;gap:16px;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,#000 93%,transparent);mask-image:linear-gradient(90deg,#000 93%,transparent);padding:4px 0 12px;margin:-4px 0 -12px}
.rail .gc{flex:0 0 227px}
.gc .t a::after{content:"";position:absolute;inset:0;z-index:1}
.gc:hover .art{transform:var(--card-lift);box-shadow:var(--shadow-lift)}
.gc .art{transition:transform var(--dur-base) var(--ease-soft),box-shadow var(--dur-base) var(--ease-soft)}
.gc:hover .t{color:var(--accent-text)}
/* 잼 띠 */
.jam{display:grid;grid-template-columns:auto minmax(0,1fr) auto;align-items:center;gap:28px;padding:30px 40px;border-radius:var(--radius-2xl);background:var(--surface-ink);color:#FFFFFF}
.jam .big{font-size:48px;line-height:1;color:var(--color-inju-400)}
.jam b{font-size:19px;font-weight:800}
.jam p{margin:5px 0 0;font-size:14px;color:rgb(255 255 255 / .72)}
.jam .when{display:flex;gap:18px;margin-top:12px;font-size:13px;color:rgb(255 255 255 / .62)}
.jam .when b{font-size:13px;color:#FFFFFF;margin-right:4px}
/* 게스트 소개 */
.intro{display:grid;grid-template-columns:minmax(0,1fr) 400px;gap:64px;align-items:center;padding:48px 0 8px}
.intro h1{margin:0;font-family:var(--font-display);font-weight:400;font-size:40px;line-height:1.2;letter-spacing:-.01em;text-wrap:balance}
.intro .lede{margin:16px 0 0;font-size:16px;line-height:1.7;color:var(--ink-2);max-width:560px}
.how{list-style:none;margin:28px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;counter-reset:h}
.how li{display:flex;flex-direction:column;gap:6px;padding-top:14px;border-top:3px solid var(--sunken-hover);font-size:14px;line-height:1.55;color:var(--ink-2)}
.how li:first-child{border-top-color:var(--accent)}
.how li b{font-size:15px;color:var(--ink-1)}
.how li b::before{counter-increment:h;content:counter(h) "  ";color:var(--accent-text);font-weight:800}
.intro .acts{display:flex;gap:8px;margin-top:28px}
.facts{display:flex;gap:18px;margin-top:18px;font-size:13px;color:var(--ink-3);font-weight:600}
.facts span{display:flex;align-items:center;gap:5px}
.facts .ic{color:var(--ok-text)}
.preview{position:relative;padding:22px 22px 20px;border-radius:var(--radius-2xl);background:var(--sunken)}
.preview .cap{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;font-size:13px;font-weight:700;color:var(--ink-3)}
.preview .gc{background:none}
.preview .gc .art{border-radius:var(--radius-lg)}
.preview .ph{display:grid;place-items:center;background:repeating-linear-gradient(-45deg,var(--sunken-hover) 0 10px,transparent 10px 20px),var(--bg);color:var(--ink-3);font-size:13px;font-weight:700}
.preview .gc .t{font-size:17px}
/* B: 일지 PICK */
.feat{display:grid;grid-template-columns:660px minmax(0,1fr);gap:40px;align-items:center}
.feat .art{border-radius:var(--radius-xl)}
.feat h3{margin:12px 0 0;font-size:28px;line-height:1.3;font-weight:800;letter-spacing:-.02em;text-wrap:balance}
.feat p{margin:14px 0 0;font-size:16px;line-height:1.7;color:var(--ink-2)}
.feat .by{display:flex;align-items:center;gap:8px;margin-top:18px;font-size:14px;color:var(--ink-3)}
.feat .by b{color:var(--ink-1)}
.strip{display:grid;grid-template-columns:auto repeat(4,minmax(0,1fr)) auto;align-items:center;gap:22px;padding:18px 0 22px;border-bottom:1px solid var(--line)}
.strip .hi{font-size:15px;font-weight:800;display:flex;align-items:center;gap:8px}
.sg{display:grid;grid-template-columns:64px minmax(0,1fr);gap:10px;align-items:center;min-width:0}
.sg .art{width:64px;border-radius:7px}
.sg b{display:block;font-size:14px;font-weight:800}
.sg .st{margin-top:3px;height:20px;font-size:11.5px;padding:0 7px}
.gband{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:24px;margin-top:28px;padding:26px 32px;border-radius:var(--radius-2xl);background:var(--accent);color:#FFFFFF}
.gband b{font-size:20px;font-weight:800}
.gband p{margin:4px 0 0;font-size:14px;color:rgb(255 255 255 / .84)}
footer.ft{margin-top:var(--footer-gap);border-top:3px solid var(--accent);padding:28px 0 48px;font-size:13px;color:var(--ink-3)}
footer.ft .links{display:flex;gap:18px;color:var(--ink-2);font-weight:600}
.memo{position:fixed;right:16px;bottom:16px;z-index:50;width:300px;padding:14px 16px;border-radius:14px;background:#151A20;color:#FFFFFF;font-size:12.5px;line-height:1.55;box-shadow:var(--shadow-pop)}
.memo b{display:block;margin-bottom:4px;font-size:13px;color:#FE6648}
.memo button{margin-top:10px;height:30px;padding:0 12px;border:0;border-radius:999px;background:rgb(255 255 255 / .14);color:#FFFFFF;font-size:12px;font-weight:700}
'''

def header(signed):
    right_g = '''<div class="ground"><a class="play" href="#">플레이</a><a class="make" href="#" aria-current="true">메이커스</a></div>
<div class="search">''' + ic("search") + '''게임, 메이커, 글 검색</div>'''
    if signed:
        right = right_g + f'''<span class="btn btn-primary btn-sm">{ic("up2")}게임 올리기</span>
<button class="icon-btn" aria-label="알림 2개">{ic("bell","ic ic20")}<span class="dot-new"></span></button>
{face("ㅍ","jjok","md")}'''
    else:
        right = right_g + f'''<span class="btn btn-secondary btn-sm" onClick="{{{{ toggle }}}}">로그인</span><span class="btn btn-primary btn-sm">{ic("up2")}게임 올리기</span>'''
    return f'''<header class="hdr"><div class="in">
<a class="brand" href="#"><span class="logo" style="font-size:22px">{logo()}</span><span class="word">MakersGround</span></a>
<nav class="gnb"><a href="#" aria-current="page">홈</a><a href="#">내 게임</a><a href="#">개발일지</a><a href="#">질문</a><a href="#">잼</a></nav>
<div class="right">{right}</div>
</div></header>'''

GAMES = [  # 메이커 '픽셀상점' 의 게임
    dict(t="루프 디버거", art="a-loop", st=("live", "공개"), note="v1.2 · 3일 전 업데이트", plays="1,204", delta="▲ 12%", rate="추천 92%", rc="38", newr="새 리뷰 2", spark=[30,42,38,55,47,61,70], act=("secondary", "답글 달기")),
    dict(t="종이 배 2", art="a-paper", st=("fix", "보완 요청"), note="스크린샷이 3장보다 적어요", noteacc=True, plays="—", delta="", rate="", rc="", newr="", spark=None, act=("primary", "고치기")),
    dict(t="그리드 러너", art="a-grid", st=("wait", "검사 중"), note="v0.3 빌드 · 보통 10분 안에 끝나요", plays="—", delta="", rate="", rc="", newr="", spark=None, steps=1, act=("secondary", "진행 보기")),
]

def status(kind, label):
    icon = {"live": ic("check"), "fix": ic("alert"), "wait": '<span class="pulse"></span>', "draft": ic("pen"), "no": ic("alert")}[kind]
    return f'<span class="st st-{kind}">{icon}{label}</span>'

def steps(now):
    names = ["작성", "검사", "심사", "공개"]
    out = []
    for i, n in enumerate(names):
        cls = "done" if i < now else ("now" if i == now else "")
        out.append(f'<span class="{cls}">{n}</span>')
    return '<span class="steps">' + "<i></i>".join(out) + "</span>"

def game_row(g):
    if g.get("spark"):
        mx = max(g["spark"])
        sp = '<span class="spark" aria-hidden="true">' + "".join(f'<i style="height:{round(v/mx*28)}px"></i>' for v in g["spark"]) + "</span>"
        kpi = f'<span class="kpi">최근 7일 플레이<b>{g["plays"]}</b><span class="up">{g["delta"]}</span></span>'
        mid = f'<span class="kpi">{g["rate"]} · 리뷰 {g["rc"]}<span style="display:flex;gap:6px;align-items:center;margin-top:4px"><span class="st st-fix" style="height:22px">{g["newr"]}</span><span class="st st-wait" style="height:22px">{ic("bug")}제보 1</span></span></span>'
        mid_html = f'<span style="display:flex;align-items:center;gap:22px">{kpi}{sp}</span>'
        return f'''<div class="mr"><span class="art {g["art"]}"><span class="shots"></span></span>
<span class="ttl"><b>{g["t"]}</b><span class="row">{status(*g["st"])}<span class="note">{g["note"]}</span></span></span>
{mid_html}{mid}<span class="act"><span class="btn btn-{g["act"][0]} btn-sm">{g["act"][1]}</span></span></div>'''
    extra = steps(g["steps"]) if g.get("steps") else '<span class="m">아직 공개 전이라 통계가 없어요</span>'
    return f'''<div class="mr"><span class="art {g["art"]}"><span class="shots"></span></span>
<span class="ttl"><b>{g["t"]}</b><span class="row">{status(*g["st"])}<span class="note{' acc' if g.get('noteacc') else ''}">{g["note"]}</span></span></span>
<span>{extra}</span><span></span><span class="act"><span class="btn btn-{g["act"][0]} btn-sm">{g["act"][1]}</span></span></div>'''

def draft_row():
    return f'''<div class="mr"><span class="art" style="display:grid;place-items:center;color:var(--ink-3);font-size:13px;font-weight:700">아트 없음</span>
<span class="ttl"><b>이름 없는 프로젝트</b><span class="row">{status("draft","작성 중")}<span class="note">8단계 중 3단계 · 어제 저장</span></span></span>
<span>{steps(0)}</span><span></span><span class="act"><span class="btn btn-secondary btn-sm">이어서 쓰기</span></span></div>'''

def new_row():
    return f'''<div class="mr new"><span class="art">{ic("plus","ic ic20")}</span><span><b>새 게임 올리기</b><span class="m" style="display:block;margin-top:2px">웹 빌드(zip)는 브라우저에서 바로, 설치 파일은 보안 검사 후 공개돼요</span></span><span class="act"><span class="btn btn-primary btn-sm">{ic("up2")}올리기</span></span></div>'''

TODOS = [
    ("alert", True, "‘종이 배 2’ 보완 요청이 왔어요", "스크린샷을 3장 이상 올려 주세요 · 심사 담당 · 2시간 전", ("primary", "고치기")),
    ("cmt", False, "‘루프 디버거’ 새 리뷰 2개", "답글을 달면 리뷰 쓴 사람에게 알림이 가요", ("secondary", "답글 달기")),
    ("bug", False, "‘루프 디버거’ 버그 제보 1개", "Windows · Chrome 131 · 3단계에서 소리가 안 나요", ("secondary", "보기")),
]
def todo_list():
    rows = []
    for icn, acc, t, m, (k, lab) in TODOS:
        rows.append(f'<div class="td"><span class="ico{" acc" if acc else ""}">{ic(icn,"ic ic16")}</span><span><b>{t}</b><span class="m">{m}</span></span><span class="btn btn-{k} btn-sm">{lab}</span></div>')
    return '<div class="todo">' + "".join(rows) + "</div>"

LOGS = [
    ("a-ash", "보스 패턴을 세 번 갈아엎은 이야기", "플레이 테스트에서 ‘억울하다’는 말이 제일 많았던 2페이즈. 예고 동작을 0.4초 늘린 것만으로 완주율이 두 배가 됐어요.", "ㅈ", "ju", "잿빛토끼", "재의 도시", 48, 14),
    ("a-tess", "웹 빌드 40MB를 9MB로 줄인 방법", "텍스처 압축, 오디오 스트리밍, 안 쓰는 셰이더 빼기. 첫 로딩이 12초에서 3초로 줄었어요.", "ㄴ", "haneul", "노을공방", "테셀레이트", 112, 31),
    ("a-loop", "첫 리뷰 38개를 읽고 바꾼 것들", "‘튜토리얼이 길다’는 말이 9번. 첫 스테이지를 퍼즐 하나로 줄이고 힌트 버튼을 넣었어요.", "ㅍ", "jjok", "픽셀상점", "루프 디버거", 67, 22),
    ("a-paper", "Godot 4 웹 내보내기에서 소리가 안 날 때", "브라우저는 첫 클릭 전엔 소리를 막아요. 시작 화면에 버튼 하나를 두는 게 가장 깔끔했어요.", "ㅊ", "cheongnok", "청록상회", "종이 배", 39, 8),
    ("a-grid", "48시간 잼 회고 — 주제 ‘다시 한 번’", "되감기 기능을 둘째 날 새벽에 버린 게 신의 한 수였어요. 남은 시간에 사운드를 넣었거든요.", "ㅂ", "bora", "보라네", "그리드 러너", 54, 17),
    ("a-demon", "16색 팔레트로 들판 그리기", "색을 줄이니 오히려 계절이 잘 보였어요. 팔레트 파일도 같이 올려요.", "ㅍ", "pul", "풀잎", "들판의 악마", 83, 12),
]
def log_card(l, show_excerpt=True):
    art, t, ex, ch, col, who, game, like, cmt = l
    p = f"<p class='two-line'>{ex}</p>" if show_excerpt else ""
    return f'''<article class="logc"><span class="art {art}"><span class="shots"></span></span>
<b>{t}</b>{p}<span class="by">{face(ch, col, "xs")}{who} · <span class="g">{game}</span><span class="react"><span>{ic("heart")}{like}</span><span>{ic("cmt")}{cmt}</span></span></span></article>'''

QS = [
    ("Unity WebGL 빌드가 아이폰 사파리에서 멈춰요", "Unity · 웹 빌드 · 2시간 전", "ok", 2, "해결"),
    ("세이브를 브라우저에 저장하는 가장 안전한 방법?", "웹 · 저장 · 35분 전", "zero", 0, "답변"),
    ("다른 사이트에 올린 게임을 여기에도 올려도 되나요?", "운영 · 어제", "ok", 4, "해결"),
    ("픽셀 폰트 라이선스, 상업용 아니어도 표기해야 하나요?", "아트 · 폰트 · 어제", "", 1, "답변"),
]
RS = [
    ("픽셀 아티스트 1명 · 3개월 · 온라인", "로그라이크 ‘재의 도시’ 후속작 · 주 10시간", "ㅈ", "ju", "잿빛토끼"),
    ("사운드 · 겨울 잼 기간만", "효과음 위주, 음악은 있으면 좋아요", "ㅂ", "bora", "보라네"),
    ("Godot 프로그래머 · 취미 프로젝트", "퍼즐 플랫포머, 매주 토요일 온라인 회의", "ㅊ", "cheongnok", "청록상회"),
]
def qa_block():
    qi = "".join(f'''<div class="qi"><b>{t}</b><span class="m">{m}</span><span class="ans {k}"><b>{n}</b>{lab}</span></div>''' for t, m, k, n, lab in QS)
    ri = "".join(f'''<div class="qi"><b>{t}</b><span class="m" style="display:flex;align-items:center;gap:6px">{face(ch,col,"xs")}{who} · {m}</span><span class="ans" style="width:auto;padding:0 12px;height:36px;flex-direction:row;font-size:13px;color:var(--ink-1)">{ic("team")}&nbsp;연락</span></div>''' for t, m, ch, col, who in RS)
    return f'''<div class="qa">
<div><div class="sh" style="margin-bottom:6px">{EAR}<h2 style="font-size:19px">답을 기다리는 질문</h2><div class="r"><a class="link" href="#">질문하기</a></div></div><div class="ql">{qi}</div></div>
<div><div class="sh" style="margin-bottom:6px">{EAR}<h2 style="font-size:19px">팀원 모집</h2><div class="r"><a class="link" href="#">모집 글 쓰기</a></div></div><div class="ql">{ri}</div></div>
</div>'''

NEWG = [("a-tess", "테셀레이트", "노을공방", "ㄴ", "haneul", "퍼즐 · 10분", "web"), ("a-demon", "들판의 악마", "풀잎", "ㅍ", "pul", "전략 · 30분", "dl"), ("a-halcyon", "할시온 바다", "하늘섬", "ㅎ", "haneul", "탐험 · 20분", "web"), ("a-ash", "재의 도시", "잿빛토끼", "ㅈ", "ju", "생존 · 40분", "dl"), ("a-paper", "종이 배", "청록상회", "ㅊ", "cheongnok", "탐험 · 20분", "web"), ("a-grid", "그리드 러너", "보라네", "ㅂ", "bora", "액션 · 3분", "web")]
def game_card(a):
    art, t, who, ch, col, meta, plat = a
    pl = ic("web", "ic ic12") if plat == "web" else ic("dl", "ic ic12") + '<svg class="ic ic12 ok"><use href="#i-shield"></use></svg>'
    return f'''<div class="gc"><span class="art {art}"><span class="shots"></span><span class="plat">{pl}</span><span class="jf maker" style="background:var(--color-face-{col})">{ch}<i>ㅅ</i>{ch}</span></span><span class="t"><a href="#">{t}</a></span><span class="meta">{who} · {meta}</span></div>'''

def new_games():
    return f'''<section class="sec wrap"><div class="sh">{EAR}<h2>이번 주 공개된 게임</h2><span class="sub">다른 메이커들의 새 게임</span><div class="r"><span class="arw" style="opacity:.4">{ic("chev","ic")}</span><span class="arw">{ic("chev","ic")}</span></div></div>
<div class="rail">{"".join(game_card(a) for a in NEWG)}</div></section>'''

def jam():
    return f'''<section class="sec wrap"><div class="jam"><span class="big disp">D-3</span>
<div><b>겨울 잼 · 주제는 시작할 때 공개</b><p>48시간 동안 혼자 또는 팀으로. 끝나면 PlayGround 잼 아케이드에서 바로 플레이돼요.</p>
<div class="when"><span><b>시작</b>12/12(금) 19:00</span><span><b>제출</b>12/14(일) 19:00</span><span><b>참가</b>212명 · 팀 58</span></div></div>
<span class="btn btn-primary">참가 신청</span></div></section>'''

def logs_band(title="개발일지", n=6, tabs=True):
    t = '<div class="ptabs" role="tablist"><button role="tab" aria-selected="true">전체</button><button role="tab">팔로우</button><button role="tab">내 게임 언급</button></div>' if tabs else ""
    return f'''<section class="sec band"><div class="wrap"><div class="sh">{EAR}<h2>{title}</h2><div class="r">{t}<span class="btn btn-primary btn-sm">{ic("pen")}일지 쓰기</span></div></div>
<div class="logs">{"".join(log_card(l) for l in LOGS[:n])}</div></div></section>'''

def footer():
    return f'''<footer class="ft"><div class="wrap" style="display:flex;flex-direction:column;gap:14px">
<div style="display:flex;align-items:center;gap:10px"><b style="color:var(--ink-2)">공지</b><a href="#">심사 기준을 쉽게 고쳐 썼어요</a><span>·</span><a href="#">설치형 게임 보안 검사를 시작했어요</a></div>
<div class="links"><a href="#">처음 올리는 분</a><a href="#">심사 기준</a><a href="#">이용약관</a><a href="#"><b>개인정보처리방침</b></a><a href="#">운영정책</a><a href="#">고객센터</a><a href="#" style="color:var(--play-strong)">PlayGround 로</a></div>
<div style="display:flex;align-items:flex-end;gap:10px"><span class="logo" style="font-size:18px;color:var(--ink-3);--ears:var(--ink-4)">{logo()}</span><span>aDmD Games · 광고 없는 인디 게임 플랫폼</span></div>
</div></footer>'''

def guest_intro():
    return f'''<section class="wrap"><div class="intro">
<div><h1>만든 게임, 여기에 올려 보세요</h1>
<p class="lede">웹 빌드는 올리자마자 브라우저에서 바로 플레이되고, 설치 파일은 보안 검사를 거쳐 내려받게 해요. 광고도 수수료도 없어요.</p>
<ol class="how"><li><b>메이커 프로필 만들기</b>이름과 얼굴만 있으면 돼요. 팀도 괜찮아요.</li><li><b>게임 올리기</b>웹 빌드 zip 또는 설치 파일. 저장하며 진행해서 휴대폰으로 이어서 써도 돼요.</li><li><b>검사 · 심사 후 공개</b>보통 하루 안에 끝나요. 고칠 게 있으면 어디를 고칠지 알려 드려요.</li></ol>
<div class="acts"><span class="btn btn-primary">{ic("up2","ic ic16")}첫 게임 올리기</span><span class="btn btn-secondary">올리기 전에 읽어 보기</span></div>
<div class="facts"><span>{ic("check")}무료</span><span>{ic("check")}보안 검사 무료</span><span>{ic("check")}언제든 비공개로 전환</span></div></div>
<div class="preview"><div class="cap"><span>올리면 이렇게 보여요</span><span>PlayGround 카드</span></div>
<div class="gc"><span class="art ph"><span>내 게임 대표 그림 1920×1080</span><span class="badge" style="background:var(--color-graphite-950)">새로 공개</span><span class="plat">{ic("web","ic ic12")}</span><span class="jf md maker" style="background:var(--color-face-olive)">ㄴ<i>ㅅ</i>ㄴ</span></span><span class="t">내 게임 이름</span><span class="meta">내 이름 · 장르 · 한 판 시간</span></div>
<p class="m" style="margin:14px 0 0">카드 · 상세 · 공유 미리보기에서 어떻게 잘리는지 올릴 때 바로 확인할 수 있어요.</p></div>
</div></section>'''

def page(title, body, height, memo, width=1440):
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
{TOK}
{COMMON}
{MG_CSS}
</style>
</helmet>
<div class="ds" data-theme="{{{{ theme }}}}" data-ground="make">
{SPRITE}
{EXTRA_ICONS}
{body}
<sc-if value="{{{{ showMemo }}}}" hint-placeholder-val="{{{{ true }}}}"><aside class="memo"><b>{title}</b>{memo}</aside></sc-if>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{width},"height":{height}}},"startSignedIn":{{"editor":"boolean","default":true,"tsType":"boolean"}},"theme":{{"editor":"enum","default":"light","options":["light","dark"],"tsType":"string"}},"showMemo":{{"editor":"boolean","default":true,"tsType":"boolean"}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    const signed = this.state.signed ?? (this.props.startSignedIn ?? true);
    return {{ signedIn: signed, guest: !signed, theme: this.props.theme ?? 'light', showMemo: this.props.showMemo ?? true, toggle: () => this.setState({{ signed: !signed }}) }};
  }}
}}
</script>
</body>
</html>'''

def signed_block(signed_html, guest_html):
    return f'''<sc-if value="{{{{ signedIn }}}}" hint-placeholder-val="{{{{ true }}}}">{signed_html}</sc-if>
<sc-if value="{{{{ guest }}}}" hint-placeholder-val="{{{{ false }}}}">{guest_html}</sc-if>'''

# ── 시안 A · 작업 먼저 ──
def page_a():
    member = f'''<section class="wrap" style="margin-top:36px">
<div style="display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:48px;align-items:start">
<div><div class="sh">{EAR}<h2>할 일</h2><span class="cnt">3</span></div>{todo_list()}</div>
<div><div class="sh">{EAR}<h2>바로 하기</h2></div>
<div style="display:flex;flex-direction:column;gap:8px">
<span class="btn btn-primary" style="justify-content:flex-start">{ic("up2","ic ic16")}새 게임 올리기</span>
<span class="btn btn-secondary" style="justify-content:flex-start">{ic("box","ic ic16")}새 버전 올리기 · 루프 디버거</span>
<span class="btn btn-secondary" style="justify-content:flex-start">{ic("pen","ic ic16")}개발일지 쓰기</span></div>
<p class="m" style="margin:12px 2px 0">심사는 보통 하루 안에 끝나요. 지금 대기 14개.</p></div>
</div></section>
<section class="sec wrap"><div class="sh">{EAR}<h2>내 게임</h2><span class="sub">4개</span><div class="r"><a class="link" href="#">통계 · 전체 관리</a></div></div>
<div class="mg-rows">{"".join(game_row(g) for g in GAMES)}{draft_row()}</div></section>'''
    guest = guest_intro()
    body = header_block() + signed_block(member, guest) + logs_band() + new_games() + f'<section class="sec wrap">{qa_block()}</section>' + jam() + footer()
    memo = "할 일 → 내 게임 상태 → 동료(일지·새 게임·질문) 순. 메이커가 들어와서 할 일을 바로 찾게 했다. 게스트는 지표 대신 ‘올리는 법 3단계 + 올리면 이렇게 보여요’. Tweaks 에서 게스트/회원 · 다크 전환.<br><button onClick=\"{{ toggle }}\">게스트 ↔ 회원</button>"
    return page("MakersGround 홈 A · 작업 먼저", body, 3000, memo)

def header_block():
    return signed_block(header(True), header(False))

# ── 시안 B · 일지 먼저 ──
def page_b():
    strip_games = "".join(f'<div class="sg"><span class="art {g["art"]}"></span><span><b class="clip">{g["t"]}</b>{status(*g["st"])}</span></div>' for g in GAMES)
    strip_games += f'<div class="sg"><span class="art" style="display:grid;place-items:center;font-size:11px;color:var(--ink-3)">—</span><span><b class="clip">이름 없는 프로젝트</b>{status("draft","작성 중")}</span></div>'
    member = f'''<section class="wrap"><div class="strip"><span class="hi">{face("ㅍ","jjok","md")}내 게임</span>{strip_games}<span style="display:flex;gap:8px"><span class="btn btn-secondary btn-sm">할 일 <span class="cnt" style="margin-left:2px">3</span></span><span class="btn btn-primary btn-sm">{ic("up2")}올리기</span></span></div></section>'''
    guest = f'''<section class="wrap"><div class="gband"><div><b>만든 게임, 여기에 올려 보세요</b><p>웹 빌드는 바로 플레이 · 설치 파일은 무료 보안 검사 · 광고와 수수료 없음 · 보통 하루 안에 공개</p></div><span style="display:flex;gap:8px"><span class="btn btn-glass">올리기 전에 읽어 보기</span><span class="btn btn-on-color">첫 게임 올리기</span></span></div></section>'''
    l = LOGS[1]
    feat = f'''<section class="sec wrap" style="margin-top:44px"><div class="sh">{EAR}<h2>이번 주 일지 PICK</h2></div>
<div class="feat"><span class="art {l[0]}"><span class="shots"></span><span class="badge mk" style="--overlay-inset:12px">{ic("crown","ic ic12")}PICK</span></span>
<div><span class="st st-fix">웹 빌드 · 최적화</span><h3>{l[1]}</h3><p>{l[2]} 압축 설정 표와 전후 비교 빌드를 같이 올려 두었어요.</p>
<div class="by">{face(l[3], l[4], "md")}<span><b>{l[5]}</b> · {l[6]} · 3일 전</span><span class="react" style="margin-left:14px"><span>{ic("heart")}{l[7]}</span><span>{ic("cmt")}{l[8]}</span></span></div>
<div style="display:flex;gap:8px;margin-top:22px"><span class="btn btn-primary">읽기</span><span class="btn btn-secondary">{ic("play","ic ic16")}테셀레이트 플레이</span></div></div></div></section>'''
    rest = [x for i, x in enumerate(LOGS) if i != 1]
    grid = f'''<section class="sec wrap"><div class="sh">{EAR}<h2>새 개발일지</h2><div class="r"><div class="chips"><button class="chip" aria-pressed="true">전체</button><button class="chip">팔로우</button><button class="chip">웹 빌드</button><button class="chip">아트</button><button class="chip">회고</button></div><span class="btn btn-primary btn-sm">{ic("pen")}일지 쓰기</span></div></div>
<div class="logs" style="grid-template-columns:repeat(4,minmax(0,1fr))">{"".join(log_card(x, False) for x in rest[:4])}</div></section>'''
    qa = f'<section class="sec band"><div class="wrap">{qa_block()}</div></section>'
    body = header_block() + signed_block(member, guest) + feat + grid + qa + new_games() + jam() + footer()
    memo = "커뮤니티 먼저. 내 게임 상태는 맨 위 한 줄로 줄이고, 일지 PICK(큰 그림 + 요약)과 새 일지 그리드가 주인공. 메이커끼리 배우고 자극받는 곳이라는 인상이 강하다. 대신 할 일은 한 번 더 눌러야 보인다.<br><button onClick=\"{{ toggle }}\">게스트 ↔ 회원</button>"
    return page("MakersGround 홈 B · 일지 먼저", body, 2800, memo)

if __name__ == "__main__":
    out = sys.argv_out
    for name, fn in [("MakersGround 홈 A.dc.html", page_a), ("MakersGround 홈 B.dc.html", page_b)]:
        html = fn()
        assert "[[" not in html
        open(os.path.join(out, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
