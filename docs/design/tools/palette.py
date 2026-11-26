import math,sys
sys.stdout.reconfigure(encoding="utf-8")
def oklch_to_srgb(L,C,h):
    a=C*math.cos(math.radians(h)); b=C*math.sin(math.radians(h))
    l_=L+0.3963377774*a+0.2158037573*b; m_=L-0.1055613458*a-0.0638541728*b; s_=L-0.0894841775*a-1.2914855480*b
    l,m,s=l_**3,m_**3,s_**3
    r=4.0767416621*l-3.3077115913*m+0.2309699292*s
    g=-1.2684380046*l+2.6097574011*m-0.3413193965*s
    bb=-0.0041960863*l-0.7034186147*m+1.7076147010*s
    return r,g,bb
def lin2s(x): return 12.92*x if x<=0.0031308 else 1.055*x**(1/2.4)-0.055
def s2lin(x): return x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4
def ing(rgb): return all(-1e-6<=c<=1+1e-6 for c in rgb)
def Y(rgb): r,g,b=rgb; return 0.2126*r+0.7152*g+0.0722*b
def hexs(rgb): return "#"+"".join(f"{round(min(1,max(0,lin2s(c)))*255):02X}" for c in rgb)
def hex2Y(h): r,g,b=[s2lin(int(h[i:i+2],16)/255) for i in (1,3,5)]; return 0.2126*r+0.7152*g+0.0722*b
def cr(y1,y2): a,b=max(y1,y2),min(y1,y2); return (a+.05)/(b+.05)
def at_luminance(h,target,cmax=0.4):
    best=None
    C=0.0
    while C<=cmax:
        lo,hi=0.0,1.0
        for _ in range(60):
            mid=(lo+hi)/2
            if Y(oklch_to_srgb(mid,C,h))<target: lo=mid
            else: hi=mid
        rgb=oklch_to_srgb(hi,C,h)
        if ing(rgb): best=(hi,C,rgb)
        C+=0.002
    return best
target=float(sys.argv[1]) if len(sys.argv)>1 else 0.155
surfaces={"white":"#FFFFFF"}
for extra in sys.argv[2:]: surfaces[extra]=extra
print("target Y",target)
for h in [20,28,35,41,48,140,150,160,240,250,255,260,265,270,280,300,330,350]:
    L,C,rgb=at_luminance(h,target)
    y=Y(rgb)
    print(f"h{h:>3} L{L:.3f} C{C:.3f} {hexs(rgb)} "+" ".join(f"{k}:{cr(y,hex2Y(v)):.2f}" for k,v in surfaces.items()))
