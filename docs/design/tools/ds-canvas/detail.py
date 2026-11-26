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

# ── PG05 게임 상세 v4 (2026-11-27 2차 피드백) ──────────────────────────────────
# 첫 화면 = 게임(자동으로 넘어가는 큰 미리보기) + 오른쪽 '할까 말까' 패널. 아래 탭은 내용 전환.
# 필드 정의: docs/product/game-metadata.md · 리뷰 설계: docs/design/research/04-reviews.md
MEDIA = [("cover", "a-loop"), ("video", "a-tess", "0:42"), ("video", "a-grid", "0:15"), ("img", "a-halcyon"), ("img", "a-paper"), ("img", "a-demon"), ("img", "a-refac"), ("img", "a-bazaar"), ("img", "a-solvent")]
SLOT = 4  # 초 — 이미지 한 장. 영상은 실제로는 끝까지 재생(시안에서는 같은 칸)
N = len(MEDIA); CYCLE = SLOT * N

def _kf():
    out = []
    for n in range(N):
        a, b = n * 100 / N, (n + 1) * 100 / N
        on = "opacity:1"; off = "opacity:0"
        if n == 0:
            out.append(f"@keyframes vl{n}{{0%,{b - .01:.2f}%{{{on}}}{b:.2f}%,100%{{{off}}}}}")
        else:
            out.append(f"@keyframes vl{n}{{0%,{a - .01:.2f}%{{{off}}}{a:.2f}%,{b - .01:.2f}%{{{on}}}{b:.2f}%,100%{{{off}}}}}")
        ring_on = "opacity:1;box-shadow:0 0 0 2px var(--accent)"; ring_off = "opacity:.6;box-shadow:none"
        if n == 0:
            out.append(f"@keyframes th{n}{{0%,{b - .01:.2f}%{{{ring_on}}}{b:.2f}%,100%{{{ring_off}}}}}")
        else:
            out.append(f"@keyframes th{n}{{0%,{a - .01:.2f}%{{{ring_off}}}{a:.2f}%,{b - .01:.2f}%{{{ring_on}}}{b:.2f}%,100%{{{ring_off}}}}}")
        out.append(f"@keyframes tp{n}{{0%,{a:.2f}%{{transform:scaleX(0)}}{b - .01:.2f}%{{transform:scaleX(1)}}{b:.2f}%,100%{{transform:scaleX(0)}}}}")
        out.append(f".viewer .ly:nth-child({n + 1}){{animation:vl{n} {CYCLE}s linear infinite}}")
        out.append(f".viewer .ly:nth-child({n + 1}) .vp i{{animation:tp{n} {CYCLE}s linear infinite}}")
        out.append(f".strip .it:nth-child({n + 1}) .art{{animation:th{n} {CYCLE}s linear infinite}}")
        out.append(f".strip .it:nth-child({n + 1}) .tp{{animation:tp{n} {CYCLE}s linear infinite}}")
    return "\n".join(out)

