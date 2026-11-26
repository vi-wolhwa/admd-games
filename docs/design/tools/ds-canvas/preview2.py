# .dc.html → 로컬 미리보기 HTML (sc-if 평가, {{ }} 치환)
import sys,re,os
sys.stdout.reconfigure(encoding='utf-8')
HERE=os.path.dirname(os.path.abspath(__file__))
# 사용: python preview2.py "<페이지>.dc.html" <태그> [원본 폴더] [출력 폴더]
P=sys.argv[3] if len(sys.argv)>3 else os.path.join(HERE,"..","..","canvas")
OUT=sys.argv[4] if len(sys.argv)>4 else os.path.join(HERE,"preview")
def conv(name, out, vals):
    s=open(os.path.join(P,name),encoding='utf-8').read()
    head=re.search(r"<helmet>(.*?)</helmet>",s,re.S).group(1)
    body=re.search(r"</helmet>(.*?)</x-dc>",s,re.S).group(1)
    def scif(m):
        v=vals.get(m.group(1),False)
        return m.group(2) if v else ""
    prev=None
    while prev!=body:
        prev=body
        body=re.sub(r'<sc-if value="\{\{ (\w+) \}\}"[^>]*>((?:(?!<sc-if).)*?)</sc-if>',scif,body,flags=re.S)
    for k,v in vals.items(): body=body.replace("{{ %s }}"%k,str(v))
    body=re.sub(r'onClick="\{\{ \w+ \}\}"','',body)
    assert "{{" not in body, re.findall(r"\{\{[^}]*\}\}",body)[:5]
    open(os.path.join(OUT,out),"w",encoding="utf-8").write(f"<!doctype html><html lang='ko'><head><meta charset='utf-8'>{head}</head><body>{body}</body></html>")
if __name__=="__main__":
    name=sys.argv[1]; tag=sys.argv[2]
    for signed in (True,False):
        for theme in ("light","dark"):
            conv(name,f"{tag}-{'m' if signed else 'g'}-{theme}.html",dict(signedIn=signed,guest=not signed,theme=theme,showMemo=False))
    print("ok",tag)
