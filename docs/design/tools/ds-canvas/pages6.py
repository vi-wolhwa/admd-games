# 처음 올리는 분(MG-START) · 개발일지 쓰기(MG-LOG 작성) · 지난 PICK(PG-ISSUE) 시안 생성기
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + [OUT]
import importlib.util
spec = importlib.util.spec_from_file_location("p5", os.path.join(HERE, "pages5.py"))
p5 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p5)
dt, mg = p5.dt, p5.mg
ic, face, logo, EAR = mg.ic, mg.face, mg.logo, mg.EAR

CSS = r'''
.st-hero{display:grid;grid-template-columns:minmax(0,1fr) 420px;gap:56px;align-items:center;margin-top:40px}
.st-hero h1{margin:0;font-family:var(--font-display);font-weight:400;font-size:44px;line-height:1.18}
.st-hero .lede{margin:16px 0 0;font-size:17px;line-height:1.7;color:var(--ink-2)}
.st-hero .acts{display:flex;gap:8px;margin-top:24px}
.pv{padding:22px;border-radius:var(--radius-2xl);background:var(--sunken)}
.pv .cap{display:flex;justify-content:space-between;margin-bottom:12px;font-size:13px;font-weight:700;color:var(--ink-3)}
.pv .ph{display:grid;place-items:center;background:repeating-linear-gradient(-45deg,var(--sunken-hover) 0 10px,transparent 10px 20px),var(--bg);color:var(--ink-3);font-size:13px;font-weight:700;border-radius:var(--radius-lg)}
.pv .gc .t{font-size:17px}
.what{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.what > div{padding:24px;border-radius:var(--radius-xl);box-shadow:inset 0 0 0 1px var(--line);display:flex;flex-direction:column;gap:10px}
.what h3{margin:0;font-size:19px;font-weight:800;display:flex;align-items:center;gap:10px}
.what ul{margin:0;padding-left:18px;font-size:15px;line-height:1.8;color:var(--ink-2)}
.flow{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;counter-reset:f}
.flow > div{padding:18px;border-radius:var(--radius-lg);background:var(--sunken);font-size:14px;line-height:1.6;color:var(--ink-2);position:relative}
.flow > div::before{counter-increment:f;content:counter(f);display:grid;place-items:center;width:28px;height:28px;margin-bottom:10px;border-radius:999px;background:var(--accent);color:#FFFFFF;font-weight:800;font-size:13px}
.flow b{display:block;font-size:15.5px;color:var(--ink-1);margin-bottom:4px}
.rules{display:grid;grid-template-columns:1fr 1fr;gap:12px 40px}
.rule{display:grid;grid-template-columns:24px minmax(0,1fr);gap:10px;font-size:15px;line-height:1.6;color:var(--ink-2)}
.rule .ic{width:18px;height:18px;margin-top:3px}
.rule.ok .ic{color:var(--ok-text)}
.rule.no .ic{color:var(--danger-text)}
.rule b{color:var(--ink-1)}
.faq > div{padding:16px 0;border-top:1px solid var(--line)}
.faq > div:first-child{border-top:0}
.faq b{display:block;font-size:16px}
.faq p{margin:6px 0 0;font-size:15px;line-height:1.65;color:var(--ink-2)}
/* 에디터 */
.ed{width:860px;margin:0 auto}
.ed-top{display:flex;align-items:center;gap:10px;margin-top:24px}
.ed-top .saved{margin-left:auto;font-size:13px;color:var(--ok-text);font-weight:700;display:flex;align-items:center;gap:6px}
.ed-meta{display:flex;gap:10px;margin-top:18px;flex-wrap:wrap}
.sel{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 12px 0 14px;border-radius:var(--radius-md);background:var(--sunken);font-size:14px;font-weight:700}
.sel .k{color:var(--ink-3);font-weight:600}
.sel .ic{color:var(--ink-3)}
.ed-title{margin-top:22px;font-size:30px;font-weight:800;letter-spacing:-.02em;color:var(--ink-1);padding-bottom:14px;border-bottom:1px solid var(--line)}
.ed-title .ph{color:var(--ink-4)}
.toolbar{position:sticky;top:68px;z-index:5;display:flex;gap:2px;padding:8px 0;background:var(--bg);border-bottom:1px solid var(--line)}
.toolbar span{display:grid;place-items:center;min-width:36px;height:36px;padding:0 8px;border-radius:8px;font-size:14px;font-weight:800;color:var(--ink-2)}
.toolbar span:hover{background:var(--sunken)}
.toolbar .sep{min-width:1px;width:1px;padding:0;background:var(--line);margin:6px 6px}
.ed-body{padding:22px 0;font-size:17px;line-height:1.85}
.ed-body p{margin:0 0 16px}
.ed-body h3{margin:18px 0 10px;font-size:21px;font-weight:800}
.ed-img{position:relative;margin:6px 0 18px;border-radius:12px;overflow:hidden;box-shadow:0 0 0 2px var(--accent)}
.ed-img .art{border-radius:0;aspect-ratio:16/7}
.ed-img .bar2{position:absolute;right:10px;top:10px;display:flex;gap:4px}
.ed-img .bar2 span{height:30px;padding:0 10px;border-radius:999px;background:rgb(16 19 22/.75);color:#FFFFFF;font-size:12.5px;font-weight:700;display:inline-flex;align-items:center}
.ed-img figcaption{padding:8px 12px;font-size:13px;color:var(--ink-3);background:var(--sunken)}
.caret{display:inline-block;width:2px;height:1.1em;background:var(--accent);vertical-align:-3px;margin-left:1px}
.ed-foot{position:sticky;bottom:0;display:flex;align-items:center;gap:10px;padding:14px 0;border-top:1px solid var(--line);background:var(--bg)}
.ed-foot .sp{margin-left:auto;display:flex;gap:8px}
.tip2{display:flex;gap:10px;margin-top:14px;padding:14px 16px;border-radius:var(--radius-lg);background:var(--accent-tint);font-size:14px;line-height:1.6;color:var(--ink-1)}
.tip2 .ic{color:var(--accent-text);margin-top:3px}
/* 지난 PICK */
.issues{display:flex;flex-direction:column;gap:40px;margin-top:28px}
.iss{display:grid;grid-template-columns:200px minmax(0,1fr);gap:32px;padding-top:28px;border-top:1px solid var(--line)}
.iss:first-child{border-top:0;padding-top:0}
.iss .wk b{display:block;font-family:var(--font-display);font-weight:400;font-size:28px;line-height:1.1}
.iss .wk span{display:block;margin-top:6px;font-size:14px;color:var(--ink-3)}
.iss .wk p{margin:12px 0 0;font-size:14px;line-height:1.6;color:var(--ink-2)}
.iss .row4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px}
.iss .gc .why{display:flex;gap:7px;align-items:baseline;margin-top:3px;font-size:13px;line-height:1.5;color:var(--ink-2)}
.iss .gc .why::before{content:"";flex:none;width:5px;height:5px;border-radius:2px;background:var(--accent);transform:translateY(-1px)}
.colls{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.coll{position:relative;display:flex;flex-direction:column;gap:10px}
.coll .stack{position:relative;aspect-ratio:16/9}
.coll .stack .art{position:absolute;border-radius:12px;width:78%}
.coll .stack .art:nth-child(1){left:0;top:12%;z-index:1;opacity:.6}
.coll .stack .art:nth-child(2){left:11%;top:6%;z-index:2;opacity:.85}
.coll .stack .art:nth-child(3){left:22%;top:0;z-index:3;box-shadow:var(--shadow-lift)}
.coll b{font-size:17px;font-weight:800}
'''