G_CSS = r'''
.g5{display:grid;grid-template-columns:minmax(0,1fr) 392px;gap:36px;margin-top:20px;align-items:start}
.viewer{position:relative}
.viewer .stage{position:relative;display:block;aspect-ratio:16/9;border-radius:var(--radius-xl);overflow:hidden;background:var(--sunken)}
.viewer .ly{position:absolute;inset:0;opacity:0}
.viewer .ly > i{position:absolute;inset:0}
.viewer .ly.v > i{animation:vidpan 8s linear infinite}
@keyframes vidpan{0%{transform:scale(1.04) translate(-2%,0)}50%{transform:scale(1.14) translate(3%,-2%)}100%{transform:scale(1.04) translate(-2%,0)}}
.viewer .lab{position:absolute;left:12px;bottom:12px;z-index:3;display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 10px;border-radius:999px;background:var(--scrim);color:#FFFFFF;font-size:12.5px;font-weight:700}
.viewer .lab .ic{width:12px;height:12px}
.viewer .cnt1{position:absolute;right:12px;bottom:12px;z-index:3;height:28px;padding:0 10px;border-radius:999px;background:var(--scrim);color:#FFFFFF;font-size:12.5px;font-weight:700;display:inline-flex;align-items:center}
.viewer .mute{position:absolute;right:12px;bottom:12px;z-index:3;width:32px;height:32px;border:0;border-radius:999px;background:var(--scrim);color:#FFFFFF;display:grid;place-items:center}
.viewer .vp{position:absolute;left:0;right:0;bottom:0;z-index:2;height:3px;background:rgb(255 255 255 / .25)}
.viewer .vp i{display:block;height:100%;background:#FFFFFF;transform-origin:left}
.viewer .badge,.viewer .plat{z-index:4}
.viewer .stage{overflow:visible}
.viewer .stage > .ly{border-radius:var(--radius-xl);overflow:hidden}
.viewer .plat{cursor:help}
.viewer .plat .tip{opacity:0;visibility:hidden;transform:translateY(-4px);transition:opacity var(--dur-fast) var(--ease-soft),transform var(--dur-fast) var(--ease-soft),visibility 0s linear var(--dur-fast);pointer-events:none}
.viewer .plat:hover .tip,.viewer .plat:focus-visible .tip{opacity:1;visibility:visible;transform:none;transition-delay:120ms,120ms,0s}
.viewer .plat{height:28px;padding:0 10px;font-size:12.5px;gap:7px;right:12px;top:12px}
.viewer .badge{left:12px;top:12px}
.viewer:hover .ly,.viewer:hover .ly *,.viewer:hover .strip *{animation-play-state:paused}
.strip-w{position:relative;margin-top:10px}
.strip{display:flex;gap:8px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding:3px;margin:-3px}
.strip::-webkit-scrollbar{display:none}
.strip .it{all:unset;box-sizing:border-box;position:relative;flex:0 0 calc((100% - 40px) / 6);scroll-snap-align:start;cursor:pointer;border-radius:9px}
.strip .it:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.strip .it .art{display:block;border-radius:9px;opacity:.6}
.strip .it .tag2{position:absolute;left:5px;bottom:7px;z-index:2;height:18px;padding:0 6px;border-radius:5px;background:var(--scrim);color:#FFFFFF;font-size:11px;font-weight:800;display:inline-flex;align-items:center;gap:3px}
.strip .it .tag2 .ic{width:9px;height:9px}
.strip .it .tp{position:absolute;left:6px;right:6px;bottom:3px;z-index:2;height:2px;border-radius:2px;background:#FFFFFF;transform:scaleX(0);transform-origin:left}
.strip-w .fade{position:absolute;right:-1px;top:0;bottom:0;width:72px;background:linear-gradient(90deg,transparent,var(--bg) 75%);pointer-events:none}
.strip-w .nav{all:unset;box-sizing:border-box;position:absolute;right:0;top:50%;transform:translateY(-50%);z-index:3;width:32px;height:32px;border-radius:999px;background:var(--bg);box-shadow:var(--shadow-pop);display:grid;place-items:center;color:var(--ink-1);cursor:pointer}
@media (prefers-reduced-motion:reduce){.viewer .ly,.viewer .ly *,.strip *{animation:none!important}.viewer .ly:first-child{opacity:1}}
.idp{display:flex;flex-direction:column;gap:18px}
.idp h1{margin:0;font-size:32px;line-height:1.2;font-weight:800;letter-spacing:-.025em}
.idp .pitch{margin:8px 0 0;font-size:15.5px;line-height:1.6;color:var(--ink-2)}
.idp .gt{display:flex;flex-wrap:wrap;gap:6px}
.idp .gt span{height:26px;padding:0 10px;border-radius:7px;background:var(--sunken);font-size:13px;font-weight:700;color:var(--ink-2);display:inline-flex;align-items:center}
.keyf{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border-radius:var(--radius-md);background:var(--sunken)}
.keyf > span{display:flex;flex-direction:column;gap:5px;padding:12px 10px;font-size:12px;color:var(--ink-3);font-weight:600}
.keyf > span + span{box-shadow:inset 1px 0 0 var(--line)}
.keyf > span b{font-size:14px;line-height:1.3;color:var(--ink-1);font-weight:800}
.recl{display:flex;align-items:center;gap:10px;padding-top:16px;border-top:1px solid var(--line)}
.recl .n{display:inline-flex;align-items:center;gap:6px;font-size:20px;font-weight:800}
.recl .n .ic{color:var(--accent-text)}
.recl .t{font-size:14px;color:var(--ink-2);white-space:nowrap}
.recl .btn{margin-left:auto}
.lastp{margin:2px 0 0;font-size:13px;color:var(--ink-3);text-align:center}
.recl-note{margin:-8px 0 0;font-size:12.5px;color:var(--ink-3);text-align:right}
.btn.pressed{background:var(--accent-tint);color:var(--accent-text);box-shadow:inset 0 0 0 1.5px var(--accent)}
.btn.locked{opacity:.5;cursor:not-allowed}
.ttabs{position:sticky;top:68px;z-index:10;margin-top:48px;background:color-mix(in srgb,var(--bg) 94%,transparent);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.ttabs .in{width:1200px;margin:0 auto;display:flex;align-items:center;gap:4px;height:56px}
.ttabs button{all:unset;box-sizing:border-box;height:56px;padding:0 16px;font-size:16px;font-weight:700;color:var(--ink-3);box-shadow:inset 0 -2px 0 transparent;cursor:pointer;display:inline-flex;align-items:center}
.ttabs button:hover{color:var(--ink-1)}
.ttabs button:focus-visible{outline:2px solid var(--accent);outline-offset:-4px}
.ttabs button[aria-selected="true"]{color:var(--ink-1);box-shadow:inset 0 -2px 0 var(--ink-1)}
.ttabs button .n{margin-left:5px;font-size:14px;color:var(--ink-3);font-weight:600}
.tpanel{margin-top:36px;min-height:620px}
.two{display:grid;grid-template-columns:minmax(0,1fr) 392px;gap:56px;align-items:start}
.two > aside{position:sticky;top:148px;display:flex;flex-direction:column;gap:16px}
.ab-txt{max-width:720px}
.ab-txt h2{margin:0 0 14px;font-size:20px;font-weight:800}
.ab-txt p{margin:0 0 16px;font-size:16px;line-height:1.8}
.ab-txt ul{margin:20px 0 0;padding:0;list-style:none;display:flex;flex-direction:column;gap:10px}
.ab-txt li{display:flex;gap:10px;font-size:15.5px;line-height:1.6}
.ab-txt li .ic{flex:none;margin-top:5px;color:var(--accent-text)}
.mkc{display:grid;grid-template-columns:auto minmax(0,1fr);gap:12px;align-items:center;padding:16px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line)}
.mkc b{display:block;font-size:16px}
.mkc .m{display:block;margin-top:2px;font-size:13px}
.mkc .acts{grid-column:1 / -1;display:grid;grid-template-columns:1fr 1fr;gap:8px}
.infobox{padding:16px 18px;border-radius:var(--radius-lg);background:var(--sunken)}
.infobox h3{margin:0 0 6px;font-size:12.5px;font-weight:800;color:var(--ink-3);letter-spacing:.02em}
.infobox h3 + dl{margin-top:0}
.infobox dl{margin:0}
.infobox dl > div{display:grid;grid-template-columns:76px minmax(0,1fr);gap:12px;padding:6px 0;font-size:14px;line-height:1.5}
.infobox dt{color:var(--ink-3);font-weight:600}
.infobox dd{margin:0;color:var(--ink-1);font-weight:600}
.infobox .sep{height:1px;background:var(--line);margin:12px 0}
.infobox .okt{color:var(--ok-text);font-weight:800}
.rpt{display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.rpt .m{font-size:12.5px}
.rvsum{display:grid;grid-template-columns:1fr 1fr;border-radius:var(--radius-lg);background:var(--sunken)}
.rvsum > div{padding:16px 18px;display:flex;flex-direction:column;gap:2px}
.rvsum > div + div{box-shadow:inset 1px 0 0 var(--line)}
.rvsum b{font-size:30px;line-height:1.1;font-weight:800}
.rvsum span{font-size:13px;color:var(--ink-3);font-weight:600}
.rvacts{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.rvacts.one{grid-template-columns:1fr}
.rvf b{display:block;margin-bottom:8px;font-size:13px;font-weight:800;color:var(--ink-3)}
.rvf .chips .chip{height:32px;font-size:13px;padding:0 12px}
.rvnote{margin:0;font-size:12.5px;line-height:1.6;color:var(--ink-3)}
.rlist{display:flex;flex-direction:column;max-width:720px}
.ri{display:flex;flex-direction:column;gap:10px;padding:28px 0;border-top:1px solid var(--line)}
.ri:first-child{border-top:0;padding-top:0}
.ri-h{position:relative;display:flex;align-items:center;gap:12px}
.ri-h .who b{display:block;font-size:15.5px;font-weight:800}
.ri-h .who .m{display:flex;align-items:center;gap:6px;margin-top:1px;font-size:13px}
.ri-h .rec{display:inline-flex;align-items:center;gap:4px;color:var(--accent-text);font-weight:800}
.ri-h .rec .ic{width:12px;height:12px}
.ri-more{all:unset;box-sizing:border-box;margin-left:auto;width:32px;height:32px;border-radius:8px;display:grid;place-items:center;color:var(--ink-3);cursor:pointer;font-size:18px;line-height:1;letter-spacing:1px}
.ri-more:hover{background:var(--sunken);color:var(--ink-1)}
.ri-menu{position:absolute;right:0;top:38px;z-index:5;width:168px;padding:6px;border-radius:var(--radius-lg);background:var(--bg);box-shadow:var(--shadow-pop),0 0 0 1px var(--line);display:flex;flex-direction:column}
[data-theme="dark"] .ri-menu{background:var(--raised)}
.ri-menu span{display:flex;align-items:center;gap:8px;height:36px;padding:0 10px;border-radius:8px;font-size:14px;font-weight:600}
.ri-menu span:hover{background:var(--sunken)}
.ri-menu .danger{color:var(--danger-text)}
.ri-ctx{margin:0;display:flex;flex-wrap:wrap;gap:4px 10px;font-size:13px;color:var(--ink-3)}
.ri-ctx b{color:var(--ink-2);font-weight:700}
.ri-tags{display:flex;flex-wrap:wrap;gap:6px}
.ri-tags span{height:24px;padding:0 9px;border-radius:6px;background:var(--sunken);font-size:12.5px;font-weight:700;color:var(--ink-2);display:inline-flex;align-items:center}
.ri-body{margin:0;font-size:16px;line-height:1.75;color:var(--ink-1)}
.ri-body.clamp{display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.ri-moretxt{align-self:flex-start;font-size:14px;font-weight:700;color:var(--ink-2);text-decoration:underline;text-underline-offset:3px}
.ri-act{display:flex;align-items:center;gap:10px;margin-top:2px}
.help{all:unset;box-sizing:border-box;display:inline-flex;align-items:center;gap:6px;height:34px;padding:0 12px;border-radius:999px;box-shadow:inset 0 0 0 1px var(--line);font-size:13.5px;font-weight:700;color:var(--ink-2);cursor:pointer}
.help:hover{background:var(--sunken)}
.help b{color:var(--ink-1)}
.help.on{background:var(--accent-tint);color:var(--accent-text);box-shadow:inset 0 0 0 1.5px var(--accent)}
.help.on b{color:var(--accent-text)}
.help .ic{width:14px;height:14px}
.ri-reply{display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px;margin:6px 0 0 52px}
.ri-reply .jf{width:28px;height:28px;font-size:11px}
.ri-reply .hd{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--ink-3)}
.ri-reply .hd b{color:var(--ink-1);font-size:14px;font-weight:800}
.ri-reply .mk{height:20px;padding:0 7px;border-radius:999px;background:var(--accent-tint);color:var(--accent-text);font-size:11.5px;font-weight:800;display:inline-flex;align-items:center}
.ri-reply p{margin:4px 0 0;font-size:15px;line-height:1.7;color:var(--ink-1)}
.logs2{display:flex;flex-direction:column;max-width:880px}
.logs2 a{display:grid;grid-template-columns:220px minmax(0,1fr);gap:22px;padding:20px 0;border-top:1px solid var(--line);align-items:center}
.logs2 a:first-child{border-top:0;padding-top:0}
.logs2 .art{border-radius:var(--radius-md)}
.logs2 .k{font-size:12.5px;font-weight:800;color:var(--make-strong)}
.logs2 b{display:block;margin-top:4px;font-size:18px;line-height:1.4}
.logs2 p{margin:6px 0 0;font-size:14.5px;line-height:1.6;color:var(--ink-2)}
.logs2 .m{display:flex;gap:10px;margin-top:8px;font-size:13px}
.seg{display:inline-flex;padding:3px;border-radius:999px;background:var(--bg);box-shadow:inset 0 0 0 1px var(--line-strong)}
.seg span{height:32px;padding:0 12px;border-radius:999px;display:inline-flex;align-items:center;font-size:13px;font-weight:700;color:var(--ink-3)}
.seg span.on{background:var(--ink-1);color:var(--bg)}
.simsec{margin-top:72px;padding-top:40px;border-top:1px solid var(--line)}
''' + _kf()

