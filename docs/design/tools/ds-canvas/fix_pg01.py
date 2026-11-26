# PG01 홈(손으로 만든 확정본) 2차 피드백 반영 — 2026-11-27
# 사용: python fix_pg01.py <PG01-home.dc.html 경로>   (한 번만 적용. 다시 돌리면 이미 적용됐다고 멈춤)
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
P = sys.argv[1]
s = open(P, encoding="utf-8").read()
if "/* 2차 피드백" in s:
    raise SystemExit("이미 적용됨")

def must(old, new, count=1):
    global s
    assert old in s, old[:80]
    s = s.replace(old, new, count)

# 1) 아이콘: 추천(엄지)
THUMB = '<symbol id="i-thumb" viewBox="0 0 16 16"><path d="M5 7.2v6.3H2.6V7.2z"></path><path d="M5 7.2 7.7 2.6c.9 0 1.6.8 1.4 1.7l-.4 2.5h3.6c1 0 1.7.9 1.5 1.8l-.9 4c-.2.6-.7.9-1.3.9H5"></path></symbol>\n'
must('<symbol id="i-bm" ', THUMB + '<symbol id="i-bm" ')
from_sprite = True

# 2) 툴팁: 카드 hover 때 아트를 transform 으로 올리면 쌓임 맥락이 생겨 카드 전체 링크 덮개 아래로 깔림 → top 으로 올림
must(".gc .art{border-radius:10px;margin-bottom:7px;transition:transform 240ms var(--ease),box-shadow 240ms var(--ease)}",
     ".gc .art{border-radius:10px;margin-bottom:7px;top:0;transition:top 240ms var(--ease),box-shadow 240ms var(--ease)}")
must(".gc:hover .art{transform:translateY(-3px);box-shadow:var(--lift)}", ".gc:hover .art{top:-3px;box-shadow:var(--lift)}")
must(".pick .art{margin:0;border-radius:14px;transition:transform 240ms var(--ease),box-shadow 240ms var(--ease)}",
     ".pick .art{margin:0;border-radius:14px;top:0;transition:top 240ms var(--ease),box-shadow 240ms var(--ease)}")
must(".pick:hover .art{transform:translateY(-3px);box-shadow:var(--lift)}", ".pick:hover .art{top:-3px;box-shadow:var(--lift)}")
# 배너의 실행 칩에도 툴팁
must('<span class="plat" aria-label="브라우저에서 바로"><svg class="ic" aria-hidden="true"><use href="#i-web"></use></svg><span style="font-size:12px;font-weight:700">바로 플레이</span></span>',
     '<span class="plat" aria-label="브라우저에서 바로 플레이, 휴대폰 가능" tabindex="0"><svg class="ic" aria-hidden="true"><use href="#i-web"></use></svg><span style="font-size:12px;font-weight:700">바로 플레이</span><span class="tip" role="tooltip"><span><svg class="ic" aria-hidden="true"><use href="#i-web"></use></svg>브라우저에서 바로 플레이 · 설치 없음</span><span><svg class="ic" aria-hidden="true"><use href="#i-phone"></use></svg>휴대폰에서도 가능</span></span></span>')

# 3) 호버 미리보기: 이미지 5장을 2.5초마다(12.5초 한 바퀴), 영상이 있으면 영상 1개 반복
must("@keyframes shot2{0%,30%{opacity:0}34%,64%{opacity:1}68%,100%{opacity:0}}\n@keyframes shot3{0%,64%{opacity:0}68%,96%{opacity:1}100%{opacity:0}}",
     "@keyframes shot2{0%,19%{opacity:0}20%,39%{opacity:1}40%,100%{opacity:0}}\n@keyframes shot3{0%,39%{opacity:0}40%,59%{opacity:1}60%,100%{opacity:0}}\n@keyframes shot4{0%,59%{opacity:0}60%,79%{opacity:1}80%,100%{opacity:0}}\n@keyframes shot5{0%,79%{opacity:0}80%,99%{opacity:1}100%{opacity:0}}\n@keyframes fr1{0%,19.9%{background:#FFFFFF}20%,100%{background:rgb(255 255 255 / .45)}}\n@keyframes fr2{0%,19.9%{background:rgb(255 255 255 / .45)}20%,39.9%{background:#FFFFFF}40%,100%{background:rgb(255 255 255 / .45)}}\n@keyframes fr3{0%,39.9%{background:rgb(255 255 255 / .45)}40%,59.9%{background:#FFFFFF}60%,100%{background:rgb(255 255 255 / .45)}}\n@keyframes fr4{0%,59.9%{background:rgb(255 255 255 / .45)}60%,79.9%{background:#FFFFFF}80%,100%{background:rgb(255 255 255 / .45)}}\n@keyframes fr5{0%,79.9%{background:rgb(255 255 255 / .45)}80%,100%{background:#FFFFFF}}\n@keyframes vidpan{0%{transform:scale(1.04) translate(-2%,0)}50%{transform:scale(1.16) translate(3%,-2%)}100%{transform:scale(1.04) translate(-2%,0)}}\n@keyframes vidbar{from{transform:scaleX(0)}to{transform:scaleX(1)}}")
