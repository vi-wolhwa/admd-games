# PlayGround 게임 상세(PG05) 생성기 — v3 재설계(2026-11-27). page()·pg_header()·footer() 는 다른 생성기도 쓴다
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
.rate-line b{display:inline-flex;align-items:center;gap:6px;font-size:22px;font-weight:800;color:var(--ink-1)}
.rate-line b .ic{color:var(--accent-text)}
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

REVIEWS = [
    ("ㅅ", "hong", "새벽코딩", True, "3.2시간", "회사에서 하는 일이랑 너무 똑같아서 웃겼어요. 그런데 이건 고치면 칭찬을 해 주네요. 15스테이지 이후로 난이도가 확 오르는데 힌트가 잘 잡아줘요.", "15스테이지 구간은 다음 업데이트에서 단계를 하나 더 넣을게요. 고마워요!"),
    ("ㄱ", "gyul", "귤껍질", True, "48분", "출퇴근길에 한 판씩 하기 딱 좋아요. 휴대폰 가로 모드에서도 블록이 안 작아서 좋았어요.", None),
    ("ㅁ", "bora", "모래시계", False, "1.1시간", "튜토리얼이 너무 길어요. 처음 세 스테이지는 건너뛰기가 있으면 좋겠어요.", "v1.2 에서 튜토리얼을 한 스테이지로 줄였어요. 다시 한 번 봐 주세요!"),
]
def footer():
    return f'''<footer class="ft"><div class="wrap" style="display:flex;flex-direction:column;gap:14px">
<div class="links"><a href="#">이용약관</a><a href="#"><b>개인정보처리방침</b></a><a href="#">운영정책</a><a href="#">저작권 신고</a><a href="#">고객센터</a><a href="#" style="color:var(--make-strong)">게임 올리기</a></div>
<div style="display:flex;align-items:flex-end;gap:10px"><span class="logo" style="font-size:18px;color:var(--ink-3);--ears:var(--ink-4)">{logo()}</span><span>aDmD Games · 광고 없는 인디 게임 플랫폼</span></div></div></footer>'''

STATES = ["처음", "진행 중", "완료", "다운로드", "이 기기 불가"]
def page(title, body, height, memo):
    props = '{"$preview":{"width":1440,"height":%d},"state":{"editor":"enum","default":"처음","options":["처음","진행 중","완료","다운로드","이 기기 불가"],"tsType":"string"},"theme":{"editor":"enum","default":"light","options":["light","dark"],"tsType":"string"},"showMemo":{"editor":"boolean","default":true,"tsType":"boolean"}}' % height
    return mg._catify(_page_html(title, body, height, memo, props))

def _page_html(title, body, height, memo, props):
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