def g_media():
    plat_web = f'<span class="plat" tabindex="0" aria-label="브라우저에서 바로 플레이, 휴대폰 가능">{ic("web","ic ic12")}브라우저 {ic("phone","ic ic12")}휴대폰<span class="tip" role="tooltip"><span>{ic("web")}브라우저에서 바로 플레이 · 설치 없음</span><span>{ic("phone")}휴대폰에서도 가능(가로)</span></span></span>'
    plat_dl = f'<span class="plat" tabindex="0" aria-label="설치형, 보안 검사 통과">{ic("dl","ic ic12")}설치형 <svg class="ic ic12 ok"><use href="#i-shield"></use></svg>검사 통과<span class="tip" role="tooltip"><span>{ic("dl")}설치형 · 내려받아 설치</span><span class="ok">{ic("shield")}보안 검사 통과 · 11/24</span></span></span>'
    layers, items = "", ""
    img_no = 0
    for i, m in enumerate(MEDIA):
        kind, art = m[0], m[1]
        if kind == "cover":
            layers += f'<span class="ly"><i class="{art}"></i><span class="cnt1">대표 · 1 / {N}</span></span>'
            items += f'<button class="it" aria-label="대표 그림"><span class="art {art}"></span><span class="tag2">대표</span><span class="tp"></span></button>'
        elif kind == "video":
            layers += f'<span class="ly v"><i class="{art}"></i><span class="lab">{ic("play")}영상 · {m[2]} · 소리 꺼짐</span><button class="mute" aria-label="소리 켜기"><svg class="ic" viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 6h2.5L8.5 3v10L5 10H2.5z"></path><path d="M11 6l3.5 4M14.5 6 11 10"></path></svg></button><span class="vp"><i></i></span></span>'
            items += f'<button class="it" aria-label="영상 {m[2]}"><span class="art {art}"></span><span class="tag2">{ic("play")}{m[2]}</span><span class="tp"></span></button>'
        else:
            img_no += 1
            layers += f'<span class="ly"><i class="{art}"></i><span class="cnt1">{i + 1} / {N}</span></span>'
            items += f'<button class="it" aria-label="이미지 {img_no}"><span class="art {art}"></span><span class="tp"></span></button>'
    return f'''<div class="viewer" aria-roledescription="미리보기" aria-label="루프 디버거 미리보기 — {SLOT}초마다 넘어감, 마우스를 올리면 멈춤">
<span class="stage">{layers}<span class="badge">{ic("crown","ic ic12")}이번 주 PICK</span>{sif("isWeb", plat_web, True)}{sif("isDl", plat_dl)}</span>
<div class="strip-w"><div class="strip" role="list">{items}</div><span class="fade"></span><button class="nav" aria-label="미리보기 더 보기">{ic("chev")}</button></div></div>'''