def start_page():
    body = mg.header2(False, "홈") + f'''<main class="wrap">
<div class="st-hero"><div><span class="board-chip" style="display:inline-flex;height:24px;padding:0 9px;border-radius:6px;background:var(--accent-tint);color:var(--accent-text);font-size:12px;font-weight:800;align-items:center">처음 올리는 분</span>
<h1>만든 게임,<br>여기에 올려 보세요</h1>
<p class="lede">완성작이 아니어도 괜찮아요. 잼 작품, 프로토타입, 몇 분짜리 실험도 환영해요. 올리기 전에 알아 두면 좋은 것만 모았어요.</p>
<div class="acts"><span class="btn btn-primary">{ic("up2","ic ic16")}PC 에서 첫 게임 올리기</span><span class="btn btn-secondary">커뮤니티에 먼저 물어보기</span></div></div>
<div class="pv"><div class="cap"><span>올리면 이렇게 보여요</span><span>PlayGround 카드</span></div>
<div class="gc"><span class="art ph" style="display:grid">내 게임 대표 그림 1920×1080<span class="plat">{ic("web","ic ic12")}</span><span class="jf md maker" style="background:var(--color-face-olive)">ㄴ<i>ㅅ</i>ㄴ</span></span><span class="t">내 게임 이름</span><span class="meta">내 이름 · 장르 · 한 판 시간</span></div>
<p class="m" style="margin:12px 0 0">카드 · 상세 · 공유 미리보기에서 어떻게 잘리는지 올릴 때 바로 확인해요.</p></div></div>
<section class="sec"><div class="sh">{EAR}<h2>올릴 수 있는 것</h2></div><div class="what">
<div><h3>{ic("web","ic ic20")}웹 빌드 — 브라우저에서 바로</h3><ul><li><b>index.html</b> 이 든 zip 하나, 최대 200MB</li><li>Godot · Unity(WebGL) · 웹 엔진 모두</li><li>올리자마자 미리 플레이로 확인</li></ul></div>
<div><h3>{ic("dl","ic ic20")}설치형 — 내려받아 실행</h3><ul><li>Windows · macOS · Android 파일, <b>파일당 최대 500MB</b></li><li>모든 파일은 <b>무료 보안 검사</b>를 거쳐요</li><li>코드 서명이 없어도 괜찮아요 — 설치 안내를 대신 보여 줘요</li></ul></div></div></section>
<section class="sec"><div class="sh">{EAR}<h2>공개까지</h2><span class="sub">보통 이틀 안</span></div><div class="flow">
<div><b>올리기</b>8단계 마법사. 자동 저장되고, 휴대폰에서는 글 · 설정만 고칠 수 있어요.</div>
<div><b>자동 검사</b>악성코드 · 용량 · 실행 여부를 확인해요. 보통 10분.</div>
<div><b>심사</b>운영자가 직접 플레이해 보고 승인해요. 고칠 게 있으면 어디를 고칠지 알려 드려요.</div>
<div><b>공개</b>PlayGround 에 올라가고, 팔로워에게 알림이 가요. 언제든 비공개로 바꿀 수 있어요.</div></div></section>
<section class="sec"><div class="sh">{EAR}<h2>지켜 주세요</h2></div><div class="rules">
<div class="rule ok">{ic("check")}<span><b>직접 만든 것</b> — 다른 사람 에셋은 라이선스를 지켜서</span></div>
<div class="rule ok">{ic("check")}<span><b>대표 그림에 글자 넣지 않기</b> — 제목은 aDmD 가 붙여요</span></div>
<div class="rule ok">{ic("check")}<span><b>콘텐츠 표시</b> — 폭력 · 공포 등은 올릴 때 체크</span></div>
<div class="rule ok">{ic("check")}<span><b>스크린샷 3장 이상</b> — 플레이 화면 그대로</span></div>
<div class="rule no">{ic("alert")}<span><b>광고 · 결제 유도 금지</b> — 외부 판매 링크는 메이커 페이지 링크 칸에만</span></div>
<div class="rule no">{ic("alert")}<span><b>개인정보 수집 금지</b> — 게임 안에서 로그인 · 연락처 요구 안 돼요</span></div></div></section>
<section class="sec"><div class="sh">{EAR}<h2>자주 묻는 것</h2></div><div class="faq" style="max-width:860px">
<div><b>다른 사이트에 올린 게임도 올려도 되나요?</b><p>네. 같은 게임을 여러 곳에 올려도 괜찮아요.</p></div>
<div><b>돈이 드나요?</b><p>아니요. 올리기 · 보안 검사 · 공개 모두 무료예요. 수수료도 광고도 없어요.</p></div>
<div><b>심사에서 떨어지면요?</b><p>대부분은 ‘보완 요청’ 이에요. 무엇을 고칠지 알려 드리고, 고치면 바로 다시 심사해요.</p></div>
<div><b>휴대폰으로도 올릴 수 있나요?</b><p>게임 파일 · 그림은 PC 에서 올려요. 휴대폰에서는 진행 상황 확인과 글 · 공개 설정 수정만 할 수 있어요.</p></div></div></section>
</main>''' + mg.footer()
    memo = "MG-START. 게스트가 ‘올려 볼까?’ 할 때 읽는 한 장. ‘올리면 이렇게 보여요’ 카드 미리보기는 여기로(M4). 올릴 수 있는 것(웹 · 설치형 500MB) → 공개까지 4단계(보통 이틀, 운영자 승인) → 지켜 주세요 → 자주 묻는 것. 버튼은 ‘PC 에서’."
    return mg.page("처음 올리는 분", body, 2600, memo).replace("</style>", CSS + "\n</style>", 1)

