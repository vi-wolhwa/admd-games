# 자모 얼굴 타일 색 12개 — 같은 휘도(Y .155, 흰 글자 5.1:1) · 색상각 고르게 · 채도 상한 C .12(차분하게)
# 실행: python faces.py
import sys; sys.stdout.reconfigure(encoding="utf-8")
exec(open("palette.py",encoding="utf-8").read().split("target=float")[0])
names=["홍","주","귤","황","올리브","풀","비취","청록","하늘","쪽","보라","자두"]
for i,h in enumerate([20,45,62,95,115,140,160,195,225,254,290,335]):
    L,C,rgb=at_luminance(h,0.155,0.12); 
    print(f"{names[i]:4} h{h:>3} {hexs(rgb)}  white {cr(Y(rgb),1.0):.2f}")