KEYF_WEB = [("실행", "바로 플레이"), ("기기", "PC · 휴대폰"), ("한 판", "5분 이하"), ("인원", "혼자")]
KEYF_DL = [("실행", "설치형"), ("기기", "PC"), ("한 판", "1시간 이하"), ("인원", "혼자")]
KEYF_NO = [("실행", "바로 플레이"), ("기기", "휴대폰 · 패드"), ("한 판", "5분 이하"), ("인원", "혼자")]
def keyf(rows):
    return '<div class="keyf">' + "".join(f'<span>{k}<b>{v}</b></span>' for k, v in rows) + "</div>"

def rec_line():
    head = f'<span class="n">{ic("thumb","ic ic20")}214</span><span class="t">명이 추천 · 리뷰 38개</span>'
    guest = f'<div class="recl">{head}<span class="btn btn-secondary btn-sm">로그인하고 추천</span></div>'
    can = f'<div class="recl">{head}<span class="btn btn-secondary btn-sm">{ic("thumb","ic ic16")}추천하기</span></div>'
    return sif("guest", guest) + sif("signedIn", can, True)

def g_panel():
    first = f'''<div class="cta"><span class="btn btn-primary big" data-play>{ic("play","ic ic16")}지금 플레이</span><div class="pair"><span class="btn btn-secondary">{ic("bm","ic ic16")}즐겨찾기</span><span class="btn btn-secondary">{ic("share","ic ic16")}친구에게 보내기</span></div></div>'''
    pair = f'<div class="pair"><span class="btn btn-secondary">{ic("bm","ic ic16")}즐겨찾기</span><span class="btn btn-secondary">{ic("share","ic ic16")}친구에게 보내기</span></div>'
    played = f'''<div class="cta"><span class="btn btn-primary big" data-play>{ic("play","ic ic16")}플레이</span><p class="lastp">어제 마지막으로 함 · 모두 1시간 12분</p>{pair}</div>'''
    prog = f'''<div class="cta"><span class="btn btn-primary big" data-play>{ic("play","ic ic16")}이어하기</span>
<div class="prog-box"><div class="row"><span><b>진행 45%</b></span><span>어제 · 모두 1시간 12분</span></div><div class="bar"><i style="width:45%"></i></div><div class="row"><span class="m" style="font-size:12px">이 게임이 진행도를 알려 줘요(SDK)</span></div></div>{pair}</div>'''
    dl = f'''<div class="cta"><div class="files"><div class="file on">{ic("pc")}<span><b>Windows</b><span class="m">v1.2 · 312MB · .exe</span></span>{ic("check","ic ic16")}</div><div class="file">{ic("pc")}<span><b>macOS</b><span class="m">v1.2 · 298MB · .dmg · Apple 서명 없음</span></span><span></span></div></div>
<span class="btn btn-primary big">{ic("dl","ic ic16")}다운로드 · Windows</span>
<div class="pair" style="display:grid;grid-template-columns:1fr;gap:8px"><span class="btn btn-secondary">{ic("bm","ic ic16")}즐겨찾기</span></div>
<div class="scan">{ic("shield")}<span>보안 검사 통과 · 11/24</span><a href="#">리포트</a></div></div>'''
    no = f'''<div class="notice"><span class="qr" aria-hidden="true"></span><span><b>휴대폰에서 열어 주세요</b>터치 전용이라 PC 에서는 할 수 없어요. QR 을 찍거나 링크를 보내 보세요.</span></div>
<div class="pair" style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><span class="btn btn-secondary">내 휴대폰으로 링크 보내기</span><span class="btn btn-secondary">{ic("bm","ic ic16")}즐겨찾기</span></div>'''
    states = sif("sFirst", first, True) + sif("sPlayed", played) + sif("sProg", prog) + sif("sDl", dl) + sif("sNo", no)
    kf = sif("isWebOk", keyf(KEYF_WEB), True) + sif("isDl", keyf(KEYF_DL)) + sif("sNo", keyf(KEYF_NO))
    return f'''<aside class="idp" aria-label="게임 요약과 플레이">
<div><h1>루프 디버거</h1><p class="pitch">모든 방이 하나의 함수인 프로그래밍 퍼즐. 루프를 고쳐 갇힌 로봇을 꺼내 주세요.</p></div>
<div class="gt"><span>퍼즐</span><span>프로그래밍</span><span>짧게</span></div>
{kf}
{states}
{rec_line()}
</aside>'''

