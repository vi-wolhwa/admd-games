# L2 시안: 잼(상세 · 투표 · 결과) · 랭킹 전체 · 친구 · 같이 하기 대기실
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "..", "canvas")
sys.argv = sys.argv[:1] + [OUT]
import importlib.util
s7 = importlib.util.spec_from_file_location("p7", os.path.join(HERE, "pages7.py")); p7 = importlib.util.module_from_spec(s7); s7.loader.exec_module(p7)
mg, dt, p5 = p7.mg, p7.dt, p7.p5
ic, face, logo, EAR, status = mg.ic, mg.face, mg.logo, mg.EAR, mg.status

CSS = r'''
.utable{width:100%;border-collapse:collapse;font-size:14px}
.utable th{text-align:left;font-size:12.5px;color:var(--ink-3);font-weight:700;padding:0 10px 8px}
.utable td{padding:12px 10px;border-top:1px solid var(--line);vertical-align:middle}
.utable td .who2{display:flex;align-items:center;gap:8px;font-weight:700}
.jam-hero{position:relative;padding:44px 0 40px;background:var(--surface-ink);color:#FFFFFF}
.jam-hero .in{width:1200px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1fr) 420px;gap:48px;align-items:center}
.jam-hero .k{font-size:14px;font-weight:800;color:var(--color-inju-400)}
.jam-hero h1{margin:10px 0 0;font-size:40px;font-weight:800;letter-spacing:-.02em}
.jam-hero p{margin:12px 0 0;font-size:16px;line-height:1.7;color:rgb(255 255 255/.75)}
.jam-hero .acts{display:flex;gap:8px;margin-top:22px}
.count{display:flex;flex-direction:column;align-items:flex-start;gap:8px;padding:24px;border-radius:var(--radius-2xl);background:rgb(255 255 255/.06)}
.count .lab{font-size:13px;color:rgb(255 255 255/.6);font-weight:700}
.count .big{font-family:var(--font-display);font-size:64px;line-height:1;color:var(--color-inju-400)}
.count .theme{display:flex;align-items:center;gap:8px;margin-top:6px;padding:10px 14px;border-radius:12px;background:rgb(255 255 255/.08);font-size:14px;font-weight:700}
.tline{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:0;margin-top:8px}
.tline > div{position:relative;padding:22px 12px 0 0;font-size:14px;color:var(--ink-2)}
.tline > div::before{content:"";position:absolute;left:0;right:0;top:6px;height:3px;background:var(--sunken-hover)}
.tline > div::after{content:"";position:absolute;left:0;top:0;width:15px;height:15px;border-radius:999px;background:var(--bg);box-shadow:inset 0 0 0 3px var(--ink-4)}
.tline > div.done::before,.tline > div.done::after{background:var(--ink-2);box-shadow:none}
.tline > div.now::after{background:var(--accent);box-shadow:0 0 0 4px var(--accent-tint)}
.tline > div.now::before{background:linear-gradient(90deg,var(--accent) 40%,var(--sunken-hover) 40%)}
.tline b{display:block;font-size:15px;color:var(--ink-1)}
.stack{display:flex}
.stack .jf{margin-right:-6px}
.teams{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.team{display:flex;align-items:center;gap:12px;padding:14px 16px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line)}
.team b{display:block;font-size:15px}
.team .want{margin-left:auto;font-size:12px;font-weight:800;color:var(--accent-text)}
/* 투표 */
.vote-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.ventry{display:flex;flex-direction:column;gap:8px}
.ventry .art{border-radius:var(--radius-lg)}
.ventry b{font-size:16px}
.crit{display:flex;flex-direction:column;gap:6px;margin-top:4px}
.crit > div{display:grid;grid-template-columns:72px repeat(5,1fr);gap:4px;align-items:center;font-size:13px;color:var(--ink-3)}
.crit i{height:28px;border-radius:7px;background:var(--sunken)}
.crit i.on{background:var(--accent)}
.ventry.done .crit i{opacity:.6}
.podium{display:grid;grid-template-columns:1fr 1.25fr 1fr;gap:20px;align-items:end}
.pod{display:flex;flex-direction:column;gap:10px;align-items:stretch}
.pod .rank{font-family:var(--font-display);font-size:48px;line-height:1;color:var(--accent-text)}
.pod.first .rank{font-size:64px}
.pod .art{border-radius:var(--radius-lg)}
.pod b{font-size:17px}
.pod .sc{font-size:13px;color:var(--ink-3)}
/* 랭킹 */
.rk-top{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.rkc{position:relative;display:flex;flex-direction:column;gap:8px}
.rkc .n{position:absolute;left:12px;top:8px;z-index:4;font-family:var(--font-display);font-size:48px;line-height:1;color:#FFFFFF;text-shadow:0 2px 12px rgb(0 0 0/.4)}
.rkc .art{border-radius:var(--radius-lg)}
.rkc b{font-size:18px;font-weight:800}
.rk-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 28px;list-style:none;margin:0;padding:0}
.rk-list .rr{background:none}
.rk-list .rr:hover{background:var(--sunken)}
.rk-list .rr .n{font-family:var(--font-display);font-size:28px}
.rk-crit{margin-top:14px;font-size:13px;color:var(--ink-3)}
/* 친구 */
.fr-grid{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:44px;align-items:start;margin-top:24px}
.fri{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center;padding:12px 6px;border-top:1px solid var(--line)}
.fri:first-child{border-top:0}
.fri b{display:block;font-size:15px}
.fri .stt{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--ink-3)}
.fri .stt i{width:8px;height:8px;border-radius:999px;background:var(--ink-4)}
.fri .stt.on i{background:var(--ok)}
.fri .stt.play{color:var(--ok-text);font-weight:700}
.fri .stt.play i{background:var(--ok)}
.fri .acts{display:flex;gap:6px}
.inv{display:flex;align-items:center;gap:8px;height:44px;padding:0 6px 0 14px;border-radius:12px;background:var(--sunken);font-size:13.5px;color:var(--ink-2)}
.inv .btn{margin-left:auto;height:34px}
/* 대기실 */
.room{display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:32px;margin-top:24px;align-items:start}
.room-head{display:grid;grid-template-columns:240px minmax(0,1fr);gap:20px;align-items:center}
.room-head .art{border-radius:var(--radius-lg)}
.room-head h1{margin:0;font-size:26px;font-weight:800}
.code{display:flex;align-items:center;gap:12px;margin-top:12px}
.code .c{font-family:var(--font-display);font-size:30px;letter-spacing:.08em}
.seats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin-top:28px}
.seat{display:flex;flex-direction:column;align-items:center;gap:10px;padding:22px 12px;border-radius:var(--radius-xl);box-shadow:inset 0 0 0 1px var(--line);text-align:center}
.seat .jf{width:64px;height:64px;font-size:24px}
.seat b{font-size:15px}
.seat.ready{box-shadow:inset 0 0 0 2px var(--ok)}
.seat.host::after{content:"방장";font-size:11px;font-weight:800;color:var(--accent-text)}
.seat.empty{background:var(--sunken);box-shadow:none;color:var(--ink-3);justify-content:center;min-height:150px}
.chat{display:flex;flex-direction:column;gap:10px;padding:18px;border-radius:var(--radius-xl);box-shadow:inset 0 0 0 1px var(--line)}
.msg{display:flex;gap:8px;align-items:flex-start;font-size:14px;line-height:1.5}
.msg b{font-size:13px;display:block}
.stamps{display:flex;gap:8px;padding-top:10px;border-top:1px solid var(--line)}
.stamp{display:grid;place-items:center;width:52px;height:44px;border-radius:12px;background:var(--sunken);font-weight:800;font-size:14px;letter-spacing:-.04em}
.start-bar{display:flex;align-items:center;gap:12px;margin-top:20px;padding:16px 18px;border-radius:var(--radius-lg);background:var(--sunken)}
.start-bar .btn{margin-left:auto}
'''

