# MakersGround 커뮤니티 중심 개정(M1~M3 결정): 홈 C · 커뮤니티 목록 · 글 보기 · 모바일
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + [OUT]
import importlib.util
spec = importlib.util.spec_from_file_location("mgm", os.path.join(HERE, "mg_mobile.py"))
mgm = importlib.util.module_from_spec(spec); spec.loader.exec_module(mgm)
mg = mgm.mg
ic, face, logo, EAR, status = mg.ic, mg.face, mg.logo, mg.EAR, mg.status

# 게시판 — 처음엔 5개(+공지). 늘리는 규칙은 07-community.md
BOARDS = [("free", "자유"), ("log", "개발일지"), ("qna", "질문"), ("fb", "피드백"), ("team", "팀원 모집")]
# (게시판, 말머리, 제목, 댓글, 얼굴, 색, 닉, 시각, 조회, 좋아요, 그림, 상태)
POSTS = [
    ("자유", "잡담", "오늘 첫 리뷰 받았어요… 손이 떨리네요", 88, "ㅅ", "hong", "새벽코딩", "12분 전", 412, 96, False, ""),
    ("피드백", "", "타이틀 화면 두 가지 중 뭐가 나아요?", 27, "ㅂ", "bora", "보라네", "25분 전", 230, 31, True, "투표 중"),
    ("질문", "웹 빌드", "Unity WebGL 빌드가 아이폰 사파리에서 멈춰요", 2, "ㄱ", "gyul", "귤껍질", "40분 전", 97, 4, False, "해결"),
    ("자유", "정보", "무료로 쓸 수 있는 효과음 사이트 정리 (2026)", 15, "ㅊ", "cheongnok", "청록상회", "1시간 전", 655, 140, False, ""),
    ("개발일지", "", "웹 빌드 40MB를 9MB로 줄인 방법", 31, "ㄴ", "haneul", "노을공방", "2시간 전", 1204, 112, True, ""),
    ("자유", "고민", "회사 다니면서 게임 끝까지 만드는 법, 다들 어떻게 하세요?", 64, "ㅈ", "ju", "잿빛토끼", "3시간 전", 980, 77, False, ""),
    ("피드백", "", "점프가 둔하게 느껴지는데 이유를 모르겠어요 (GIF)", 19, "ㅍ", "pul", "풀잎", "4시간 전", 310, 22, True, ""),
    ("팀원 모집", "", "픽셀 아티스트 1명 · 3개월 · 온라인", 5, "ㅈ", "ju", "잿빛토끼", "5시간 전", 201, 9, False, "모집 중"),
    ("자유", "잡담", "다들 주말에 몇 시간 작업하세요?", 42, "ㅁ", "olive", "모래시계", "6시간 전", 377, 18, False, ""),
    ("질문", "운영", "다른 사이트에 올린 게임을 여기에도 올려도 되나요?", 4, "ㄷ", "jadu", "달빛", "어제", 155, 6, False, "해결"),
]
HOT = [p for p in sorted(POSTS, key=lambda x: -x[8])][:6]