def editor_page():
    body = mg.header2(True, "커뮤니티") + f'''<main class="ed">
<div class="ed-top"><a class="link" href="#">{ic("chev","ic ic12")} 커뮤니티</a><span class="saved">{ic("check")}임시 저장됨 · 방금</span></div>
<div class="ed-meta"><span class="sel"><span class="k">게시판</span>개발일지{ic("chev","ic ic12")}</span><span class="sel"><span class="k">게임</span><span class="art a-loop" style="width:40px;border-radius:4px"></span>루프 디버거{ic("chev","ic ic12")}</span><span class="sel"><span class="k">말머리</span>회고{ic("chev","ic ic12")}</span></div>
<div class="ed-title">첫 리뷰 38개를 읽고 바꾼 것들<span class="caret"></span></div>
<div class="toolbar"><span>본문</span><span>제목</span><span class="sep"></span><span style="font-weight:900">B</span><span style="font-style:italic">I</span><span>링크</span><span class="sep"></span><span>그림 · GIF</span><span>영상 링크</span><span>코드</span><span class="sep"></span><span>인용</span><span>목록</span></div>
<div class="ed-body"><p>공개하고 2주 동안 리뷰가 38개 달렸어요. 하나씩 읽으면서 같은 말이 몇 번 나오는지 세어 봤어요.</p>
<h3>‘튜토리얼이 길다’ — 9번</h3><p>처음 세 스테이지를 퍼즐 하나로 합쳤어요. 대신 힌트 버튼을 첫 화면부터 보이게 했어요.</p>
<figure class="ed-img"><span class="art a-loop" style="display:block"></span><span class="bar2"><span>크게</span><span>설명</span><span>삭제</span></span><figcaption>v1.1(왼쪽)과 v1.2 의 첫 화면</figcaption></figure>
<p>그 결과 첫 판을 끝까지 하는 비율이 <b>48% → 71%</b> 가 됐어요.<span class="caret"></span></p></div>
<div class="tip2">{ic("q")}<span>개발일지는 <b>루프 디버거</b> 게임 페이지 · 메이커 페이지 · 팔로워 소식에도 실려요. 공개 전 미리보기로 확인해 보세요.</span></div>
<div class="ed-foot"><span class="m">글자 1,204 · 그림 1</span><span class="sp"><span class="btn btn-secondary">미리보기</span><span class="btn btn-secondary">임시 저장</span><span class="btn btn-primary">올리기</span></span></div>
</main>''' + mg.footer()
    memo = "MG-LOG 쓰기(커뮤니티 글쓰기와 같은 에디터). 게시판 · 게임 연결 · 말머리를 위에서 고르고, 본문은 글자 그대로 쓰는 모양(WYSIWYG). 자동 임시 저장, 그림 · GIF · 영상 링크 · 코드. 개발일지면 어디에 실리는지 알려 줌. 휴대폰에서도 쓸 수 있음(게임 업로드와 다름)."
    return mg.page("글쓰기 · 개발일지", body, 1700, memo).replace("</style>", CSS + "\n</style>", 1)

