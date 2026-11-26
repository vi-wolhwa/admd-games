# 다크 모드 토큰 계산 — palette.py / ramp.py 와 같은 OKLCH 방식
# 실행: python dark.py
import sys; sys.stdout.reconfigure(encoding="utf-8")
exec(open("ramp.py",encoding="utf-8").read().split('W=hex2Y')[0])
def cy(h1,h2): return cr(hex2Y(h1),hex2Y(h2))
print("== dark neutrals h255")
N={}
for name,L,C in [("bg",0.185,0.008),("raised",0.225,0.010),("sunken",0.255,0.011),("sunken-2",0.29,0.012),("line",0.285,0.010),("ink-4",0.56,0.010),("ink-3",0.73,0.010),("ink-2",0.83,0.008),("ink-1",0.955,0.004)]:
    rgb,c=lc(L,C,255); N[name]=hexs(rgb)
    print(f"{name:9} {N[name]}  bg {cy(N[name],N.get('bg',N[name])):.2f}")
for k in ["ink-1","ink-2","ink-3","ink-4"]:
    print(f"  {k} on bg {cy(N[k],N['bg']):.2f} / sunken {cy(N[k],N['sunken']):.2f} / raised {cy(N[k],N['raised']):.2f}")
print("== dark accents: text (Y target) and tint (L .30)")
for name,h,ty in [("play",254,0.30),("make",33,0.31),("ok",152,0.31),("danger",18,0.31)]:
    L,C,rgb=at_luminance(h,ty); t=hexs(rgb)
    tint,_=lc(0.27,0.055,h); tint=hexs(tint)
    print(f"{name:7} text {t} on bg {cy(t,N['bg']):.2f} on sunken {cy(t,N['sunken']):.2f} on tint {cy(t,tint):.2f} | tint {tint} | ink-1 on tint {cy(N['ink-1'],tint):.2f}")
print("== light-mode fills kept in dark (white text / vs bg)")
for name,f in [("play",'#046DCE'),("make",'#D22C02'),("ok",'#047F3F'),("danger",'#DB0240')]:
    print(f"{name:7} {f} white-on {cy('#FFFFFF',f):.2f} vs dark bg {cy(f,N['bg']):.2f}")
print("== dark tint-2 (L .32)")
for name,h in [("play",254),("make",33)]:
    t,_=lc(0.32,0.07,h); print(name,hexs(t))