CSS = r'''
.board-chip{display:inline-flex;align-items:center;height:22px;padding:0 8px;border-radius:6px;background:var(--sunken);font-size:12px;font-weight:800;color:var(--ink-2);white-space:nowrap}
.board-chip.log{background:var(--accent-tint);color:var(--accent-text)}
.prow{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center;min-height:52px;padding:8px 6px;border-top:1px solid var(--line)}
.prow:first-child{border-top:0}
.prow:hover{background:var(--sunken);border-radius:10px}
.prow .tt{display:flex;align-items:center;gap:6px;min-width:0;font-size:15px;font-weight:600}
.prow .tt .t2{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.prow .tt .c{color:var(--accent-text);font-weight:800;font-size:13.5px;flex:none}
.prow .tt .ic{color:var(--ink-3);flex:none}
.prow .side{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--ink-3);white-space:nowrap}
.st-sm{height:20px;font-size:11.5px;padding:0 7px}
.hot{display:flex;flex-direction:column;counter-reset:h}
.hot > div{display:grid;grid-template-columns:28px minmax(0,1fr);gap:10px;align-items:start;padding:11px 0;border-top:1px solid var(--line)}
.hot > div:first-child{border-top:0}
.hot > div::before{counter-increment:h;content:counter(h);font-size:17px;font-weight:800;color:var(--ink-3);text-align:center;line-height:1.3}
.hot > div:nth-child(-n+3)::before{color:var(--accent-text)}
.hot b{display:block;font-size:14.5px;font-weight:700;line-height:1.45}
.hot .m{display:block;margin-top:3px;font-size:12.5px}
.cm-grid{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:48px;align-items:start}
.fbg{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px}
.fbc{display:flex;flex-direction:column;gap:8px}
.fbc .art{border-radius:var(--radius-lg)}
.fbc b{font-size:15px;line-height:1.45}
.fbc .by{display:flex;align-items:center;gap:6px;font-size:12.5px;color:var(--ink-3)}
.vote{display:flex;height:6px;border-radius:999px;overflow:hidden;background:var(--sunken-hover)}
.vote i{background:var(--accent)}
.write-fab{display:inline-flex;align-items:center;gap:6px}
/* 커뮤니티 목록 */
.cm-head{display:flex;align-items:flex-end;gap:16px;margin-top:28px}
.cm-head h1{margin:0;font-size:28px;font-weight:800;letter-spacing:-.02em}
.cm-head .m{padding-bottom:5px;font-size:14px}
.cm-head .btn{margin-left:auto}
.cm-tabs{margin-top:16px}
.cm-tabs a .n{margin-left:5px;font-size:12px;color:var(--ink-3);font-weight:700}
.cm-desc{display:flex;align-items:center;gap:12px;margin:18px 0 10px}
.cm-desc .chips .chip{height:34px;font-size:13.5px;padding:0 13px}
.cm-desc .search{margin-left:auto;width:240px}
.cm-sort{display:flex;gap:4px;font-size:13.5px;font-weight:700;color:var(--ink-3)}
.cm-sort span{padding:6px 8px;border-radius:8px}
.cm-sort span.on{color:var(--ink-1);background:var(--sunken)}
.blist{display:flex;flex-direction:column;border-top:2px solid var(--ink-1)}
.brow{display:grid;grid-template-columns:72px minmax(0,1fr) 150px 80px 64px 64px;gap:12px;align-items:center;min-height:54px;padding:6px 8px;border-bottom:1px solid var(--line);font-size:14px}
.brow.hd{min-height:40px;font-size:12.5px;font-weight:700;color:var(--ink-3)}
.brow.pin{background:var(--sunken)}
.brow.pin .k{color:var(--accent-text);font-weight:800}
.brow:not(.hd):hover{background:var(--sunken)}
.brow .k{font-size:12.5px;font-weight:700;color:var(--ink-3);text-align:center}
.brow .tt{display:flex;align-items:center;gap:6px;min-width:0;font-weight:600}
.brow .tt .t2{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.brow .tt .c{color:var(--accent-text);font-weight:800;font-size:13px;flex:none}
.brow .tt .ic{color:var(--ink-3);flex:none}
.brow .who{display:flex;align-items:center;gap:6px;min-width:0;color:var(--ink-2)}
.brow .n2{text-align:right;color:var(--ink-3);font-variant-numeric:tabular-nums;font-size:13px}
.pager2{display:flex;justify-content:center;gap:4px;margin-top:24px}
.pager2 span{display:grid;place-items:center;min-width:36px;height:36px;padding:0 8px;border-radius:10px;font-size:14px;font-weight:700;color:var(--ink-2)}
.pager2 span.on{background:var(--ink-1);color:var(--bg)}
.board-rule{margin-top:40px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.board-rule > div{padding:16px 18px;border-radius:var(--radius-lg);background:var(--sunken);font-size:13.5px;line-height:1.6;color:var(--ink-2)}
.board-rule b{display:block;color:var(--ink-1);font-size:14.5px;margin-bottom:4px}
/* 글 보기 */
.post{width:820px;margin:0 auto}
.post .crumb2{margin-top:28px}
.post h1{margin:12px 0 0;font-size:30px;line-height:1.35;font-weight:800;letter-spacing:-.02em;text-wrap:balance}
.post .by{display:flex;align-items:center;gap:10px;margin-top:16px;padding-bottom:20px;border-bottom:1px solid var(--line);font-size:14px;color:var(--ink-3)}
.post .by b{color:var(--ink-1);font-size:15px}
.post .by .sp{margin-left:auto;display:flex;gap:2px}
.post .body{padding:28px 0 8px;font-size:17px;line-height:1.85}
.post .body p{margin:0 0 18px}
.post .imgs{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0 18px}
.post .imgs figure{margin:0;display:flex;flex-direction:column;gap:6px;font-size:13px;color:var(--ink-3);font-weight:700}
.post .imgs .art{border-radius:12px}
.poll{display:flex;flex-direction:column;gap:8px;margin:10px 0 24px;padding:18px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line)}
.poll .q{font-size:15px;font-weight:800;margin-bottom:4px}
.poll .opt{position:relative;display:flex;align-items:center;justify-content:space-between;height:44px;padding:0 14px;border-radius:10px;background:var(--sunken);overflow:hidden;font-size:15px;font-weight:700}
.poll .opt i{position:absolute;left:0;top:0;bottom:0;background:var(--accent-tint-2)}
.poll .opt span{position:relative}
.poll .opt.me{box-shadow:inset 0 0 0 2px var(--accent)}
.gamelink{display:grid;grid-template-columns:120px minmax(0,1fr) auto;gap:14px;align-items:center;padding:10px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line);margin-bottom:24px}
.gamelink .art{border-radius:9px}
.gamelink b{display:block;font-size:15px}
.reacts{display:flex;justify-content:center;gap:8px;padding:12px 0 28px;border-bottom:1px solid var(--line)}
.reacts .btn .n{font-weight:800}
.reacts .btn.on{background:var(--accent-tint);color:var(--accent-text)}
.cmts{padding-top:24px}
.cmts h3{margin:0 0 14px;font-size:18px;font-weight:800;display:flex;align-items:center;gap:8px}
.cmt-in{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center;padding:12px;border-radius:var(--radius-lg);background:var(--sunken);font-size:15px;color:var(--ink-3)}
.cmt{display:grid;grid-template-columns:auto minmax(0,1fr);gap:12px;padding:18px 0;border-bottom:1px solid var(--line)}
.cmt .hd{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--ink-3)}
.cmt .hd b{color:var(--ink-1);font-size:14px}
.cmt p{margin:6px 0 8px;font-size:15px;line-height:1.65}
.cmt .ac{display:flex;gap:14px;font-size:12.5px;color:var(--ink-3);font-weight:700}
.cmt.reply{margin-left:44px}
.mine{display:inline-flex;align-items:center;height:20px;padding:0 7px;border-radius:999px;background:var(--accent);color:#FFFFFF;font-size:11px;font-weight:800}
.mkb2{display:inline-flex;align-items:center;height:20px;padding:0 7px;border-radius:999px;background:var(--sunken-hover);color:var(--ink-2);font-size:11px;font-weight:800}
.more-list{margin-top:44px}
'''

