# 전체 게임(PG-CAT) · 공개 프로필(PG-PROFILE) · 알림(SH-NOTI) · 설정(SH-SETTINGS) 시안 생성기
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + [OUT]
import importlib.util
spec = importlib.util.spec_from_file_location("detail", os.path.join(HERE, "detail.py"))
dt = importlib.util.module_from_spec(spec); spec.loader.exec_module(dt)
mg = dt.mg
ic, face, logo, EAR, status = mg.ic, mg.face, mg.logo, mg.EAR, mg.status

def pgh(active="게임", signed=True):
    h = dt.pg_header(signed)
    nav = "".join(f'<a href="#"{" aria-current=\"page\"" if n == active else ""}>{n}</a>' for n in ["홈", "게임", "랭킹", "같이", "잼"])
    return re.sub(r'<nav class="gnb">.*?</nav>', f'<nav class="gnb">{nav}</nav>', h, count=1, flags=re.S)

CSS = r'''
.pg-title{display:flex;align-items:flex-end;gap:14px;margin-top:28px}
.pg-title h1{margin:0;font-size:28px;font-weight:800;letter-spacing:-.02em}
.pg-title .m{padding-bottom:5px;font-size:14px}
.pg-title .r{margin-left:auto;display:flex;gap:8px;align-items:center}
.filters{display:flex;flex-direction:column;gap:10px;margin-top:20px;padding:16px 18px;border-radius:var(--radius-lg);background:var(--sunken)}
.frow{display:grid;grid-template-columns:72px minmax(0,1fr);gap:12px;align-items:center}
.frow > b{font-size:13px;color:var(--ink-3);font-weight:700}
.frow .chips .chip{height:34px;font-size:13.5px;padding:0 13px;background:var(--bg)}
.frow .chips .chip[aria-pressed="true"]{background:var(--ink-1);color:var(--bg)}
.applied{display:flex;align-items:center;gap:8px;margin:18px 0 14px;font-size:14px;color:var(--ink-2)}
.applied .x{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 10px 0 12px;border-radius:999px;background:var(--accent-tint);color:var(--accent-text);font-size:13px;font-weight:800}
.applied .sort{margin-left:auto;display:flex;gap:4px;font-size:13.5px;font-weight:700;color:var(--ink-3)}
.applied .sort span{padding:6px 8px;border-radius:8px}
.applied .sort span.on{color:var(--ink-1);background:var(--sunken)}
.cgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:36px 24px}
.cgrid .gc .art{border-radius:var(--radius-lg);margin-bottom:10px}
.cgrid .gc .t{font-size:17px}
.cgrid .gc .meta{font-size:14px}
.cgrid .rate{font-size:13px;color:var(--ink-2);margin-top:2px}
.cgrid .rate b{color:var(--ink-1)}
.cgrid .qplay{opacity:0;transform:translateY(6px) scale(.9);transition:opacity var(--dur-fast) var(--ease-soft),transform var(--dur-fast) var(--ease-soft)}
.cgrid .gc:hover .qplay,.cgrid .gc:first-child .qplay{opacity:1;transform:none}
.cgrid .gc:first-child .art{transform:var(--card-lift);box-shadow:var(--shadow-lift)}
.more{display:flex;justify-content:center;margin-top:36px}
/* 프로필 */
.pf-hero{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:28px;align-items:center;margin-top:36px}
.pf-hero .jf{width:120px;height:120px;font-size:44px}
.pf-hero h1{margin:0;font-size:32px;font-weight:800;letter-spacing:-.02em}
.pf-hero p{margin:8px 0 0;font-size:15px;color:var(--ink-2)}
.pf-hero .meta{display:flex;gap:18px;margin-top:12px;font-size:14px;color:var(--ink-3)}
.pf-hero .meta b{color:var(--ink-1)}
.vis-tag{display:inline-flex;align-items:center;gap:5px;height:22px;padding:0 8px;border-radius:999px;background:var(--sunken);font-size:12px;font-weight:700;color:var(--ink-3)}
.pf-grid{display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:48px;align-items:start}
.mini-rv{display:flex;flex-direction:column;gap:6px;padding:16px 0;border-top:1px solid var(--line)}
.mini-rv:first-child{border-top:0}
.mini-rv .hd{display:flex;align-items:center;gap:10px}
.mini-rv .hd .art{width:88px;border-radius:8px}
.mini-rv .hd b{font-size:15px}
.mini-rv p{margin:4px 0 0;font-size:15px;line-height:1.6}
.follow{display:flex;flex-direction:column;gap:4px}
.follow > div{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center;padding:10px 0;border-top:1px solid var(--line)}
.follow > div:first-child{border-top:0}
.follow b{display:block;font-size:15px}
/* 알림 */
.npanel{position:absolute;right:120px;top:60px;z-index:40;width:400px;border-radius:var(--radius-xl);background:var(--bg);box-shadow:var(--shadow-pop),0 0 0 1px var(--line);overflow:hidden}
[data-theme="dark"] .npanel{background:var(--raised)}
.npanel .hd{display:flex;align-items:center;gap:8px;padding:16px 18px 10px}
.npanel .hd b{font-size:17px;font-weight:800}
.npanel .hd a{margin-left:auto;font-size:13px;font-weight:700;color:var(--ink-3)}
.npanel .tabs2{display:flex;gap:4px;padding:0 14px 8px}
.npanel .tabs2 span{height:30px;padding:0 10px;border-radius:999px;display:inline-flex;align-items:center;font-size:13px;font-weight:700;color:var(--ink-3)}
.npanel .tabs2 span.on{background:var(--sunken);color:var(--ink-1)}
.npanel .ft{display:block;text-align:center;padding:12px;border-top:1px solid var(--line);font-size:14px;font-weight:700;color:var(--ink-2)}
.ni{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:start;padding:12px 18px;font-size:14px;line-height:1.5;position:relative}
.ni.new{background:var(--accent-tint)}
.ni.new::before{content:"";position:absolute;left:7px;top:22px;width:6px;height:6px;border-radius:999px;background:var(--accent)}
.ni .who{position:relative}
.ni .kind{position:absolute;right:-5px;bottom:-4px;display:grid;place-items:center;width:18px;height:18px;border-radius:999px;background:var(--bg);color:var(--ink-2);box-shadow:0 0 0 2px var(--bg)}
.ni .kind .ic{width:11px;height:11px}
.ni .ico{display:grid;place-items:center;width:32px;height:32px;border-radius:10px;background:var(--sunken);color:var(--ink-2)}
.ni b{font-weight:700}
.ni .m{display:block;font-size:12.5px;margin-top:2px}
.ni .th{width:72px;border-radius:7px}
.nfull{width:760px;margin:0 auto}
.ngrp{margin-top:28px}
.ngrp > b{display:block;margin:0 0 6px 4px;font-size:13px;color:var(--ink-3);font-weight:800}
.ngrp .ni{border-radius:12px}
.stagebg2{position:relative;height:600px;overflow:hidden;border-radius:14px;box-shadow:0 0 0 1px var(--line)}
.stagebg2 .ghost{position:absolute;inset:0;opacity:.55;pointer-events:none}
/* 설정 */
.set{width:820px;margin:0 auto}
.set .stab{position:sticky;top:68px;z-index:5;background:color-mix(in srgb,var(--bg) 94%,transparent);backdrop-filter:blur(12px)}
.sset{margin-top:40px}
.sset h2{margin:0 0 6px;font-size:20px;font-weight:800}
.sset > p{margin:0 0 14px;font-size:14px;color:var(--ink-3)}
.srow{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:20px;align-items:center;min-height:64px;padding:12px 0;border-top:1px solid var(--line)}
.srow b{display:block;font-size:15px}
.srow .m{display:block;margin-top:2px}
.seg{display:inline-flex;padding:3px;border-radius:999px;background:var(--sunken)}
.seg span{height:34px;padding:0 14px;border-radius:999px;display:inline-flex;align-items:center;gap:6px;font-size:13.5px;font-weight:700;color:var(--ink-3)}
.seg span.on{background:var(--bg);color:var(--ink-1);box-shadow:var(--shadow-hairline)}
[data-theme="dark"] .seg span.on{background:var(--sunken-hover)}
.acct{display:flex;align-items:center;gap:10px}
.acct .mk{display:grid;place-items:center;width:32px;height:32px;border-radius:9px;background:var(--ink-1);color:var(--bg);font-weight:900;font-size:14px}
.danger-zone{margin-top:12px;padding:18px 20px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--danger-tint);background:color-mix(in srgb,var(--danger-tint) 40%,transparent)}
'''