def g_tabs():
    tabs = [("tAbout", "goAbout", "소개", ""), ("tRev", "goRev", "리뷰", "38"), ("tLog", "goLog", "개발일지", "3"), ("tUpd", "goUpd", "업데이트", "2")]
    b = "".join(f'<button type="button" role="tab" aria-selected="{{{{ {v} }}}}" onClick="{{{{ {fn} }}}}">{n}{f"<span class=\"n\">{c}</span>" if c else ""}</button>' for v, fn, n, c in tabs)
    return f'<div class="ttabs"><div class="in" role="tablist" aria-label="게임 내용">{b}</div></div>'

def dl_rows(rows):
    return "<dl>" + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"

def maker_card():
    return f'''<div class="mkc">{face("ㅍ","jjok","lg")}<span><b>픽셀상점</b><span class="m">1인 메이커 · 게임 4 · 팔로워 312</span></span>
<div class="acts"><span class="btn btn-primary btn-sm">팔로우</span><span class="btn btn-secondary btn-sm">메이커 페이지</span></div></div>'''

def t_about():
    web = dl_rows([("실행", "브라우저에서 바로 · 설치 없음"), ("기기", "PC · 휴대폰(가로)"), ("조작", "키보드 · 터치"), ("한 판", "5분 이하"), ("인원", "혼자"), ("언어", "한국어 · 영어"), ("이용 주의", "없음")])
    dlr = dl_rows([("실행", "설치형 · 다운로드"), ("기기", "Windows 10+ · macOS 12+"), ("사양", "RAM 4GB · 내장 그래픽"), ("조작", "키보드 · 마우스"), ("한 판", "1시간 이하"), ("인원", "혼자"), ("언어", "한국어"), ("보안 검사", '<span class="okt">통과</span> · 11/24 · <a class="link" href="#" style="font-size:14px">리포트</a>')])
    no = dl_rows([("실행", "브라우저에서 바로"), ("기기", "휴대폰 · 패드만"), ("조작", "터치"), ("한 판", "5분 이하"), ("인원", "혼자"), ("언어", "한국어"), ("이용 주의", "깜빡이는 화면")])
    info = dl_rows([("공개", "2026년 10월 2일"), ("업데이트", "v1.2 · 11월 23일")])
    return f'''<div class="two"><div class="ab-txt">
<h2>소개</h2>
<p>모든 방이 하나의 함수인 프로그래밍 퍼즐. 손으로 쓴 코드 블록을 옮겨 루프를 고치면, 갇힌 로봇이 다음 방으로 넘어가요.</p>
<p>문법을 몰라도 괜찮아요. 블록은 그림으로 되어 있고, 틀리면 로봇이 어디서 멈췄는지 바로 보여 줘요.</p>
<ul><li>{ic("check")}<span>스테이지 하나가 짧아서 출퇴근길에 한 판씩 하기 좋아요</span></li><li>{ic("check")}<span>힌트는 세 단계 — 답을 바로 알려 주지 않아요</span></li><li>{ic("check")}<span>직접 만든 문제를 링크로 친구에게 보낼 수 있어요</span></li></ul>
</div>
<aside>{maker_card()}
<div class="infobox"><h3>플레이</h3>{sif("isWebOk", web, True)}{sif("isDl", dlr)}{sif("sNo", no)}<div class="sep"></div><h3>정보</h3>{info}</div>
<div class="rpt"><span class="btn btn-secondary btn-sm">{ic("flag","ic ic16")}문제 알리기</span><span class="m">실행이 안 돼요 · 버그 · 설명과 달라요 · 부적절한 내용</span></div>
</aside></div>'''

