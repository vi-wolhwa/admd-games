# DS04 게임 카드(손으로 만든 견본) — PG01 2차 피드백과 같은 카드 규칙 반영 (2026-11-27)
# 사용: python fix_ds04.py <DS04-game-cards.dc.html 경로>
import re, sys
sys.stdout.reconfigure(encoding="utf-8")
P = sys.argv[1]
s = open(P, encoding="utf-8").read()
if "/* 2차 피드백" in s:
    raise SystemExit("이미 적용됨")

def must(old, new):
    global s
    assert old in s, old[:90]
    s = s.replace(old, new, 1)

THUMB = '<symbol id="i-thumb" viewBox="0 0 16 16"><path d="M5 7.2v6.3H2.6V7.2z"></path><path d="M5 7.2 7.7 2.6c.9 0 1.6.8 1.4 1.7l-.4 2.5h3.6c1 0 1.7.9 1.5 1.8l-.9 4c-.2.6-.7.9-1.3.9H5"></path></symbol>\n'
must('<symbol id="i-bm" ', THUMB + '<symbol id="i-bm" ')

# 툴팁이 덮개 아래로 깔리지 않게: transform 대신 top
s = s.replace(".gc:hover .art,.gc.hov .art{transform:translateY(-3px);box-shadow:var(--lift)}", ".gc:hover .art,.gc.hov .art{top:-3px;box-shadow:var(--lift)}")
s = s.replace(".pick:hover .art{transform:translateY(-3px);box-shadow:var(--lift)}", ".pick:hover .art{top:-3px;box-shadow:var(--lift)}")
s = re.sub(r"transition:transform 240ms var\(--ease\),box-shadow 240ms var\(--ease\)", "top:0;transition:top 240ms var(--ease),box-shadow 240ms var(--ease)", s)

# 호버 미리보기: 5장 · 2.5초
must("@keyframes shot2{0%,30%{opacity:0}34%,64%{opacity:1}68%,100%{opacity:0}}\n@keyframes shot3{0%,64%{opacity:0}68%,96%{opacity:1}100%{opacity:0}}",
     "@keyframes shot2{0%,19%{opacity:0}20%,39%{opacity:1}40%,100%{opacity:0}}\n@keyframes shot3{0%,39%{opacity:0}40%,59%{opacity:1}60%,100%{opacity:0}}\n@keyframes shot4{0%,59%{opacity:0}60%,79%{opacity:1}80%,100%{opacity:0}}\n@keyframes shot5{0%,79%{opacity:0}80%,99%{opacity:1}100%{opacity:0}}\n"
     + "".join(f"@keyframes fr{n}{{0%,{(n-1)*20 - .1 if n > 1 else 0}%{{background:rgb(255 255 255 / .45)}}{(n-1)*20}%,{n*20 - .1}%{{background:#FFFFFF}}{n*20}%,100%{{background:rgb(255 255 255 / .45)}}}}\n" for n in range(1, 6)))
s = re.sub(r"\.gc:hover \.shots i:nth-child\(2\),\.pick:hover \.shots i:nth-child\(2\)\{animation:shot2 3\.6s \.4s linear infinite\}\n\.gc:hover \.shots i:nth-child\(3\),\.pick:hover \.shots i:nth-child\(3\)\{animation:shot3 3\.6s \.4s linear infinite\}",
           lambda m: "".join(f".gc:hover .shots i:nth-child({n}),.gc.hov .shots i:nth-child({n}),.pick:hover .shots i:nth-child({n}){{animation:shot{n} 12.5s .3s linear infinite}}\n" for n in range(2, 6))
           + "".join(f".gc:hover .frames b:nth-child({n}),.gc.hov .frames b:nth-child({n}){{animation:fr{n} 12.5s .3s linear infinite}}\n" for n in range(1, 6)).rstrip("\n"), s)
must(".s3{transform:scale(1.5) translate(10%,-6%);filter:brightness(1.08)}",
     ".s3{transform:scale(1.5) translate(10%,-6%);filter:brightness(1.08)}\n.s4{transform:scale(1.35) translate(8%,8%) rotate(-2deg);filter:hue-rotate(-12deg)}\n.s5{transform:scale(1.8) translate(-12%,-4%);filter:contrast(1.1)}")