def page(title, body, h, memo, make=False):
    html = (mg.page if make else dt.page)(title, body, h, memo)
    return html.replace("</style>", p7.BASE_CSS + p7.CSS + CSS + "\n</style>", 1)

def jam_page():
    stackf = "".join(face(c, col, "md") for c, col in [("ㅂ", "bora"), ("ㅈ", "ju"), ("ㅊ", "cheongnok"), ("ㄴ", "haneul"), ("ㅍ", "pul")])
    teams = "".join(f'<div class="team"><span class="stack">{"".join(face(c,col,"") for c,col in m)}</span><span><b>{t}</b><span class="m">{d}</span></span>{"<span class=\"want\">" + w + "</span>" if w else ""}</div>' for t, d, m, w in [("새벽 셋", "프로그래머 · 아트 · 사운드", [("ㅅ","hong"),("ㄱ","gyul"),("ㅁ","olive")], ""), ("보라네", "혼자", [("ㅂ","bora")], "팀원 찾는 중 · 아트"), ("청록상회", "2명", [("ㅊ","cheongnok"),("ㅎ","haneul")], "사운드 구해요")])
    body = mg.header2(True, "잼") + f'''<section class="jam-hero"><div class="in"><div><span class="k">aDmD 겨울 잼 #3 · 48시간</span><h1>주제는 시작할 때 공개돼요</h1><p>혼자 또는 팀으로 48시간 동안 하나를 만들어요. 끝나면 PlayGround 잼 아케이드에서 바로 플레이되고, 투표로 상을 정해요.</p><div class="acts"><span class="btn btn-primary">참가 신청</span><span class="btn btn-glass">팀원 찾기</span></div></div>
<div class="count"><span class="lab">시작까지</span><span class="big">D-3</span><span class="m" style="color:rgb(255 255 255/.7)">12/12(금) 19:00 시작 · 12/14(일) 19:00 제출 마감</span><span class="theme">{ic("alert","ic ic16")}주제는 12/12 19:00 에 이 자리에 공개</span></div></div></section>
<main class="wrap"><section class="sec" style="margin-top:44px"><div class="sh">{EAR}<h2>일정</h2></div><div class="tline"><div class="done"><b>참가 신청</b>지금 ~ 12/12 19:00</div><div class="now"><b>시작 · 주제 공개</b>12/12(금) 19:00</div><div><b>제출 마감</b>12/14(일) 19:00</div><div><b>투표</b>12/14 ~ 12/21</div><div><b>결과 · PICK</b>12/22(월)</div></div></section>
<section class="sec"><div class="split3"><div><div class="sh">{EAR}<h2>규칙</h2></div><ul style="margin:0;padding-left:18px;font-size:15px;line-height:1.9;color:var(--ink-2)"><li>시작 뒤에 만든 것만 — 엔진 · 무료 에셋은 써도 되고, 출처를 적어 주세요</li><li>웹 빌드 또는 설치형(500MB 이하), 제출은 일반 게임 올리기와 같아요</li><li>투표: 참가자 + 플레이어 누구나, 재미 · 주제 · 완성도 세 가지</li><li>마감 뒤 고친 버전은 잼 투표에 쓰지 않아요(따로 공개는 돼요)</li></ul></div>
<aside class="panel2"><h3>참가 212명 · 팀 58</h3><span class="stack">{stackf}</span><p class="m" style="margin:0">혼자 참가도 환영해요. 팀은 최대 4명.</p></aside></div></section>
<section class="sec"><div class="sh">{EAR}<h2>팀원 찾는 팀</h2><div class="r"><a class="link" href="#">팀원 모집 게시판</a></div></div><div class="teams">{teams}</div></section></main>''' + mg.footer()
    memo = "MG-JAMS 상세(L2). 먹 띠 무대 + 인주 Gasoek D-day · 주제는 시작 시각에 같은 자리에 공개 · 다섯 단계 일정 막대 · 규칙(일반 업로드 재사용) · 참가 수와 얼굴 · 팀원 찾는 팀."
    return page("잼 · 상세", body, 1700, memo, make=True)