# ── PG05 게임 상세 v3 (2026-11-27 재설계) ──────────────────────────────────
# 첫 화면 = 게임(큰 미리보기) + 오른쪽 '정체 · 행동' 패널. 아래는 탭으로 나눈 내용(소개 · 리뷰 · 개발일지 · 업데이트) — 한 번에 하나만 보인다.
G_CSS = r'''
.g5{display:grid;grid-template-columns:minmax(0,1fr) 392px;gap:36px;margin-top:20px;align-items:start}
.g5 .viewer{position:relative;--overlay-inset:12px}
.g5 .viewer .art{border-radius:var(--radius-xl)}
.g5 .viewer .plat{height:28px;padding:0 10px;font-size:12.5px;gap:7px}
.g5 .viewer .vcount{position:absolute;right:12px;bottom:12px;z-index:3;height:26px;padding:0 10px;border-radius:999px;background:var(--scrim);color:#FFFFFF;font-size:12.5px;font-weight:700;display:inline-flex;align-items:center}
.strip-w{position:relative;margin-top:10px}
.strip{display:flex;gap:8px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding:3px 3px 4px;margin:-3px -3px -4px}
.strip::-webkit-scrollbar{display:none}
.strip .it{position:relative;flex:0 0 calc((100% - 40px) / 6);scroll-snap-align:start;border-radius:9px}
.strip .it .art{border-radius:9px;opacity:.7}
.strip .it.on .art{opacity:1;box-shadow:0 0 0 2px var(--bg),0 0 0 4px var(--accent)}
.strip .it .lab{position:absolute;left:5px;bottom:5px;z-index:2;height:18px;padding:0 6px;border-radius:5px;background:var(--scrim);color:#FFFFFF;font-size:11px;font-weight:800;display:inline-flex;align-items:center;gap:3px}
.strip .it .lab .ic{width:9px;height:9px}
.strip .it.v .art::after{content:"";position:absolute;inset:0;border-radius:inherit;background:rgb(16 19 22 / .28)}
.strip .it.v .pl{position:absolute;inset:0;z-index:2;display:grid;place-items:center;color:#FFFFFF}
.strip-w .fade{position:absolute;right:-1px;top:0;bottom:0;width:64px;background:linear-gradient(90deg,transparent,var(--bg) 70%);pointer-events:none}
.strip-w .nav{position:absolute;right:0;top:50%;transform:translateY(-50%);z-index:3;width:32px;height:32px;border-radius:999px;background:var(--bg);box-shadow:var(--shadow-pop),0 0 0 1px var(--line);display:grid;place-items:center;color:var(--ink-1)}
.strip-w .nav.l{left:0;right:auto;opacity:.0}
.idp{display:flex;flex-direction:column;gap:16px}
.idp h1{margin:0;font-size:32px;line-height:1.2;font-weight:800;letter-spacing:-.025em}
.idp .by{display:flex;align-items:center;gap:8px;font-size:15px;font-weight:700;color:var(--ink-2)}
.idp .by .fl{margin-left:2px;font-size:13px;font-weight:800;color:var(--accent-text)}
.idp .pitch{margin:0;font-size:15.5px;line-height:1.6;color:var(--ink-2)}
.idp .gt{display:flex;flex-wrap:wrap;gap:6px}
.idp .gt span{height:26px;padding:0 10px;border-radius:7px;background:var(--sunken);font-size:13px;font-weight:700;color:var(--ink-2);display:inline-flex;align-items:center}
.keyf{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.keyf > span{display:flex;flex-direction:column;gap:4px;padding:12px;border-radius:var(--radius-md);background:var(--sunken);font-size:12.5px;color:var(--ink-3);font-weight:600}
.keyf > span b{display:flex;align-items:center;gap:6px;font-size:14px;color:var(--ink-1);font-weight:800}
.keyf > span b .ic{color:var(--accent-text)}
.keyf > span.ok b .ic{color:var(--ok-text)}
.idp .rate-line{padding-top:14px;border-top:1px solid var(--line)}
.ttabs{position:sticky;top:68px;z-index:10;margin-top:48px;background:color-mix(in srgb,var(--bg) 94%,transparent);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.ttabs .in{width:1200px;margin:0 auto;display:flex;align-items:center;gap:4px;height:56px}
.ttabs button{height:56px;padding:0 16px;border:0;background:transparent;font:inherit;font-size:16px;font-weight:700;color:var(--ink-3);box-shadow:inset 0 -2px 0 transparent;cursor:pointer}
.ttabs button:hover{color:var(--ink-1)}
.ttabs button[aria-selected="true"]{color:var(--ink-1);box-shadow:inset 0 -2px 0 var(--ink-1)}
.ttabs button .n{margin-left:4px;font-size:14px;color:var(--ink-3);font-weight:600}
.ttabs .mini{margin-left:auto;display:flex;align-items:center;gap:10px;font-size:14px;font-weight:800}
.ttabs .mini .art{width:56px;border-radius:6px}
.tpanel{margin-top:36px;min-height:640px}
.ab2{display:grid;grid-template-columns:minmax(0,1fr) 392px;gap:56px;align-items:start}
.ab2 h2{margin:0 0 14px;font-size:20px;font-weight:800}
.ab2 p{margin:0 0 14px;font-size:16px;line-height:1.8}
.ab2 .feat{display:flex;flex-direction:column;align-items:flex-start;text-align:left;gap:10px;margin:18px 0 0;padding:18px 20px;border-radius:var(--radius-lg);background:var(--sunken)}
.ab2 .feat span{display:flex;gap:10px;font-size:15px;color:var(--ink-1)}
.ab2 .feat .ic{color:var(--accent-text);margin-top:4px}
.infoc{display:flex;flex-direction:column;gap:18px}
.infog > b{display:block;margin-bottom:4px;font-size:13px;font-weight:800;color:var(--ink-3)}
.infog dl{margin:0;display:flex;flex-direction:column}
.infog dl > div{display:grid;grid-template-columns:72px minmax(0,1fr);gap:12px;padding:9px 0;border-top:1px solid var(--line);font-size:14px}
.infog dl > div:first-child{border-top:0}
.infog dt{color:var(--ink-3);font-weight:600}
.infog dd{margin:0;font-weight:600}
.infog .okt{color:var(--ok-text);font-weight:800}
.mkc{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center;padding:16px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line)}
.mkc b{display:block;font-size:15px}
.mkc .m{display:block;font-size:13px}
.rptl{display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:700;color:var(--ink-3)}
.rv2top{display:flex;align-items:flex-end;gap:28px;padding-bottom:22px;border-bottom:1px solid var(--line)}
.rv2top .disp{font-size:52px;line-height:1;color:var(--accent-text)}
.rv2top .t b{display:block;font-size:16px}
.rv2top .t .m{display:block;margin-top:4px}
.rv2top .r{margin-left:auto;display:flex;gap:8px}
.rv2bar{display:flex;align-items:center;gap:8px;margin:18px 0 4px;flex-wrap:wrap}
.rv2bar .sort{margin-left:auto;display:flex;gap:4px;font-size:13.5px;font-weight:700;color:var(--ink-3)}
.rv2bar .sort span{padding:6px 8px;border-radius:8px}
.rv2bar .sort span.on{color:var(--ink-1);background:var(--sunken)}
.rv2list{display:grid;grid-template-columns:1fr 1fr;gap:4px 40px}
.rv2list .rv{border-top:1px solid var(--line);padding:20px 0 18px}
.logs2{display:flex;flex-direction:column}
.logs2 a{display:grid;grid-template-columns:220px minmax(0,1fr);gap:22px;padding:20px 0;border-top:1px solid var(--line);align-items:center}
.logs2 a:first-child{border-top:0;padding-top:0}
.logs2 .art{border-radius:var(--radius-md)}
.logs2 .k{font-size:12.5px;font-weight:800;color:var(--make-strong)}
.logs2 b{display:block;margin-top:4px;font-size:18px;line-height:1.4}
.logs2 p{margin:6px 0 0;font-size:14.5px;line-height:1.6;color:var(--ink-2)}
.logs2 .m{display:flex;gap:10px;margin-top:8px;font-size:13px}
.simsec{margin-top:72px;padding-top:40px;border-top:1px solid var(--line)}
'''

