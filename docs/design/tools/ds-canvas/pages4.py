# 메이커 페이지(PG-MAKER), 게임 관리·통계(MG-GAME · MG-STATS), 심사 대기열(AD-REVIEW) 시안 생성기
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

OLD_NAV = '<nav class="gnb"><a href="#" aria-current="page">홈</a><a href="#">내 게임</a><a href="#">개발일지</a><a href="#">질문</a><a href="#">잼</a></nav>'
CSS = r'''
.mk-hero{position:relative;padding:48px 0 36px;background:var(--accent-tint)}
.mk-hero .in{width:1200px;margin:0 auto;display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:32px;align-items:center}
.mk-hero .jf{width:132px;height:132px;font-size:48px;border-radius:36px;box-shadow:0 0 0 5px var(--bg)}
.mk-hero h1{margin:0;font-size:36px;font-weight:800;letter-spacing:-.025em}
.mk-hero p{margin:10px 0 0;font-size:16px;line-height:1.7;color:var(--ink-2);max-width:620px}
.mk-hero .meta{display:flex;gap:18px;margin-top:14px;font-size:14px;color:var(--ink-3)}
.mk-hero .meta b{color:var(--ink-1)}
.mk-hero .links2{display:flex;gap:8px;margin-top:14px}
.mk-hero .links2 span{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 12px;border-radius:999px;background:var(--raised-hover);font-size:13px;font-weight:700;color:var(--ink-2)}
.mk-hero .acts{display:flex;flex-direction:column;gap:8px;align-self:start}
.wip{display:grid;grid-template-columns:420px minmax(0,1fr);gap:32px;align-items:center}
.wip .art{border-radius:var(--radius-lg)}
.wip h3{margin:8px 0 0;font-size:22px;font-weight:800}
.wip p{margin:8px 0 0;font-size:15px;line-height:1.7;color:var(--ink-2)}
.wip .prg{display:flex;gap:6px;margin-top:16px}
.wip .prg span{flex:1;display:flex;flex-direction:column;gap:6px;font-size:12px;font-weight:700;color:var(--ink-3)}
.wip .prg span::before{content:"";height:4px;border-radius:999px;background:var(--sunken-hover)}
.wip .prg span.done::before{background:var(--accent)}
.timeline{display:flex;flex-direction:column}
.tl{display:grid;grid-template-columns:90px 20px minmax(0,1fr);gap:14px;padding-bottom:22px;position:relative}
.tl::before{content:"";position:absolute;left:99px;top:18px;bottom:0;width:2px;background:var(--sunken-hover)}
.tl:last-child::before{display:none}
.tl .d{font-size:13px;color:var(--ink-3);font-weight:700;padding-top:2px;text-align:right}
.tl i{width:12px;height:12px;margin:5px 4px 0;border-radius:999px;background:var(--accent);position:relative;z-index:1;box-shadow:0 0 0 4px var(--bg)}
.tl i.g{background:var(--ink-4)}
.tl b{font-size:15px}
.tl .m{display:block;margin-top:2px}
/* 게임 관리 */
.mg-h{display:flex;align-items:center;gap:16px;margin-top:28px}
.mg-h .art{width:120px;border-radius:10px}
.mg-h h1{margin:0;font-size:28px;font-weight:800}
.mg-h .row{display:flex;gap:8px;align-items:center;margin-top:6px}
.mg-h .acts{margin-left:auto;display:flex;gap:8px}
.kpis{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:24px}
.kp{padding:18px 20px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line)}
.kp span{font-size:13px;color:var(--ink-3);font-weight:700}
.kp b{display:block;margin-top:6px;font-size:26px;font-weight:800;font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.kp small{font-size:12.5px;font-weight:800;color:var(--ok-text)}
.kp small.dn{color:var(--ink-3)}
.chart{position:relative;height:220px;display:flex;align-items:flex-end;gap:6px;padding:20px 0 26px;border-bottom:1px solid var(--line)}
.chart i{flex:1;border-radius:4px 4px 1px 1px;background:var(--sunken-hover);position:relative}
.chart i.on{background:var(--accent)}
.chart i.ev::after{content:"v1.2";position:absolute;left:50%;top:-22px;transform:translateX(-50%);font:800 11px/1 var(--font-sans);color:var(--accent-text);font-style:normal}
.chart .axis{position:absolute;left:0;right:0;bottom:4px;display:flex;justify-content:space-between;font-size:12px;color:var(--ink-3)}
.split2{display:grid;grid-template-columns:1fr 1fr;gap:40px}
.dist{display:flex;flex-direction:column;gap:10px}
.dist > div{display:grid;grid-template-columns:110px minmax(0,1fr) 48px;gap:12px;align-items:center;font-size:14px}
.dist .b{height:10px;border-radius:999px;background:var(--sunken);overflow:hidden}
.dist .b i{display:block;height:100%;background:var(--ink-2);border-radius:999px}
.dist .b i.on{background:var(--accent)}
.dist .n{text-align:right;color:var(--ink-3);font-variant-numeric:tabular-nums}
.ver{display:flex;flex-direction:column}
.ver > div{display:grid;grid-template-columns:70px minmax(0,1fr) auto auto;gap:14px;align-items:center;min-height:52px;border-top:1px solid var(--line);font-size:14px}
.ver > div:first-child{border-top:0}
.fb{display:flex;flex-direction:column}
.fb > div{display:grid;grid-template-columns:28px minmax(0,1fr) auto;gap:12px;align-items:start;padding:14px 0;border-top:1px solid var(--line);font-size:14px}
.fb > div:first-child{border-top:0}
.fb .env{display:block;margin-top:4px;font-size:12.5px;color:var(--ink-3);font-family:ui-monospace,Consolas,monospace}
/* 운영자 심사 */
.ad-h{display:flex;align-items:center;gap:12px;margin-top:24px}
.ad-h h1{margin:0;font-size:26px;font-weight:800}
.ad-h .tag2{height:24px;padding:0 9px;border-radius:999px;background:var(--surface-ink);color:#FFFFFF;font-size:12px;font-weight:800;display:inline-flex;align-items:center}
.ad{display:grid;grid-template-columns:420px minmax(0,1fr);gap:28px;margin-top:20px;align-items:start}
.q{display:flex;flex-direction:column;gap:6px}
.qrow{display:grid;grid-template-columns:96px minmax(0,1fr) auto;gap:12px;align-items:center;padding:10px;border-radius:12px}
.qrow.on{background:var(--accent-tint);box-shadow:inset 0 0 0 2px var(--accent)}
.qrow .art{width:96px;border-radius:8px}
.qrow b{display:block;font-size:14.5px}
.qrow .m{display:block;font-size:12.5px}
.qrow .age{font-size:12px;font-weight:800;color:var(--ink-3);text-align:right}
.qrow .age.late{color:var(--danger-text)}
.rv-pane{display:flex;flex-direction:column;gap:18px;padding:24px;border-radius:var(--radius-xl);box-shadow:inset 0 0 0 1px var(--line)}
.rv-pane .top{display:flex;align-items:center;gap:14px}
.rv-pane .top .art{width:200px;border-radius:12px}
.rv-pane .top h2{margin:0;font-size:22px;font-weight:800}
.ck2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.ck2 > div{display:flex;align-items:center;gap:10px;min-height:44px;padding:0 12px;border-radius:10px;background:var(--sunken);font-size:14px}
.ck2 .y{color:var(--ok-text)}
.ck2 .w{color:var(--accent-text)}
.ck2 > div.flag{background:var(--accent-tint)}
.reason{display:flex;flex-direction:column;gap:8px}
.reason .chips .chip{height:34px;font-size:13px}
.reason textarea{height:84px;resize:none;padding:12px 14px;border:0;border-radius:12px;background:var(--sunken);font:15px/1.5 var(--font-sans);color:var(--ink-1)}
.decide{display:flex;gap:8px;justify-content:flex-end;padding-top:14px;border-top:1px solid var(--line)}
.kbd{display:inline-grid;place-items:center;min-width:22px;height:20px;padding:0 5px;border-radius:5px;background:rgb(255 255 255/.2);font-size:11px;font-weight:800;margin-left:6px}
.kbd.d{background:var(--sunken-hover);color:var(--ink-2)}
'''