must(".frames b{width:16px;height:3px;border-radius:2px;background:rgb(255 255 255 / .45)}", ".frames b{width:12px;height:3px;border-radius:2px;background:rgb(255 255 255 / .45)}\n.frames b:first-child{background:#FFFFFF}")
s = re.sub(r'<i class="(a-[a-z]+) s3"></i>', r'<i class="\1 s3"></i><i class="\1 s4"></i><i class="\1 s5"></i>', s)
s = s.replace('<span class="frames" aria-hidden="true"><b></b><b></b><b></b></span>', '<span class="frames" aria-hidden="true"><b></b><b></b><b></b><b></b><b></b></span>')

# 설치형: 오른쪽 아래 다운로드 버튼
QDL = '<span class="qplay" aria-hidden="true"><svg class="ic" style="width:16px;height:16px"><use href="#i-dl"></use></svg></span>'
s, k = re.subn(r'(<div class="gc m"><span class="art"><span class="shots"><i class="a-null"></i>.*?<span class="jf j26 maker"[^>]*>.*?</span>)(<span class="frames")', lambda m: m.group(1) + QDL + m.group(2), s, count=1, flags=re.S)
assert k == 1
must('<div class="lbl">설치형 · 빠른 플레이 없음</div>', '<div class="lbl">설치형 · 호버하면 다운로드 버튼</div>')

# 추천 = 개수 · 리뷰 = 개수, 글자로
CNT = lambda rec, rv: f'<span class="cnt"><svg class="ic" aria-hidden="true"><use href="#i-thumb"></use></svg>추천 <b>{rec:,}</b></span><span class="cnt"><svg class="ic" aria-hidden="true"><use href="#i-cmt"></use></svg>리뷰 <b>{rv:,}</b></span>'
s, k1 = re.subn(r'<span class="soc"><b>추천 (\d+)%</b> · 리뷰 (\d+)</span>', lambda m: f'<span class="soc">{CNT(int(int(m.group(2)) * int(m.group(1)) / 14), int(m.group(2)))}</span>', s)
assert k1 == 3, k1
must('<span class="soc" style="color:var(--ink-3)">아직 리뷰 3개</span></div><div class="lbl">신작 · 리뷰 10개 미만 (% 숨김)</div>', f'<span class="soc">{CNT(18, 3)}</span></div><div class="lbl">신작 · 숫자가 작아도 그대로 표시</div>')
must('<span class="soc"><span class="tag">진행 88%</span><b>추천 95%</b></span>', f'<span class="soc"><span class="tag">진행 88%</span>{CNT(612, 90)}</span>')
s = re.sub(r'<span class="soc" style="color:var\(--ok\);font-weight:700"><svg[^>]*><use href="#i-shield"></use></svg>Windows · 검사 통과 11\.24</span>', f'<span class="soc">{CNT(96, 11)}</span>', s, count=1)
s = s.replace("리뷰 10개 이상일 때 추천 % · 또는 친구 n명이 플레이(공개 설정 시)", "추천 수 · 리뷰 수(아이콘 + 글자, 싫어요 없음) · 또는 친구 n명이 플레이(공개 설정 시)")
must(".gc .soc b{color:var(--ink-1)}", ".gc .soc b{color:var(--ink-1);font-weight:700}\n.gc .soc{gap:12px;color:var(--ink-3)}\n.gc .soc .cnt{display:inline-flex;align-items:center;gap:4px}\n.gc .soc .cnt .ic{width:13px;height:13px;color:var(--ink-4)}")
s = s.replace("/* 자모 얼굴 = 고양이 얼굴 실루엣 */", "/* 2차 피드백(2026-11-27): 툴팁 · 호버 5장 2.5초 · 다운로드 버튼 · 추천 수 */\n/* 자모 얼굴 = 고양이 얼굴 실루엣 */", 1)
assert "/* 2차 피드백" in s
open(P, "w", encoding="utf-8", newline="").write(s)
print("ok")