COVER = "a-loop"
MEDIA = [("cover", "a-loop"), ("video", "a-tess", "0:42"), ("video", "a-grid", "0:15"), ("img", "a-halcyon"), ("img", "a-paper"), ("img", "a-demon"), ("img", "a-refac"), ("img", "a-bazaar"), ("img", "a-solvent")]

def g_media():
    plat_web = f'<span class="plat">{ic("web","ic ic12")}브라우저 {ic("phone","ic ic12")}휴대폰</span>'
    plat_dl = f'<span class="plat">{ic("dl","ic ic12")}설치형 <svg class="ic ic12 ok"><use href="#i-shield"></use></svg>검사 통과</span>'
    items = ""
    for i, m in enumerate(MEDIA):
        kind, art = m[0], m[1]
        if kind == "cover":
            items += f'<button class="it on" aria-label="대표 그림" aria-current="true"><span class="art {art}"></span><span class="lab">대표</span></button>'
        elif kind == "video":
            items += f'<button class="it v" aria-label="영상 {m[2]}"><span class="art {art}"></span><span class="pl">{ic("play","ic ic16")}</span><span class="lab">{ic("play")}{m[2]}</span></button>'
        else:
            items += f'<button class="it" aria-label="이미지 {i - 2}"><span class="art {art}"></span></button>'
    return f'''<div class="viewer"><span class="art main {COVER}"><span class="shots"></span><span class="badge">{ic("crown","ic ic12")}이번 주 PICK</span>{sif("isWeb", plat_web, True)}{sif("isDl", plat_dl)}<span class="vcount">대표 · 1 / {len(MEDIA)}</span></span>
<div class="strip-w"><div class="strip" role="list" aria-label="미리보기 — 대표 그림, 영상, 이미지 순서">{items}</div><span class="fade"></span><button class="nav" aria-label="다음 미리보기">{ic("chev")}</button></div></div>'''