def ptitle(p, maxc=None):
    b, tag, t, c, *_ = p
    img = ic("pad", "ic ic12") if False else ""
    return t

def prow(p, show_board=True):
    b, tag, t, c, ch, col, who, when, views, likes, img, st = p
    chip = f'<span class="board-chip{" log" if b == "개발일지" else ""}">{b if show_board else (tag or b)}</span>'
    imgi = '<svg class="ic ic12" viewBox="0 0 16 16"><rect x="2" y="3" width="12" height="10" rx="2"></rect><circle cx="6" cy="7" r="1.2"></circle><path d="M3 12l3.5-3 2.5 2 2-1.5 2.5 2.5"></path></svg>' if img else ""
    stc = ""
    if st == "해결": stc = f'<span class="st st-live st-sm">{ic("check")}해결</span>'
    elif st == "모집 중": stc = '<span class="st st-fix st-sm">모집 중</span>'
    elif st == "투표 중": stc = '<span class="st st-wait st-sm">투표 중</span>'
    return f'''<div class="prow">{chip}<span class="tt"><span class="t2">{t}</span>{imgi}<span class="c">[{c}]</span>{stc}</span><span class="side">{face(ch, col, "xs")}{who} · {when}</span></div>'''

def gband():
    return f'''<section class="wrap" style="margin-top:28px"><div class="gband" style="margin-top:0"><div><b>만들고, 묻고, 수다 떠는 곳</b><p>게임을 올리지 않아도 누구나 글을 쓸 수 있어요. 첫 게임은 PC 에서 올려 보세요 — 광고 · 수수료 없음 · 보안 검사 무료.</p></div><span style="display:flex;gap:8px"><span class="btn btn-glass">처음 올리는 분</span><span class="btn btn-on-color">로그인하고 글쓰기</span></span></div></section>'''

