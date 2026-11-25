# 플레이 화면(PG-PLAY 상태 4종) · 플레이 종료(PG-END) 시안 생성기
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
.frames-page{display:flex;flex-direction:column;gap:56px;padding:48px 0 80px;background:var(--sunken)}
.fr{width:1200px;margin:0 auto;display:flex;flex-direction:column;gap:12px}
.fr > .cap{display:flex;align-items:baseline;gap:12px}
.fr > .cap b{font-size:18px;font-weight:800}
.fr > .cap span{font-size:13px;color:var(--ink-3)}
.screen{position:relative;width:1200px;height:675px;border-radius:14px;overflow:hidden;background:#0B0D10;color:#FFFFFF;box-shadow:0 24px 48px -24px rgb(0 0 0/.5)}
.pbar{position:absolute;left:0;right:0;top:0;height:48px;display:flex;align-items:center;gap:10px;padding:0 10px 0 6px;background:#101316;border-bottom:1px solid #1F2328;z-index:5;font-size:14px}
.pbar .ib{display:grid;place-items:center;width:36px;height:36px;border-radius:999px;color:rgb(255 255 255/.85)}
.pbar .ib:hover,.pbar .ib.hv{background:rgb(255 255 255/.1)}
.pbar .t{font-weight:800}
.pbar .m{color:rgb(255 255 255/.55);font-size:13px}
.pbar .sp{margin-left:auto;display:flex;align-items:center;gap:2px}
.pbar .sep{width:1px;height:20px;background:#272C31;margin:0 6px}
.pbar .exit{height:32px;padding:0 12px;border-radius:999px;background:rgb(255 255 255/.1);font-weight:700;font-size:13px;display:flex;align-items:center;gap:6px}
.game{position:absolute;left:0;right:0;top:48px;bottom:0;display:grid;place-items:center}
.game .canvas{width:960px;aspect-ratio:16/9;max-height:100%}
.game .canvas.focus{box-shadow:0 0 0 2px var(--accent)}
.hint{position:absolute;left:50%;top:64px;transform:translateX(-50%);display:flex;align-items:center;gap:10px;height:40px;padding:0 16px;border-radius:999px;background:rgb(16 19 22/.86);backdrop-filter:blur(8px);font-size:13.5px;font-weight:600;z-index:6}
.hint kbd{display:inline-grid;place-items:center;min-width:28px;height:22px;padding:0 6px;border-radius:5px;background:rgb(255 255 255/.14);font:700 12px/1 var(--font-sans)}
.loading{position:absolute;inset:48px 0 0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;background:#101316}
.loading .logo{font-size:80px;color:#FFFFFF;--ears:var(--accent)}
.loading .lbar{width:280px;height:4px;border-radius:999px;background:#272C31;overflow:hidden}
.loading .lbar i{display:block;width:62%;height:100%;background:var(--accent)}
.loading .m{color:rgb(255 255 255/.6);font-size:13px}
.loading .tip{position:static;opacity:1;visibility:visible;transform:none;background:rgb(255 255 255/.06);box-shadow:none;margin-top:18px}
.loading .tip::before{display:none}
.overlay{position:absolute;inset:48px 0 0;background:rgb(11 13 16/.72);backdrop-filter:blur(6px);display:grid;place-items:center;z-index:4}
.pause{width:380px;padding:24px;border-radius:22px;background:#191C20;display:flex;flex-direction:column;gap:8px}
.pause h3{margin:0 0 8px;font-size:22px;font-weight:800;display:flex;align-items:center;gap:10px}
.pause .row{display:flex;align-items:center;gap:10px;height:48px;padding:0 14px;border-radius:12px;background:rgb(255 255 255/.06);font-size:15px;font-weight:700}
.pause .row .k{margin-left:auto;color:rgb(255 255 255/.5);font-size:13px;font-weight:600}
.pause .row.dg{color:#FE6270}
.keys{display:grid;grid-template-columns:auto 1fr;gap:8px 14px;padding:10px 4px 4px;font-size:13.5px;color:rgb(255 255 255/.75)}
.keys kbd{display:inline-grid;place-items:center;min-width:30px;height:24px;padding:0 7px;border-radius:6px;background:rgb(255 255 255/.12);font:700 12px/1 var(--font-sans);color:#FFFFFF}
.err{position:absolute;inset:48px 0 0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;text-align:center;background:#101316}
.err .logo{font-size:96px;color:#FFFFFF;--ears:rgb(255 255 255/.35)}
.err h3{margin:8px 0 0;font-size:28px;font-weight:800}
.err p{margin:0;font-size:16px;line-height:1.6;color:rgb(255 255 255/.7);max-width:440px}
.err .env{margin-top:6px;padding:12px 16px;border-radius:12px;background:rgb(255 255 255/.05);font-size:12.5px;color:rgb(255 255 255/.55);font-family:ui-monospace,Consolas,monospace;text-align:left}
.err .acts{display:flex;gap:8px;margin-top:6px}
.toast2{position:absolute;right:20px;top:68px;display:flex;align-items:center;gap:12px;padding:10px 16px 10px 10px;border-radius:14px;background:rgb(16 19 22/.9);backdrop-filter:blur(8px);font-size:14px;font-weight:700;z-index:6;box-shadow:var(--shadow-pop)}
.toast2 .badge-i{display:grid;place-items:center;width:36px;height:36px;border-radius:10px;background:var(--accent)}
.toast2 small{display:block;font-size:12px;font-weight:600;color:rgb(255 255 255/.6)}
/* 종료 */
.end{display:grid;grid-template-columns:minmax(0,1fr) 400px;gap:40px;margin-top:36px;align-items:start}
.result{position:relative;border-radius:22px;overflow:hidden;color:#FFFFFF;background:#173250;padding:36px 40px 32px;min-height:300px}
.result .bg{position:absolute;inset:0;opacity:.35}
.result > *{position:relative}
.result .k{font-size:14px;font-weight:700;color:rgb(255 255 255/.72)}
.result .big{display:block;font-size:72px;line-height:1;margin-top:10px}
.result .row{display:flex;gap:28px;margin-top:22px;font-size:14px;color:rgb(255 255 255/.75)}
.result .row b{display:block;font-size:20px;color:#FFFFFF;margin-bottom:2px}
.result .best{display:inline-flex;align-items:center;gap:6px;margin-top:14px;height:30px;padding:0 12px;border-radius:999px;background:rgb(255 255 255/.14);font-size:13px;font-weight:800}
.result .acts{display:flex;gap:8px;margin-top:26px}
.side{display:flex;flex-direction:column;gap:16px}
.box{padding:20px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line)}
.box h4{margin:0 0 12px;font-size:16px;font-weight:800;display:flex;align-items:center;gap:8px}
.box .yn{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.box .yn span{height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;gap:6px;font-weight:800;background:var(--sunken)}
.box .yn span.on{background:var(--accent);color:#FFFFFF}
.box .chips{margin-top:10px}
.box .chip{height:32px;font-size:13px;padding:0 12px}
.cheer{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center}
.cheer b{display:block;font-size:15px}
.share{display:flex;gap:8px;align-items:center;margin-top:10px;padding:0 6px 0 14px;height:44px;border-radius:12px;background:var(--sunken);font-size:13px;color:var(--ink-2)}
.share .btn{margin-left:auto;height:34px}
'''

def bar(title="루프 디버거", hv=None):
    def b(name, label, cls=""):
        return f'<span class="ib{" hv" if hv == name else ""}" aria-label="{label}" title="">{ic(name, "ic ic16")}</span>'
    snd = '<svg class="ic ic16" viewBox="0 0 16 16"><path d="M3 6h2.5L9 3v10L5.5 10H3z"></path><path d="M11.5 5.5a3.5 3.5 0 0 1 0 5"></path></svg>'
    full = '<svg class="ic ic16" viewBox="0 0 16 16"><path d="M2.5 6V2.5H6M10 2.5h3.5V6M13.5 10v3.5H10M6 13.5H2.5V10"></path></svg>'
    return f'''<div class="pbar"><span class="ib" aria-label="뒤로"><svg class="ic ic16" viewBox="0 0 16 16"><path d="M10 3 5 8l5 5"></path></svg></span>
<span class="logo" style="font-size:15px;color:#FFFFFF">{logo()}</span><span class="sep"></span>
<span class="t">{title}</span>{face("ㅍ","jjok","xs")}<span class="m">픽셀상점</span>
<span class="sp"><span class="ib" aria-label="소리">{snd}</span><span class="ib" aria-label="조작 방법">{ic("q","ic ic16")}</span><span class="ib" aria-label="문제 알리기">{ic("alert","ic ic16")}</span><span class="ib" aria-label="전체 화면">{full}</span><span class="sep"></span><span class="exit">나가기</span></span></div>'''

def screen_loading():
    return f'''<div class="screen">{bar()}<div class="loading"><span class="logo f-wow big-face">{logo("o")}</span><span class="lbar"><i></i></span><span class="m">불러오는 중 · 9.2MB 중 5.7MB</span>
<span class="tip"><span>{ic("q")}게임을 누르면 키보드가 게임으로 들어가요</span><span>{ic("check")}Esc 를 누르면 일시정지 · 진행은 자동 저장</span></span></div></div>'''

def screen_play():
    return f'''<div class="screen">{bar()}<div class="game"><span class="canvas a-loop focus"></span></div>
<div class="hint">{ic("check")}게임에 들어왔어요 · 방향키가 페이지를 움직이지 않아요 · <kbd>Esc</kbd> 일시정지</div>
<div class="toast2"><span class="badge-i">{ic("crown","ic ic16")}</span><span>도전과제 달성<small>첫 루프 탈출 · 7 / 12</small></span></div></div>'''

def screen_pause():
    return f'''<div class="screen">{bar()}<div class="game"><span class="canvas a-loop"></span></div><div class="overlay"><div class="pause">
<h3>일시정지</h3>
<span class="row" style="background:var(--accent)">{ic("play","ic ic16")}계속하기<span class="k" style="color:rgb(255 255 255/.75)">Esc</span></span>
<div class="keys"><kbd>← →</kbd><span>블록 고르기</span><kbd>Space</kbd><span>블록 놓기</span><kbd>R</kbd><span>방 다시 시작</span><kbd>H</kbd><span>힌트</span></div>
<span class="row">소리 <span class="k">70%</span></span>
<span class="row">{ic("alert","ic ic16")}문제 알리기<span class="k">환경 정보 자동 첨부</span></span>
<span class="row dg">나가기<span class="k">진행은 저장됐어요</span></span>
</div></div></div>'''

def screen_error():
    return f'''<div class="screen">{bar()}<div class="err"><span class="logo f-down big-face">{logo("n")}</span><h3>게임을 불러오지 못했어요</h3>
<p>잠깐 연결이 끊겼거나 게임 파일에 문제가 있을 수 있어요. 다시 해 보고, 계속 안 되면 메이커에게 알려 주세요.</p>
<div class="acts"><span class="btn btn-primary">다시 불러오기</span><span class="btn btn-glass">문제 알리기</span></div>
<div class="env">같이 보내는 정보 · Chrome 131 · Windows 11 · 화면 1920×1080 · 루프 디버거 v1.2 · 오류 코드 LOAD_TIMEOUT</div></div></div>'''

def play_page():
    frames = [("불러오는 중", "놀란 얼굴(o) + 진행 막대 + 조작 요령. 용량을 숫자로", screen_loading()),
              ("플레이 중", "얇은 바(48px)만 남기고 게임을 최대로. 처음 들어오면 키보드 안내를 4초 보여 주고 사라짐. 도전과제는 오른쪽 위 토스트(L2)", screen_play()),
              ("일시정지 (Esc)", "계속하기 · 조작 방법 · 소리 · 문제 알리기 · 나가기. 나가기는 위 바의 나가기 버튼 또는 Esc → 여기서", screen_pause()),
              ("오류", "시무룩 얼굴 + 원인과 할 일 + 다시 불러오기 · 문제 알리기(환경 정보 자동 첨부, 무엇이 가는지 보여 줌)", screen_error())]
    body = '<div class="frames-page">' + "".join(f'<div class="fr"><div class="cap"><b>{t}</b><span>{d}</span></div>{s}</div>' for t, d, s in frames) + "</div>"
    memo = "PG-PLAY. 게임 영역이 주인공 — 플랫폼 UI 는 얇은 먹색 바 하나. 다크 고정(사이트 테마와 무관). 키 입력 가두기 · Esc 일시정지 · 다른 탭이면 자동 일시정지(SDK 게임). 나가기 = 바의 나가기 버튼 한 번, 또는 Esc 일시정지 → 나가기(P2 결정)."
    html = dt.page("플레이 화면", body, 3200, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

def end_page():
    nexts = "".join(mg.game_card(a) for a in mg.NEWG[:4])
    body = dt.pg_header() + f'''<main class="wrap"><div class="end">
<div><div class="result"><span class="bg a-loop"></span><span class="k">루프 디버거 · 스테이지 18 끝</span><span class="big disp">03:42</span><span class="best">{ic("crown","ic ic12")}내 최고 기록 · 지난번보다 12초 빨라요</span>
<div class="row"><span><b>18 / 40</b>진행</span><span><b>1시간 12분</b>총 플레이</span><span><b>7 / 12</b>도전과제</span></div>
<div class="acts"><span class="btn btn-on-color" data-play>{ic("play","ic ic16")}다음 스테이지</span><span class="btn btn-glass">다시 하기</span><span class="btn btn-glass">게임 정보</span></div></div>
<section class="sec" style="margin-top:44px"><div class="sh">{EAR}<h2>다음에 해 볼 게임</h2><span class="sub">퍼즐 · 한 판 10분 안쪽</span></div><div class="g4c" style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px">{nexts}</div></section></div>
<aside class="side">
<div class="box"><h4>재미있었나요?</h4><div class="yn"><span class="on">{ic("up","ic ic16")}추천</span><span><svg class="ic ic16" style="transform:rotate(180deg)"><use href="#i-up"></use></svg>별로</span></div>
<div class="chips"><button class="chip" aria-pressed="true">짧고 굵음</button><button class="chip">퍼즐 좋아하면</button><button class="chip">힌트가 친절해요</button><button class="chip">어려워요</button></div>
<span class="btn btn-secondary btn-sm" style="margin-top:12px">한 줄 더 쓰기</span></div>
<div class="box"><h4>만든 사람에게</h4><div class="cheer">{face("ㅍ","jjok","md")}<span><b>픽셀상점</b><span class="m">새 일지 · 첫 리뷰 38개를 읽고</span></span><span class="btn btn-primary btn-sm">팔로우</span></div></div>
<div class="box"><h4>친구에게 도전장</h4><p class="m" style="margin:0">내 기록 03:42 를 넘어 보라고 링크를 보내요. 받은 친구는 로그인 없이 바로 플레이해요.</p>
<div class="share"><span class="clip">admd.games/p/loop?vs=03:42</span><span class="btn btn-primary btn-sm">링크 복사</span></div></div>
</aside></div></main>''' + dt.footer()
    memo = "PG-END. ‘끝은 다음의 시작’ — 기록(Gasoek 큰 숫자, 게임색 바탕) → 다음 스테이지 · 다시 하기 / 오른쪽: 한 번 눌러 끝나는 평가 · 메이커 팔로우 · 친구에게 도전장 / 아래: 다음 게임 4개."
    html = dt.page("플레이 종료", body, 1500, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

if __name__ == "__main__":
    for name, fn in [("PG06-play.dc.html", play_page), ("PG07-play-end.dc.html", end_page)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