KEYF_WEB = [("web", "실행", "바로 플레이", "브라우저 · 휴대폰 가로", ""), ("clock", "한 판", "5분", "전체 40스테이지", ""), ("duo", "인원", "혼자", "한국어 · 영어", "")]
KEYF_DL = [("dl", "실행", "설치형", "Windows · macOS", ""), ("shield", "보안 검사", "통과", "11/24 · 엔진 3종", "ok"), ("clock", "한 판", "40분", "저장 가능", "")]
KEYF_NO = [("phone", "실행", "휴대폰 전용", "터치 조작 · PC 안 됨", ""), ("clock", "한 판", "3분", "", ""), ("duo", "인원", "혼자", "한국어", "")]
def keyf(rows):
    return '<div class="keyf">' + "".join(f'<span class="{c}">{k}<b>{ic(i)}{v}</b>{s}</span>' for i, k, v, s, c in rows) + "</div>"

def g_panel():
    first = f'''<div class="cta"><span class="btn btn-primary big" data-play>{ic("play","ic ic16")}지금 플레이</span><div class="pair"><span class="btn btn-secondary">{ic("bm","ic ic16")}저장</span><span class="btn btn-secondary">친구에게 도전장</span></div></div>'''
    prog = f'''<div class="cta"><span class="btn btn-primary big" data-play>{ic("play","ic ic16")}이어하기 · 23스테이지</span>
<div class="prog-box"><div class="row"><span><b>진행 45%</b> · 18 / 40</span><span>어제 · 1시간 12분 플레이</span></div><div class="bar"><i style="width:45%"></i></div><div class="row"><span class="m" style="font-size:12px">진행도는 게임이 알려 준 값이에요</span><span>{ic("bmf","ic ic12")} 저장함</span></div></div></div>'''
    done = f'''<div class="cta"><span class="btn btn-primary big" data-play>{ic("play","ic ic16")}다시 하기</span>
<div class="prog-box"><div class="row"><span><b>끝까지 함</b> · 11/20</span><span>총 2시간 14분</span></div><div class="row"><span>최고 기록</span><b class="num">03:42.18</b></div></div>
<span class="btn btn-secondary">내 기록으로 친구에게 도전장</span></div>'''
    dl = f'''<div class="cta"><div class="files"><div class="file on">{ic("pc")}<span><b>Windows</b><span class="m">v1.2 · 312MB · 설치 파일(.exe)</span></span>{ic("check","ic ic16")}</div><div class="file">{ic("pc")}<span><b>macOS</b><span class="m">v1.2 · 298MB · .dmg · Apple 서명 없음</span></span><span></span></div></div>
<span class="btn btn-primary big">{ic("dl","ic ic16")}다운로드 · Windows</span>
<a class="link" href="#" style="font-size:13px">Windows 가 경고를 띄우나요? 설치 안내 보기 ›</a></div>'''
    no = f'''<div class="notice"><span class="qr" aria-hidden="true"></span><span><b>휴대폰에서 열어 주세요</b>터치 전용이라 PC 에서는 할 수 없어요. QR 을 찍거나 링크를 보내 보세요.</span></div>
<div class="pair" style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><span class="btn btn-secondary">내 휴대폰으로 링크 보내기</span><span class="btn btn-secondary">{ic("bm","ic ic16")}저장</span></div>'''
    states = sif("sFirst", first, True) + sif("sProg", prog) + sif("sDone", done) + sif("sDl", dl) + sif("sNo", no)
    kf = sif("isWebOk", keyf(KEYF_WEB), True) + sif("isDl", keyf(KEYF_DL)) + sif("sNo", keyf(KEYF_NO))
    return f'''<aside class="idp" aria-label="게임 정보와 플레이">
<div><h1>루프 디버거</h1><div class="by" style="margin-top:8px">{face("ㅍ","jjok","")}픽셀상점<a class="fl" href="#">팔로우</a></div></div>
<p class="pitch">모든 방이 하나의 함수인 프로그래밍 퍼즐. 루프를 고쳐 갇힌 로봇을 꺼내 주세요.</p>
<div class="gt"><span>퍼즐</span><span>프로그래밍</span><span>짧게</span><span>한 손</span></div>
{kf}
{states}
<div class="rate-line"><b>{ic("thumb","ic ic20")}214</b><span style="white-space:nowrap">명이 추천 · 리뷰 38개</span><span class="btn btn-secondary btn-sm" style="margin-left:auto">{ic("thumb","ic ic16")}추천하기</span></div>
</aside>'''