# ── PG03 전체 게임 · 갤러리형 v2 (2026-11-27 재개편: 콘텐츠 폭 1200 · 4열 큰 카드 · 장르는 태그 여러 개 선택) ──
GAL_CSS = r"""
.cat-head{display:flex;align-items:flex-end;gap:12px;margin-top:32px}
.cat-head h1{margin:0;font-size:28px;font-weight:800;letter-spacing:-.02em}
.cat-head .m{padding-bottom:5px;font-size:14px}
.cat-head .r{margin-left:auto}
.gtags{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}
.gtag{display:inline-flex;align-items:center;gap:5px;height:36px;padding:0 14px;border:0;font-family:inherit;border-radius:999px;background:var(--sunken);font-size:14px;font-weight:700;color:var(--ink-2)}
.gtag:hover{background:var(--sunken-hover)}
.gtag .ic{width:13px;height:13px}
.gtag[aria-pressed="true"]{background:var(--accent-tint);color:var(--accent-text);box-shadow:inset 0 0 0 1.5px var(--accent)}
.gtag .n{font-weight:600;font-size:12.5px;opacity:.65}
.cat-tools{display:flex;align-items:center;gap:8px;margin-top:14px;padding-top:14px;border-top:1px solid var(--line)}
.cat-tools .sum{font-size:14px;color:var(--ink-2)}
.cat-tools .sum b{color:var(--ink-1)}
.cat-tools .clear{font-size:13.5px;font-weight:700;color:var(--ink-3);text-decoration:underline;text-underline-offset:3px}
.cat-tools .r{margin-left:auto;display:flex;align-items:center;gap:8px}
.dd{position:relative;display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 12px 0 14px;border-radius:999px;background:var(--sunken);font-size:13.5px;font-weight:700;color:var(--ink-3);white-space:nowrap}
.dd b{color:var(--ink-1)}
.dd.on{background:var(--accent-tint);color:var(--accent-text)}
.dd.on b{color:var(--accent-text)}
.dd .ic{width:12px;height:12px}
.dd .dn{transform:rotate(90deg)}
.dd-pop{position:absolute;right:0;top:calc(100% + 8px);z-index:30;width:200px;padding:6px;border-radius:var(--radius-lg);background:var(--bg);box-shadow:var(--shadow-pop),0 0 0 1px var(--line);display:flex;flex-direction:column}
[data-theme="dark"] .dd-pop{background:var(--raised)}
.dd-pop span{display:flex;align-items:center;justify-content:space-between;height:38px;padding:0 10px;border-radius:8px;font-size:14px;font-weight:600;color:var(--ink-1)}
.dd-pop span.on{background:var(--sunken);font-weight:800}
.dd-pop span em{font-style:normal;font-size:12.5px;color:var(--ink-3);font-weight:600}
.gal{margin-top:24px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:40px 24px}
.gal .gc{position:relative}
.gal .gc:hover,.gal .gc:focus-within{z-index:6}
.gal .gc .art{border-radius:14px;margin-bottom:12px;top:0;transition:top var(--dur-fast) var(--ease-soft),box-shadow var(--dur-fast) var(--ease-soft)}
.gal .gc:hover .art{top:-3px;box-shadow:var(--shadow-lift)}
.gal .gc .t{font-size:18px;font-weight:800;line-height:1.35;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.gal .gc .t a::after{content:"";position:absolute;inset:0;z-index:1}
.gal .gc:hover .t{color:var(--accent-text)}
.gal .gc .meta{font-size:14px;margin-top:2px}
.gal .gc .gt{display:flex;gap:5px;margin-top:7px}
.gal .gc .gt span{height:22px;padding:0 8px;border-radius:6px;background:var(--sunken);font-size:12px;font-weight:700;color:var(--ink-2);display:inline-flex;align-items:center}
.gal .gc .gt span.hit{background:var(--accent-tint);color:var(--accent-text)}
.gal .gc .cnts{margin-top:8px}
.gal .plat,.gal .qplay,.gal .badge{z-index:3}
.gal .plat{cursor:help}
.gal .tip{opacity:0;visibility:hidden;transform:translateY(-4px);transition:opacity var(--dur-fast) var(--ease-soft),transform var(--dur-fast) var(--ease-soft),visibility 0s linear var(--dur-fast);pointer-events:none}
.gal .plat:hover .tip,.gal .plat:focus-visible .tip{opacity:1;visibility:visible;transform:none;transition-delay:120ms,120ms,0s}
.gal .qplay{width:48px;height:48px;opacity:0;transform:translateY(6px) scale(.9);transition:opacity var(--dur-fast) var(--ease-soft),transform var(--dur-fast) var(--ease-soft)}
.gal .gc:hover .qplay{opacity:1;transform:none}
.gal .gc.demo .qplay{opacity:1;transform:none}
.gal .gc.demo .art{top:-3px;box-shadow:var(--shadow-lift)}
.gal .gc.demo .shots::before{animation:hovshots 12.5s .3s steps(1,end) infinite}
.gmore{display:flex;flex-direction:column;align-items:center;gap:8px;margin:48px 0 0}
.state-box{margin-top:72px;padding:28px 32px 32px;border-radius:var(--radius-xl);box-shadow:inset 0 0 0 1px var(--line)}
.state-box > .sub{display:block;margin:0 0 18px;font-size:13px;font-weight:800;color:var(--ink-3)}
.few{display:grid;grid-template-columns:1fr 1fr;gap:28px}
.fewc{display:grid;grid-template-columns:260px minmax(0,1fr);gap:20px;align-items:center}
.fewc .art{border-radius:var(--radius-lg)}
.fewc b{font-size:19px;font-weight:800}
.fewc p{margin:6px 0 10px;font-size:14.5px;line-height:1.6;color:var(--ink-2)}
.relax{margin-top:24px;padding:18px 20px;border-radius:var(--radius-lg);background:var(--sunken);display:flex;align-items:center;gap:18px}
.relax b{font-size:15px}
.relax .chips .chip{height:34px;font-size:13.5px;background:var(--bg)}
"""

