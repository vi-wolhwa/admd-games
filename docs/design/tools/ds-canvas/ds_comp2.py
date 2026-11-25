# 캔버스 '디자인 시스템 · 컴포넌트 2' — 시안에서 생긴 컴포넌트 견본 (각 시안 모듈의 마크업 · CSS 재사용)
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + [OUT]
import importlib.util
def load(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(HERE, n + ".py")); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
mc, p2, p3, p4, p5, pl, pm, mm = (load(n) for n in ("mg_c", "pages2", "pages3", "pages4", "pages5", "play", "pg_mobile", "mg_mobile"))
dt, mg = p5.dt, p5.mg
ic, face, logo, EAR, status = mg.ic, mg.face, mg.logo, mg.EAR, mg.status

PAGE_CSS = r'''
body{min-width:0}
.dspage{width:1280px;margin:0 auto;padding:56px 40px 96px;display:flex;flex-direction:column;gap:64px}
.dspage > header h1{margin:0;font-size:30px;font-weight:800;letter-spacing:-.02em}
.dspage > header p{margin:10px 0 0;max-width:780px;font-size:16px;line-height:1.65;color:var(--ink-2)}
.grp2 > h2{margin:0 0 18px;font-size:22px;font-weight:800;display:flex;align-items:center;gap:10px}
.cells{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px 36px}
.cells.three{grid-template-columns:repeat(3,minmax(0,1fr))}
.cell2{display:flex;flex-direction:column;gap:10px;min-width:0}
.cell2.wide{grid-column:1 / -1}
.cell2 > .nm{display:flex;align-items:baseline;gap:8px;font-size:14px;font-weight:800}
.cell2 > .nm code{font-size:12px;font-weight:600;color:var(--ink-3);font-family:ui-monospace,Consolas,monospace}
.dspage > div[data-ground]{display:contents}
.cell2 > .nm .cand{font-size:11px;font-weight:800;color:var(--accent-text);background:var(--accent-tint);padding:2px 7px;border-radius:999px}
.spec{position:relative;padding:18px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line);min-width:0}
.spec.dark{background:#101316;color:#FFFFFF}
.spec.pad0{padding:0;overflow:hidden}
.spec .chart{height:160px}
.spec .sheet,.spec .cta-bar,.spec .tabbar{position:relative;left:auto;right:auto;bottom:auto}
.spec .fab{position:relative;right:auto;bottom:auto;display:inline-flex}
.spec .cbar{position:relative;bottom:auto}
.spec.phonew{width:375px;padding:0;overflow:hidden;border-radius:18px}
'''

def cell(name, code, inner, wide=False, cls="", cand=False):
    c = '<span class="cand">후보</span>' if cand else ""
    return f'<div class="cell2{" wide" if wide else ""}"><span class="nm">{name}<code>{code}</code>{c}</span><div class="spec {cls}">{inner}</div></div>'

def grp(title, cells, three=False):
    return f'<section class="grp2"><h2>{EAR}{title}</h2><div class="cells{" three" if three else ""}">{"".join(cells)}</div></section>'

def todo1():
    icn, acc, t, m, (k, lab) = mg.TODOS[0]
    return f'<div class="todo"><div class="td"><span class="ico{" acc" if acc else ""}">{ic(icn,"ic ic16")}</span><span><b>{t}</b><span class="m">{m}</span></span><span class="btn btn-{k} btn-sm">{lab}</span></div></div>'