def g_tabs():
    tabs = [("tAbout", "goAbout", "소개", ""), ("tRev", "goRev", "리뷰", "38"), ("tLog", "goLog", "개발일지", "3"), ("tUpd", "goUpd", "업데이트", "2")]
    b = "".join(f'<button type="button" role="tab" aria-selected="{{{{ {v} }}}}" onClick="{{{{ {fn} }}}}">{n}{f"<span class=\"n\">{c}</span>" if c else ""}</button>' for v, fn, n, c in tabs)
    return f'<div class="ttabs"><div class="in" role="tablist" aria-label="게임 내용">{b}<span class="mini"><span class="art a-loop"></span>루프 디버거<span class="btn btn-primary btn-sm" data-play>{ic("play")}플레이</span></span></div></div>'

def info_rows(rows):
    return "<dl>" + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"

def t_about():
    play_web = info_rows([("실행", "브라우저에서 바로 · 설치 없음"), ("기기", "PC · 휴대폰(가로)"), ("조작", "키보드 또는 터치"), ("한 판", "5분 안팎 · 전체 40스테이지"), ("인원", "혼자"), ("언어", "한국어 · 영어"), ("저장", "브라우저 · 로그인하면 계정")])
    play_dl = info_rows([("실행", "설치형 · Windows · macOS"), ("사양", "Windows 10 이상 · 4GB RAM"), ("보안 검사", '<span class="okt">통과</span> · 11/24 · <a class="link" href="#" style="font-size:14px">리포트</a>'), ("한 판", "40분 · 저장 가능"), ("인원", "혼자"), ("언어", "한국어")])
    play_no = info_rows([("실행", "휴대폰 · 패드 전용"), ("조작", "터치"), ("한 판", "3분"), ("인원", "혼자"), ("언어", "한국어")])
    made = info_rows([("메이커", "픽셀상점 (1인)"), ("공개", "2026.10.02"), ("최근", "v1.2 · 11/23"), ("엔진", "Godot 4"), ("콘텐츠", "표시할 내용 없음")])
    return f'''<div class="ab2"><div>
<h2>소개</h2>
<p>모든 방이 하나의 함수인 프로그래밍 퍼즐. 손으로 쓴 코드 블록을 옮겨 루프를 고치면, 갇힌 로봇이 다음 방으로 넘어가요.</p>
<p>문법을 몰라도 괜찮아요. 블록은 그림으로 되어 있고, 틀리면 로봇이 어디서 멈췄는지 바로 보여 줘요. 진행은 브라우저에 저장되고, 로그인하면 다른 기기에서도 이어서 할 수 있어요.</p>
<div class="feat"><span>{ic("check")}40개 스테이지 · 스테이지당 3~8분</span><span>{ic("check")}힌트는 세 단계 — 답을 바로 알려 주지 않아요</span><span>{ic("check")}스테이지 편집기로 만든 문제를 링크로 공유</span></div>
</div>
<div class="infoc">
<div class="infog"><b>플레이</b>{sif("isWebOk", play_web, True)}{sif("isDl", play_dl)}{sif("sNo", play_no)}</div>
<div class="infog"><b>만든 정보</b>{made}</div>
<div class="mkc">{face("ㅍ","jjok","md")}<span><b>픽셀상점</b><span class="m">퍼즐만 만드는 1인 메이커 · 게임 4 · 개발일지 12</span></span><span class="btn btn-secondary btn-sm">메이커 페이지</span></div>
<a class="rptl" href="#">{ic("alert")}게임 신고 — 작동 안 함 · 저작권 · 설명과 다름</a>
</div></div>'''