TIPS = {"web": ("web", "브라우저에서 바로 플레이"), "dl": ("dl", "설치형 · 다운로드"), "pc": ("pc", "PC (Windows)"), "phone": ("phone", "휴대폰에서도 가능"), "duo": ("duo", "여럿이 같이"), "shield": ("shield", "보안 검사 통과")}
SEL = ("퍼즐", "액션")  # 예시 상태: 장르 태그 두 개를 함께 고름
# (아트, 제목, 메이커, 장르 태그, 한 판, 실행 방식, 추천, 리뷰, 배지)
CAT = [
    ("a-ash", "애쉬폴 러너", "잿빛토끼", ("액션", "스피드런"), "6분", "web", 2031, 296, "왕좌"),
    ("a-loop", "루프 디버거", "픽셀상점", ("퍼즐", "프로그래밍"), "5분", "web phone", 214, 38, ""),
    ("a-tess", "테셀레이트", "노을공방", ("퍼즐",), "10분", "web", 342, 54, "신작"),
    ("a-grid", "그리드 러너", "보라네", ("액션", "퍼즐"), "3분", "web phone", 61, 6, "신작"),
    ("a-tilt", "틸트 이론", "기울기연구소", ("퍼즐", "물리"), "40분", "dl pc shield", 284, 41, ""),
    ("a-refac", "리팩터 러시", "리팩터클럽", ("액션", "아케이드"), "3분", "web phone", 18, 3, "신작"),
    ("a-solvent", "솔벤트", "물방울", ("퍼즐", "협동"), "12분", "web duo", 112, 17, ""),
    ("a-paper", "페이퍼 벡터", "벡터공방", ("액션", "대전"), "5분", "web duo", 1442, 216, ""),
    ("a-null", "널 포인터", "레몬게임즈", ("액션", "로그라이크"), "저녁", "dl pc shield", 96, 11, ""),
    ("a-grid", "블록 우체국", "보라네", ("퍼즐",), "10분", "web phone", 188, 26, ""),
    ("a-loop", "루프 디버거 2", "픽셀상점", ("퍼즐", "프로그래밍"), "8분", "web", 73, 9, "신작"),
    ("a-ash", "재의 도시", "잿빛토끼", ("액션", "생존"), "40분", "dl pc shield", 233, 35, ""),
]
CHEVD = '<svg class="ic dn"><use href="#i-chev"></use></svg>'

