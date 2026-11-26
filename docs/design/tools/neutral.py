import sys; sys.stdout.reconfigure(encoding="utf-8")
exec(open("ramp.py",encoding="utf-8").read().split('W=hex2Y')[0])
for name,L,C in [("canvas",0.968,0.003),("sunken",0.946,0.004),("sunken-hover",0.925,0.005),("line",0.905,0.005),("line-strong",0.84,0.006),("ink-4",0.70,0.008),("ink-3",0.52,0.010),("ink-2",0.44,0.011),("ink-1",0.215,0.014),("ink-1-hover",0.30,0.014)]:
    rgb,c=lc(L,C,255); y=Y(rgb)
    print(f"{name:13} {hexs(rgb)} white {cr(y,1.0):.2f} canvas {cr(y,hex2Y('#F5F6F7')):.2f}")
