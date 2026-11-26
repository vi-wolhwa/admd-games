# 자모 얼굴 → 고양이 얼굴 실루엣 (S2 결정, 2026-11-26 · F1 개정: 실루엣 키우고 글자 줄임)
# 모든 캔버스 페이지에 같은 변환을 적용한다: 인라인 background → --f 변수, 글자 감싸기, 실루엣 마스크 CSS 주입
import re

# 100×100 고양이 머리(둥근 귀 끝) — 로고 귀와 같은 비례
CAT_PATH = "M8 44 Q8 24 11 8 Q12 2 17 5 L36 20 Q50 16 64 20 L83 5 Q88 2 89 8 Q92 24 92 44 Q99 56 97 69 Q93 97 50 97 Q7 97 3 69 Q1 56 8 44 Z"
MASK = ("url(\"data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpath d='"
        + CAT_PATH + "'/%3E%3C/svg%3E\") center/100% 100% no-repeat")

START = "/* 자모 얼굴 = 고양이 얼굴 실루엣 */"
END = "/* /자모 얼굴 */"
# 레이아웃 칸(정사각)은 그대로 두고, 실루엣은 칸보다 크게(가로 124% · 세로 118%) 그려 얼굴 영역을 넓힌다.
# 글자는 .jfg 로 감싸 0.8배 · 좁은 자간 → 머리 안(귀 아래)에 들어간다.
CSS = START + """
.jf{background:none!important;border-radius:0!important;box-shadow:none!important;isolation:isolate;box-sizing:border-box;padding-top:.5em;overflow:visible}
.jf:not(.maker):not([class*="maker"]){position:relative}
.jf::before{content:"";position:absolute;inset:-14% -12% -4%;z-index:-1;background:var(--f,#3870B1);-webkit-mask:MASK;mask:MASK}
.jf.maker::after,.facerow .jf::after,.band-login .jf::after,.mk-hero .jf::after,.onb .left > .jf::after,.jf.ring::after{content:"";position:absolute;inset:-22% -19% -11%;z-index:-2;background:#FFFFFF;-webkit-mask:MASK;mask:MASK}
.jfg{display:inline-flex;align-items:center;font-size:.8em;letter-spacing:-.1em;line-height:1;white-space:nowrap}
.jf i{top:.02em}
""".replace("MASK", MASK) + END + "\n"

_TAG = re.compile(r'<span class="(jf[^"]*)"([^>]*)>')
_INNER = re.compile(r'(<span class="jf[^"]*"[^>]*>)((?:(?!<span|</span>).)*?<i>(?:(?!</span>).)*?</i>(?:(?!<span|</span>).)*?)(</span>)', re.S)

def _fix_tag(m):
    cls, rest = m.group(1), m.group(2)
    rest = re.sub(r'style="([^"]*)"', lambda s: 'style="' + re.sub(r'(^|;)\s*background:', r'\1--f:', s.group(1)) + '"', rest)
    return f'<span class="{cls}"{rest}>'

def catify(html: str) -> str:
    # 예전에 넣은 블록(옛 표식 포함)은 지우고 새로 넣는다
    html = re.sub(r"/\* 자모 얼굴 = 고양이 얼굴 실루엣.*?(?:/\* /자모 얼굴 \*/\n|\.jf i\{top:\.02em\}\n)", "", html, flags=re.S)
    html = _TAG.sub(_fix_tag, html)
    if 'class="jfg"' not in html:
        html = _INNER.sub(lambda m: m.group(1) + '<b class="jfg">' + m.group(2) + '</b>' + m.group(3), html)
    i = html.rfind("</style>")
    return html[:i] + CSS + html[i:]
