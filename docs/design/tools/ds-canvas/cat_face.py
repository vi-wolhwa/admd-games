# 자모 얼굴 → 고양이 얼굴 실루엣 (S2 결정, 2026-11-26)
# 모든 캔버스 페이지에 같은 변환을 적용한다: 인라인 background → --f 변수, 실루엣 마스크 CSS 주입
import re

# 100×100 고양이 머리(둥근 귀 끝) — 로고 귀와 같은 비례
CAT_PATH = "M8 44 Q8 24 11 8 Q12 2 17 5 L36 20 Q50 16 64 20 L83 5 Q88 2 89 8 Q92 24 92 44 Q99 56 97 69 Q93 97 50 97 Q7 97 3 69 Q1 56 8 44 Z"
MASK = ("url(\"data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cpath d='"
        + CAT_PATH + "'/%3E%3C/svg%3E\") center/100% 100% no-repeat")

CSS = """
/* 자모 얼굴 = 고양이 얼굴 실루엣 (S2) — 색은 --f, 모양은 마스크 */
.jf{background:none!important;border-radius:0!important;box-shadow:none!important;isolation:isolate;box-sizing:border-box;padding-top:.62em;overflow:visible}
.jf:not(.maker):not([class*="maker"]){position:relative}
.jf::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--f,#3870B1);-webkit-mask:MASK;mask:MASK}
.jf.maker::after,.facerow .jf::after,.band-login .jf::after,.mk-hero .jf::after,.onb .left > .jf::after,.jf.ring::after{content:"";position:absolute;inset:-9%;z-index:-2;background:#FFFFFF;-webkit-mask:MASK;mask:MASK}
.jf i{top:.02em}
""".replace("MASK", MASK)

_TAG = re.compile(r'<span class="(jf[^"]*)"([^>]*)>')

def _fix_tag(m):
    cls, rest = m.group(1), m.group(2)
    rest = re.sub(r'style="([^"]*)"', lambda s: 'style="' + re.sub(r'(^|;)\s*background:', r'\1--f:', s.group(1)) + '"', rest)
    return f'<span class="{cls}"{rest}>'

def catify(html: str) -> str:
    if "자모 얼굴 = 고양이 얼굴 실루엣" in html:
        return html
    html = _TAG.sub(_fix_tag, html)
    # 마지막 </style> 앞에 넣어 다른 규칙보다 나중에 적용
    i = html.rfind("</style>")
    return html[:i] + CSS + html[i:]