must(".gc:hover .shots i:nth-child(2),.pick:hover .shots i:nth-child(2){animation:shot2 3.6s .4s linear infinite}\n.gc:hover .shots i:nth-child(3),.pick:hover .shots i:nth-child(3){animation:shot3 3.6s .4s linear infinite}",
     "".join(f".gc:hover .shots i:nth-child({n}),.pick:hover .shots i:nth-child({n}){{animation:shot{n} 12.5s .3s linear infinite}}\n" for n in range(2, 6))
     + "".join(f".gc:hover .frames b:nth-child({n}){{animation:fr{n} 12.5s .3s linear infinite}}\n" for n in range(1, 6)).rstrip("\n"))
must(".s3{transform:scale(1.5) translate(10%,-6%);filter:brightness(1.08)}",
     ".s3{transform:scale(1.5) translate(10%,-6%);filter:brightness(1.08)}\n.s4{transform:scale(1.35) translate(8%,8%) rotate(-2deg);filter:hue-rotate(-12deg)}\n.s5{transform:scale(1.8) translate(-12%,-4%);filter:contrast(1.1)}")
must(".frames b{width:16px;height:3px;border-radius:2px;background:rgb(255 255 255 / .45)}",
     ".frames b{width:12px;height:3px;border-radius:2px;background:rgb(255 255 255 / .45)}\n.frames b:first-child{background:#FFFFFF}\n.frames.vid b{position:relative;width:56px;overflow:hidden}\n.frames.vid b::after{content:\"\";position:absolute;inset:0;background:#FFFFFF;transform-origin:left;transform:scaleX(0)}\n.gc:hover .frames.vid b{animation:none}\n.gc:hover .frames.vid b::after{animation:vidbar 6s .3s linear infinite}\n.shots.vid i:not(:first-child){display:none}\n.gc:hover .shots.vid i:first-child{animation:vidpan 6s .3s linear infinite}\n.vtag{position:absolute;right:8px;top:8px;z-index:2;opacity:0}")
# 카드 5장으로
s = re.sub(r'<i class="(a-[a-z]+) s3"></i>', r'<i class="\1 s3"></i><i class="\1 s4"></i><i class="\1 s5"></i>', s)
s = s.replace('<span class="frames" aria-hidden="true"><b></b><b></b><b></b></span>', '<span class="frames" aria-hidden="true"><b></b><b></b><b></b><b></b><b></b></span>')
# 영상을 올린 게임 예시 2개: 테서랙트 드리프트 · 데몬 가든
for art in ("a-tess", "a-demon"):
    old = f'<span class="shots"><i class="{art}"></i>'
    assert old in s
    s = s.replace(old, f'<span class="shots vid"><i class="{art}"></i>')
s = re.sub(r'(<span class="shots vid"><i class="a-(?:tess|demon)"></i>.*?)<span class="frames" aria-hidden="true">(?:<b></b>)+</span>',
           r'\1<span class="frames vid" aria-hidden="true"><b></b></span>', s, flags=re.S)
# (위 정규식은 같은 카드 안에서만 맞도록 확인)
assert s.count('class="frames vid"') == 2, s.count('class="frames vid"')

# 4) 다운로드만 되는 게임은 오른쪽 아래 버튼이 다운로드
QDL = '<span class="qplay" aria-hidden="true"><svg class="ic" style="width:16px;height:16px"><use href="#i-dl"></use></svg></span>'
n = 0
for art in ("a-null", "a-tilt"):
    pat = re.compile(r'(<div class="gc"><span class="art"><span class="shots"><i class="' + art + r'"></i>.*?</span><span class="jf j26 maker"[^>]*>.*?</span>)(<span class="frames")', re.S)
    s, k = pat.subn(r'\1' + QDL.replace("\\", "\\\\") + r'\2', s, count=1)
    n += k
