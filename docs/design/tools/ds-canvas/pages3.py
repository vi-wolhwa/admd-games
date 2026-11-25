# 로그인 · 얼굴 만들기(SH-LOGIN · SH-ONBOARD), 업로드 마법사(MG-UPLOAD), 검색 결과(PG-SRCH) 시안 생성기
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
.stagebg{display:flex;flex-direction:column;gap:56px;padding:48px 0 80px;background:var(--sunken)}
.fr{width:1200px;margin:0 auto;display:flex;flex-direction:column;gap:12px}
.fr > .cap{display:flex;align-items:baseline;gap:12px}
.fr > .cap b{font-size:18px;font-weight:800}
.fr > .cap span{font-size:13px;color:var(--ink-3)}
.scr{position:relative;width:1200px;height:720px;border-radius:14px;overflow:hidden;background:var(--bg);box-shadow:0 24px 48px -24px rgb(0 0 0/.35)}
.scr .dim{position:absolute;inset:0;background:rgb(16 19 22/.5);display:grid;place-items:center;z-index:30}
.scr .ghost{position:absolute;inset:0;filter:saturate(.9)}
.dlg{width:440px;padding:32px 32px 26px;border-radius:var(--radius-2xl);background:var(--bg);box-shadow:var(--shadow-pop);display:flex;flex-direction:column;gap:12px;text-align:center}
[data-theme="dark"] .dlg{background:var(--raised);box-shadow:var(--shadow-pop),0 0 0 1px var(--line)}
.dlg .logo{font-size:44px;align-self:center;margin:6px 0 6px}
.dlg h2{margin:0;font-size:22px;font-weight:800}
.dlg p{margin:0;font-size:14.5px;line-height:1.6;color:var(--ink-2)}
.prov{display:flex;align-items:center;justify-content:center;gap:10px;height:52px;border-radius:14px;font-size:16px;font-weight:800;background:var(--sunken);color:var(--ink-1)}
.prov .mk{display:grid;place-items:center;width:26px;height:26px;border-radius:7px;background:var(--ink-1);color:var(--bg);font-size:13px;font-weight:900}
.dlg .keep{display:flex;gap:10px;text-align:left;padding:12px 14px;border-radius:12px;background:var(--accent-tint);font-size:13.5px;line-height:1.55;color:var(--ink-1)}
.dlg .keep .ic{color:var(--accent-text);margin-top:3px}
.dlg .fine{font-size:12.5px;color:var(--ink-3);line-height:1.6}
.dlg .fine a{text-decoration:underline;text-underline-offset:2px}
.x{position:absolute;right:16px;top:16px}
/* 얼굴 만들기 */
.onb{display:grid;grid-template-columns:420px minmax(0,1fr);height:100%}
.onb .left{background:var(--accent);color:#FFFFFF;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;position:relative}
.onb .left > .jf{width:168px;height:168px;font-size:62px;border-radius:46px;box-shadow:0 0 0 6px rgb(255 255 255/.95),0 30px 60px -20px rgb(0 0 0/.5)}
.onb .left b{font-size:22px;font-weight:800}
.onb .left .m{color:rgb(255 255 255/.75);font-size:14px}
.onb .left .where{display:flex;gap:10px;margin-top:18px;align-items:center;font-size:12.5px;color:rgb(255 255 255/.8)}
.onb .left .where span{display:flex;align-items:center;gap:6px;height:32px;padding:0 10px 0 4px;border-radius:999px;background:rgb(255 255 255/.14)}
.onb .right{padding:32px 48px;display:flex;flex-direction:column;gap:16px;overflow:hidden}
.onb .step{font-size:13px;font-weight:800;color:var(--accent-text)}
.onb h2{margin:4px 0 0;font-size:28px;font-weight:800;letter-spacing:-.02em}
.fld{display:flex;flex-direction:column;gap:8px}
.fld > label{font-size:14px;font-weight:800}
.fld .help{font-size:13px;color:var(--ink-3)}
.pick-grid{display:grid;grid-template-columns:repeat(14,minmax(0,1fr));gap:6px}
.pick-grid span{display:grid;place-items:center;height:40px;border-radius:10px;background:var(--sunken);font-size:17px;font-weight:800}
.pick-grid span.on{background:var(--ink-1);color:var(--bg)}
.mouths{display:flex;gap:6px}
.mouths span{display:grid;place-items:center;width:48px;height:40px;border-radius:10px;background:var(--sunken);font-size:17px;font-weight:800}
.mouths span.on{background:var(--ink-1);color:var(--bg)}
.colors{display:flex;gap:8px}
.colors span{width:36px;height:36px;border-radius:10px}
.colors span.on{box-shadow:0 0 0 2px var(--bg),0 0 0 4px var(--ink-1)}
.vis{display:grid;grid-template-columns:auto minmax(0,1fr);gap:12px;align-items:center;padding:12px 14px;border-radius:12px;background:var(--sunken);font-size:14px}
.vis b{display:block;font-size:14px}
.vis .m{display:block}
.switch{width:40px;height:24px;border-radius:999px;background:var(--sunken-hover);position:relative;flex:none}
.switch::after{content:"";position:absolute;left:2px;top:2px;width:20px;height:20px;border-radius:999px;background:#FFFFFF;box-shadow:var(--shadow-hairline)}
.switch.on{background:var(--accent)}
.switch.on::after{transform:translateX(16px)}
.onb .foot{margin-top:auto;display:flex;align-items:center;gap:10px}
.onb .foot .skip{font-size:14px;font-weight:700;color:var(--ink-3)}
.input2{display:flex;align-items:center;height:48px;padding:0 14px;border-radius:12px;background:var(--bg);box-shadow:inset 0 0 0 2px var(--accent);font-size:16px;font-weight:700}
.input2 .cnt2{margin-left:auto;font-size:13px;color:var(--ink-3);font-weight:600}
.okline{display:flex;align-items:center;gap:6px;font-size:13px;font-weight:700;color:var(--ok-text)}
/* 업로드 마법사 */
.wz-top{display:flex;align-items:center;gap:14px;padding:18px 28px;border-bottom:1px solid var(--line)}
.wz-top b{font-size:17px}
.wz-top .saved{margin-left:auto;display:flex;align-items:center;gap:6px;font-size:13px;color:var(--ok-text);font-weight:700}
.wz-steps{display:flex;gap:4px;padding:16px 28px 0}
.wz-steps span{flex:1;display:flex;flex-direction:column;gap:7px;font-size:12px;font-weight:700;color:var(--ink-3)}
.wz-steps span::before{content:"";height:4px;border-radius:999px;background:var(--sunken-hover)}
.wz-steps span.done::before{background:var(--ink-2)}
.wz-steps span.now{color:var(--ink-1)}
.wz-steps span.now::before{background:var(--accent)}
.wz-body{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:40px;padding:28px 28px 0}
.wz-body h2{margin:0;font-size:24px;font-weight:800;letter-spacing:-.02em}
.wz-body .lede{margin:6px 0 0;font-size:14.5px;color:var(--ink-2);line-height:1.6}
.drop{margin-top:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;height:150px;border-radius:var(--radius-lg);background:var(--sunken);box-shadow:inset 0 0 0 2px var(--sunken-hover);font-size:14px;color:var(--ink-2);text-align:center}
.drop b{font-size:16px;color:var(--ink-1)}
.upfile{margin-top:12px;display:grid;grid-template-columns:40px minmax(0,1fr) auto;gap:12px;align-items:center;padding:12px 14px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line)}
.upfile .fi{display:grid;place-items:center;width:40px;height:40px;border-radius:10px;background:var(--accent-tint);color:var(--accent-text)}
.upfile b{display:block;font-size:15px}
.checks2{margin-top:14px;display:flex;flex-direction:column;gap:2px}
.checks2 > div{display:grid;grid-template-columns:22px minmax(0,1fr) auto;gap:10px;align-items:center;min-height:38px;font-size:14px}
.checks2 .y{color:var(--ok-text)}
.checks2 .w{color:var(--accent-text)}
.checks2 .m{font-size:13px}
.aside-tip{display:flex;flex-direction:column;gap:12px;padding:20px;border-radius:var(--radius-lg);background:var(--sunken);font-size:14px;line-height:1.6;color:var(--ink-2)}
.aside-tip b{color:var(--ink-1);font-size:15px}
.aside-tip ul{margin:0;padding-left:18px}
.wz-foot{position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;gap:10px;padding:16px 28px;border-top:1px solid var(--line);background:var(--bg)}
.wz-foot .sp{margin-left:auto;display:flex;gap:8px}
.crops{width:66%;display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:14px;margin-top:14px;align-items:end}
.crop{display:flex;flex-direction:column;gap:8px;font-size:13px;color:var(--ink-3);font-weight:600}
.crop .frame{position:relative;border-radius:12px;overflow:hidden}
.crop .safe{position:absolute;inset:10% 8%;border:1.5px dashed rgb(255 255 255/.8);border-radius:6px}
.crop b{color:var(--ink-1);font-size:14px}
.big-art{position:relative;width:56%;aspect-ratio:16/9;border-radius:var(--radius-lg);overflow:hidden;margin-top:18px}
.big-art .handles{position:absolute;inset:8% 6%;box-shadow:0 0 0 999px rgb(0 0 0/.45);border:2px solid #FFFFFF;border-radius:4px}
.big-art .handles i{position:absolute;width:12px;height:12px;background:#FFFFFF;border-radius:3px}
/* 검색 */
.sr-h{display:flex;align-items:flex-end;gap:16px;margin-top:32px}
.sr-h .q{font-size:28px;font-weight:800}
.sr-h .q em{font-style:normal;color:var(--accent-text)}
.sr-h .m{padding-bottom:5px;font-size:14px}
.sr-tabs{margin-top:18px}
.grp{margin-top:36px}
.grp .sh h2{font-size:19px}
.mk-row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.mkc{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:12px;align-items:center;padding:14px;border-radius:var(--radius-lg);box-shadow:inset 0 0 0 1px var(--line)}
.mkc b{display:block;font-size:15px}
.hl{background:linear-gradient(transparent 55%,var(--accent-tint-2) 55%);font-weight:800}
.logrow{display:grid;grid-template-columns:minmax(0,1fr) 140px;gap:20px;align-items:center;padding:14px 0;border-top:1px solid var(--line)}
.logrow:first-child{border-top:0}
.logrow b{font-size:16px}
.logrow .m{display:block;margin-top:4px}
.logrow .art{border-radius:10px}
.noresult{display:grid;grid-template-columns:auto minmax(0,1fr);gap:28px;align-items:center;padding:32px 36px;border-radius:var(--radius-2xl);background:var(--sunken)}
.noresult .logo{font-size:64px}
.noresult h3{margin:0;font-size:22px;font-weight:800}
.noresult p{margin:6px 0 12px;font-size:15px;color:var(--ink-2)}
'''

def ghost_home():
    # 로그인 대화상자 뒤에 깔리는 흐린 홈
    return f'<div class="ghost">{dt.pg_header(False)}<div class="wrap" style="margin-top:24px"><span class="art a-loop" style="display:block;height:380px;border-radius:16px;aspect-ratio:auto"></span></div></div>'

def login_frame():
    return f'''<div class="scr">{ghost_home()}<div class="dim"><div class="dlg" role="dialog" aria-modal="true" aria-labelledby="lg-t" style="position:relative">
<button class="icon-btn x" aria-label="닫기"><svg class="ic ic16" viewBox="0 0 16 16"><path d="M4 4l8 8M12 4l-8 8"></path></svg></button>
<span class="logo f-up big-face">{logo("w")}</span>
<h2 id="lg-t">로그인하고 내 얼굴 만들기</h2><p>비밀번호는 만들지 않아요. 쓰던 계정으로 바로 들어와요.</p>
<span class="prov"><span class="mk">G</span>Google 로 계속하기</span>
<span class="prov"><span class="mk" style="border-radius:999px">{ic("user","ic ic12")}</span>GitHub 로 계속하기</span>
<div class="keep">{ic("check")}<span>로그인 전에 한 기록은 그대로 옮겨져요 — 진행 2개, 저장 3개.</span></div>
<p class="fine">계속하면 <a href="#">이용약관</a>과 <a href="#">개인정보처리방침</a>에 동의하는 것으로 봐요. 광고용으로 정보를 쓰지 않아요.</p>
</div></div></div>'''

def onboard_frame():
    eyes = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ"
    eg = "".join(f'<span class="{"on" if c == "ㅇ" else ""}">{c}</span>' for c in eyes)
    mouths = "".join(f'<span class="{"on" if c == "ㅅ" else ""}">{c}</span>' for c in "ㅅㅁㅇㅂㅡㅗ")
    cols = ["hong", "ju", "gyul", "hwang", "olive", "pul", "bichwi", "cheongnok", "haneul", "jjok", "bora", "jadu"]
    cg = "".join(f'<span class="{"on" if c == "olive" else ""}" style="background:var(--color-face-{c})"></span>' for c in cols)
    return f'''<div class="scr"><div class="onb"><div class="left"><span class="jf" style="background:var(--color-face-olive)">ㅇ<i>ㅅ</i>ㅇ</span><b>오렌지맛</b><span class="m">이 얼굴로 리뷰 · 기록 · 친구 목록에 나와요</span>
<div class="where"><span>{face("ㅇ","olive","xs")}리뷰</span><span>{face("ㅇ","olive","xs")}랭킹</span><span>{face("ㅇ","olive","xs")}헤더</span></div></div>
<div class="right"><div><span class="step">1 / 1 · 언제든 바꿀 수 있어요</span><h2>내 얼굴 만들기</h2></div>
<div class="fld"><label for="nick">닉네임</label><div class="input2" id="nick">오렌지맛|<span class="cnt2">3 / 12</span></div><span class="okline">{ic("check")}쓸 수 있는 닉네임이에요 · 첫 글자 ‘ㅇ’ 이 눈이 돼요</span></div>
<div class="fld"><label>눈</label><div class="pick-grid">{eg}</div></div>
<div class="fld"><label>입</label><div class="mouths">{mouths}</div></div>
<div class="fld"><label>색</label><div class="colors">{cg}</div><span class="help">12색 모두 같은 밝기라 어떤 색을 골라도 얼굴이 또렷해요</span></div>
<div class="vis"><span class="switch on" role="switch" aria-checked="true" aria-label="친구에게 지금 하는 게임 보이기"></span><span><b>친구에게 지금 하는 게임이 보여요</b><span class="m">서로 친구인 사람에게만 · 설정에서 언제든 끌 수 있어요</span></span></div>
<div class="foot"><span class="skip">건너뛰기 — 닉네임 첫 글자로 자동으로 만들어요</span><span class="btn btn-primary" style="margin-left:auto">이 얼굴로 시작</span></div>
</div></div></div>'''

def login_page():
    body = f'''<div class="stagebg">
<div class="fr"><div class="cap"><b>로그인 (모달)</b><span>페이지를 떠나지 않는 대화상자. 기쁨 표정 고양이 · 쓰던 계정 2개 · 게스트 기록 병합 안내</span></div>{login_frame()}</div>
<div class="fr"><div class="cap"><b>첫 로그인 · 내 얼굴 만들기</b><span>닉네임 첫 자음이 눈 → 눈 · 입 · 색을 바꿔 보며 왼쪽에서 바로 확인. 건너뛰어도 기본 얼굴이 생김</span></div>{onboard_frame()}</div>
</div>'''
    memo = "SH-LOGIN · SH-ONBOARD. ‘로그인하면 내 얼굴이 생겨요’ 약속을 지키는 화면. 그라운드 색 큰 면 위에 내 얼굴(168px)을 크게. 눈 14자 × 입 6자 × 색 12 = 1,008 가지."
    html = dt.page("로그인 · 내 얼굴 만들기", body, 1700, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

STEPS = ["기본 정보", "실행 방식", "빌드 올리기", "미리 플레이", "화면", "상세 정보", "공개 설정", "제출"]
def steps_bar(now):
    return '<div class="wz-steps">' + "".join(f'<span class="{"done" if i < now else ("now" if i == now else "")}">{i+1} {n}</span>' for i, n in enumerate(STEPS)) + "</div>"

def wz_top():
    return f'<div class="wz-top"><span class="logo" style="font-size:18px">{logo()}</span><b>새 게임 올리기 · 종이 배 2</b><span class="saved">{ic("check")}자동 저장됨 · 방금</span><button class="icon-btn" aria-label="닫기"><svg class="ic ic16" viewBox="0 0 16 16"><path d="M4 4l8 8M12 4l-8 8"></path></svg></button></div>'

def wz_foot(next_label):
    return f'<div class="wz-foot"><span class="btn btn-secondary">이전</span><span class="m">휴대폰에서 이어서 하려면 같은 계정으로 MakersGround 를 여세요</span><span class="sp"><span class="btn btn-secondary">나중에 이어서</span><span class="btn btn-primary">{next_label}</span></span></div>'

def wz_build():
    return f'''<div class="scr">{wz_top()}{steps_bar(2)}<div class="wz-body"><div>
<h2>빌드 올리기</h2><p class="lede">웹 빌드는 <b>index.html 이 들어 있는 zip</b> 하나를 올려요. 올리는 동안 다음 단계를 먼저 써도 돼요.</p>
<div class="drop">{ic("up2","ic ic20")}<b>zip 파일을 끌어다 놓거나 눌러서 고르기</b><span class="m">최대 200MB · Godot · Unity · 웹 엔진 모두 가능</span></div>
<div class="upfile"><span class="fi">{ic("box","ic ic20")}</span><span><b>paper-boat-2-web.zip</b><span class="bar" style="margin-top:8px"><i style="width:100%"></i></span></span><span class="m">9.2MB · 완료</span></div>
<div class="checks2">
<div>{ic("check","ic ic16 y")}<span>index.html 을 찾았어요</span><span class="m">/index.html</span></div>
<div>{ic("check","ic ic16 y")}<span>용량 9.2MB — 첫 로딩이 빠른 편이에요</span><span class="m">권장 50MB 이하</span></div>
<div>{ic("check","ic ic16 y")}<span>외부 서버 요청 없음</span><span class="m"></span></div>
<div>{ic("alert","ic ic16 w")}<span>소리가 첫 클릭 전에 시작돼요 — 브라우저가 막을 수 있어요</span><a class="link" href="#" style="font-size:13px">해결 방법</a></div>
</div></div>
<aside class="aside-tip"><b>올리기 전에</b><ul><li>Godot: 내보내기 → Web → ‘스레드 사용’ 끄기</li><li>Unity: 압축은 Gzip, ‘Decompression Fallback’ 켜기</li><li>저장은 브라우저 저장소(localStorage · IndexedDB)를 써요</li></ul><a class="link" href="#" style="font-size:14px">엔진별 안내 전체 보기 ›</a></aside></div>
{wz_foot("다음 · 미리 플레이")}</div>'''

def wz_art():
    return f'''<div class="scr">{wz_top()}{steps_bar(4)}<div class="wz-body"><div>
<h2>대표 그림</h2><p class="lede">1920×1080 그림 하나를 모든 곳에서 잘라 써요. 글자는 그림에 넣지 마세요 — 제목은 aDmD 가 붙여요.</p>
<div class="big-art a-paper"><div class="handles"><i style="left:-6px;top:-6px"></i><i style="right:-6px;top:-6px"></i><i style="left:-6px;bottom:-6px"></i><i style="right:-6px;bottom:-6px"></i></div></div>
<div class="crops"><div class="crop"><b>카드</b><span class="frame art a-paper" style="aspect-ratio:16/9"><span class="safe"></span></span>16:9</div>
<div class="crop"><b>공유 미리보기</b><span class="frame art a-paper" style="aspect-ratio:1.91/1"><span class="safe"></span></span>1200×630</div>
<div class="crop"><b>정사각 아이콘</b><span class="frame art a-paper" style="aspect-ratio:1/1;width:70%"><span class="safe"></span></span>선택 · 없으면 가운데</div></div></div>
<aside class="aside-tip"><b>이렇게 보여요</b><div class="gc"><span class="art a-paper"><span class="shots"></span><span class="plat">{ic("web","ic ic12")}</span><span class="jf maker" style="background:var(--color-face-cheongnok)">ㅊ<i>ㅅ</i>ㅊ</span></span><span class="t">종이 배 2</span><span class="meta">청록상회 · 탐험 · 20분</span></div><span>점선 안쪽에 중요한 걸 두면 어디서 잘려도 보여요. 얼굴 · 배지 자리는 모서리라 비워 두면 좋아요.</span></aside></div>
{wz_foot("다음 · 상세 정보")}</div>'''

def upload_page():
    body = f'''<div class="stagebg">
<div class="fr"><div class="cap"><b>3단계 · 빌드 올리기</b><span>8단계 막대 · 자동 저장 · 올린 즉시 형식 검사(통과 · 주의를 문장으로)</span></div>{wz_build()}</div>
<div class="fr"><div class="cap"><b>5단계 · 대표 그림</b><span>한 장으로 카드 · 공유 · 아이콘을 잘라 미리 보여 줌(R-MK-04). 안전 영역 점선</span></div>{wz_art()}</div>
</div>'''
    memo = "MG-UPLOAD. 8단계 마법사(기본 정보 → 실행 방식 → 빌드 → 미리 플레이 → 화면 → 상세 → 공개 → 제출). 사이드바 대신 위 단계 막대 + 아래 고정 버튼. 모든 단계 자동 저장, 휴대폰에서 이어 쓰기."
    html = dt.page("업로드 마법사", body, 1700, memo).replace('data-ground="play"', 'data-ground="make"')
    return html.replace("</style>", CSS + "\n</style>", 1)

def search_page():
    games = "".join(mg.game_card(a) for a in [("a-loop", "루프 디버거", "픽셀상점", "ㅍ", "jjok", "퍼즐 · 5분", "web"), ("a-grid", "픽셀 러너", "보라네", "ㅂ", "bora", "액션 · 3분", "web"), ("a-demon", "픽셀 들판", "풀잎", "ㅍ", "pul", "전략 · 30분", "dl"), ("a-tess", "픽셀 퍼즐 상자", "노을공방", "ㄴ", "haneul", "퍼즐 · 10분", "web")])
    games = games.replace("픽셀 ", '<span class="hl">픽셀</span> ').replace("픽셀상점", '<span class="hl">픽셀</span>상점')
    mk = "".join(f'<div class="mkc">{face(c,col,"md")}<span><b>{n}</b><span class="m">{d}</span></span><span class="btn btn-secondary btn-sm">팔로우</span></div>' for c, col, n, d in [("ㅍ", "jjok", '<span class="hl">픽셀</span>상점', "퍼즐 · 게임 4"), ("ㅍ", "hong", '<span class="hl">픽셀</span>공방', "아트 · 게임 1"), ("ㅍ", "pul", '<span class="hl">픽셀</span>나무', "잼 팀 · 게임 2")])
    logs = "".join(f'<div class="logrow"><span><b>{t}</b><span class="m">{w} · {d}</span></span><span class="art {a}"></span></div>' for t, w, d, a in [('<span class="hl">픽셀</span> 아트 팔레트 16색으로 줄이기', "풀잎", "3일 전 · 좋아요 83", "a-demon"), ('<span class="hl">픽셀</span> 폰트 라이선스 정리', "청록상회", "1주 전 · 좋아요 41", "a-paper")])
    body = dt.pg_header() + f'''<main class="wrap">
<div class="sr-h"><span class="q">‘<em>픽셀</em>’ 검색 결과</span><span class="m">게임 4 · 메이커 3 · 개발일지 2</span></div>
<nav class="utabs sr-tabs"><a href="#" aria-current="page">전체</a><a href="#">게임 4</a><a href="#">메이커 3</a><a href="#">개발일지 2</a><a href="#">태그</a></nav>
<div class="grp"><div class="sh">{EAR}<h2>게임</h2><div class="r"><div class="chips"><button class="chip" aria-pressed="true">관련순</button><button class="chip">최신순</button><button class="chip">{ic("web")}바로 플레이</button></div></div></div><div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px">{games}</div></div>
<div class="grp"><div class="sh">{EAR}<h2>메이커</h2></div><div class="mk-row">{mk}</div></div>
<div class="grp"><div class="sh">{EAR}<h2>개발일지</h2></div>{logs}</div>
<section class="sec"><p class="sub" style="font-size:14px;font-weight:800;color:var(--ink-2);margin:0 0 12px">결과가 없을 때 (예: ‘ㅍㄹㄱ’)</p>
<div class="noresult"><span class="logo f-sleep big-face">{logo("z")}</span><div><h3>‘ㅍㄹㄱ’ 에 맞는 게임이 없어요</h3><p>초성으로 찾았다면 한 글자 더 적어 보세요. 이런 건 어때요?</p>
<div class="chips"><button class="chip">플랫포머</button><button class="chip">퍼즐</button><button class="chip">이번 주 PICK</button><button class="chip">한 판 3분</button></div></div></div></section>
</main>''' + dt.footer()
    memo = "PG-SRCH. 게임 · 메이커 · 개발일지를 나눠 한 화면에(R-SRCH-01), 검색어는 형광펜 밑줄. 결과 없음은 졸린 고양이 + 조건 완화 제안 + 큐레이션 출구(R-SRCH-02)."
    html = dt.page("검색 결과", body, 2000, memo)
    return html.replace("</style>", CSS + "\n</style>", 1)

if __name__ == "__main__":
    for name, fn in [("로그인 · 내 얼굴 만들기.dc.html", login_page), ("업로드 마법사.dc.html", upload_page), ("검색 결과.dc.html", search_page)]:
        html = fn()
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print(name, len(html))