def cat_card(c, demo=False):
    art, t, who, tags, length, plat, rec, rv, badge = c
    keys = plat.split()
    icons = "".join(ic(k, "ic ic12" + (" ok" if k == "shield" else "")) for k in keys)
    tip = "".join(f'<span{" class=\"ok\"" if k == "shield" else ""}>{ic(TIPS[k][0])}{TIPS[k][1]}</span>' for k in keys)
    instant = "web" in keys
    qp = f'<span class="qplay" aria-hidden="true">{ic("play" if instant else "dl", "ic ic16")}</span>'
    bd = f'<span class="badge">{ic("spark" if badge == "신작" else "crown", "ic ic12")}{badge}</span>' if badge else ""
    label = " · ".join(TIPS[k][1] for k in keys)
    gt = "".join(f'<span{" class=\"hit\"" if g in SEL else ""}>{g}</span>' for g in tags)
    return (f'<div class="gc{" demo" if demo else ""}"><span class="art {art}"><span class="shots"></span>{bd}'
            f'<span class="plat" tabindex="0" aria-label="{label}">{icons}<span class="tip" role="tooltip">{tip}</span></span>{qp}</span>'
            f'<span class="t"><a href="#">{t}</a></span><span class="meta">{who} · 한 판 {length}</span><span class="gt">{gt}</span>{mg.counts(rec, rv)}</div>')