def maker_page():
    games = "".join(mg.game_card(a) for a in [("a-loop", "루프 디버거", "픽셀상점", "ㅍ", "jjok", "퍼즐 · 5분", "web"), ("a-paper", "종이 배", "픽셀상점", "ㅍ", "jjok", "탐험 · 20분", "web"), ("a-grid", "그리드 러너", "픽셀상점", "ㅍ", "jjok", "액션 · 3분", "web"), ("a-tess", "타일 정원", "픽셀상점", "ㅍ", "jjok", "퍼즐 · 10분", "dl")])
    logs = "".join(mg.log_card(l) for l in [mg.LOGS[2], ("a-grid", "그리드 러너를 잼에서 꺼내 다듬기까지", "48시간 버전에서 뺀 것 세 가지와 다시 넣은 것 하나.", "ㅍ", "jjok", "픽셀상점", "그리드 러너", 41, 9), ("a-paper", "종이 배 2 — 물 표현을 바꾼 이유", "셰이더 대신 손으로 그린 6프레임. 모바일에서 프레임이 두 배가 됐어요.", "ㅍ", "jjok", "픽셀상점", "종이 배 2", 29, 6)])
    body = dt.pg_header() + f'''<section class="mk-hero"><div class="in">{face("ㅍ","jjok","")}
<div><h1>픽셀상점</h1><p>퍼즐만 만드는 1인 메이커예요. 회사 다니면서 주말에 만들어요. 작은 아이디어를 끝까지 다듬는 걸 좋아해요.</p>
<div class="meta"><span><b>게임 4</b></span><span><b>개발일지 12</b></span><span><b>팔로워 318</b></span><span>2025년부터 · Godot</span></div>
<div class="links2"><span>{ic("web","ic ic12")}pixelshop.dev</span><span>{ic("cmt","ic ic12")}이메일 공개 안 함</span></div></div>
<div class="acts"><span class="btn btn-primary">팔로우</span><span class="btn btn-secondary">공유</span></div></div></section>
<main>
<section class="sec wrap" style="margin-top:44px"><div class="sh">{EAR}<h2>만들고 있는 것</h2><span class="sub">메이커가 직접 공개한 진행 중 프로젝트</span></div>
<div class="wip"><span class="art a-paper"><span class="shots"></span><span class="badge ink">개발 중</span></span><div><span class="st st-wait"><span class="pulse"></span>심사 준비 중</span><h3>종이 배 2</h3><p>접은 종이배로 강을 따라 내려가는 짧은 탐험. 1편보다 강이 두 배 길어지고, 비 오는 날 스테이지가 생겨요.</p>
<div class="prg"><span class="done">기획</span><span class="done">프로토타입</span><span class="done">제작</span><span>심사</span><span>공개</span></div>
<div style="display:flex;gap:8px;margin-top:18px"><span class="btn btn-secondary btn-sm">{ic("bell")}공개되면 알림</span><a class="link" href="#" style="align-self:center">개발일지 5개 ›</a></div></div></div></section>
<section class="sec wrap"><div class="sh">{EAR}<h2>게임</h2><span class="sub">4개</span></div><div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px">{games}</div></section>
<section class="sec band"><div class="wrap"><div class="sh">{EAR}<h2>개발일지</h2><div class="r"><a class="link" href="#">전체 12</a></div></div><div class="logs">{logs}</div></div></section>
<section class="sec wrap"><div class="sh">{EAR}<h2>지나온 길</h2></div><div class="timeline">
<div class="tl"><span class="d">2026.11</span><i></i><span><b>루프 디버거 v1.2</b><span class="m">리뷰 38개를 읽고 튜토리얼을 줄였어요</span></span></div>
<div class="tl"><span class="d">2026.10</span><i></i><span><b>루프 디버거 공개 · 이번 주 PICK</b><span class="m">첫 주 추천 94%</span></span></div>
<div class="tl"><span class="d">2026.08</span><i class="g"></i><span><b>여름 잼 3위 · 그리드 러너</b><span class="m">주제 ‘다시 한 번’ · 팀 2명</span></span></div>
<div class="tl"><span class="d">2025.12</span><i class="g"></i><span><b>aDmD 에 첫 게임</b><span class="m">종이 배</span></span></div></div></section>
</main>''' + dt.footer()
    memo = "PG-MAKER. ‘만든 사람이 보이는 곳’의 중심. 옅은 그라운드 띠 위 큰 얼굴(132) · 소개 · 팔로우 → 만들고 있는 것(진행 단계 · 공개 알림) → 게임 → 개발일지 → 지나온 길(공개 · 업데이트 · 잼). 팔로워 수는 메이커 페이지에서만."
    html = dt.page("메이커 페이지", body, 2600, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

def game_admin_page():
    vals = [22, 30, 28, 35, 31, 40, 38, 44, 41, 60, 92, 110, 96, 88]
    mx = max(vals)
    bars = "".join(f'<i class="{"on" if i == len(vals)-1 else ""}{" ev" if i == 10 else ""}" style="height:{round(v/mx*100)}%"></i>' for i, v in enumerate(vals))
    dist = [("3분 이하", 18), ("3~10분", 46), ("10~30분", 27), ("30분 이상", 9)]
    dd = "".join(f'<div><span>{k}</span><span class="b"><i class="{"on" if v == 46 else ""}" style="width:{v*2}%"></i></span><span class="n">{v}%</span></div>' for k, v in dist)
    src = [("PlayGround 홈 PICK", 41), ("검색", 22), ("메이커 페이지 · 팔로우", 17), ("외부 링크 · 공유", 14), ("기타", 6)]
    ss = "".join(f'<div><span>{k}</span><span class="b"><i style="width:{v*2}%"></i></span><span class="n">{v}%</span></div>' for k, v in src)
    body = mg.header2(True, "내 게임") + f'''<main class="wrap">
<div class="crumb2"><a href="#">내 게임</a>{ic("chev")}<span>루프 디버거</span></div>
<div class="mg-h"><span class="art a-loop"></span><span><h1>루프 디버거</h1><span class="row">{mg.status("live","공개")}<span class="m">v1.2 · 11/23 · 브라우저</span></span></span><span class="acts"><span class="btn btn-secondary">{ic("web","ic ic16")}PlayGround 에서 보기</span><span class="btn btn-secondary">스토어 정보 수정</span><span class="btn btn-primary">{ic("up2","ic ic16")}새 버전 올리기</span></span></div>
<nav class="utabs" style="margin-top:22px"><a href="#" aria-current="page">통계</a><a href="#">리뷰 38 <span class="cnt" style="height:18px;min-width:18px;font-size:11px;padding:0 5px">2</span></a><a href="#">버그 제보 1</a><a href="#">버전</a><a href="#">공개 설정</a></nav>
<div class="kpis"><div class="kp"><span>최근 7일 플레이</span><b>1,204</b><small>▲ 12% 지난주보다</small></div><div class="kp"><span>평균 플레이 시간</span><b>14분</b><small>▲ 3분 · v1.2 이후</small></div><div class="kp"><span>추천</span><b>92%</b><small class="dn">리뷰 38 · 새 리뷰 2</small></div><div class="kp"><span>완주</span><b>11%</b><small class="dn">40스테이지 끝까지</small></div></div>
<section class="sec" style="margin-top:36px"><div class="sh">{EAR}<h2>하루 플레이</h2><div class="r"><div class="chips"><button class="chip">7일</button><button class="chip" aria-pressed="true">14일</button><button class="chip">30일</button></div></div></div>
<div class="chart">{bars}<span class="axis"><span>11/13</span><span>11/19</span><span>오늘</span></span></div><p class="m" style="margin:10px 0 0">v1.2 공개(11/23) 뒤 플레이가 두 배가 됐어요. 숫자는 본인에게만 보여요.</p></section>
<section class="sec"><div class="split2"><div><div class="sh">{EAR}<h2 style="font-size:19px">한 판 길이</h2></div><div class="dist">{dd}</div></div><div><div class="sh">{EAR}<h2 style="font-size:19px">어디서 왔나요</h2><span class="sub">L2</span></div><div class="dist">{ss}</div></div></div></section>
<section class="sec"><div class="split2"><div><div class="sh">{EAR}<h2 style="font-size:19px">버그 제보</h2><div class="r"><a class="link" href="#">전체</a></div></div><div class="fb">
<div>{ic("bug","ic ic16")}<span><b>3단계에서 소리가 안 나요</b><span class="env">Windows 11 · Chrome 131 · 1920×1080 · v1.2</span></span><span class="btn btn-secondary btn-sm">답하기</span></div>
<div>{ic("bug","ic ic16")}<span><b>세로 모드에서 블록이 잘려요</b><span class="env">iOS 18 · Safari · 390×844 · v1.1</span></span>{mg.status("live","고침 · v1.2")}</div></div></div>
<div><div class="sh">{EAR}<h2 style="font-size:19px">버전</h2><div class="r"><a class="link" href="#">되돌리기</a></div></div><div class="ver">
<div><b>v1.2</b><span>튜토리얼 축소 · 힌트 수정</span>{mg.status("live","공개 중")}<span class="m">11/23</span></div>
<div><b>v1.1</b><span>편집기 공유 · 효과음 볼륨</span><span class="st st-draft">보관</span><span class="m">10/20</span></div>
<div><b>v1.0</b><span>첫 공개</span><span class="st st-draft">보관</span><span class="m">10/02</span></div></div></div></div></section>
</main>''' + mg.footer()
    memo = "MG-GAME · MG-STATS. 숫자는 메이커 본인에게만 — 행동을 돕는 것만(7일 플레이 · 평균 시간 · 추천 · 완주). 그래프는 단순하게, 업데이트 시점 표시. 버그 제보는 환경 정보와 함께, 버전은 되돌리기 가능."
    html = dt.page("게임 관리 · 통계", body, 2100, memo).replace('data-ground="play"', 'data-ground="make"')
    return html.replace("</style>", CSS + "\n</style>", 1)

def review_page():
    q = [("a-paper", "종이 배 2", "청록상회 · 웹 · 재심사", "2시간", False, True), ("a-demon", "들판의 악마 v2.1", "풀잎 · 설치형 · 업데이트", "5시간", False, False), ("a-halcyon", "할시온 바다", "하늘섬 · 웹 · 처음", "21시간", False, False), ("a-ash", "재의 도시 v1.3", "잿빛토끼 · 설치형 · 업데이트", "30시간", True, False), ("a-grid", "격자 탈출", "새 메이커 · 웹 · 처음", "31시간", True, False)]
    rows = "".join(f'<div class="qrow{" on" if on else ""}"><span class="art {a}"></span><span><b>{t}</b><span class="m">{s}</span></span><span class="age{" late" if late else ""}">{age}</span></div>' for a, t, s, age, late, on in q)
    body = mg.header2(True, "심사 14", ["심사 14", "신고 3", "큐레이션", "공지", "사용자"]).replace('MakersGround</span>', '운영</span>', 1) + f'''<main class="wrap">
<div class="ad-h"><h1>심사 대기열</h1><span class="tag2">운영자</span><span class="m" style="margin-left:8px">대기 14 · 24시간 넘은 것 2 · 오늘 처리 9</span><span style="margin-left:auto" class="chips"><button class="chip" aria-pressed="true">오래된 순</button><button class="chip">처음 올림</button><button class="chip">설치형</button></span></div>
<div class="ad"><div class="q">{rows}</div>
<div class="rv-pane"><div class="top"><span class="art a-paper"></span><span><span class="m">청록상회 · 웹 빌드 · 재심사(보완 요청 후)</span><h2>종이 배 2</h2><span class="row" style="display:flex;gap:6px;margin-top:6px"><span class="tag">탐험</span><span class="tag">20분</span><span class="tag">콘텐츠 표시 없음</span></span></span><span style="margin-left:auto;display:flex;flex-direction:column;gap:6px"><span class="btn btn-primary btn-sm">{ic("play")}실제로 플레이</span><span class="btn btn-secondary btn-sm">지난 심사 보기</span></span></div>
<div class="ck2"><div>{ic("check","ic ic16 y")}자동 검사 통과</div><div>{ic("check","ic ic16 y")}외부 요청 없음</div><div>{ic("check","ic ic16 y")}스크린샷 4장 (지난번 2장)</div><div>{ic("check","ic ic16 y")}대표 그림에 글자 없음</div><div class="flag">{ic("alert","ic ic16 w")}소개에 외부 판매 링크 1개</div><div>{ic("check","ic ic16 y")}콘텐츠 표시 입력됨</div></div>
<div class="reason"><b style="font-size:15px">보완 요청 이유 (메이커에게 그대로 보여요)</b><div class="chips"><button class="chip" aria-pressed="true">외부 판매 링크</button><button class="chip">스크린샷 부족</button><button class="chip">실행 안 됨</button><button class="chip">설명과 다름</button><button class="chip">저작권 의심</button></div>
<textarea aria-label="보완 요청 내용">소개 마지막 줄의 외부 판매 링크를 빼 주세요. 메이커 페이지의 링크 칸에는 넣을 수 있어요.</textarea></div>
<div class="decide"><span class="btn btn-secondary">반려<span class="kbd d">R</span></span><span class="btn btn-secondary">보완 요청<span class="kbd d">E</span></span><span class="btn btn-primary">공개 승인<span class="kbd">A</span></span></div></div></div>
</main>'''
    memo = "AD-REVIEW. 운영자 1~2명이 하루 안에 처리할 수 있게: 왼쪽 오래된 순 대기열(24시간 넘으면 다홍) · 오른쪽 자동 검사 결과 + 사람이 볼 것만 강조 · 이유 칩 + 메이커에게 그대로 가는 문장 · 키보드 A/E/R."
    html = dt.page("심사 대기열", body, 1100, memo).replace('data-ground="play"', 'data-ground="make"')
    return html.replace("</style>", CSS + "\n</style>", 1)

if __name__ == "__main__":
    for name, fn in [("메이커 페이지.dc.html", maker_page), ("게임 관리 · 통계.dc.html", game_admin_page), ("심사 대기열.dc.html", review_page)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