def jam_vote_page():
    entries = [("a-grid", "다시, 그리드", "보라네", [4, 5, 3], False), ("a-paper", "한 번 더 접기", "청록상회 외 1", [5, 4, 4], True), ("a-refac", "되감기 금지", "새벽 셋", [0, 0, 0], False)]
    ve = ""
    for a, t, who, sc, done in entries:
        crit = "".join(f'<div><span>{k}</span>{"".join(f"<i class=\"{"on" if i < s else ""}\"></i>" for i in range(5))}</div>' for k, s in zip(["재미", "주제", "완성도"], sc))
        ve += f'<div class="ventry{" done" if done else ""}"><span class="art {a}"><span class="shots"></span></span><b>{t}</b><span class="m">{who} · {"투표함" if done else ("아직" if sc[0]==0 else "저장됨")}</span><div class="crit">{crit}</div><span class="btn btn-{"secondary" if sc[0] else "primary"} btn-sm" style="align-self:flex-start">{ic("play")}플레이하고 평가</span></div>'
    pod = "".join(f'<div class="pod{" first" if r == 1 else ""}"><span class="rank">{r}</span><span class="art {a}"></span><b>{t}</b><span class="sc">{who} · 평균 {s}</span></div>' for r, a, t, who, s in [(2, "a-paper", "한 번 더 접기", "청록상회 외 1", "4.4"), (1, "a-grid", "다시, 그리드", "보라네", "4.6"), (3, "a-tess", "두 번째 기회", "노을공방", "4.2")])
    body = mg.header2(True, "잼") + f'''<main class="wrap"><div class="pg-title"><h1>겨울 잼 #3 · 투표</h1><span class="m">주제 ‘다시 한 번’ · 58개 · 12/21 마감 · 내가 한 투표 7</span></div>
<section class="sec" style="margin-top:24px"><div class="vote-grid">{ve}</div><p class="m" style="margin-top:16px">작품마다 플레이한 뒤에만 평가할 수 있어요. 점수는 마감까지 비공개.</p></section>
<section class="sec"><div class="sh">{EAR}<h2>결과 (예시 · 12/22 공개)</h2><span class="sub">수상작은 PlayGround 이번 주 PICK 으로</span></div><div class="podium" style="width:900px;margin:0 auto">{pod}</div></section></main>''' + mg.footer()
    memo = "MG-JAMS 투표 · 결과(L2). 작품 카드마다 세 기준 5칸 평가(플레이한 뒤에만, 마감까지 점수 비공개). 결과는 Gasoek 순위 숫자 단상(1위 가운데 크게) → 수상작은 PlayGround PICK 으로(R-JAM-04)."
    return page("잼 · 투표 · 결과", body, 1500, memo, make=True)