REV2 = REVIEWS + [
    ("ㅈ", "ju", "주말개발자", True, "2.4시간", "편집기로 만든 문제를 친구한테 보냈더니 밤새 풀더라고요. 공유 링크가 진짜 좋아요.", None),
    ("ㅎ", "haneul", "하늘다람쥐", False, "35분", "소리가 조금 작아요. 효과음 크기를 따로 조절할 수 있으면 좋겠어요.", "v1.1 에서 효과음 볼륨을 따로 둘 수 있게 했어요!"),
    ("ㅂ", "bichwi", "비취색", True, "5.0시간", "40스테이지 다 깼어요. 마지막 다섯 개는 정말 머리 아팠지만 힌트 두 번째 단계에서 딱 풀리게 돼 있어서 좋았어요.", None),
]
def t_reviews():
    cards = ""
    for ch, col, who, yes, time, text, reply in REV2:
        verdict = f'<span class="yes">{ic("thumb","ic ic12")}추천함</span>' if yes else ""
        rep = f'<div class="reply">{face("ㅍ","jjok","xs")}<span><b>픽셀상점 · 메이커 답글</b>{reply}</span></div>' if reply else ""
        cards += f'<article class="rv"><div class="hd">{face(ch,col,"xs")}<b>{who}</b>{verdict}<span>· 플레이 {time}</span></div><p>{text}</p>{rep}<div class="foot"><span>11/2{len(who)}</span><span>도움이 됐어요 12</span><span>신고</span></div></article>'
    tags = "".join(f'<button class="chip">{t} <span class="c">{n}</span></button>' for t, n in [("짧고 굵음", 21), ("퍼즐 좋아하면", 18), ("한 손으로", 9), ("힌트가 친절해요", 8), ("튜토리얼이 길어요", 4)])
    return f'''<div class="rv2top"><span class="disp">214</span><span class="t"><b>명이 추천했어요 · 리뷰 38개</b><span class="m">플레이한 사람만 쓸 수 있어요 · 싫어요는 없어요</span></span><div class="r"><span class="btn btn-secondary">{ic("thumb","ic ic16")}추천하기</span><span class="btn btn-primary">{ic("pen","ic ic16")}리뷰 쓰기</span></div></div>
<div class="rv2bar">{tags}<span class="sort"><span class="on">도움 많은</span><span>최신</span><span>추천한 사람</span></span></div>
<div class="rv2list">{cards}</div>
<div style="display:flex;justify-content:center;margin-top:24px"><span class="btn btn-secondary">리뷰 32개 더 보기</span></div>'''

def t_logs():
    logs = [("a-loop", "회고", "첫 리뷰 38개를 읽고 바꾼 것들", "튜토리얼이 길다는 말이 가장 많았어요. 세 스테이지를 한 스테이지로 줄이면서 배운 것.", "3일 전", 24),
            ("a-grid", "기술", "Godot 4 웹 빌드를 12MB 에서 7MB 로", "텍스처 압축과 쓰지 않는 모듈을 빼는 것만으로 첫 로딩이 2초 빨라졌어요.", "2주 전", 17),
            ("a-tess", "개발 일지", "스테이지 편집기를 만든 이유", "다른 사람이 만든 문제를 풀어 보는 게 제일 재미있다는 걸 알게 됐어요.", "1달 전", 9)]
    rows = "".join(f'<a href="#"><span class="art {a}"></span><span><span class="k">{k}</span><b>{t}</b><p>{p}</p><span class="m">{d} · {ic("cmt")} {c}</span></span></a>' for a, k, t, p, d, c in logs)
    return f'<div class="logs2">{rows}</div><div style="display:flex;justify-content:center;margin-top:24px"><span class="btn btn-secondary" style="color:var(--make-strong)">메이커스에서 개발일지 모두 보기</span></div>'