def issues_page():
    weeks = [("11월 넷째 주", "11.24 – 11.30", "짧고 단단한 퍼즐 넷.", [("a-loop", "루프 디버거", "픽셀상점", "ㅍ", "jjok", "이번 주 플레이 수 · 완주율 1위"), ("a-refac", "리팩터 러시", "리팩터클럽", "ㄹ", "gyul", "3분이면 끝나는 아케이드"), ("a-tilt", "틸트 이론", "기울기연구소", "ㄱ", "hwang", "추천 90% · 리뷰 30"), ("a-bazaar", "바이트 바자", "바이트마켓", "ㅂ", "bora", "점심시간에 딱 맞는 길이")]),
             ("11월 셋째 주", "11.17 – 11.23", "잼에서 태어난 게임들.", [("a-grid", "그리드 러너", "보라네", "ㅂ", "bora", "여름 잼 3위작의 정식판"), ("a-paper", "종이 배", "청록상회", "ㅊ", "cheongnok", "완주율 1위 · 20분"), ("a-tess", "테셀레이트", "노을공방", "ㄴ", "haneul", "규칙 하나 · 문제 40개"), ("a-demon", "들판의 악마", "풀잎", "ㅍ", "pul", "16색으로 그린 전략")])]
    def card(a):
        art, t, who, ch, col, why = a
        return f'<div class="gc"><span class="art {art}"><span class="shots"></span><span class="jf maker" style="background:var(--color-face-{col})">{ch}<i>ㅅ</i>{ch}</span></span><span class="t"><a href="#">{t}</a></span><span class="meta">{who}</span><span class="why">{why}</span></div>'
    iss = "".join(f'<div class="iss"><div class="wk"><b>{w}</b><span>{d}</span><p>{s}</p></div><div class="row4">{"".join(card(x) for x in g)}</div></div>' for w, d, s, g in weeks)
    colls = [("퇴근길 한 손 게임", "휴대폰 가로 · 한 판 5분 안쪽 · 12개", ("a-loop", "a-refac", "a-tilt")), ("친구랑 같이", "2~4명 · 같은 방에서 · 8개", ("a-solvent", "a-null", "a-grid")), ("이야기가 있는 게임", "30분 이상 · 엔딩 있음 · 9개", ("a-halcyon", "a-ash", "a-paper"))]
    ch = "".join(f'<div class="coll"><div class="stack">{"".join(f"<span class=\"art {a}\"></span>" for a in arts)}</div><b>{t}</b><span class="m">{d}</span></div>' for t, d, arts in colls)
    body = p5.pgh("홈") + f'''<main class="wrap">
<div class="pg-title"><h1>지난 PICK</h1><span class="m">매주 월요일, 네 개씩</span></div>
<section class="sec" style="margin-top:28px"><div class="sh">{EAR}<h2>컬렉션</h2><span class="sub">주제로 묶은 목록</span><div class="r"><a class="link" href="#">전체 컬렉션</a></div></div><div class="colls">{ch}</div></section>
<section class="sec"><div class="sh">{EAR}<h2>주간 PICK 보관함</h2><div class="r"><div class="chips"><button class="chip" aria-pressed="true">2026</button><button class="chip">2025</button></div></div></div><div class="issues">{iss}</div>
<div class="more"><span class="btn btn-secondary">이전 주 더 보기</span></div></section>
</main>''' + dt.footer()
    memo = "PG-ISSUE · PG-COLL. 지난 주 PICK 을 주 단위로(Gasoek 주 이름 · 한 줄 주제 · 카드 4 + 이유 한 줄, ‘누가 골랐다’ 없음). 위에는 주제 컬렉션(겹친 카드 그림)."
    return dt.page("지난 PICK · 컬렉션", body, 2100, memo).replace("</style>", p5.CSS + CSS + "\n</style>", 1)

if __name__ == "__main__":
    for name, fn in [("처음 올리는 분.dc.html", start_page), ("글쓰기 · 개발일지.dc.html", editor_page), ("지난 PICK · 컬렉션.dc.html", issues_page)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