def catalog_page():
    genres = [("퍼즐", 38), ("액션", 27), ("탐험", 14), ("전략", 9), ("생존", 7), ("이야기", 12), ("리듬", 5), ("경영", 6), ("아케이드", 18), ("로그라이크", 6), ("대전", 8), ("협동", 7), ("프로그래밍", 4), ("물리", 5)]
    tags = (f'<div class="gtags" role="group" aria-label="장르 — 여러 개 고를 수 있어요"><button class="gtag" aria-pressed="false">전체</button>'
            + "".join(f'<button class="gtag" aria-pressed="{"true" if g in SEL else "false"}">{ic("check") if g in SEL else ""}{g} <span class="n">{n}</span></button>' for g, n in genres) + "</div>")
    pop = '<span class="dd-pop" role="listbox" aria-label="정렬">' + "".join(f'<span{" class=\"on\"" if o == "많이 하는" else ""}>{o}</span>' for o in ["많이 하는", "추천 많은", "새로 나온", "짧은 순"]) + "</span>"
    tools = (f'<div class="cat-tools"><span class="sum"><b>퍼즐</b> 또는 <b>액션</b> · <b>46</b>개</span><a class="clear" href="#">모두 지우기</a>'
             f'<div class="r"><span class="dd"><span>한 판</span><b>전체</b>{CHEVD}</span><span class="dd"><span>실행</span><b>전체</b>{CHEVD}</span><span class="dd"><span>인원</span><b>전체</b>{CHEVD}</span>'
             f'<span class="dd"><span>정렬</span><b>많이 하는</b>{CHEVD}{pop}</span></div></div>')
    grid = "".join(cat_card(c, demo=(i == 1)) for i, c in enumerate(CAT))
    few = [("a-solvent", "솔벤트", "물방울 · 협동 퍼즐 · 12분 · 같이(2명)", "물이 되어 친구와 번갈아 길을 여는 협동 퍼즐. 한 사람은 얼음, 한 사람은 증기.", 112, 17),
           ("a-null", "널 포인터", "레몬게임즈 · 퍼즐 · 15분 · 같이(2~4명) · 설치형", "서로의 코드를 고쳐 주는 파티 퍼즐. 화면 공유 없이 같은 방에서.", 96, 11)]
    fewh = "".join(f'<div class="fewc"><span class="art {a}"></span><span><b>{t}</b><span class="m" style="display:block;margin-top:4px">{m}</span><p>{d}</p>{mg.counts(r1, r2)}<span style="display:flex;margin-top:12px"><span class="btn btn-primary btn-sm">{ic("play")}플레이</span></span></span></div>' for a, t, m, d, r1, r2 in few)
    body = pgh("게임") + f"""<main class="wrap">
<div class="cat-head"><h1>전체 게임</h1><span class="m">128개 · 모두 광고 없이 무료</span><div class="r"><div class="search" style="width:280px">{ic("search")}전체 게임에서 찾기</div></div></div>
{tags}
{tools}
<div class="gal">{grid}</div>
<div class="gmore"><span class="btn btn-secondary">더 보기</span><span class="m">12 / 46</span></div>
<section class="state-box"><span class="sub">상태 예시 — 결과가 적을 때 (협동 · 같이 · 2개) R-DISC-04</span>
<div class="few">{fewh}</div>
<div class="relax"><b>조건을 조금 넓혀 볼까요?</b><div class="chips"><button class="chip">‘같이’ 빼면 +30</button><button class="chip">설치형도 보기 +4</button><button class="chip">이번 주 PICK 보기</button></div></div></section>
</main>""" + dt.footer()
    memo = "PG-CAT 갤러리형 v2(11/27 재개편). 콘텐츠 폭(1200) 안에 4열 큰 카드. 장르는 태그 — 여러 개를 함께 고름(예: 퍼즐 + 액션 = 둘 중 하나라도 해당, ‘전체’ 를 누르면 모두 풀림). 카드에 장르 태그를 보여 주고 고른 태그는 쪽빛. 그 아래 한 판 · 실행 · 인원 드롭다운(첫 항목 ‘전체’) + 정렬(펼친 예시). 카드 호버 = 영상 반복 또는 이미지 2.5초 순환 + 오른쪽 아래 플레이/다운로드(2번째 카드가 호버 예시)."
    html = dt.page("전체 게임", body, 2500, memo)
    return html.replace("</style>", CSS + GAL_CSS + "\n</style>", 1)

