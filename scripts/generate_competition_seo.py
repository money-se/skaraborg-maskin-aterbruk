#!/usr/bin/env python3
"""Publish static SEO pages for active/ended public competitions."""
import html
import json
import os
import re
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

BASE = "https://skaraborgmaskin.se"
SUPABASE = "https://jnorvriiehandxlvwkkg.supabase.co"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tavlingar"
MARK = "<!-- GENERATED COMPETITION SEO PAGE -->"

def safe(value):
    return html.escape(str(value or ""), quote=True)

def text_section(title, value):
    if not value:
        return ""
    return '<section><h2>'+safe(title)+'</h2><p class="multiline">'+safe(value)+'</p></section>'

def render(item):
    slug = item["slug"]
    title = item["title"].strip()
    url = BASE + "/tavlingar/" + slug + ".html"
    summary = " ".join((item.get("description") or "").split())[:155] or ("Månadens maskin – " + title + ". Tävling hos Skaraborg Maskin & Återbruk.")
    site_title = (title + " – Månadens maskin | Skaraborg Maskin & Återbruk")[:100]
    images = [SUPABASE+"/storage/v1/object/public/competition-images/"+p for p in item.get("image_paths",[]) if isinstance(p,str) and re.fullmatch(r"[a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+",p)]
    imgs = "".join('<img alt="'+safe(title)+" – bild "+str(i+1)+'" loading="lazy" src="'+safe(im)+'">' for i,im in enumerate(images))
    started = str(item.get("starts_at") or "")[:16].replace("T"," ")
    ended = str(item.get("ends_at") or "")[:16].replace("T"," ")
    facebook = item.get("facebook_url") or ""
    link = ('<p><a class="cta" rel="noopener noreferrer" target="_blank" href="'+safe(facebook)+'">Delta på Facebook →</a></p>') if item["status"]=="active" and not item.get("is_test") and facebook.startswith("https://") else ""
    ld = {"@context":"https://schema.org","@type":"WebPage","name":title+" – Månadens maskin","description":summary,"url":url,"inLanguage":"sv-SE","isPartOf":{"@type":"WebSite","name":"Skaraborg Maskin & Återbruk","url":BASE}}
    if images:ld["primaryImageOfPage"]={"@type":"ImageObject","url":images[0]}
    jsonld=json.dumps(ld,ensure_ascii=False).replace("<","\\u003c")
    ogimg='<meta property="og:image" content="'+safe(images[0])+'">' if images else ""
    test_banner = '<p style="background:#fff0cf;padding:14px;font-weight:800">TESTTÄVLING – endast demonstration. Inget deltagande och inget pris delas ut.</p>' if item.get('is_test') else ''
    return f'''<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{safe(site_title)}</title><meta name="description" content="{safe(summary)}"><meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{safe(url)}"><meta property="og:type" content="website"><meta property="og:title" content="{safe(title)}"><meta property="og:description" content="{safe(summary)}"><meta property="og:url" content="{safe(url)}">{ogimg}
<script type="application/ld+json">{jsonld}</script><style>
*{{box-sizing:border-box}}body{{margin:0;color:#1a3523;background:#f2f6f0;font:16px/1.65 system-ui,sans-serif}}header{{background:#173925;color:#fff;padding:18px}}header a{{color:white}}.wrap{{max-width:1000px;margin:auto;padding:20px}}article{{background:white;border:1px solid #d6e2d4;padding:25px;border-radius:18px}}h1{{line-height:1.2}}.gallery{{display:flex;gap:12px;overflow:auto;margin:24px 0}}.gallery img{{width:min(90vw,580px);height:350px;object-fit:contain;background:#f0f3ef;border-radius:12px;flex:none}}.multiline{{white-space:pre-wrap;overflow-wrap:anywhere}}.cta{{display:inline-block;background:#215a36;color:white;text-decoration:none;padding:13px 19px;border-radius:10px;font-weight:bold}}@media(max-width:600px){{.wrap{{padding:12px}}article{{padding:18px}}.gallery img{{height:240px}}}}
</style><script defer src="/partials1/site-shell.js" data-shared-site-shell></script>
</head><body>{MARK}
<div id="site-header"></div><header><div class="wrap"><a href="/tavlingar.html">← Månadens maskin</a><p>Skaraborg Maskin & Återbruk</p></div></header>
<main class="wrap"><article><h1>{safe(title)}</h1>{test_banner}<p><strong>{'Aktiv tävling' if item["status"]=="active" else 'Avslutad tävling'}</strong></p><div class="gallery">{imgs}</div>
{text_section("Om maskinen",item.get("description"))}
{text_section("Skick och kända fel",item.get("prize_condition"))}
<p><strong>Tävlingsperiod:</strong> {safe(started)} – {safe(ended)} (UTC)</p>
{text_section("Tävlingsvillkor",item.get("rules"))}
{text_section("Vinnare",item.get("winner_name"))}
{link}<p>Deltagande sker endast via det aktuella tävlingsinlägget på Facebook, inte via denna webbplats.</p>
<p><a href="/tavlingar.html">Se fler tävlingar</a></p></article></main><div id="site-footer"></div></body></html>'''

def main():
    key=os.environ["SUPABASE_PUBLISHABLE_KEY"]
    query="/rest/v1/competitions?select=slug,title,description,prize_condition,image_paths,facebook_url,starts_at,ends_at,status,rules,winner_name,is_test&published=eq.true&is_test=eq.false&status=in.(active,ended)&order=starts_at.desc&limit=500"
    req=urllib.request.Request(SUPABASE+query,headers={"apikey":key,"Accept":"application/json"})
    with urllib.request.urlopen(req,timeout=30) as response: items=json.load(response)
    OUT.mkdir(exist_ok=True)
    wanted=set()
    urls=[]
    for item in items:
        slug=item.get("slug","")
        if not isinstance(slug,str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",slug):continue
        if not item.get("title"):continue
        filename=slug+".html"
        wanted.add(filename)
        (OUT/filename).write_text(render(item),encoding="utf-8")
        urls.append(BASE+"/tavlingar/"+filename)
    for file in OUT.glob("*.html"):
        if file.name not in wanted and MARK in file.read_text(encoding="utf-8")[:10000]:file.unlink()
    xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml+='  <url><loc>'+BASE+'/tavlingar.html</loc></url>\n'
    xml+=''.join("  <url><loc>"+escape(u)+"</loc></url>\n" for u in urls)
    (ROOT/"sitemap-tavlingar.xml").write_text(xml+"</urlset>\n",encoding="utf-8")
    print("COMPETITION_SEO_PAGES="+str(len(urls)))
if __name__=="__main__":main()