# (얼굴, 색, 이름, 쓴 리뷰 수, 추천함, 지금 플레이, 쓸 때 플레이, 버전, 날짜, 고른 말, 본문, 도움, 내가 누름, 답글(본문, 날짜, 고침 표시))
RV = [
    ("ㅅ", "hong", "새벽코딩", 12, True, "3.2시간", "1.1시간", "v1.1", "11월 21일", ("짧고 굵음", "힌트가 친절해요"),
     "회사에서 하는 일이랑 너무 똑같아서 웃겼어요. 그런데 이건 고치면 칭찬을 해 주네요. 15스테이지부터 난이도가 확 오르는데, 힌트가 세 단계라 답을 보지 않고도 풀 수 있게 잡아 줘요.", 41, True,
     ("15스테이지 구간에 연습 스테이지를 하나 더 넣었어요. 고마워요!", "11월 22일", "v1.2 에서 고침")),
    ("ㅁ", "bora", "모래시계", 3, False, "1.1시간", "1.1시간", "v1.1", "11월 20일", ("튜토리얼이 길어요",),
     "튜토리얼이 너무 길어요. 처음 세 스테이지는 이미 아는 내용이라 건너뛰기가 있으면 좋겠어요.", 17, False,
     ("튜토리얼을 한 스테이지로 줄였어요. 다시 한 번 봐 주세요!", "11월 23일", "v1.2 에서 고침")),
    ("ㅂ", "bichwi", "비취색", 28, True, "5.0시간", "5.0시간", "v1.2", "11월 25일", ("퍼즐 좋아하면",),
     "마지막까지 다 해 봤어요. 후반 다섯 개는 정말 머리가 아팠지만, 힌트 두 번째 단계에서 딱 풀리게 돼 있어서 억지스럽지 않았어요. 편집기로 만든 문제를 친구한테 보냈더니 밤새 풀더라고요. 공유 링크 덕분에 같이 노는 맛이 생겼어요. 다음 게임도 이런 식이면 바로 할 것 같아요.", 9, False, None),
    ("ㄱ", "gyul", "귤껍질", 1, True, "", "", "v1.2", "11월 26일", ("한 손으로", "짧고 굵음"),
     "출퇴근길에 한 판씩 하기 딱 좋아요. 휴대폰 가로 모드에서도 블록이 작지 않아요.", 2, False, None),
]

