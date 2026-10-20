#!/usr/bin/env python3
"""Generate SEO-friendly static pages for published weekly blog posts."""
import html,json,os,re,urllib.request,unicodedata
from pathlib import Path
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"veckoblogg"
BASE="https://skaraborgmaskin.se"
SB="https://jnorvriiehandxlvwkkg.supabase.co"
KEY=os.environ["SUPABASE_PUBLISHABLE_KEY"]
MARKER="<!-- GENERATED WEEKLY BLOG SEO; DO NOT EDIT -->"
def safe(v): return html.escape(str(v or ""),quote=True)
def slug(v):
    x=unicodedata.normalize("NFKD",v.lower())
    x="".join(c for c in x if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+","-",x).strip("-")[:65] or "veckan"
def fetch():
    url=SB+"/rest/v1/weekly_blog_posts?select=id,week_start,title,body,image_paths,updated_at&published=eq.true&order=week_start.desc&limit=500"
    req=urllib.request.Request(url,headers={"apikey":KEY,"Accept":"application/json"})
    with urllib.request.urlopen(req,timeout=30) as response:return json.load(response)
def render(p,url):
    title=str(p["title"]).strip()
    body=str(p["body"]).strip()
    intro=" ".join(body.split())[:155]
    desc=intro or ("Följ veckan hos Skaraborg Maskin & Återbruk.")
    images=[SB+"/storage/v1/object/public/ad-images/"+x for x in p.get("image_paths",[]) if isinstance(x,str) and not x.startswith("/") and ".." not in x]
    ld={"@context":"https://schema.org","@type":"BlogPosting","headline":title,"description":desc,"mainEntityOfPage":url,"url":url,"author":{"@type":"Organization","name":"Skaraborg Maskin & Återbruk"},"publisher":{"@type":"Organization","name":"Skaraborg Maskin & Återbruk"},"datePublished":p["week_start"],"dateModified":str(p.get("updated_at") or p["week_start"])[:10]}
    if images:ld["image"]=images
    ldtext=json.dumps(ld,ensure_ascii=False).replace("<",r"\u003c")
    photos="".join('<img src="'+safe(x)+'" alt="'+safe(title)+' – bild från veckan" loading="lazy">' for x in images)
    return f"""<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{safe(title)} | Veckan hos oss – Skaraborg Maskin &amp; Återbruk</title>
<meta name="description" content="{safe(desc)}"><link rel="canonical" href="{safe(url)}">
<meta property="og:type" content="article"><meta property="og:title" content="{safe(title)}"><meta property="og:description" content="{safe(desc)}"><meta property="og:url" content="{safe(url)}">
<script type="application/ld+json">{ldtext}</script>
<style>*{{box-sizing:border-box}}body{{margin:0;background:#eff4eb;color:#1a3925;font:16px/1.65 system-ui,sans-serif}}header{{background:#193b26;color:white;padding:25px 16px}}header a{{color:white}}main{{max-width:860px;margin:25px auto;padding:15px}}article{{background:white;padding:28px;border-radius:17px;border:1px solid #d6e2d7}}h1{{line-height:1.2}}.body{{white-space:pre-wrap;overflow-wrap:anywhere}}.photos{{display:flex;flex-wrap:wrap;gap:12px}}.photos img{{width:min(100%,360px);max-height:300px;object-fit:contain;border-radius:10px}}a{{color:#24583a}}@media(max-width:600px){{article{{padding:18px}}}}</style><script defer src="/statistik-raknare.js" data-page="blogg:{safe(p['id'])}"></script></head><body>{MARKER}<header><div style="max-width:860px;margin:auto"><a href="/veckan-hos-oss.html">← Alla veckoinlägg</a><p>Skaraborg Maskin &amp; Återbruk</p></div></header>
<main><article><p>Veckan som börjar {safe(p["week_start"])}</p><h1>{safe(title)}</h1><div class="body">{safe(body)}</div><div class="photos">{photos}</div></article></main></body></html>"""
def main():
    posts=fetch()
    OUT.mkdir(exist_ok=True)
    wanted=set()
    urls=[]
    for p in posts:
        if not p.get("title") or not p.get("body"):continue
        if not re.fullmatch(r"[a-f0-9-]{36}",str(p.get("id",""))):continue
        name=p["week_start"]+"-"+slug(p["title"])+"-"+p["id"][:8]+".html"
        wanted.add(name)
        u=BASE+"/veckoblogg/"+name
        (OUT/name).write_text(render(p,u),encoding="utf-8")
        urls.append(u)
    for f in OUT.glob("*.html"):
        if f.name not in wanted and MARKER in f.read_text(encoding="utf-8")[:10000]:f.unlink()
    xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml+="".join("  <url><loc>"+escape(u)+"</loc></url>\n" for u in urls)
    xml+="</urlset>\n"
    (ROOT/"sitemap-veckoblogg.xml").write_text(xml,encoding="utf-8")
    print("WEEKLY_BLOG_SEO_OK="+str(len(urls)))
if __name__=="__main__":main()
