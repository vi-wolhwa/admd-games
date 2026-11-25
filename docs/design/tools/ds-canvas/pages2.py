# 다운로드 · 보안 검사(PG-DL · PG-SCAN), 라이브러리(PG-LIB) 시안 생성기
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + [OUT]
import importlib.util
spec = importlib.util.spec_from_file_location("detail", os.path.join(HERE, "detail.py"))
dt = importlib.util.module_from_spec(spec); spec.loader.exec_module(dt)
mg = dt.mg
ic, face, logo, EAR = mg.ic, mg.face, mg.logo, mg.EAR

CSS = r'''
.pg-h{display:flex;align-items:center;gap:16px;margin-top:28px}
.pg-h .art{width:120px;border-radius:10px}
.pg-h h1{margin:0;font-size:28px;line-height:1.25;font-weight:800;letter-spacing:-.02em}
.pg-h .m{display:block;margin-top:4px;font-size:14px}
.two-col{display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:48px;align-items:start;margin-top:32px}
.started{display:flex;align-items:center;gap:14px;padding:18px 20px;border-radius:var(--radius-lg);background:var(--ok-tint);color:var(--ink-1)}
.started .ic{width:22px;height:22px;color:var(--ok-text)}
.started b{display:block;font-size:16px}
.started .m{display:block}
.started a{margin-left:auto;font-size:14px;font-weight:700;color:var(--ink-2)}
.isteps{list-style:none;margin:28px 0 0;padding:0;display:flex;flex-direction:column;gap:0;counter-reset:s}
.isteps > li{display:grid;grid-template-columns:36px minmax(0,1fr);gap:16px;padding:20px 0;border-top:1px solid var(--line)}
.isteps > li::before{counter-increment:s;content:counter(s);display:grid;place-items:center;width:32px;height:32px;border-radius:999px;background:var(--ink-1);color:var(--bg);font-weight:800}
.isteps b{display:block;font-size:17px;margin-bottom:4px}
.isteps p{margin:0;font-size:15px;line-height:1.65;color:var(--ink-2)}
.mock{margin-top:14px;width:440px;border-radius:10px;overflow:hidden;box-shadow:0 0 0 1px var(--line),var(--shadow-lift)}
.mock .top{height:28px;background:#1F5FA8}
.mock .bd{padding:18px 20px;background:#1F5FA8;color:#FFFFFF;font-size:13px;line-height:1.55}
.mock .bd b{font-size:19px;font-weight:600;display:block;margin-bottom:8px}
.mock .bd u{font-weight:700}
.mock .ft{display:flex;justify-content:flex-end;gap:8px;padding:12px 20px;background:#1F5FA8}
.mock .ft span{height:30px;padding:0 18px;display:grid;place-items:center;border:1px solid rgb(255 255 255/.7);font-size:13px;color:#FFFFFF}
.mock .ft span.hl{outline:3px solid #FFD43B;outline-offset:2px}
.mark{display:inline-block;padding:0 4px;border-radius:3px;background:#FFD43B;color:#151A20;font-weight:800}
.why{margin-top:16px;padding:16px 18px;border-radius:var(--radius-lg);background:var(--sunken);font-size:14px;line-height:1.65;color:var(--ink-2)}
.why b{color:var(--ink-1)}
.card2{padding:20px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line);display:flex;flex-direction:column;gap:12px}
.card2 h3{margin:0;font-size:16px;font-weight:800;display:flex;align-items:center;gap:8px}
.kv2{display:flex;flex-direction:column;font-size:14px}
.kv2 > div{display:grid;grid-template-columns:84px minmax(0,1fr);gap:10px;padding:8px 0;border-top:1px solid var(--line)}
.kv2 > div:first-child{border-top:0}
.kv2 span:first-child{color:var(--ink-3);font-weight:600}
/* 검사 리포트 */
.verdict{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:22px;align-items:center;margin-top:28px;padding:28px 32px;border-radius:var(--radius-2xl);background:var(--ok-tint)}
.verdict .shield{display:grid;place-items:center;width:72px;height:72px;border-radius:20px;background:var(--ok);color:#FFFFFF}
.verdict .shield .ic{width:36px;height:36px}
.verdict h2{margin:0;font-size:26px;font-weight:800;letter-spacing:-.02em}
.verdict p{margin:6px 0 0;font-size:15px;line-height:1.6;color:var(--ink-2)}
.verdict .when{text-align:right;font-size:13px;color:var(--ink-3)}
.verdict .when b{display:block;font-size:15px;color:var(--ink-1)}
.tbl{width:100%;border-collapse:collapse;font-size:14px}
.tbl th{text-align:left;font-size:12.5px;color:var(--ink-3);font-weight:700;padding:0 12px 10px}
.tbl td{padding:14px 12px;border-top:1px solid var(--line);vertical-align:middle}
.tbl td b{font-weight:700}
.hash{display:flex;align-items:center;gap:8px;font-family:ui-monospace,Consolas,monospace;font-size:12.5px;color:var(--ink-2)}
.hash span{display:inline-flex;align-items:center;height:26px;padding:0 9px;border-radius:999px;background:var(--sunken);font-family:var(--font-sans);font-size:12px;font-weight:700;color:var(--ink-1)}
.legend4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.lg4{display:flex;flex-direction:column;gap:8px;padding:16px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line);font-size:13.5px;line-height:1.55;color:var(--ink-2)}
.lg4 .st{align-self:flex-start}
.does{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.does > div{padding:20px;border-radius:var(--radius-lg);background:var(--sunken);font-size:14.5px;line-height:1.7;color:var(--ink-2)}
.does b{display:block;font-size:15px;color:var(--ink-1);margin-bottom:6px}
.does ul{margin:0;padding-left:18px}
/* 라이브러리 */
.lib-h{display:flex;align-items:center;gap:18px;margin-top:32px}
.lib-h h1{margin:0;font-size:28px;font-weight:800}
.lib-h .stats{display:flex;gap:22px;margin-left:auto;font-size:13px;color:var(--ink-3)}
.lib-h .stats b{display:block;font-size:20px;color:var(--ink-1);font-weight:800}
.lib-tools{display:flex;align-items:center;gap:10px;margin:18px 0 8px}
.lib-tools .search{width:260px}
.lr{display:grid;grid-template-columns:128px minmax(0,1.4fr) minmax(0,1fr) minmax(0,1fr) auto;gap:20px;align-items:center;padding:10px 14px 10px 10px;border-radius:var(--radius-lg)}
.lr:hover{background:var(--sunken)}
.lr .art{width:128px;border-radius:9px}
.lr b{display:block;font-size:16px;font-weight:800}
.lr .m{display:block;margin-top:3px}
.lr .p{display:flex;flex-direction:column;gap:6px;font-size:13px;color:var(--ink-3)}
.lr .p .bar{width:160px}
.lr .acts{display:flex;gap:6px;align-items:center}
.upd-chip{align-self:flex-start;display:inline-flex;align-items:center;gap:5px;height:24px;padding:0 9px;border-radius:999px;background:var(--accent-tint);color:var(--accent-text);font-size:12px;font-weight:800}
.empty-mini{display:flex;align-items:center;gap:14px;padding:22px;border-radius:var(--radius-lg);background:var(--sunken);font-size:14px;color:var(--ink-2)}
'''