def review_item(r, i):
    ch, col, who, nrev, rec, now, at, ver, date, tags, body, helpn, mine, reply = r
    recb = f'<span class="rec">{ic("thumb")}추천함</span>' if rec else ""
    menu = f'<span class="ri-menu" role="menu"><span role="menuitem">링크 복사</span><span role="menuitem" class="danger">{ic("alert")}리뷰 신고</span></span>' if i == 1 else ""
    play = (f'<b>플레이 {now}</b>' + (f'<span>(쓸 때 {at})</span>' if at != now else "")) if now else '<b>플레이 기록 없음</b>'
    ctx = play + f'<span>· {ver} 에서 씀</span><span>· {date}</span>'
    tg = "".join(f"<span>{t}</span>" for t in tags)
    long = len(body) > 150
    more = '<a class="ri-moretxt" href="#">더 보기</a>' if long else ""
    rep = ""
    if reply:
        rep = f'<div class="ri-reply">{face("ㅍ","jjok","sm")}<div><div class="hd"><b>픽셀상점</b><span class="mk">메이커</span><span>{reply[1]}</span><span>· {reply[2]}</span></div><p>{reply[0]}</p></div></div>'
    return f'''<article class="ri"><header class="ri-h">{face(ch, col, "md")}<span class="who"><b>{who}</b><span class="m">리뷰 {nrev}개{" · " if rec else ""}{recb}</span></span><button class="ri-more" aria-label="{who} 리뷰 메뉴" aria-haspopup="menu">···</button>{menu}</header>
<p class="ri-ctx">{ctx}</p>
<div class="ri-tags">{tg}</div>
<p class="ri-body{" clamp" if long else ""}">{body}</p>{more}
<div class="ri-act"><button class="help{" on" if mine else ""}" aria-pressed="{"true" if mine else "false"}">{ic("thumb")}도움이 됐어요 <b>{helpn + (0 if not mine else 0)}</b></button></div>
{rep}</article>'''

def t_reviews():
    items = "".join(review_item(r, i) for i, r in enumerate(RV))
    tags = "".join(f'<button class="chip">{t} <span class="c">{n}</span></button>' for t, n in [("짧고 굵음", 21), ("퍼즐 좋아하면", 18), ("한 손으로", 9), ("힌트가 친절해요", 8), ("튜토리얼이 길어요", 4)])
    acts_guest = f'<div class="rvacts one"><span class="btn btn-primary">로그인하고 추천 · 리뷰 쓰기</span></div>'
    acts_can = f'<div class="rvacts"><span class="btn btn-secondary">{ic("thumb","ic ic16")}추천하기</span><span class="btn btn-primary">{ic("pen","ic ic16")}리뷰 쓰기</span></div>'
    acts = sif("guest", acts_guest) + sif("signedIn", acts_can, True)
    side = f'''<aside><div class="rvsum"><div><b>214</b><span>명이 추천</span></div><div><b>38</b><span>개 리뷰</span></div></div>
{acts}
<div class="rvf"><b>자주 고른 말로 보기</b><div class="chips">{tags}</div></div>
<div class="rvf"><b>정렬</b><div class="seg"><span class="on">도움 많은</span><span>최신</span><span>오래 한 사람</span></div></div>
<p class="rvnote">로그인하면 누구나 추천하고 리뷰를 쓸 수 있어요. 싫어요는 없어요 — 아쉬운 점은 리뷰로 알려 주세요.</p></aside>'''
    return f'''<div class="two"><div class="rlist">{items}<div style="padding-top:8px"><span class="btn btn-secondary">리뷰 34개 더 보기</span></div></div>{side}</div>'''

def t_logs():
    logs = [("a-loop", "회고", "첫 리뷰 38개를 읽고 바꾼 것들", "튜토리얼이 길다는 말이 가장 많았어요. 세 스테이지를 한 스테이지로 줄이면서 배운 것.", "3일 전", 24),
            ("a-grid", "기술", "웹 빌드를 12MB 에서 7MB 로", "텍스처 압축과 쓰지 않는 모듈을 빼는 것만으로 첫 로딩이 2초 빨라졌어요.", "2주 전", 17),
            ("a-tess", "개발 일지", "문제 편집기를 만든 이유", "다른 사람이 만든 문제를 풀어 보는 게 제일 재미있다는 걸 알게 됐어요.", "1달 전", 9)]
    rows = "".join(f'<a href="#"><span class="art {a}"></span><span><span class="k">{k}</span><b>{t}</b><p>{p}</p><span class="m">{d} · {ic("cmt")} {c}</span></span></a>' for a, k, t, p, d, c in logs)
    return f'<div class="logs2">{rows}</div><div style="margin-top:24px"><span class="btn btn-secondary" style="color:var(--make-strong)">메이커스에서 개발일지 모두 보기</span></div>'