def home_c():
    tabs = '<div class="chips"><button class="chip" aria-pressed="true">전체</button>' + "".join(f'<button class="chip">{n}</button>' for _, n in BOARDS) + "</div>"
    now = "".join(prow(p) for p in POSTS[:9])
    hot = "".join(f'<div><span><b>{p[2]}</b><span class="m">{p[0]} · 댓글 {p[3]} · 조회 {p[8]:,}</span></span></div>' for p in HOT)
    l = mg.LOGS[1]
    feat = f'''<section class="sec wrap"><div class="sh">{EAR}<h2>이번 주 일지 PICK</h2></div>
<div class="feat"><span class="art {l[0]}"><span class="shots"></span><span class="badge mk" style="--overlay-inset:12px">{ic("crown","ic ic12")}PICK</span></span>
<div><span class="board-chip log">개발일지</span><h3>{l[1]}</h3><p>{l[2]} 압축 설정 표와 전후 비교 빌드를 같이 올려 두었어요.</p>
<div class="by">{face(l[3], l[4], "md")}<span><b>{l[5]}</b> · {l[6]} · 3일 전</span><span class="react" style="margin-left:14px"><span>{ic("heart")}{l[7]}</span><span>{ic("cmt")}{l[8]}</span></span></div>
<div style="display:flex;gap:8px;margin-top:22px"><span class="btn btn-primary">읽기</span><span class="btn btn-secondary">{ic("play","ic ic16")}테셀레이트 플레이</span></div></div></div></section>'''
    fbs = [("a-grid", "타이틀 화면 두 가지 중 뭐가 나아요?", "ㅂ", "bora", "보라네", 27, 62), ("a-demon", "점프가 둔하게 느껴지는데 이유를 모르겠어요", "ㅍ", "pul", "풀잎", 19, None), ("a-halcyon", "바다 색감 너무 어두운가요?", "ㅎ", "haneul", "하늘섬", 11, None), ("a-ash", "보스 2페이즈 예고 동작 영상", "ㅈ", "ju", "잿빛토끼", 23, None)]
    fbg = "".join(f'''<div class="fbc"><span class="art {a}"><span class="shots"></span>{('<span class="badge ink">투표 중</span>' if v else '')}</span><b class="two-line">{t}</b>{(f'<span class="vote"><i style="width:{v}%"></i></span>' if v else '')}<span class="by">{face(ch,col,"xs")}{who} · 댓글 {n}</span></div>''' for a, t, ch, col, who, n, v in fbs)
    body = mg.header2(True, "홈") .replace("", "")
    body = mg.signed_block(mg.header2(True, "홈"), mg.header2(False, "홈")) + mg.signed_block("", gband()) + f'''
<section class="sec wrap" style="margin-top:36px"><div class="cm-grid">
<div><div class="sh">{EAR}<h2>지금 커뮤니티</h2><div class="r">{tabs}</div></div><div>{now}</div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-top:12px"><a class="link" href="#">커뮤니티 전체 보기 ›</a><span class="btn btn-primary btn-sm">{ic("pen")}글쓰기</span></div></div>
<div><div class="sh">{EAR}<h2 style="font-size:19px">오늘 많이 본 글</h2></div><div class="hot">{hot}</div></div>
</div></section>''' + feat + f'''
<section class="sec wrap"><div class="sh">{EAR}<h2>피드백을 기다리는 작업</h2><span class="sub">스크린샷 · GIF 를 올리고 의견을 물어봐요</span><div class="r"><a class="link" href="#">피드백 게시판</a></div></div><div class="fbg">{fbg}</div></section>
''' + mg.logs_band("새 개발일지", 3, False) + f'<section class="sec wrap">{mg.qa_block()}</section>' + mg.new_games() + mg.jam() + mg.footer()
    memo = "M1 결정 반영: B 기반 · 홈에서 내 게임 제거 · 커뮤니티가 주인공. 지금 커뮤니티(게시판 섞인 최신 글) + 오늘 많이 본 글 → 일지 PICK → 피드백(그림 게시판) → 개발일지 → 질문 · 모집 → 공개된 게임 → 잼. 내 게임은 메뉴와 알림으로."
    html = mg.page("MakersGround 홈 C · 커뮤니티", body, 3200, memo)
    return html.replace("</style>", CSS + "\n</style>", 1).replace('"startSignedIn":{"editor":"boolean","default":true', '"startSignedIn":{"editor":"boolean","default":false')

