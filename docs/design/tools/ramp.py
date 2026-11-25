import sys; sys.stdout.reconfigure(encoding="utf-8")
exec(open("palette.py",encoding="utf-8").read().split("target=float")[0])
def lc(L,C,h):
    # reduce chroma until in gamut
    while C>0 and not ing(oklch_to_srgb(L,C,h)): C-=0.002
    return oklch_to_srgb(L,C,h),C
W=hex2Y("#FFFFFF")
print("== accents at Y .155 (text+fill), strong Y .10 (hover/text on tint), tint L .965")
for name,h in [("jjok(play)",254),("inju(make)",33),("jade(ok)",152),("crimson(danger)",18)]:
    L,C,rgb=at_luminance(h,0.155); 
    Ls,Cs,rgbs=at_luminance(h,0.10)
    t,tc=lc(0.965,0.03,h); t2,tc2=lc(0.93,0.06,h)
    print(f"{name:16} base {hexs(rgb)} (L{L:.3f} C{C:.3f})  strong {hexs(rgbs)}  tint {hexs(t)}  tint2 {hexs(t2)}  strong-on-tint {cr(Y(rgbs),Y(t)):.2f} base-on-tint {cr(Y(rgb),Y(t)):.2f}")
print("== neutral ramp h255 C~0.008")
for L in [0.985,0.965,0.945,0.925,0.88,0.80,0.70,0.60,0.52,0.44,0.36,0.28,0.22,0.18,0.15]:
    rgb,C=lc(L,0.009 if L>0.3 else 0.012,255)
    print(f"L{L:.3f} {hexs(rgb)} vsWhite {cr(Y(rgb),W):.2f} vs#F4F5F6 {cr(Y(rgb),hex2Y('#F4F5F6')):.2f}")
