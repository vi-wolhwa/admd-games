# 손으로 만든 페이지(PG01 홈 · DS04 게임 카드) — 3차 피드백(2026-11-27) 전역 규칙 반영
# 즐겨찾기(별) · 누를 수 있는 것에 테두리 · '이어하기' 는 게임이 진행도를 알려 줄 때만
# 사용: python fix_1127c.py <PG01-home.dc.html> <DS04-game-cards.dc.html>
import sys
sys.stdout.reconfigure(encoding="utf-8")
STAR = 'M8 1.9l1.85 3.8 4.15.6-3 2.95.7 4.15L8 11.45 4.3 13.4l.7-4.15-3-2.95 4.15-.6z'
MARK = "/* 3차 피드백(2026-11-27) */"

def common(s):
    s = s.replace('<symbol id="i-bm" viewBox="0 0 16 16"><path d="M4 2h8v12l-4-3-4 3z"></path></symbol>', f'<symbol id="i-bm" viewBox="0 0 16 16"><path d="{STAR}"></path></symbol>')
    s = s.replace('<symbol id="i-bmf" viewBox="0 0 16 16"><path d="M4 2h8v12l-4-3-4 3z" fill="currentColor"></path></symbol>', f'<symbol id="i-bmf" viewBox="0 0 16 16"><path d="{STAR}" fill="currentColor"></path></symbol>')
    s = s.replace('aria-label="저장 취소"', 'aria-label="즐겨찾기 해제"').replace('aria-label="저장"', 'aria-label="즐겨찾기"')
    assert "M4 2h8v12" not in s
    css = (f"{MARK}\n:root{{--line-strong:#D3D6DA}}\n[data-theme=\"dark\"]{{--line-strong:#3B4046}}\n"
           ".chip{background:var(--bg);box-shadow:inset 0 0 0 1px var(--line-strong)}\n.chip:hover{background:var(--sunken)}\n.chip[aria-pressed=\"true\"]{box-shadow:none}\n"
           ".arw{background:var(--bg);box-shadow:inset 0 0 0 1px var(--line-strong)}\n.arw:hover{background:var(--sunken)}\n"
           ".save:hover{color:var(--accent-strong)}\n")
    return s.replace("/* 자모 얼굴 = 고양이 얼굴 실루엣 */", css + "/* 자모 얼굴 = 고양이 얼굴 실루엣 */", 1)

pg01, ds04 = sys.argv[1], sys.argv[2]
s = open(pg01, encoding="utf-8").read()
if MARK in s: raise SystemExit("이미 적용됨")
s = common(s)
for a, b in [('<h2 id="cont-title">이어하기</h2>', '<h2 id="cont-title">최근 플레이</h2>'),
             ('<div class="m num">그저께 · 1시간 40분 플레이</div></div><button type="button" class="go"><svg class="ic" aria-hidden="true"><use href="#i-play"></use></svg>이어하기</button>',
              '<div class="m num">그저께 · 1시간 40분 플레이</div></div><button type="button" class="go"><svg class="ic" aria-hidden="true"><use href="#i-play"></use></svg>플레이</button>')]:
    assert a in s, a[:60]; s = s.replace(a, b, 1)
open(pg01, "w", encoding="utf-8", newline="").write(s)

s = open(ds04, encoding="utf-8").read()
if MARK in s: raise SystemExit("DS04 이미 적용됨")
s = common(s)
open(ds04, "w", encoding="utf-8", newline="").write(s)
print("ok")