def community_list():
    tabs = '<nav class="utabs cm-tabs"><a href="#">전체</a>' + "".join(f'<a href="#"{" aria-current=\"page\"" if n == "자유" else ""}>{n}<span class="n">{k}</span></a>' for (_, n), k in zip(BOARDS, ["1,240", "86", "312", "158", "24"])) + "</nav>"
    pins = f'''<div class="brow pin"><span class="k">공지</span><span class="tt"><span class="t2">자유 게시판 이용 규칙 — 홍보 글은 한 달에 한 번</span></span><span class="who">{logo() and '<span class="mkb2">운영</span>'} aDmD</span><span class="n2">11/02</span><span class="n2">2,310</span><span class="n2">—</span></div>
<div class="brow pin"><span class="k">공지</span><span class="tt"><span class="t2">새 게시판 ‘피드백’ 을 열었어요</span></span><span class="who"><span class="mkb2">운영</span> aDmD</span><span class="n2">11/20</span><span class="n2">1,488</span><span class="n2">—</span></div>'''
    free = [p for p in POSTS if p[0] == "자유"] + [
        ("자유", "잡담", "aDmD 고양이 로고 귀여워서 스티커로 만들었어요", 33, "ㄷ", "jadu", "달빛", "어제", 540, 71, True, ""),
        ("자유", "정보", "Godot 4.5 웹 내보내기 바뀐 점 정리", 21, "ㅊ", "cheongnok", "청록상회", "어제", 812, 64, False, ""),
        ("자유", "고민", "첫 게임을 너무 크게 잡은 것 같아요", 39, "ㄱ", "gyul", "귤껍질", "2일 전", 433, 25, False, ""),
        ("자유", "잡담", "잼 끝나고 다들 뭐 하세요", 12, "ㅂ", "bora", "보라네", "2일 전", 190, 8, False, ""),
        ("자유", "정보", "무료 폰트 중 게임 UI 에 괜찮은 것들", 17, "ㅎ", "haneul", "하늘섬", "3일 전", 702, 58, True, ""),
    ]
    def brow(p, i):
        b, tag, t, c, ch, col, who, when, views, likes, img, st = p
        imgi = '<svg class="ic ic12" viewBox="0 0 16 16"><rect x="2" y="3" width="12" height="10" rx="2"></rect><circle cx="6" cy="7" r="1.2"></circle><path d="M3 12l3.5-3 2.5 2 2-1.5 2.5 2.5"></path></svg>' if img else ""
        return f'<div class="brow"><span class="k">{tag}</span><span class="tt"><span class="t2">{t}</span>{imgi}<span class="c">[{c}]</span></span><span class="who">{face(ch,col,"xs")}<span class="clip">{who}</span></span><span class="n2">{when}</span><span class="n2">{views:,}</span><span class="n2">{likes}</span></div>'
    rows = "".join(brow(p, i) for i, p in enumerate(free))
    body = mg.header2(True, "커뮤니티") + f'''<main class="wrap">
<div class="cm-head"><h1>커뮤니티</h1><span class="m">메이커도, 플레이어도, 만들어 보고 싶은 사람도 누구나</span><span class="btn btn-primary">{ic("pen","ic ic16")}글쓰기</span></div>
{tabs}
<div class="cm-desc"><div class="chips"><button class="chip" aria-pressed="true">전체</button><button class="chip">잡담</button><button class="chip">정보</button><button class="chip">고민</button></div><div class="cm-sort"><span class="on">최신</span><span>인기</span><span>댓글 많은</span></div><div class="search">{ic("search")}자유 게시판에서 찾기</div></div>
<div class="blist"><div class="brow hd"><span class="k">말머리</span><span>제목</span><span>글쓴이</span><span class="n2">날짜</span><span class="n2">조회</span><span class="n2">좋아요</span></div>{pins}{rows}</div>
<div class="pager2"><span>‹</span><span class="on">1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>›</span></div>
<div class="board-rule"><div><b>자유</b>무엇이든 편하게 — 잡담 · 정보 · 고민. 홍보는 한 달에 한 번.</div><div><b>게시판은 필요할 때 늘려요</b>한 말머리 글이 한 달 동안 많아지면(주 20개 이상) 게시판으로 독립시켜요.</div><div><b>게시판 제안</b>새 게시판이 필요하면 자유 게시판에 ‘제안’ 으로 올려 주세요.</div></div>
</main>''' + mg.footer()
    memo = "커뮤니티 목록(MG-COMM). 처음 게시판 5개: 자유(잡담·정보·고민) · 개발일지 · 질문 · 피드백 · 팀원 모집. 말머리로 먼저 나누고, 커지면 게시판으로 독립. 목록은 한국 커뮤니티에 익숙한 표 형식(말머리 · 제목[댓글] · 글쓴이 · 날짜 · 조회 · 좋아요)."
    html = mg.page("커뮤니티 목록", body, 1500, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

def post_view():
    more = "".join(prow(p) for p in [x for x in POSTS if x[0] == "피드백"] + POSTS[:3])
    body = mg.header2(True, "커뮤니티") + f'''<main class="post">
<div class="crumb2"><a href="#">커뮤니티</a>{ic("chev")}<a href="#">피드백</a></div>
<h1>타이틀 화면 두 가지 중 뭐가 나아요?</h1>
<div class="by">{face("ㅂ","bora","md")}<span><b>보라네</b> <span class="mkb2">메이커 · 게임 2</span><br>25분 전 · 조회 230</span><span class="sp"><button class="icon-btn" aria-label="저장">{ic("bm","ic ic16")}</button><button class="icon-btn" aria-label="공유">{ic("up2","ic ic16")}</button><button class="icon-btn" aria-label="신고">{ic("alert","ic ic16")}</button></span></div>
<div class="body"><p>‘그리드 러너’ 정식판 타이틀을 두 가지로 만들어 봤어요. A 는 잼 때 쓰던 걸 다듬은 거고, B 는 새로 그렸어요. 첫인상으로 어느 쪽이 더 해 보고 싶나요?</p>
<div class="imgs"><figure><span class="art a-grid"></span>A · 잼 버전 다듬기</figure><figure><span class="art a-tess"></span>B · 새로 그림</figure></div>
<div class="poll"><span class="q">어느 쪽이 더 해 보고 싶나요? · 83명 참여 · 2일 남음</span><span class="opt"><i style="width:38%"></i><span>A · 잼 버전</span><span>38%</span></span><span class="opt me"><i style="width:62%"></i><span>B · 새로 그림 {ic("check","ic ic12")}</span><span>62%</span></span></div>
<p>글자 크기나 색 의견도 환영이에요!</p></div>
<a class="gamelink" href="#"><span class="art a-grid"></span><span><b>그리드 러너</b><span class="m">보라네 · 액션 · 3분 · PlayGround 에서 플레이</span></span>{ic("chev","ic ic16")}</a>
<div class="reacts"><span class="btn btn-secondary on">{ic("heart","ic ic16")}좋아요 <span class="n">31</span></span><span class="btn btn-secondary">{ic("bm","ic ic16")}저장</span></div>
<section class="cmts"><h3>댓글 <span style="color:var(--accent-text)">27</span><span style="margin-left:auto" class="cm-sort"><span class="on">등록순</span><span>최신순</span></span></h3>
<div class="cmt-in">{face("ㅇ","olive","md")}<span>따뜻한 말로 의견을 남겨 주세요</span><span class="btn btn-primary btn-sm">등록</span></div>
<div class="cmt">{face("ㅍ","jjok","md")}<span><span class="hd"><b>픽셀상점</b><span class="mkb2">메이커</span>· 20분 전</span><p>B 요! 캐릭터 실루엣이 바로 읽혀요. 다만 로고 아래 그림자가 조금 무거운 느낌이라 한 단계만 연하게 하면 좋겠어요.</p><span class="ac"><span>좋아요 12</span><span>답글</span><span>신고</span></span></span></div>
<div class="cmt reply">{face("ㅂ","bora","md")}<span><span class="hd"><b>보라네</b><span class="mine">글쓴이</span>· 18분 전</span><p>오 그림자 맞아요. 바로 고쳐 볼게요 고마워요!</p><span class="ac"><span>좋아요 3</span><span>답글</span></span></span></div>
<div class="cmt">{face("ㅅ","hong","md")}<span><span class="hd"><b>새벽코딩</b>· 15분 전</span><p>A 의 색감이 더 게임 느낌이 나긴 하는데… 처음 보는 사람이면 B 가 더 끌릴 듯해요.</p><span class="ac"><span>좋아요 5</span><span>답글</span><span>신고</span></span></span></div>
</section>
<section class="more-list"><div class="sh">{EAR}<h2 style="font-size:18px">피드백 게시판 다른 글</h2></div>{more}</section>
</main>''' + mg.footer()
    memo = "글 보기(MG-POST). 본문 820px 한 열 · 17px/1.85 읽기 좋은 글자. 피드백 게시판은 그림 · 간단 투표 · 게임 링크 카드. 댓글: 글쓴이 · 메이커 표시, 답글 한 단계, 신고. 아래에 같은 게시판 다른 글."
    html = mg.page("커뮤니티 글 보기", body, 2300, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

# ── 모바일 (M3: 게임 업로드 UI 없음) ──
M_CSS2 = r'''
.mchips{display:flex;gap:6px;overflow:hidden;padding:0 18px;margin:0 -18px 6px}
.mchips .chip{height:34px;font-size:13.5px;padding:0 12px;flex:none}
.mpost{display:flex;flex-direction:column;gap:5px;padding:12px 0;border-top:1px solid var(--line)}
.mpost:first-child{border-top:0}
.mpost .tt{display:flex;align-items:flex-start;gap:6px;font-size:15px;font-weight:700;line-height:1.45}
.mpost .tt .c{color:var(--accent-text);font-weight:800;font-size:13px;flex:none;margin-top:2px}
.mpost .by{display:flex;align-items:center;gap:6px;font-size:12.5px;color:var(--ink-3)}
.fab{position:absolute;right:18px;bottom:100px;z-index:7;display:flex;align-items:center;gap:6px;height:48px;padding:0 18px;border-radius:999px;background:var(--accent);color:#FFFFFF;font-weight:800;font-size:15px;box-shadow:var(--shadow-float)}
.mfeat{display:flex;flex-direction:column;gap:8px}
.mfeat .art{border-radius:14px}
.mfeat b{font-size:17px;line-height:1.4}
.mp-body{padding:0 18px;font-size:16px;line-height:1.8}
.mp-body h1{margin:4px 0 0;font-size:22px;line-height:1.4;font-weight:800}
.mp-body .by{display:flex;align-items:center;gap:8px;margin:12px 0 14px;font-size:13px;color:var(--ink-3)}
.mp-body p{margin:0 0 12px}
.mp-body .imgs{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px}
.mp-body .imgs .art{border-radius:10px}
.mpoll{display:flex;flex-direction:column;gap:6px;margin-bottom:14px}
.mpoll .opt{position:relative;display:flex;justify-content:space-between;align-items:center;height:44px;padding:0 12px;border-radius:10px;background:var(--sunken);overflow:hidden;font-size:14px;font-weight:700}
.mpoll .opt i{position:absolute;left:0;top:0;bottom:0;background:var(--accent-tint-2)}
.mpoll .opt span{position:relative}
.mpoll .opt.me{box-shadow:inset 0 0 0 2px var(--accent)}
.mcmt{display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px;padding:12px 18px;border-top:1px solid var(--line);font-size:14px;line-height:1.6}
.mcmt .hd{display:flex;gap:6px;align-items:center;font-size:12.5px;color:var(--ink-3)}
.mcmt .hd b{color:var(--ink-1);font-size:13.5px}
.cbar{position:absolute;left:0;right:0;bottom:84px;z-index:7;display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:10px;align-items:center;padding:8px 12px;background:var(--bg);border-top:1px solid var(--line);font-size:14px;color:var(--ink-3)}
.pcnote{display:flex;gap:10px;align-items:flex-start;margin-top:10px;padding:12px 14px;border-radius:12px;background:var(--sunken);font-size:13.5px;line-height:1.55;color:var(--ink-2)}
.pcnote .ic{margin-top:3px;color:var(--ink-3)}
'''

def phone2(inner, active=0, extra=""):
    tabs = [("home", "홈"), ("cmt", "커뮤니티"), ("box", "내 게임"), ("bell", "알림"), ("user", "나")]
    tb = "".join(f'<a href="#"{" aria-current=\"page\"" if i == active else ""}>{ic(t)}{n}</a>' for i, (t, n) in enumerate(tabs))
    return f'<div class="phone"><div class="sbar"><span>9:41</span><span>5G</span></div><div class="pscroll">{inner}</div>{extra}<nav class="tabbar">{tb}</nav></div>'

def m_home2():
    chips = '<div class="mchips"><button class="chip" aria-pressed="true">전체</button>' + "".join(f'<button class="chip">{n}</button>' for _, n in BOARDS) + "</div>"
    posts = "".join(f'<div class="mpost"><span class="tt"><span class="board-chip{" log" if p[0]=="개발일지" else ""}" style="margin-top:1px">{p[0]}</span><span>{p[2]}</span><span class="c">[{p[3]}]</span></span><span class="by">{face(p[4],p[5],"xs")}{p[6]} · {p[7]}</span></div>' for p in POSTS[:5])
    l = mg.LOGS[1]
    inner = f'''{mgm.mtop()}
<div class="msec" style="margin-top:8px"><div class="msh">{EAR}<h2>지금 커뮤니티</h2><span class="r">전체</span></div>{chips}{posts}</div>
<div class="msec"><div class="msh">{EAR}<h2>이번 주 일지 PICK</h2></div><div class="mfeat"><span class="art {l[0]}"></span><b>{l[1]}</b><span class="m">{l[5]} · {l[6]}</span></div></div>'''
    return phone2(inner, 0, f'<span class="fab">{ic("pen","ic ic16")}글쓰기</span>')

def m_post():
    inner = f'''<div class="mback"><button class="icon-btn" aria-label="뒤로"><svg class="ic ic20" viewBox="0 0 16 16"><path d="M10 3 5 8l5 5"></path></svg></button><span class="t" style="font-size:15px">피드백</span><span style="margin-left:auto;display:flex"><button class="icon-btn" aria-label="공유">{ic("up2","ic ic16")}</button><button class="icon-btn" aria-label="더 보기"><svg class="ic ic16" viewBox="0 0 16 16"><circle cx="3.5" cy="8" r=".8"></circle><circle cx="8" cy="8" r=".8"></circle><circle cx="12.5" cy="8" r=".8"></circle></svg></button></span></div>
<div class="mp-body"><h1>타이틀 화면 두 가지 중 뭐가 나아요?</h1><div class="by">{face("ㅂ","bora","xs")}<b style="color:var(--ink-1)">보라네</b> · 25분 전 · 조회 230</div>
<p>‘그리드 러너’ 정식판 타이틀을 두 가지로 만들어 봤어요.</p>
<div class="imgs"><span class="art a-grid"></span><span class="art a-tess"></span></div>
<div class="mpoll"><span class="opt"><i style="width:38%"></i><span>A · 잼 버전</span><span>38%</span></span><span class="opt me"><i style="width:62%"></i><span>B · 새로 그림</span><span>62%</span></span></div></div>
<div class="mcmt">{face("ㅍ","jjok","")}<span><span class="hd"><b>픽셀상점</b><span class="mkb2">메이커</span>· 20분 전</span>B 요! 실루엣이 바로 읽혀요. 그림자만 한 단계 연하게.</span></div>
<div class="mcmt">{face("ㅅ","hong","")}<span><span class="hd"><b>새벽코딩</b>· 15분 전</span>처음 보는 사람이면 B 가 더 끌릴 듯해요.</span></div>'''
    bar = f'<div class="cbar">{face("ㅇ","olive","")}<span>댓글 달기</span><span class="btn btn-primary btn-sm" style="height:34px">등록</span></div>'
    return phone2(inner, 1, bar)

def m_game2():
    inner = f'''<div class="mback"><button class="icon-btn" aria-label="뒤로"><svg class="ic ic20" viewBox="0 0 16 16"><path d="M10 3 5 8l5 5"></path></svg></button><span class="t">종이 배 2</span><span style="margin-left:auto">{status("fix", "보완 요청")}</span></div>
<div class="msec" style="margin-top:8px"><div class="vsteps">
<div class="vs done"><i>{ic("check", "ic ic12")}</i><span><b>작성</b><span class="m">11/24 제출</span></span></div>
<div class="vs done"><i>{ic("check", "ic ic12")}</i><span><b>자동 검사 통과</b><span class="m">악성코드 · 용량 · 실행 확인</span></span></div>
<div class="vs now"><i></i><span><b>심사 — 보완 요청</b><span class="m">2시간 전</span>
<div class="fixbox"><b>{ic("alert")}고칠 것 1개</b>이미지 · 영상을 5개 이상 올려 주세요. 지금 3개예요.</div>
<div class="pcnote">{ic("pc")}<span>그림 · 빌드 올리기는 PC 에서 할 수 있어요. <a class="link" href="#" style="font-size:13.5px">PC 로 링크 보내기</a></span></div></span></div>
<div class="vs"><i></i><span><b style="color:var(--ink-3)">공개 — 운영자 승인 후</b></span></div>
</div></div>
<div class="msec" style="margin-top:4px"><div class="msh"><h2 style="font-size:16px">휴대폰에서 고칠 수 있는 것</h2></div>
<div class="kv"><div><span>한 줄 소개</span><span class="clip">접은 종이배로 강을 따라 내려가요</span>{ic("chev")}</div><div><span>태그</span><span>탐험 · 힐링 · 20분</span>{ic("chev")}</div><div><span>공개 설정</span><span>승인 후 바로 공개</span>{ic("chev")}</div></div></div>'''
    return phone2(inner, 2)

def mobile2():
    cols = [("홈", "커뮤니티가 첫 화면. 게시판 칩 + 지금 올라온 글 + 일지 PICK. 글쓰기는 떠 있는 버튼.", m_home2()),
            ("글 보기", "피드백 글 · 투표 · 댓글. 아래 고정 댓글 입력.", m_post()),
            ("내 게임 · 보완 요청", "업로드 화면 없음 — 그림 · 빌드는 ‘PC 에서’. 글자 · 태그 · 공개 설정만 휴대폰에서.", m_game2())]
    body = '<div class="phones">' + "".join(f'<div class="pcol"><b>{t}</b><span>{d}</span>{p}</div>' for t, d, p in cols) + "</div>"
    memo = "M3 결정 반영: 모바일에는 게임 업로드 UI 를 두지 않는다. 탭바 = 홈 · 커뮤니티 · 내 게임 · 알림 · 나(모두 같은 모양). 글쓰기는 커뮤니티 화면의 떠 있는 버튼."
    html = mg.page("MakersGround 모바일", body, 1000, memo, width=1400)
    return html.replace("</style>", mgm.M_CSS + M_CSS2 + CSS + "\n</style>", 1)

if __name__ == "__main__":
    for name, fn in [("MG01-home.dc.html", home_c), ("MG08-community.dc.html", community_list), ("MG09-post.dc.html", post_view), ("MG91-mobile.dc.html", mobile2)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