def dl_page():
    body = dt.pg_header() + f'''<main class="wrap">
<div class="pg-h"><span class="art a-ash"></span><span><h1>재의 도시 받기</h1><span class="m">잿빛토끼 · v1.2 · Windows · 312MB</span></span></div>
<div class="two-col"><div>
<div class="started">{ic("check")}<span><b>다운로드를 시작했어요</b><span class="m">ash-city-1.2-win.exe · 312MB</span></span><a href="#">안 받아지나요? 다시 받기</a></div>
<ol class="isteps">
<li><span><b>받은 파일을 열어요</b><p>브라우저 아래나 오른쪽 위 다운로드 목록에서 <b>ash-city-1.2-win.exe</b> 를 눌러요.</p></span></li>
<li><span><b>“Windows의 PC 보호” 창이 뜨면</b><p><span class="mark">추가 정보</span> 를 누른 뒤 <span class="mark">실행</span> 을 눌러요. 처음 보는 프로그램이면 Windows 가 늘 띄우는 창이에요.</p>
<div class="mock" aria-label="Windows 경고 창 예시"><div class="top"></div><div class="bd"><b>Windows의 PC 보호</b>Microsoft Defender SmartScreen이 인식할 수 없는 앱의 시작을 차단했습니다. …<br><u style="background:#FFD43B;color:#151A20;text-decoration:none;padding:0 3px">추가 정보</u></div><div class="ft"><span class="hl">실행</span><span>실행 안 함</span></div></div>
<div class="why"><b>왜 이 창이 뜨나요?</b> 코드 서명 인증서는 해마다 비용이 들어서, 작은 인디 메이커는 없는 경우가 많아요. 이 파일은 서명이 없지만 <b>aDmD 가 올라온 그대로의 파일을 보안 검사했고 문제를 찾지 못했어요.</b> 검사 뒤 파일이 바뀌지 않았는지는 아래 SHA-256 으로 확인할 수 있어요.</div></span></li>
<li><span><b>설치하고 실행해요</b><p>설치가 끝나면 바탕화면의 ‘재의 도시’ 를 열어요. 라이브러리 → 다운로드함에서 새 버전 알림을 받을 수 있어요.</p></span></li>
</ol></div>
<aside style="display:flex;flex-direction:column;gap:16px">
<div class="card2"><h3><span class="st st-live">{ic("shield")}검사 통과</span></h3><p class="m" style="margin:0">엔진 3종 모두 문제를 찾지 못했어요 · 11/24 14:02</p><a class="btn btn-secondary btn-sm" href="#">검사 리포트 보기</a></div>
<div class="card2"><h3>이 파일</h3><div class="kv2"><div><span>파일</span><span class="clip">ash-city-1.2-win.exe</span></div><div><span>크기</span><span>312MB</span></div><div><span>버전</span><span>v1.2 · 11/23</span></div><div><span>서명</span><span>없음</span></div><div><span>SHA-256</span><span class="clip" style="font-family:ui-monospace,Consolas,monospace;font-size:12.5px">9f2c4e…a71b03</span></div></div></div>
<div class="card2"><h3>필요한 사양</h3><div class="kv2"><div><span>OS</span><span>Windows 10 이상 (64비트)</span></div><div><span>메모리</span><span>4GB</span></div><div><span>저장 공간</span><span>1.2GB</span></div></div></div>
<div class="card2"><h3>다른 플랫폼</h3><div class="kv2"><div><span>macOS</span><span>298MB · 서명 없음 · <a class="link" href="#" style="font-size:14px">받기</a></span></div></div></div>
</aside></div></main>''' + dt.footer()
    memo = "PG-DL. 다운로드 뒤에 ‘이제 뭘 하지?’를 없앤다. 설치 3단계 + SmartScreen 경고 창을 미리 보여 주고(어디를 누를지 노란 표시), 왜 뜨는지 솔직히 설명. 오른쪽: 검사 결과 · 파일 · 사양."
    html = dt.page("다운로드 안내", body, 1700, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

def scan_page():
    rows = [("검사 엔진 1", "시그니처 검사", "문제 없음"), ("검사 엔진 2", "시그니처 검사", "문제 없음"), ("검사 엔진 3", "행동 기반 검사", "문제 없음")]
    trs = "".join(f'<tr><td><b>{a}</b></td><td>{b}</td><td><span class="st st-live">{ic("check")}{c}</span></td><td style="color:var(--ink-3)">11/24 14:02</td></tr>' for a, b, c in rows)
    hist = [("v1.2", "11/24", "live", "통과", "엔진 3종 문제 없음"), ("v1.1", "10/20", "live", "통과", "엔진 3종 문제 없음"), ("v1.0", "10/02", "fix", "주의 → 통과", "엔진 1이 설치 도구를 의심 → 메이커가 설치 도구를 바꿔 다시 올림")]
    htr = "".join(f'<tr><td><b>{v}</b></td><td>{d}</td><td><span class="st st-{k}">{ic("check") if k=="live" else ic("alert")}{s}</span></td><td style="color:var(--ink-2)">{n}</td></tr>' for v, d, k, s, n in hist)
    body = dt.pg_header() + f'''<main class="wrap">
<div class="pg-h"><span class="art a-ash"></span><span><h1>보안 검사 리포트</h1><span class="m">재의 도시 · 잿빛토끼 · 설치형</span></span></div>
<div class="verdict"><span class="shield">{ic("shield")}</span><div><h2>문제를 찾지 못했어요</h2><p>올라온 파일 그대로를 검사 엔진 3종으로 확인했어요. 검사는 알려진 악성코드와 수상한 동작을 찾는 것이고, 100% 안전을 보장하지는 않아요.</p></div><div class="when">검사 시각<b>2026.11.24 14:02</b></div></div>
<section class="sec" style="margin-top:44px"><div class="sh">{EAR}<h2>검사한 파일</h2></div>
<table class="tbl"><thead><tr><th>파일</th><th>크기</th><th>SHA-256</th><th></th></tr></thead><tbody>
<tr><td><b>ash-city-1.2-win.exe</b></td><td>312MB</td><td><span class="hash">9f2c4e81d0b7…3f5a71b03</span></td><td><span class="hash"><span>전체 복사</span></span></td></tr>
<tr><td><b>ash-city-1.2-mac.dmg</b></td><td>298MB</td><td><span class="hash">41ad09c2e6f1…8c0e2d914</span></td><td><span class="hash"><span>전체 복사</span></span></td></tr></tbody></table></section>
<section class="sec"><div class="sh">{EAR}<h2>엔진별 결과</h2><span class="sub">엔진 이름은 검사 방식이 정해지면 채워요</span></div>
<table class="tbl"><thead><tr><th>엔진</th><th>방식</th><th>결과</th><th>시각</th></tr></thead><tbody>{trs}</tbody></table></section>
<section class="sec"><div class="sh">{EAR}<h2>검사 결과는 네 가지예요</h2></div><div class="legend4">
<div class="lg4"><span class="st st-live">{ic("check")}검사 통과</span>모든 엔진이 문제를 찾지 못했어요. 받을 수 있어요.</div>
<div class="lg4"><span class="st st-wait"><span class="pulse"></span>검사 중</span>보통 10분 안에 끝나요. 끝나기 전엔 받을 수 없어요.</div>
<div class="lg4"><span class="st st-fix">{ic("alert")}주의</span>엔진 하나가 의심했어요. 받기 전에 이유를 보여 주고, 메이커에게 알려요.</div>
<div class="lg4"><span class="st st-no">{ic("alert")}차단</span>문제가 확인돼 내려받을 수 없어요. 메이커에게 사유를 보냈어요.</div></div></section>
<section class="sec"><div class="sh">{EAR}<h2>버전별 이력</h2></div><table class="tbl"><thead><tr><th>버전</th><th>검사일</th><th>결과</th><th>메모</th></tr></thead><tbody>{htr}</tbody></table></section>
<section class="sec"><div class="does"><div><b>검사가 하는 일</b><ul><li>알려진 악성코드 · 광고 프로그램 찾기</li><li>설치할 때 수상한 동작(다른 프로그램 몰래 설치 등) 찾기</li><li>검사한 파일과 받는 파일이 같은지 지문(SHA-256)으로 확인</li></ul></div>
<div><b>검사가 못 하는 일</b><ul><li>아직 알려지지 않은 새 악성코드를 모두 막지는 못해요</li><li>게임이 재미있는지, 잘 돌아가는지는 판단하지 않아요</li><li>이상하면 <a class="link" href="#" style="font-size:14.5px">신고</a>해 주세요 — 운영자가 바로 확인해요</li></ul></div></div></section>
</main>''' + dt.footer()
    memo = "PG-SCAN. 신뢰는 ‘안전합니다’라는 단언이 아니라 무엇을 했는지 보여 주는 데서 온다 — 결과 · 파일 지문 · 엔진별 결과 · 네 가지 상태 · 버전 이력 · 하는 일/못 하는 일. 검사 방식(무료)은 결정 대기(D4)."
    html = dt.page("보안 검사 리포트", body, 2300, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

LIB = [
    ("a-loop", "루프 디버거", "픽셀상점 · 브라우저", 45, "18 / 40 · 어제", "1시간 12분 · 도전과제 7/12", ("primary", "이어하기"), None),
    ("a-ash", "재의 도시", "잿빛토끼 · 설치형 v1.1", 62, "3일 전", "8시간 40분", ("primary", "업데이트"), "v1.2 있음"),
    ("a-tess", "테셀레이트", "노을공방 · 브라우저", 100, "완주 · 11/20", "2시간 14분 · 최고 03:42", ("secondary", "다시 하기"), None),
    ("a-halcyon", "할시온 바다", "하늘섬 · 브라우저", 8, "1주 전", "22분", ("primary", "이어하기"), None),
    ("a-demon", "들판의 악마", "풀잎 · 설치형 v2.0", 0, "아직 안 함", "받음 · 1.1GB", ("secondary", "실행 방법"), None),
]
def lib_page():
    rows = ""
    for art, t, sub, pct, last, total, (k, lab), upd in LIB:
        up = f'<span class="upd-chip">{ic("up2","ic ic12")}{upd}</span>' if upd else ""
        bar = f'<span class="bar"><i style="width:{pct}%"></i></span>' if 0 < pct < 100 else ('<span class="st st-live" style="align-self:flex-start">' + ic("check") + '완주</span>' if pct == 100 else "")
        rows += f'''<div class="lr"><span class="art {art}"></span><span><b>{t}</b><span class="m">{sub}</span></span>
<span class="p">{bar}<span>{"진행 " + str(pct) + "% · " if 0 < pct < 100 else ""}{last}</span></span><span class="p"><span>플레이 {total}</span>{up}</span>
<span class="acts"><span class="btn btn-{k} btn-sm"{" data-play" if lab in ("이어하기","다시 하기") else ""}>{lab}</span><button class="save" aria-label="더 보기"><svg class="ic ic16" viewBox="0 0 16 16"><circle cx="3.5" cy="8" r=".8"></circle><circle cx="8" cy="8" r=".8"></circle><circle cx="12.5" cy="8" r=".8"></circle></svg></button></span></div>'''
    body = dt.pg_header() + f'''<main class="wrap">
<div class="lib-h">{face("ㅇ","olive","lg")}<h1>내 라이브러리</h1><div class="stats"><span><b>12</b>플레이한 게임</span><span><b>7</b>저장함</span><span><b>2</b>받은 설치형</span><span><b>31시간</b>이번 달</span></div></div>
<nav class="utabs" style="margin-top:24px"><a href="#" aria-current="page">이어하기 5</a><a href="#">저장함 7</a><a href="#">다운로드함 2</a><a href="#">플레이 기록</a></nav>
<div class="lib-tools"><div class="search">{ic("search")}내 게임에서 찾기</div><div class="chips"><button class="chip" aria-pressed="true">최근 플레이 순</button><button class="chip">진행률 순</button><button class="chip">브라우저</button><button class="chip">설치형</button></div></div>
<div class="mg-rows">{rows}</div>
<section class="sec"><div class="sh">{EAR}<h2>저장함에서 아직 안 한 게임</h2><div class="r"><a class="link" href="#">저장함 전체</a></div></div>
<div class="rail">{"".join(mg.game_card(a) for a in mg.NEWG)}</div></section>
<section class="sec"><div class="empty-mini">{ic("q","ic ic20")}<span>다른 기기에서 하던 게임이 안 보이나요? 같은 계정으로 로그인하면 진행이 이어져요. 설치형 게임의 세이브는 메이커가 지원할 때만 옮겨져요.</span></div></section>
</main>''' + dt.footer()
    memo = "PG-LIB. 탭 4개(이어하기 · 저장함 · 다운로드함 · 기록). 줄마다 진행 · 마지막 플레이 · 총 시간 · 설치형 업데이트 표시와 주 버튼 하나. 아래엔 ‘저장만 하고 안 한 게임’으로 다음 행동 제안."
    html = dt.page("내 라이브러리", body, 1700, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

if __name__ == "__main__":
    for name, fn in [("다운로드 안내.dc.html", dl_page), ("보안 검사 리포트.dc.html", scan_page), ("내 라이브러리.dc.html", lib_page)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