assert n == 2, n

# 5) 추천 = 개수, 리뷰 = 개수, 둘 다 글자로 (싫어요 없음)
CNT = lambda rec, rv: f'<span class="cnt"><svg class="ic" aria-hidden="true"><use href="#i-thumb"></use></svg>추천 <b>{rec:,}</b></span><span class="cnt"><svg class="ic" aria-hidden="true"><use href="#i-cmt"></use></svg>리뷰 <b>{rv:,}</b></span>'
def rec_of(pct, rv): return int(rv * pct / 14)
def soc_pct(m):
    pct, rv = int(m.group(1)), int(m.group(2))
    return f'<span class="soc">{CNT(rec_of(pct, rv), rv)}</span>'
s, k1 = re.subn(r'<span class="soc"><b>추천 (\d+)%</b> · (?:리뷰 )?(\d+)</span>', soc_pct, s)
s, k2 = re.subn(r'<span class="soc" style="color:var\(--ink-3\)">아직 리뷰 (\d+)개</span>', lambda m: f'<span class="soc">{CNT(int(m.group(1)) * 6, int(m.group(1)))}</span>', s)
must('<span class="soc"><span class="tag">진행 45%</span><b>추천 84%</b></span>', f'<span class="soc"><span class="tag">진행 45%</span>{CNT(212, 37)}</span>')
must('<span class="soc" style="color:var(--ok);font-weight:700"><svg class="ic" aria-hidden="true"><use href="#i-shield"></use></svg>Windows · 검사 통과</span>', f'<span class="soc">{CNT(96, 11)}</span>')
print("soc", k1, k2)
must(".gc .soc b{color:var(--ink-1)}", ".gc .soc b{color:var(--ink-1);font-weight:700}\n.gc .soc{gap:12px;color:var(--ink-3)}\n.gc .soc .cnt{display:inline-flex;align-items:center;gap:4px}\n.gc .soc .cnt .ic{width:13px;height:13px;color:var(--ink-4)}")

# 6) 이어하기: 진행도는 게임이 SDK 로 알려 줄 때만, 설치형은 플레이 기록 없음
must('<span class="bar" role="progressbar" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100" aria-label="진행 62%"><i style="width:62%"></i></span><div class="row"><div style="min-width:0"><b class="t" style="font-size:16px"><a href="#">루프 컴파일러</a></b><div class="m num">62% · 어제 · 도전과제 23/40</div>',
     '<span class="bar" role="progressbar" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100" aria-label="진행 62%"><i style="width:62%"></i></span><div class="row"><div style="min-width:0"><b class="t" style="font-size:16px"><a href="#">루프 컴파일러</a></b><div class="m num">진행 62% · 어제 · 2시간 10분 플레이</div>')
must('<span class="bar" aria-label="진행 88%"><i style="width:88%"></i></span><div class="row"><div style="min-width:0"><b class="t" style="font-size:16px"><a href="#">그리드락</a></b><div class="m num">88% · 그저께 · 도전과제 7/8</div>',
     '<div class="row"><div style="min-width:0"><b class="t" style="font-size:16px"><a href="#">그리드락</a></b><div class="m num">그저께 · 1시간 40분 플레이</div>')
must('<span class="bar" aria-label="진행 31%"><i style="width:31%"></i></span><div class="row"><div style="min-width:0"><b class="t" style="font-size:16px"><a href="#">틸트 이론</a></b><div class="m num">31% · 설치형 · 5일 전</div>',
     '<div class="row"><div style="min-width:0"><b class="t" style="font-size:16px"><a href="#">틸트 이론</a></b><div class="m num">설치형 · v1.3 받음 · 5일 전</div>')

# 7) 다크 모드: 랭킹 띠의 쪽빛 바탕을 없애고 페이지 바탕과 같게
must('[data-theme="dark"] .rr{background:#191C20}', '[data-theme="dark"] .band{background:transparent;padding:0}\n[data-theme="dark"] .rr{background:#191C20}')

s = s.replace("/* 자모 얼굴 = 고양이 얼굴 실루엣 */", "/* 2차 피드백(2026-11-27): 툴팁 · 호버 미디어 · 다운로드 버튼 · 추천 수 · 이어하기 · 다크 랭킹 */\n/* 자모 얼굴 = 고양이 얼굴 실루엣 */", 1)
open(P, "w", encoding="utf-8", newline="").write(s)
print("ok", len(s))