def t_updates():
    rows = [("v1.2", "11/23", ["튜토리얼을 세 스테이지에서 한 스테이지로 줄였어요", "15스테이지 앞에 연습 스테이지를 넣었어요", "휴대폰 가로 모드에서 블록 크기를 키웠어요"]), ("v1.1", "10/20", ["문제 편집기 공유 링크", "효과음 볼륨을 따로 조절할 수 있어요"])]
    r = "".join(f'<div class="up-row"><span class="v">{v}<span>{d}</span></span><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>' for v, d, xs in rows)
    return f'<div class="upd" style="max-width:880px">{r}</div>'

def page_game(title, body, height, memo):
    props = '{"$preview":{"width":1440,"height":%d},"state":{"editor":"enum","default":"처음","options":["처음","해 본 적 있음","진행 중 (SDK)","다운로드","이 기기 불가"],"tsType":"string"},"tab":{"editor":"enum","default":"소개","options":["소개","리뷰","개발일지","업데이트"],"tsType":"string"},"login":{"editor":"boolean","default":true,"tsType":"boolean"},"theme":{"editor":"enum","default":"light","options":["light","dark"],"tsType":"string"},"showMemo":{"editor":"boolean","default":true,"tsType":"boolean"}}' % height
    html = _page_html(title, body, height, memo, props).replace("sProg: s === '진행 중', sDone: s === '완료', ", "", 1)
    old = "isWeb: s !== '다운로드', isWebOk: s !== '다운로드' && s !== '이 기기 불가', isDl: s === '다운로드' };"
    assert old in html, "renderVals"
    new = ("isWeb: s !== '다운로드', isWebOk: s !== '다운로드' && s !== '이 기기 불가', isDl: s === '다운로드',\n"
           "      signedIn: li, guest: !li, sPlayed: s === '해 본 적 있음', sProg: s === '진행 중 (SDK)',\n"
           "      tAbout: t === '소개', tRev: t === '리뷰', tLog: t === '개발일지', tUpd: t === '업데이트',\n"
           "      goAbout: () => this.setState({ tab: '소개' }), goRev: () => this.setState({ tab: '리뷰' }), goLog: () => this.setState({ tab: '개발일지' }), goUpd: () => this.setState({ tab: '업데이트' }) };")
    html = html.replace(old, new, 1)
    html = html.replace("    const s = this.props.state ?? '처음';", "    const s = this.props.state ?? '처음';\n    const t = this.state.tab ?? (this.props.tab ?? '소개');\n    const li = this.props.login ?? true;\n    const played = s === '진행 중' || s === '완료';", 1)
    html = html.replace("</style>", G_CSS + "\n</style>", 1)
    return mg._catify(html)

def page_a():
    panels = sif("tAbout", t_about(), True) + sif("tRev", t_reviews()) + sif("tLog", t_logs()) + sif("tUpd", t_updates())
    head = sif("signedIn", pg_header(True), True) + sif("guest", pg_header(False))
    body = head + f'''<main class="wrap">
<div class="crumb2"><a href="#">게임</a>{ic("chev")}<a href="#">퍼즐</a></div>
<div class="g5">{g_media()}{g_panel()}</div></main>
{g_tabs()}
<div class="wrap"><section class="tpanel" role="tabpanel">{panels}</section>
<section class="simsec"><div class="sh">{EAR}<h2>비슷한 게임</h2><div class="r"><span class="arw" style="opacity:.4"><svg class="ic" style="transform:rotate(180deg)"><use href="#i-chev"></use></svg></span><span class="arw">{ic("chev","ic")}</span></div></div>
<div class="rail">{"".join(mg.game_card(a) for a in mg.NEWG)}</div></section></div>''' + footer()
    memo = ("v5(11/27 3차). state = 처음 / 해 본 적 있음(플랫폼이 아는 것: 마지막 날 · 시간 — 버튼은 그냥 ‘플레이’, 저장은 게임 몫) / 진행 중 (SDK — 게임이 알려 줄 때만 ‘이어하기’) / 다운로드 / 이 기기 불가. ‘다시 하기 · 완료’ 는 없음(엔딩을 플랫폼이 모름). 미리보기는 대표 → 영상 → 이미지 순서로 " + str(SLOT) + "초마다 자동으로 넘어가고(영상은 소리 끈 채 자동 재생 · 실제로는 끝까지 본 뒤 다음), 마우스를 올리면 멈춤, 썸네일을 누르면 그 항목으로 · 자동 넘김 끝. 오른쪽 = 제목 · 한 줄 소개 · 태그 · 핵심 4칸 · 상태별 버튼 · 추천. "
            "추천 · 리뷰는 로그인한 사람 누구나(Tweaks login 을 끄면 게스트). 탭은 내용 전환. 소개 탭 오른쪽 = 메이커 카드 → 플레이 · 정보 → 문제 알리기(실행 안 됨 · 버그 → 메이커 피드백함, 부적절 · 저작권 → 운영자). 리뷰 = 한 열 목록 + 오른쪽 요약 · 거르기(설계: docs/design/research/04-reviews.md).")
    return page_game("게임 상세", body, 2700, memo)

if __name__ == "__main__":
    for name, fn in [("PG05-game.dc.html", page_a)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