def ranking_page():
    top = "".join(f'<div class="rkc"><span class="n">{i}</span><span class="art {a}"><span class="shots"></span><span class="jf md maker" style="background:var(--color-face-{col})">{ch}<i>ㅅ</i>{ch}</span></span><b>{t}</b><span class="m">{who} · {k}</span></div>' for i, a, t, who, ch, col, k in [(1, "a-ash", "애쉬폴 러너", "잿빛토끼", "ㅈ", "ju", "이번 주 1,820명 · ▲3"), (2, "a-paper", "페이퍼 벡터", "벡터공방", "ㅂ", "bichwi", "1,402명 · ▲1"), (3, "a-loop", "루프 디버거", "픽셀상점", "ㅍ", "jjok", "1,204명 · –")])
    rows = ""
    data = [("a-grid", "그리드락", "보라네", "▼1"), ("a-tess", "테셀레이트 드리프트", "노을공방", "NEW"), ("a-demon", "대은 거든", "풀잎", "▲2"), ("a-bazaar", "바이트 바자", "바이트마켓", "▼2"), ("a-halcyon", "할시온 랩스", "하늘섬", "▲4"), ("a-refac", "리팩터 러시", "리팩터클럽", "–"), ("a-tilt", "틸트 이론", "기울기연구소", "▼3"), ("a-solvent", "솔벤트", "물방울", "▲1")]
    for i, (a, t, who, k) in enumerate(data, start=4):
        col = "var(--rank-down)" if k.startswith("▼") else ("var(--rank-up)" if k.startswith("▲") else ("var(--accent-text)" if k == "NEW" else "var(--ink-3)"))
        rows += f'<li><div class="rr"><span class="n disp">{i}</span><span class="art {a}"></span><span><b>{t}</b><span class="by">{who}</span></span><span class="k" style="color:{col}">{k}</span></div></li>'
    body = p5.pgh("랭킹") + f'''<main class="wrap"><div class="pg-title"><h1>랭킹</h1><span class="m">11.18 – 11.24</span><div class="r"><nav class="utabs" style="border:0"><a href="#" aria-current="page">주간</a><a href="#">월간</a><a href="#">친구</a></nav></div></div>
<div class="chips" style="margin-top:18px"><button class="chip" aria-pressed="true">전체</button><button class="chip">퍼즐</button><button class="chip">액션</button><button class="chip">이야기</button><button class="chip">같이 하기</button><button class="chip">새로 나온(30일)</button></div>
<section class="sec" style="margin-top:28px"><div class="rk-top">{top}</div></section>
<section class="sec" style="margin-top:36px"><ul class="rk-list">{rows}</ul><p class="rk-crit">기준: 이번 주 한 판 이상 플레이한 사람 수(같은 사람은 한 번). 매주 월요일 0시에 바뀌어요. 리뷰 10개 미만 게임도 들어가요.</p>
<div class="more"><span class="btn btn-secondary">50위까지 보기</span></div></section></main>''' + dt.footer()
    memo = "PG-RANK(L2). 주간 · 월간 · 친구 탭 + 장르 칩. 1~3위는 큰 카드(아트 위 Gasoek 순위), 4위부터 2열 RankRow(등락: 상승 빨강 ▲ · 하락 파랑 ▼ · NEW). 기준을 숫자로 밝힘(허영 지표 대신 ‘플레이한 사람 수’)."
    return page("랭킹 전체", body, 1500, memo)