def t_updates():
    rows = [("v1.2", "11/23", ["튜토리얼을 세 스테이지에서 한 스테이지로 줄였어요", "15스테이지 힌트 두 번째 단계를 고쳤어요", "휴대폰 가로 모드에서 블록 크기를 키웠어요"]), ("v1.1", "10/20", ["스테이지 편집기 공유 링크", "효과음 볼륨을 따로 조절할 수 있어요"])]
    r = "".join(f'<div class="up-row"><span class="v">{v}<span>{d}</span></span><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>' for v, d, xs in rows)
    return f'<div class="upd">{r}</div>'

def page_game(title, body, height, memo):
    props = '{"$preview":{"width":1440,"height":%d},"state":{"editor":"enum","default":"처음","options":["처음","진행 중","완료","다운로드","이 기기 불가"],"tsType":"string"},"tab":{"editor":"enum","default":"소개","options":["소개","리뷰","개발일지","업데이트"],"tsType":"string"},"theme":{"editor":"enum","default":"light","options":["light","dark"],"tsType":"string"},"showMemo":{"editor":"boolean","default":true,"tsType":"boolean"}}' % height
    html = _page_html(title, body, height, memo, props)
    old = "isWeb: s !== '다운로드', isWebOk: s !== '다운로드' && s !== '이 기기 불가', isDl: s === '다운로드' }};"
    assert old.replace("}};", "};") in html, "renderVals"
    new = ("isWeb: s !== '다운로드', isWebOk: s !== '다운로드' && s !== '이 기기 불가', isDl: s === '다운로드',\n"
           "      tAbout: t === '소개', tRev: t === '리뷰', tLog: t === '개발일지', tUpd: t === '업데이트',\n"
           "      goAbout: () => this.setState({ tab: '소개' }), goRev: () => this.setState({ tab: '리뷰' }), goLog: () => this.setState({ tab: '개발일지' }), goUpd: () => this.setState({ tab: '업데이트' }) };")
    html = html.replace(old.replace("}};", "};"), new, 1)
    html = html.replace("    const s = this.props.state ?? '처음';", "    const s = this.props.state ?? '처음';\n    const t = this.state.tab ?? (this.props.tab ?? '소개');", 1)
    html = html.replace("</style>", G_CSS + "\n</style>", 1)
    return mg._catify(html)

def page_a():
    panels = sif("tAbout", t_about(), True) + sif("tRev", t_reviews()) + sif("tLog", t_logs()) + sif("tUpd", t_updates())
    body = pg_header() + f'''<main class="wrap">
<div class="crumb2"><a href="#">게임</a>{ic("chev")}<a href="#">퍼즐</a></div>
<div class="g5">{g_media()}{g_panel()}</div></main>
{g_tabs()}
<div class="wrap"><section class="tpanel" role="tabpanel">{panels}</section>
<section class="simsec"><div class="sh">{EAR}<h2>비슷한 게임</h2><div class="r"><span class="arw" style="opacity:.4">{ic("chev","ic")}</span><span class="arw">{ic("chev","ic")}</span></div></div>
<div class="rail">{"".join(mg.game_card(a) for a in mg.NEWG)}</div></section></div>''' + footer()
    memo = "v3(11/27 재설계). 첫 화면 = 게임: 왼쪽 큰 미리보기(대표 그림 → 영상 → 이미지 순서 고정, 7개 이상이면 아래 줄을 가로로 넘김) · 오른쪽 정체와 행동(제목 · 메이커 · 한 줄 소개 · 태그 · 핵심 3칸 · 상태별 버튼 · 추천). 아래 탭은 내용을 나눠 한 번에 하나만 보여 줌 — 탭을 누르거나 Tweaks 의 tab 으로 바꿔 보세요. 자세한 정보는 ‘소개’ 탭 오른쪽에 플레이 / 만든 정보로 묶음. state 로 처음 · 진행 중 · 완료 · 다운로드 · 이 기기 불가."
    return page_game("게임 상세", body, 2700, memo)

if __name__ == "__main__":
    for name, fn in [("PG05-game.dc.html", page_a)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
