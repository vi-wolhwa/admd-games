# 캔버스 '디자인 시스템 · 기초/컴포넌트' 페이지 생성기
#   tokens.css(Tailwind 4) → 일반 CSS 변수로 바꿔 템플릿에 넣는다. 토큰을 바꾸면 다시 돌려 캔버스에 게시한다.
# 실행: python build.py <출력 폴더>   (보통 Artifact read 로 받은 …/artifact-files/57ed…/project)
import re, sys, os
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "docs", "design", "canvas")

def canvas_tokens():
    s = open(os.path.join(REPO, "docs", "design", "system", "tokens.css"), encoding="utf-8").read()
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
    s = re.sub(r"@theme inline\s*\{.*?\n\}", "", s, flags=re.S)
    # @media (prefers-color-scheme: dark) { ... } 블록 제거(캔버스는 Tweaks 로 명시 전환)
    i = s.index("@media (prefers-color-scheme: dark)")
    depth = 0; j = s.index("{", i)
    for k in range(j, len(s)):
        if s[k] == "{": depth += 1
        elif s[k] == "}":
            depth -= 1
            if depth == 0: break
    s = s[:i] + s[k + 1:]
    s = s.replace("@theme {", ":root {")
    s = "\n".join(l for l in s.split("\n") if "initial;" not in l)
    s = s.replace("'Pretendard Variable', Pretendard,", "'Pretendard',")
    s = re.sub(r"\n\s*\n+", "\n", s)
    s = re.sub(r"\n\t+", "\n", s)
    return s.strip()

EARS = '<svg class="ears" viewBox="0 0 64 20" preserveAspectRatio="none" aria-hidden="true"><path d="M3 19 L8 2 L20 10 Q32 6 44 10 L56 2 L61 19"></path></svg>'
def cat(mouth): return f'<span class="cat">{EARS}<span class="e">D</span><span class="mo">{mouth}</span><span class="e">D</span></span>'

def duo(theme):
    label = "라이트" if theme == "light" else "다크"
    return f'''<div data-theme="{theme}" data-ground="{{{{ ground }}}}">
<span class="cap">{label}</span>
<div class="chips"><button class="chip" aria-pressed="true">전체</button><button class="chip">퍼즐 <span class="c">24</span></button><span class="btn btn-primary btn-sm"><svg class="ic"><use href="#i-play"></use></svg>플레이</span><span class="btn btn-secondary btn-sm">즐겨찾기</span></div>
<div class="mini-cards">
<div class="gc lift"><span class="art a-loop"><span class="shots"></span><span class="badge">PICK</span><span class="plat"><svg class="ic ic12"><use href="#i-web"></use></svg></span><span class="jf maker" style="background:var(--color-face-jjok)">ㅍ<i>ㅅ</i>ㅍ</span></span><span class="t">루프 디버거</span><span class="meta">픽셀상점 · 퍼즐 · 5분</span></div>
<div class="gc"><span class="art a-ash"><span class="shots"></span><span class="badge ink">업데이트</span><span class="plat"><svg class="ic ic12"><use href="#i-dl"></use></svg><svg class="ic ic12 ok"><use href="#i-shield"></use></svg></span><span class="jf maker" style="background:var(--color-face-ju)">ㅈ<i>ㅅ</i>ㅈ</span><span class="prog"><i style="width:45%"></i></span></span><span class="t">재의 도시</span><span class="meta">잿빛토끼 · 진행 45%</span></div>
</div>
<div class="mini-band">
<div class="rr"><span class="n top disp">1</span><span class="art a-tess"></span><span><b>테셀레이트</b><span class="by"><span class="jf xs" style="background:var(--color-face-haneul)">ㄴ<i>ㅅ</i>ㄴ</span>노을공방</span></span><span class="k">▲ 3</span></div>
<div class="rr"><span class="n disp">4</span><span class="art a-paper"></span><span><b>종이 배</b><span class="by"><span class="jf xs" style="background:var(--color-face-cheongnok)">ㅊ<i>ㅅ</i>ㅊ</span>청록상회</span></span><span class="k dn">▼ 1</span></div>
</div>
<p class="m" style="margin:0">메타 글자 ink-3 · <span style="color:var(--accent-text);font-weight:700">강조 글자 accent-text</span> · <span style="color:var(--ok-text);font-weight:700">검사 통과</span> · <span style="color:var(--danger-text);font-weight:700">오류</span></p>
</div>'''

def build(tpl_name, out_name):
    t = open(os.path.join(HERE, tpl_name), encoding="utf-8").read()
    t = t.replace("/*TOKENS*/", canvas_tokens())
    t = t.replace("/*COMMON*/", open(os.path.join(HERE, "common.css"), encoding="utf-8").read())
    t = t.replace("[[SPRITE]]", open(os.path.join(HERE, "sprite.html"), encoding="utf-8").read())
    t = re.sub(r"\[\[LOGO (\w)\]\]", lambda m: "<span>a</span>" + cat(m.group(1)), t)
    t = re.sub(r"\[\[CAT (\w)\]\]", lambda m: cat(m.group(1)), t)
    t = re.sub(r"\[\[DUO (\w+)\]\]", lambda m: duo(m.group(1)), t)
    left = re.findall(r"\[\[[A-Z]+[^\]]*\]\]|/\*(TOKENS|COMMON)\*/", t)
    assert not left, left
    import importlib.util as _u
    _s=_u.spec_from_file_location("cat_face", os.path.join(HERE, "cat_face.py")); _m=_u.module_from_spec(_s); _s.loader.exec_module(_m)
    t = _m.catify(t)
    open(os.path.join(OUT, out_name), "w", encoding="utf-8").write(t)
    print(out_name, len(t))

if __name__ == "__main__":
    for tpl, out in [("foundations.tpl.html", "DS01-foundations.dc.html"), ("components.tpl.html", "DS02-components.dc.html")]:
        if os.path.exists(os.path.join(HERE, tpl)): build(tpl, out)