def friends_page():
    fr = "".join(f'<div class="fri">{face(c,col,"md")}<span><b>{n}</b><span class="stt {cls}"><i></i>{st}</span></span><span class="acts">{a}</span></div>' for c, col, n, cls, st, a in [
        ("ㅅ", "hong", "새벽코딩", "play", "루프 디버거 하는 중 · 23스테이지", '<span class="btn btn-primary btn-sm">같이 보기</span><span class="btn btn-secondary btn-sm">도전장</span>'),
        ("ㄱ", "gyul", "귤껍질", "on", "접속 중", '<span class="btn btn-secondary btn-sm">같이 하기 초대</span>'),
        ("ㅁ", "olive", "모래시계", "", "어제 접속 · 공개 안 함", '<span class="btn btn-secondary btn-sm">프로필</span>')])
    req = f'<div class="fri">{face("ㅋ","jjok","md")}<span><b>코코넛</b><span class="m">함께 아는 친구 1 · 리뷰 4</span></span><span class="acts"><span class="btn btn-primary btn-sm">수락</span><span class="btn btn-secondary btn-sm">거절</span></span></div>'
    body = p5.pgh("같이") + f'''<main class="wrap"><div class="pg-title"><h1>친구</h1><span class="m">서로 수락한 사이만 친구예요</span></div>
<div class="fr-grid"><div><nav class="utabs"><a href="#" aria-current="page">친구 12</a><a href="#">받은 신청 1</a><a href="#">보낸 신청</a></nav><div style="margin-top:8px">{fr}</div></div>
<aside style="display:flex;flex-direction:column;gap:16px"><div class="panel2"><h3>받은 신청 <span class="cnt">1</span></h3>{req}</div>
<div class="panel2"><h3>친구 추가</h3><div class="search" style="width:100%">{ic("search")}닉네임으로 찾기</div><div class="inv"><span class="clip">admd.games/f/orange-cat-3</span><span class="btn btn-primary btn-sm">초대 링크 복사</span></div><p class="m" style="margin:0">지금 하는 게임은 친구에게만 보여요. 설정 → 공개 범위에서 끌 수 있어요.</p></div></aside></div></main>''' + dt.footer()
    memo = "PG-FRIENDS(L2). 친구 목록(상태: 지금 하는 게임 · 접속 중 · 공개 안 함 — 설정 존중) · 행동(같이 보기 · 도전장 · 같이 하기 초대). 오른쪽: 받은 신청(수락/거절) · 닉네임 찾기 · 초대 링크."
    return page("친구", body, 1200, memo)