def profile_page():
    rvs = [("a-loop", "루프 디버거", True, "출퇴근길에 한 판씩 하기 딱 좋아요. 휴대폰 가로 모드에서도 블록이 안 작아서 좋았어요.", "48분"), ("a-tess", "테셀레이트", True, "규칙 하나로 이렇게 다양한 문제를 만들 수 있다니. 30번대 스테이지가 백미예요.", "3.1시간")]
    rv = "".join(f'<div class="mini-rv"><div class="hd"><span class="art {a}"></span><span><b>{t}</b><span class="m" style="display:block">플레이 {tm} · 11월</span></span><span class="yes" style="margin-left:auto;color:var(--accent-text);font-weight:800;font-size:13px">{ic("up","ic ic12")} 추천</span></div><p>{p}</p></div>' for a, t, y, p, tm in rvs)
    fol = "".join(f'<div>{face(c, col, "md")}<span><b>{n}</b><span class="m">{d}</span></span><span class="btn btn-secondary btn-sm">보기</span></div>' for c, col, n, d in [("ㅍ", "jjok", "픽셀상점", "퍼즐 · 게임 4"), ("ㄴ", "haneul", "노을공방", "퍼즐 · 게임 2"), ("ㅂ", "bora", "보라네", "액션 · 게임 2")])
    recent = "".join(mg.game_card(a) for a in mg.NEWG[:3])
    body = pgh("") + f'''<main class="wrap">
<div class="pf-hero"><span class="jf" style="background:var(--color-face-jadu)">^<i>ω</i>^</span><div><h1>오렌지맛</h1><p>퍼즐이랑 짧은 게임 좋아해요. 출퇴근길 플레이어.</p><div class="meta"><span><b>리뷰 12</b></span><span><b>팔로우 3</b></span><span>2026년 10월부터</span></div></div><div style="display:flex;gap:8px"><span class="btn btn-secondary">친구 신청</span><span class="btn btn-secondary">{ic("up2","ic ic16")}공유</span></div></div>
<div class="pf-grid" style="margin-top:44px"><div>
<section><div class="sh">{EAR}<h2>최근 플레이</h2><span class="vis-tag">{ic("duo","ic ic12")}친구에게만 보여요</span></div><div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px">{recent}</div></section>
<section class="sec" style="margin-top:44px"><div class="sh">{EAR}<h2>리뷰</h2><span class="sub">12개</span><div class="r"><a class="link" href="#">전체 보기</a></div></div>{rv}</section></div>
<aside><div class="sh">{EAR}<h2 style="font-size:19px">팔로우하는 메이커</h2></div><div class="follow">{fol}</div>
<div class="sh" style="margin-top:36px">{EAR}<h2 style="font-size:19px">도전과제</h2><span class="sub">출시 후</span></div><p class="m" style="margin:0">게임마다 모은 도전과제가 여기 모여요.</p></aside></div>
</main>''' + dt.footer()
    memo = "PG-PROFILE. 큰 고양이 얼굴(120) + 닉네임 · 소개 · 숫자 3개. 무엇이 누구에게 보이는지 칸마다 표시(최근 플레이 = 친구에게만, ADR 0008). 리뷰 · 팔로우 메이커는 공개. 도전과제는 출시 후(L2)."
    html = dt.page("공개 프로필", body, 1500, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

NOTI = [
    (True, "face", ("ㅍ", "jjok"), "bell", '<b>픽셀상점</b>이 새 버전을 올렸어요 — 루프 디버거 v1.2', "12분 전", "a-loop"),
    (True, "face", ("ㅍ", "jjok"), "cmt", '<b>픽셀상점</b>이 내 리뷰에 답글을 달았어요 “15스테이지 구간은 다음 업데이트에서…”', "1시간 전", None),
    (True, "face", ("ㅅ", "hong"), "duo", '<b>새벽코딩</b>님이 친구 신청을 보냈어요', "3시간 전", None),
    (False, "face", ("ㄴ", "haneul"), "pen", '<b>노을공방</b>의 새 개발일지 — 웹 빌드 40MB를 9MB로 줄인 방법', "어제", "a-tess"),
    (False, "sys", None, "check", '저장한 <b>재의 도시</b>에 업데이트가 있어요 (설치형 v1.2)', "어제", "a-ash"),
    (False, "sys", None, "alert", '<b>공지</b> 12월 정기 점검 — 12/3 02:00~04:00', "2일 전", None),
]
def ni(n):
    new, kind, f, k, text, when, th = n
    who = f'<span class="who">{face(f[0], f[1], "md")}<span class="kind">{ic(k)}</span></span>' if kind == "face" else f'<span class="ico">{ic(k, "ic ic16")}</span>'
    thumb = f'<span class="art th {th}"></span>' if th else "<span></span>"
    return f'<div class="ni{" new" if new else ""}">{who}<span>{text}<span class="m">{when}</span></span>{thumb}</div>'

def noti_page():
    panel = f'''<div class="npanel"><div class="hd"><b>알림</b><span class="cnt">3</span><a href="#">모두 읽음</a><a href="#" style="margin-left:10px">설정</a></div>
<div class="tabs2"><span class="on">전체</span><span>내 활동</span><span>팔로우</span><span>친구</span></div>{"".join(ni(n) for n in NOTI[:5])}<a class="ft" href="#">알림 전체 보기</a></div>'''
    frame1 = f'<div class="stagebg2"><div class="ghost">{pgh("홈")}<div class="wrap" style="margin-top:24px"><span class="art a-loop" style="display:block;height:380px;border-radius:16px;aspect-ratio:auto"></span></div></div>{pgh("홈").replace("<header class=\"hdr\">", "<header class=\"hdr\" style=\"position:relative;z-index:30\">")}{panel}</div>'
    full = f'''<div class="nfull"><div class="pg-title"><h1>알림</h1><div class="r"><a class="link" href="#">모두 읽음</a><span class="btn btn-secondary btn-sm">알림 설정</span></div></div>
<nav class="utabs" style="margin-top:16px"><a href="#" aria-current="page">전체</a><a href="#">내 활동</a><a href="#">팔로우 소식</a><a href="#">친구</a><a href="#">운영</a></nav>
<div class="ngrp"><b>오늘</b>{"".join(ni(n) for n in NOTI[:3])}</div><div class="ngrp"><b>이번 주</b>{"".join(ni(n) for n in NOTI[3:])}</div>
<p class="m" style="margin:24px 0 0;text-align:center">30일이 지난 알림은 자동으로 지워져요.</p></div>'''
    body = f'''{pgh("홈")}<main class="wrap"><div style="margin-top:28px"><p class="sub" style="font-size:14px;font-weight:800;color:var(--ink-2);margin:0 0 12px">헤더 종을 누르면 · 알림 패널</p>{frame1}</div>
<section class="sec"><p class="sub" style="font-size:14px;font-weight:800;color:var(--ink-2);margin:0">알림 전체 페이지</p>{full}</section></main>''' + dt.footer()
    memo = "SH-NOTI. 헤더 종 → 400px 패널(탭 4개 · 새 알림은 옅은 그라운드 바탕 + 점 · 누가 했는지 얼굴 + 종류 작은 아이콘 · 관련 그림). 전체 페이지는 오늘 / 이번 주로 묶음. 종류: 팔로우 메이커 소식 · 내 리뷰 답글 · 친구 · 업데이트 · 공지(메이커는 심사 결과도)."
    html = dt.page("알림", body, 1900, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

def settings_page():
    def sw(on=True): return f'<span class="switch{" on" if on else ""}" role="switch" aria-checked="{"true" if on else "false"}"></span>'
    swcss = ".switch{width:40px;height:24px;border-radius:999px;background:var(--sunken-hover);position:relative;flex:none;display:inline-block}.switch::after{content:\"\";position:absolute;left:2px;top:2px;width:20px;height:20px;border-radius:999px;background:#FFFFFF;box-shadow:var(--shadow-hairline)}.switch.on{background:var(--accent)}.switch.on::after{transform:translateX(16px)}"
    body = pgh("") + f'''<main class="set">
<div class="pg-title"><h1>설정</h1></div>
<div class="stab"><nav class="utabs" style="margin-top:14px"><a href="#" aria-current="page">프로필</a><a href="#">계정 연결</a><a href="#">알림</a><a href="#">공개 범위</a><a href="#">화면</a><a href="#">데이터</a></nav></div>
<section class="sset"><h2>프로필</h2><p>다른 사람에게 보이는 모습이에요.</p>
<div class="srow"><span style="display:flex;align-items:center;gap:16px"><span class="jf lg" style="background:var(--color-face-jadu)">^<i>ω</i>^</span><span><b>오렌지맛</b><span class="m">퍼즐이랑 짧은 게임 좋아해요.</span></span></span><span class="btn btn-secondary btn-sm">얼굴 · 이름 바꾸기</span></div></section>
<section class="sset"><h2>계정 연결</h2><p>비밀번호 없이, 연결한 계정으로 로그인해요.</p>
<div class="srow"><span class="acct"><span class="mk">G</span><span><b>Google</b><span class="m">연결됨 · 2026.10.02</span></span></span><span class="btn btn-secondary btn-sm">연결 끊기</span></div>
<div class="srow"><span class="acct"><span class="mk" style="border-radius:999px">{ic("user","ic ic12")}</span><span><b>GitHub</b><span class="m">연결 안 됨</span></span></span><span class="btn btn-primary btn-sm">연결하기</span></div></section>
<section class="sset"><h2>알림</h2><p>헤더 종으로 받아요. 이메일 알림은 출시 후.</p>
<div class="srow"><span><b>팔로우한 메이커의 새 게임 · 업데이트 · 일지</b></span>{sw()}</div>
<div class="srow"><span><b>내 리뷰 · 글에 달린 답글</b></span>{sw()}</div>
<div class="srow"><span><b>친구 신청</b></span>{sw()}</div>
<div class="srow"><span><b>저장한 게임의 업데이트</b></span>{sw(False)}</div></section>
<section class="sset"><h2>공개 범위</h2><p>무엇을 누구에게 보일지 정해요.</p>
<div class="srow"><span><b>지금 하는 게임 · 최근 플레이</b><span class="m">친구에게만 보여요 · 끄면 바로 사라져요</span></span>{sw()}</div>
<div class="srow"><span><b>라이브러리</b><span class="m">플레이한 게임 목록</span></span><span class="seg"><span>모두</span><span class="on">친구만</span><span>나만</span></span></div>
<div class="srow"><span><b>리뷰</b><span class="m">리뷰는 게임 페이지에 항상 공개돼요</span></span><span class="vis-tag">항상 공개</span></div></section>
<section class="sset"><h2>화면</h2><p>처음엔 라이트로 시작해요. 헤더의 달 버튼으로도 바꿀 수 있어요.</p>
<div class="srow"><span><b>테마</b></span><span class="seg"><span class="on">{ic("sun")}라이트</span><span>{ic("moon")}다크</span><span>기기 설정 따름</span></span></div>
<div class="srow"><span><b>움직임 줄이기</b><span class="m">고양이 표정 · 카드 움직임 · 호버 미리보기(영상 · 이미지 순환)를 멈춰요</span></span>{sw(False)}</div></section>
<section class="sset"><h2>데이터</h2><p>내 기록은 언제든 가져가거나 지울 수 있어요.</p>
<div class="srow"><span><b>내 데이터 내려받기</b><span class="m">플레이 기록 · 리뷰 · 글을 JSON 파일로</span></span><span class="btn btn-secondary btn-sm">요청하기</span></div>
<div class="danger-zone"><div class="srow" style="border:0;padding:0;min-height:0"><span><b style="color:var(--danger-text)">탈퇴하기</b><span class="m">기록이 모두 지워지고 되돌릴 수 없어요. 내가 만든 게임이 있으면 먼저 비공개로 바꿔 주세요.</span></span><span class="btn btn-secondary btn-sm" style="color:var(--danger-text)">탈퇴</span></div></div></section>
</main>''' + dt.footer()
    memo = "SH-SETTINGS. 사이드바 대신 위 고정 탭(누르면 해당 칸으로 이동)으로 한 페이지에. 프로필 · 계정 연결(Google · GitHub) · 알림 · 공개 범위(지금 하는 게임 = 기본 켜짐, 친구에게만) · 화면(라이트 시작 · 다크 · 기기 설정) · 데이터(내려받기 · 탈퇴)."
    html = dt.page("설정", body, 2200, memo)
    return html.replace("</style>", CSS + swcss + "\n</style>", 1)

if __name__ == "__main__":
    for name, fn in [("PG03-catalog.dc.html", catalog_page), ("PG15-profile.dc.html", profile_page), ("SH03-notifications.dc.html", noti_page), ("SH02-settings.dc.html", settings_page)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