def build():
    # 11.1 상태 · 진행
    chips = " ".join([status("live", "공개"), status("wait", "검사 중"), status("fix", "보완 요청"), status("draft", "작성 중"), status("no", "반려")])
    vsteps = f'''<div class="vsteps"><div class="vs done"><i>{ic("check","ic ic12")}</i><span><b>작성</b><span class="m">11/24 제출</span></span></div><div class="vs done"><i>{ic("check","ic ic12")}</i><span><b>자동 검사 통과</b></span></div><div class="vs now"><i></i><span><b>심사 — 보완 요청</b><div class="fixbox"><b>{ic("alert")}고칠 것 1개</b>스크린샷을 3장 이상 올려 주세요.</div></span></div><div class="vs"><i></i><span><b style="color:var(--ink-3)">공개</b></span></div></div>'''
    kpis = '<div class="kpis" style="margin:0;grid-template-columns:1fr 1fr"><div class="kp"><span>최근 7일 플레이</span><b>1,204</b><small>▲ 12% 지난주보다</small></div><div class="kp"><span>추천</span><b>92%</b><small class="dn">리뷰 38</small></div></div>'
    vals = [22, 30, 28, 35, 31, 40, 38, 44, 41, 60, 92, 110, 96, 88]; mx = max(vals)
    chart = '<div class="chart">' + "".join(f'<i class="{"on" if i == len(vals)-1 else ""}{" ev" if i == 10 else ""}" style="height:{round(v/mx*100)}%"></i>' for i, v in enumerate(vals)) + '<span class="axis"><span>11/13</span><span>오늘</span></span></div>'
    dist = '<div class="dist">' + "".join(f'<div><span>{k}</span><span class="b"><i class="{"on" if v == 46 else ""}" style="width:{v*2}%"></i></span><span class="n">{v}%</span></div>' for k, v in [("3분 이하", 18), ("3~10분", 46), ("10~30분", 27)]) + "</div>"
    g1 = grp("상태 · 진행", [cell("상태 칩", "StatusChip", f'<div style="display:flex;gap:8px;flex-wrap:wrap">{chips}</div>'),
                           cell("단계 · 가로", "StageSteps", mg.steps(1)),
                           cell("단계 · 세로", "StageSteps vertical", vsteps),
                           cell("숫자 카드", "KpiCard", kpis),
                           cell("막대 그래프", "BarChart", chart),
                           cell("분포 막대", "DistBar", dist)])
    # 11.2 커뮤니티
    rows = "".join(mc.prow(p) for p in mc.POSTS[:3])
    btab = f'''<div class="blist"><div class="brow hd"><span class="k">말머리</span><span>제목</span><span>글쓴이</span><span class="n2">날짜</span><span class="n2">조회</span><span class="n2">좋아요</span></div>
<div class="brow pin"><span class="k">공지</span><span class="tt"><span class="t2">자유 게시판 이용 규칙</span></span><span class="who"><span class="mkb2">운영</span> aDmD</span><span class="n2">11/02</span><span class="n2">2,310</span><span class="n2">—</span></div>
<div class="brow"><span class="k">잡담</span><span class="tt"><span class="t2">오늘 첫 리뷰 받았어요… 손이 떨리네요</span><span class="c">[88]</span></span><span class="who">{face("ㅅ","hong","xs")}<span class="clip">새벽코딩</span></span><span class="n2">12분 전</span><span class="n2">412</span><span class="n2">96</span></div></div>'''
    poll = '<div class="poll" style="margin:0"><span class="q">어느 쪽이 더 해 보고 싶나요? · 83명 · 2일 남음</span><span class="opt"><i style="width:38%"></i><span>A · 잼 버전</span><span>38%</span></span><span class="opt me"><i style="width:62%"></i><span>B · 새로 그림 ✓</span><span>62%</span></span></div>'
    cmt = f'''<div class="cmt" style="border:0;padding-top:0">{face("ㅍ","jjok","md")}<span><span class="hd"><b>픽셀상점</b><span class="mkb2">메이커</span>· 20분 전</span><p>B 요! 실루엣이 바로 읽혀요.</p><span class="ac"><span>좋아요 12</span><span>답글</span><span>신고</span></span></span></div>
<div class="cmt reply" style="border:0">{face("ㅂ","bora","md")}<span><span class="hd"><b>보라네</b><span class="mine">글쓴이</span>· 18분 전</span><p>바로 고쳐 볼게요!</p></span></div>'''
    glink = f'<a class="gamelink" href="#" style="margin:0"><span class="art a-grid"></span><span><b>그리드 러너</b><span class="m">보라네 · 액션 · 3분 · PlayGround 에서 플레이</span></span>{ic("chev","ic ic16")}</a>'
    qrow = '<div class="ql">' + "".join(f'<div class="qi"><b>{t}</b><span class="m">{m}</span><span class="ans {k}"><b>{n}</b>{lab}</span></div>' for t, m, k, n, lab in mg.QS[:2]) + "</div>"
    g2 = '<div data-ground="make">' + grp("커뮤니티", [cell("게시판 칩", "BoardChip", '<div style="display:flex;gap:6px"><span class="board-chip">자유</span><span class="board-chip log">개발일지</span><span class="board-chip">질문</span><span class="board-chip">피드백</span></div>'),
                         cell("글 줄", "PostRow", rows),
                         cell("게시판 표", "BoardTable", btab, wide=True),
                         cell("투표", "Poll", poll), cell("댓글", "CommentItem", cmt),
                         cell("게임 링크 카드", "GameLinkCard", glink), cell("질문 줄", "QuestionRow", qrow),
                         cell("일지 카드", "LogCard", f'<div style="width:300px">{mg.log_card(mg.LOGS[1])}</div>')]) + '</div>'
    # 11.3 메이커 도구
    up = f'''<div class="drop" style="margin:0;height:110px">{ic("up2","ic ic20")}<b>zip 파일을 끌어다 놓거나 눌러서 고르기</b><span class="m">최대 200MB</span></div>
<div class="upfile"><span class="fi">{ic("box","ic ic20")}</span><span><b>paper-boat-2-web.zip</b><span class="bar" style="margin-top:8px"><i style="width:100%"></i></span></span><span class="m">9.2MB · 완료</span></div>
<div class="checks2"><div>{ic("check","ic ic16 y")}<span>index.html 을 찾았어요</span><span class="m"></span></div><div>{ic("alert","ic ic16 w")}<span>소리가 첫 클릭 전에 시작돼요</span><a class="link" href="#" style="font-size:13px">해결 방법</a></div></div>'''
    crop = '<div class="big-art a-paper" style="width:100%;margin:0"><div class="handles"><i style="left:-6px;top:-6px"></i><i style="right:-6px;top:-6px"></i><i style="left:-6px;bottom:-6px"></i><i style="right:-6px;bottom:-6px"></i></div></div>'
    g3 = '<div data-ground="make">' + grp("메이커 도구", [cell("마법사 단계 막대", "WizardStepBar", p3.steps_bar(2).replace('class="wz-steps"', 'class="wz-steps" style="padding:0"'), wide=True),
                            cell("업로드 · 형식 검사", "Dropzone · UploadFileRow · CheckList", up), cell("자르기", "CropPreview", crop),
                            cell("내 게임 줄", "MakerGameRow", f'<div class="mg-rows">{mg.game_row(mg.GAMES[0])}</div>', wide=True, cand=True),
                            cell("할 일 줄", "TodoRow", todo1(), cand=True)]) + '</div>'
    # 11.4 신뢰
    verdict = f'<div class="verdict" style="margin:0"><span class="shield">{ic("shield")}</span><div><h2>문제를 찾지 못했어요</h2><p>올라온 파일 그대로를 검사 엔진 3종으로 확인했어요.</p></div><div class="when">검사 시각<b>11.24 14:02</b></div></div>'
    files = f'<div class="files"><div class="file on">{ic("pc")}<span><b>Windows</b><span class="m">v1.2 · 312MB · .exe</span></span>{ic("check","ic ic16")}</div><div class="file">{ic("pc")}<span><b>macOS</b><span class="m">v1.2 · 298MB · 서명 없음</span></span><span></span></div></div>'
    g4 = grp("신뢰 (다운로드 · 검사)", [cell("검사 결과", "ScanVerdict", verdict, wide=True),
                                       cell("검사 띠", "ScanBanner", f'<div class="scan">{ic("shield")}<span>보안 검사 통과 · 엔진 3종</span><a href="#">리포트</a></div>'),
                                       cell("파일 고르기", "FileChoice", files),
                                       cell("지문", "HashChip", '<span class="hash">9f2c4e81d0b7…3f5a71b03 <span>전체 복사</span></span>')])
    # 11.5 탐색 · 알림 · 설정
    def frow(label, items, on):
        return f'<div class="frow"><b>{label}</b><div class="chips">' + "".join(f'<button class="chip"{" aria-pressed=\"true\"" if x in on else ""}>{x}</button>' for x in items) + "</div></div>"
    fbox = '<div class="filters" style="margin:0">' + frow("장르", ["전체", "퍼즐", "액션", "탐험"], ["퍼즐"]) + frow("한 판", ["상관없음", "3분 이하", "15분 이하"], ["15분 이하"]) + "</div>"
    applied = '<div class="applied" style="margin:0"><span class="x">퍼즐 ✕</span><span class="x">15분 이하 ✕</span><a class="link" href="#" style="font-size:13.5px">초기화</a><span class="sort"><span class="on">추천순</span><span>최신순</span></span></div>'
    relax = '<div class="relax" style="margin:0"><b>조건을 조금 넓혀 볼까요?</b><div class="chips"><button class="chip">‘같이’ 빼면 +30</button></div></div>'
    sw = '<span class="switch on" style="display:inline-block;width:40px;height:24px;border-radius:999px;background:var(--accent);position:relative"></span>'
    srow = f'''<div class="srow" style="border:0"><span><b>지금 하는 게임 · 최근 플레이</b><span class="m">친구에게만 보여요</span></span><span class="switch on"></span></div>
<div class="srow"><span><b>라이브러리</b></span><span class="seg"><span>모두</span><span class="on">친구만</span><span>나만</span></span></div>
<div class="danger-zone"><div class="srow" style="border:0;padding:0;min-height:0"><span><b style="color:var(--danger-text)">탈퇴하기</b><span class="m">되돌릴 수 없어요</span></span><span class="btn btn-secondary btn-sm" style="color:var(--danger-text)">탈퇴</span></div></div>'''
    g5 = grp("탐색 · 알림 · 설정", [cell("필터 상자", "FilterBox", fbox, wide=True),
                                   cell("적용 조건 · 정렬", "AppliedChip · SortTabs", applied), cell("조건 넓히기", "RelaxSuggest", relax),
                                   cell("알림 줄", "NotificationItem", "".join(p5.ni(n) for n in (p5.NOTI[0], p5.NOTI[4]))),
                                   cell("설정 줄 · 분할 선택 · 위험 구역", "SettingsRow · Segmented · DangerZone", srow),
                                   cell("공개 범위 표시", "VisibilityTag", f'<span class="vis-tag">{ic("duo","ic ic12")}친구에게만 보여요</span>'),
                                   cell("테마 전환", "ThemeToggle", f'<span style="display:flex;gap:8px;align-items:center">{mg.THEME_BTN}<span class="m">라이트 = 달 · 다크 = 해 (눌러 보세요)</span></span>')])
    # 11.6 플레이
    pause = pl.screen_pause().split('<div class="pause">')[1].split('</div></div></div>')[0]
    g6 = grp("플레이", [cell("플레이어 바", "PlayerBar", f'<div style="position:relative;height:48px">{pl.bar()}</div>', wide=True, cls="dark pad0"),
                       cell("일시정지", "PauseMenu", f'<div class="pause" style="margin:0 auto">{pause}</div>', cls="dark"),
                       cell("결과 카드", "ResultCard", f'<div class="result" style="min-height:0;padding:24px 26px"><span class="bg a-loop"></span><span class="k">스테이지 18 끝</span><span class="big disp" style="font-size:56px">03:42</span><span class="best">{ic("crown","ic ic12")}내 최고 기록</span></div>')])
    # 11.7 모바일
    tabbar = '<nav class="tabbar">' + "".join(f'<a href="#"{" aria-current=\"page\"" if i == 0 else ""}>{ic(t)}{n}</a>' for i, (t, n) in enumerate([("home", "홈"), ("box", "게임"), ("bm", "라이브러리"), ("bell", "알림"), ("user", "나")])) + "</nav>"
    sheet = f'<div class="sheet" style="box-shadow:none"><div class="grab"></div><h3>필터</h3><div class="grp"><b>장르</b><div class="chips"><button class="chip" aria-pressed="true">퍼즐</button><button class="chip">액션</button></div></div><div style="display:grid;grid-template-columns:1fr 2fr;gap:8px"><span class="mbtn" style="background:var(--sunken);font-size:15px">초기화</span><span class="mbtn btn-primary" style="font-size:15px">32개 보기</span></div></div>'
    cta = f'<div class="cta-bar" style="padding-bottom:12px"><span class="sq">{ic("bm","ic ic20")}</span><span class="sq">{ic("up2","ic ic20")}</span><span class="main">{ic("play","ic ic16")}지금 플레이</span></div>'
    flag = f'<div style="width:200px">{pm.card("a-grid", "그리드 러너", "보라네", "ㅂ", "bora", "액션 3분", False)}</div>'
    g7 = grp("모바일", [cell("상단 바", "MobileTopBar", pm.top(), cls="phonew"), cell("탭바", "MobileTabBar", tabbar, cls="phonew"),
                       cell("아래 시트", "BottomSheet", sheet, cls="phonew"), cell("고정 버튼 줄", "StickyCtaBar", cta, cls="phonew"),
                       cell("기기 표시", "DeviceFlag", flag), cell("글쓰기 버튼 · 댓글 입력", "WriteFab · CommentBar", f'<span class="fab">{ic("pen","ic ic16")}글쓰기</span><div class="cbar" style="margin-top:14px;border:0">{face("ㅇ","olive","")}<span>댓글 달기</span><span class="btn btn-primary btn-sm" style="height:34px">등록</span></div>')])
    body = f'''<div class="dspage"><header><h1>컴포넌트 2 — 시안에서 생긴 것</h1><p>페이지 시안을 만들며 생긴 컴포넌트를 정식으로 등록한 견본. 각 시안의 실제 마크업 · CSS 를 그대로 가져와 그렸다. 명세: <b>docs/design/system/03-components.md §11</b>. ‘후보’ 는 비교 시안에서만 쓰였고 해당 페이지를 그릴 때 다시 검토.</p></header>
{g1}{g2}{g3}{g4}{g5}{g6}{g7}</div>'''
    memo = "시안 27개에서 나온 컴포넌트 40여 개를 7묶음으로(상태 · 커뮤니티 · 메이커 도구 · 신뢰 · 탐색/알림/설정 · 플레이 · 모바일). Tweaks 의 theme 으로 다크 확인."
    css = mc.CSS + mc.M_CSS2 + p2.CSS + p3.CSS + p4.CSS + p5.CSS + pl.CSS + mm.M_CSS + pm.CSS + PAGE_CSS
    html = dt.page("디자인 시스템 · 컴포넌트 2", body, 4200, memo)
    return html.replace("</style>", css + "\n</style>", 1)

if __name__ == "__main__":
    html = build()
    open(os.path.join(OUT, "DS03-components-2.dc.html"), "w", encoding="utf-8").write(html)
    print(len(html))