def room_page():
    seats = f'''<div class="seat host ready">{face("ㅇ","jadu","")}<b>오렌지맛</b><span class="st st-live st-sm">{ic("check")}준비</span></div>
<div class="seat ready">{face("ㅅ","hong","")}<b>새벽코딩</b><span class="st st-live st-sm">{ic("check")}준비</span></div>
<div class="seat">{face("ㄱ","gyul","")}<b>귤껍질</b><span class="st st-wait st-sm"><span class="pulse"></span>들어오는 중</span></div>
<div class="seat empty">{ic("plus","ic ic20")}<span style="font-size:14px">빈자리 · 링크로 초대</span></div>'''
    stamps = "".join(f'<span class="stamp" title="{t}">{s}</span>' for s, t in [("DwD", "좋아"), ("DoD", "놀람"), ("DnD", "아쉬움"), ("D-D", "졸림"), ("GO", "가자")])
    body = p5.pgh("같이") + f'''<main class="wrap"><div class="room"><div>
<div class="room-head"><span class="art a-null"></span><div><span class="m">같이 하기 · 2~4명 · 같은 방에서</span><h1>널 포인터 — 오렌지맛의 방</h1><div class="code"><span class="m">방 코드</span><span class="c">K7P2</span><span class="btn btn-secondary btn-sm">{ic("up2")}초대 링크 복사</span></div></div></div>
<div class="seats">{seats}</div>
<div class="start-bar"><span><b>3명 중 2명 준비</b><span class="m" style="display:block">모두 준비되면 방장이 시작해요 · 2명부터 시작 가능</span></span><span class="btn btn-secondary">나가기</span><span class="btn btn-primary" data-play style="margin-left:0">{ic("play","ic ic16")}시작</span></div></div>
<aside class="chat"><b style="font-size:15px">대기실 대화</b><div class="msg">{face("ㅅ","hong","xs")}<span><b>새벽코딩</b>저 키보드 오른쪽 쓸게요</span></div><div class="msg">{face("ㅇ","jadu","xs")}<span><b>오렌지맛</b>좋아요, 귤껍질 오면 시작해요</span></div>
<div class="msg">{face("ㄱ","gyul","xs")}<span><b>귤껍질</b><span class="stamp" style="display:inline-grid;width:auto;padding:0 8px;height:28px;font-size:12px">DwD</span></span></div>
<div class="stamps">{stamps}</div><div class="inp" style="height:40px">말 걸기…</div></aside></div></main>''' + dt.footer()
    memo = "PG-ROOM(L2). 게임 · 방 이름 · 방 코드(Gasoek) · 초대 링크 → 자리 4칸(준비 = 비취 테두리, 방장 표시, 빈자리 초대) → 준비 현황 + 시작. 대화의 빠른 반응은 이모지 대신 고양이 표정 스탬프(DwD · DoD · DnD …)."
    return page("같이 하기 대기실", body, 1100, memo)

def team_page():
    mem = "".join(f'<tr><td><span class="who2">{face(c,col,"xs")}{n}</span></td><td>{r}</td><td><span class="seg"><span{" class=\"on\"" if role=="관리" else ""}>관리</span><span{" class=\"on\"" if role=="올리기" else ""}>올리기</span><span{" class=\"on\"" if role=="보기" else ""}>보기</span></span></td><td>{a}</td></tr>' for c, col, n, r, role, a in [("ㅊ","cheongnok","청록상회","만든 사람 · 프로그래밍","관리",'<span class="m">나</span>'),("ㅎ","haneul","하늘섬","아트","올리기",'<span class="btn btn-secondary btn-sm">내보내기</span>'),("ㅁ","olive","모래시계","사운드 · 초대 수락 대기","보기",'<span class="btn btn-secondary btn-sm">초대 취소</span>')])
    body = mg.header2(True, "내 게임") + f'''<main class="wrap"><div class="pg-title"><h1>팀 관리 · 청록상회</h1><span class="m">팀 메이커 · 3명</span><div class="r"><span class="btn btn-primary">{ic("plus","ic ic16")}팀원 초대</span></div></div>
<div class="split3" style="margin-top:24px"><div><table class="utable"><thead><tr><th>팀원</th><th>맡은 일</th><th>권한</th><th></th></tr></thead><tbody>{mem}</tbody></table>
<p class="m" style="margin-top:14px">관리 = 팀 정보 · 팀원 · 공개 설정 · 올리기 = 새 버전 · 글 · 리뷰 답글 · 보기 = 통계 · 피드백 읽기. 게임 페이지의 ‘만든 사람’ 에 팀원 얼굴이 함께 나와요.</p></div>
<aside class="panel2"><h3>초대하기</h3><div class="search" style="width:100%">{ic("search")}닉네임으로 찾기</div><div class="inv"><span class="clip">admd.games/t/cheongnok?inv=9F2C</span><span class="btn btn-primary btn-sm">링크 복사</span></div><p class="m" style="margin:0">링크는 7일 동안 쓸 수 있어요. 팀은 최대 8명.</p></aside></div></main>''' + mg.footer()
    memo = "MG-TEAM(L2). 팀원 표(맡은 일 · 권한 관리/올리기/보기 분할 선택 · 내보내기/초대 취소) + 초대(닉네임 · 7일 링크). 권한 뜻을 한 줄로."
    return page("팀 관리", body, 1000, memo, make=True)

if __name__ == "__main__":
    for name, fn in [("잼 · 상세.dc.html", jam_page), ("잼 · 투표 · 결과.dc.html", jam_vote_page), ("랭킹 전체.dc.html", ranking_page), ("친구.dc.html", friends_page), ("같이 하기 대기실.dc.html", room_page), ("팀 관리.dc.html", team_page)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
