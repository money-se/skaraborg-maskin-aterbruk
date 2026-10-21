#!/usr/bin/env python3
"""Generate static, indexable pages for published, available ads. No private credentials."""
import html, json, os, re, urllib.request, unicodedata
from pathlib import Path
from datetime import datetime, timezone
from xml.sax.saxutils import escape as xml_escape

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "annonser"
BASE = "https://skaraborgmaskin.se"
SUPABASE = "https://jnorvriiehandxlvwkkg.supabase.co"
KEY = os.environ["SUPABASE_PUBLISHABLE_KEY"]
MARKER = "<!-- AUTO-GENERATED: PUBLIC AD SEO. DO NOT EDIT. -->"

def slugify(value):
    value = unicodedata.normalize("NFKD", value.lower())
    value = value.replace("å", "a").replace("ä", "a").replace("ö", "o")
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value[:65].strip("-") or "maskin"

def safe(value):
    return html.escape(str(value or ""), quote=True)

def fetch():
    url = SUPABASE + "/rest/v1/ads?select=id,title,description,price_sek,status,image_paths,created_at,location_name,marketplace_url&published=eq.true&status=in.(sale,pending)&order=created_at.desc&limit=1000"
    req = urllib.request.Request(url, headers={"apikey": KEY, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)

def render(ad, url):
    title = str(ad["title"]).strip()
    description = str(ad.get("description") or "").strip()
    place = str(ad.get("location_name") or "Hjo").strip() or "Hjo"
    summary = " ".join(description.split())[:155] or f"Begagnad {title} i {place} hos Skaraborg Maskin & Återbruk."
    seo_name = title if "begagnad" in title.lower() else f"{title} begagnad"
    page_title = f"{seo_name} i {place} | Skaraborg Maskin & Återbruk"[:95]
    available = ad["status"] == "sale"
    price = int(ad["price_sek"])
    images = [f"{SUPABASE}/storage/v1/object/public/ad-images/{path}" for path in (ad.get("image_paths") or []) if isinstance(path, str) and not path.startswith("/") and ".." not in path]
    market_url = str(ad.get("marketplace_url") or "").strip()
    market = (f'<p><a class="contact-action" href="{safe(market_url)}" target="_blank" rel="noopener noreferrer">Visa Marketplace-annons ↗</a></p>' if re.match(r"^https://(?:www\.|m\.|web\.)?facebook\.com/(?:marketplace/|share/)", market_url) else "")
    ld = {"@context":"https://schema.org","@type":"Product","name":title,"description":description or summary,"url":url,
          "itemCondition":"https://schema.org/UsedCondition",
          "offers":{"@type":"Offer","priceCurrency":"SEK","price":str(price),"availability":"https://schema.org/InStock" if available else "https://schema.org/OutOfStock","url":url,"seller":{"@type":"Organization","name":"Skaraborg Maskin & Återbruk"}}}
    if images: ld["image"] = images
    ld_json = json.dumps(ld, ensure_ascii=False).replace("<", "\\u003c")
    gallery = ""
    if images:
        thumbnails = "".join(f'<button type="button" aria-label="Visa bild {i+1}" aria-pressed="{"true" if i==0 else "false"}" data-image="{safe(img)}"><img src="{safe(img)}" alt="Miniatyr {i+1}" loading="lazy"></button>' for i,img in enumerate(images))
        gallery = f'<div class="gallery-main" role="button" tabindex="0" aria-label="Förstora vald bild"><img id="large-ad-image" src="{safe(images[0])}" alt="{safe(title)} – bild 1"></div><div class="thumb" aria-label="Fler bilder på annonsen">{thumbnails}</div>'
    contact = (f'<div class="ad-contact"><a class="contact-action" href="https://www.facebook.com/profile.php?id=61588383880828" target="_blank" rel="noopener noreferrer">Besök vår Facebooksida</a><p class="muted">Öppna vår Facebooksida och välj Meddelande. Skriv gärna vilken annons det gäller: {safe(title)}.</p></div>' if available else '<p class="muted">Annonsen är väntande. Vi tar inte emot nya förfrågningar just nu.</p>')
    status = "Till salu" if available else "Reserverad / väntande"
    return f'''<!doctype html>
<html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{safe(page_title)}</title><meta name="description" content="{safe(summary)}">
<link rel="canonical" href="{safe(url)}">
<meta property="og:type" content="product"><meta property="og:title" content="{safe(title)}"><meta property="og:description" content="{safe(summary)}"><meta property="og:url" content="{safe(url)}">
<script type="application/ld+json">{ld_json}</script>
<style>

*{{box-sizing:border-box}}body{{font:16px/1.5 system-ui,sans-serif;margin:0;background:radial-gradient(ellipse at 4% 15%,rgba(70,116,69,.13),transparent 35%),radial-gradient(ellipse at 98% 68%,rgba(128,112,63,.09),transparent 32%),repeating-linear-gradient(135deg,rgba(25,71,40,.025) 0,rgba(25,71,40,.025) 1px,transparent 1px,transparent 22px),#edf2e9;color:#16261b}}.wrap{{max-width:1120px;margin:auto;padding:20px}}header{{background:#1b3825;color:white;padding:36px 0}}a{{color:#1c5630}}a:focus-visible,button:focus-visible,input:focus-visible{{outline:3px solid #d1a345;outline-offset:2px}}.trust{{display:flex;flex-wrap:wrap;gap:12px;margin:16px 0}}.trust span{{background:#e8efe7;border-radius:8px;padding:9px 12px;font-size:14px}}.contact-action{{display:inline-block;text-decoration:none;background:#1b482a;color:white;border-radius:9px;padding:12px 18px;font-weight:700}}.contact-action:hover{{background:#123a21}}h1{{font-size:clamp(28px,5vw,43px);margin:0}}.sub{{color:#e3ebe2}}.card{{background:white;border:1px solid #d6e2d9;border-radius:13px;overflow:hidden}}.products{{display:grid;grid-template-columns:repeat(auto-fill,minmax(235px,1fr));gap:15px;margin-top:20px}}.card img,.placeholder{{width:100%;height:175px;object-fit:cover;background:#eaf0e9}}.placeholder{{display:grid;place-items:center;color:#677a6b}}.body{{padding:15px}}.body h2{{font-size:18px;line-height:1.35;margin:0 0 7px}}.price{{font-size:20px;font-weight:800}}.badge{{background:#e9eee9;border-radius:6px;padding:4px 8px;font-size:13px}}.pending{{background:#fff1d6}}.controls{{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0}}input,button{{font:inherit;border:1px solid #abc1ad;border-radius:9px;padding:11px}}input{{flex:1;min-width:230px}}button{{cursor:pointer;background:#1b482a;color:white;font-weight:700}}.body button{{margin-top:13px;width:100%}}.detail{{border:1px solid #d6e2d9;background:white;padding:20px;border-radius:13px}}.detail img{{width:100%;max-height:470px;object-fit:contain}}.description{{white-space:pre-wrap}}.thumb{{display:flex;gap:8px;flex-wrap:wrap}}.thumb button{{background:#edf2eb;padding:4px}}.thumb img{{width:80px;height:80px;object-fit:cover}}.muted{{color:#5b6f61}}.hidden{{display:none!important}}
.detail{{border:0;background:transparent;padding:0}}.detail-layout{{display:grid;grid-template-columns:minmax(0,1.8fr) minmax(250px,1fr);gap:22px;align-items:start}}.detail-main,.business-panel{{border:1px solid #d6e2d9;background:#fdfefb;border-radius:15px;padding:22px;box-shadow:0 9px 30px rgba(25,58,32,.06)}}.detail-main h2{{font-size:clamp(25px,3vw,36px);margin:16px 0 8px}}.detail-price{{font-size:27px;color:#20482e;margin:0 0 16px}}.gallery-main{{background:#edf1eb;border-radius:12px;overflow:hidden;display:grid;place-items:center;min-height:240px}}.gallery-main img{{display:block;width:100%;height:auto;max-height:540px;object-fit:contain}}.thumb{{display:flex;flex-wrap:nowrap;gap:10px;overflow-x:auto;padding:12px 2px 8px}}.thumb button{{background:#f1f5ef;border:2px solid transparent;border-radius:10px;padding:3px;flex:0 0 88px;height:78px;overflow:hidden}}.thumb button[aria-pressed="true"]{{border-color:#1e6237;box-shadow:0 0 0 2px #d6e7d7}}.thumb button img{{display:block;width:100%;height:100%;object-fit:cover;border-radius:6px}}.ad-meta{{display:inline-block;margin:8px 0 15px;padding:5px 12px;border-radius:99px;background:#e9f2e7;color:#19482b;font-weight:700;font-size:14px}}.business-panel{{background:linear-gradient(155deg,#e6efe5,#f7f9f5 55%,#fff)}}.business-panel h3{{font-size:23px;margin:3px 0 12px;color:#184029}}.business-panel p{{line-height:1.6}}.business-panel a{{display:block;margin-top:12px;font-weight:700}}.brand-banner{{background:linear-gradient(105deg,#163b27,#295a37);color:#fff;border-radius:14px;padding:20px 24px;margin:16px 0 22px}}.brand-banner strong{{font-size:19px}}.brand-banner p{{margin:6px 0 0;color:#dcebdd}}.business-details{{padding-left:20px;line-height:1.8}}.detail-actions{{display:flex;gap:12px;flex-wrap:wrap;align-items:center}}.detail-actions button{{background:#ecf2eb;color:#20432c}}.detail-top{{margin-bottom:14px}}@media(max-width:760px){{.detail-layout{{grid-template-columns:1fr}}.detail-main,.business-panel{{padding:16px}}.thumb button{{flex-basis:74px;height:68px}}.brand-banner{{padding:16px}}.detail-main h2{{font-size:27px}}}} .viewer{{position:fixed;inset:0;background:rgba(10,25,15,.94);z-index:9999;display:flex;align-items:center;justify-content:center;padding:64px 18px 26px}}.viewer img{{max-width:95vw;max-height:84vh;object-fit:contain;border-radius:8px}}.viewer button{{position:absolute;top:12px;right:18px;background:#fff;color:#173821;border:0;font-size:20px}}.viewer .viewer-count{{position:absolute;bottom:7px;color:white;font-size:14px}}.gallery-main{{cursor:zoom-in}}.gallery-main:focus-visible{{outline:3px solid #b3d2a7}}.thumb button{{cursor:pointer}}.detail-main{{background:linear-gradient(145deg,#fff 0%,#f5f9f2 100%)}}.business-panel{{background:linear-gradient(155deg,#e0eee1,#f1f7ec 50%,#dfeadd)!important;border:1px solid #bed3be;box-shadow:0 14px 38px #203d2630}}.business-panel:before{{content:"SKARABORG MASKIN & ÅTERBRUK";display:block;font-size:11px;letter-spacing:2px;color:#497350;font-weight:800;margin-bottom:15px}}.business-details li{{padding:3px 0}}.brand-banner{{background:linear-gradient(120deg,#123b27,#285e39 58%,#163a2c);position:relative;overflow:hidden}}.brand-banner:after{{content:"SMÅ";position:absolute;right:12px;top:-40px;font-size:135px;font-weight:900;color:#ffffff0d;pointer-events:none}}body{{background:radial-gradient(circle at 9% 18%,#c8dac5 0%,transparent 36%),radial-gradient(circle at 95% 65%,#d1ddc2 0%,transparent 31%),repeating-linear-gradient(135deg,#31573808 0px,#31573808 2px,transparent 2px,transparent 28px),#e7efe4}} .ad-contact{{margin:22px 0 6px;padding-top:18px;border-top:1px solid #dce6dc}}.ad-contact .contact-action{{display:inline-block;text-align:center;max-width:100%}}@media(max-width:600px){{.ad-contact .contact-action{{display:block}}}} 
</style>
<style>.seo-ad-container{{max-width:1120px;margin:auto;padding:20px}}.seo-header{{background:#1b3825;color:white;padding:22px 0}}.seo-header a{{color:#fff}}.seo-detail .detail-main{{min-width:0}}.seo-detail .description{{white-space:pre-wrap;overflow-wrap:anywhere}}.seo-detail .thumb button img{{display:block}}@media(max-width:760px){{.seo-ad-container{{padding:12px}}}}</style>
<script defer src="/statistik-raknare.js" data-page="annons:{safe(ad['id'])}"></script></head>
<body>{MARKER}
<header class="seo-header"><div class="wrap"><a href="/annonser.html">← Tillbaka till annonser</a><p class="sub">Skaraborg Maskin & Återbruk · {safe(place)}</p></div></header>
<main class="seo-ad-container">
<div class="brand-banner"><strong>Skaraborg Maskin & Återbruk</strong><p>Begagnade maskiner, redskap och återbruk från {safe(place)}</p></div>
<div class="detail-layout seo-detail"><article class="detail-main"><h1>{safe(title)}</h1><div class="detail-price">{price:,} kr</div>
{gallery}<span class="ad-meta">{status}</span><h3>Om maskinen</h3><p class="description">{safe(description) if description else "Kontakta oss för mer information om maskinen."}</p>
<p class="muted">Begagnade varor säljs i befintligt skick. Fråga gärna om fler bilder eller information före köp.</p>{market}{contact}
</article><aside class="business-panel"><h3>Handla av oss i Skaraborg</h3><p>Vi arbetar med begagnade maskiner, redskap och återbruk. Hör gärna av dig om objektet eller om du har något du vill sälja.</p><ul class="business-details"><li>Vi finns i Hjo</li><li>Frågor och visning enligt överenskommelse</li><li>Vi beskriver skick och kända brister i annonserna</li></ul><a href="/om-oss.html">Läs mer om företaget →</a></aside></div>
</main>
<script>
document.querySelectorAll('.thumb button').forEach(button=>button.addEventListener('click',()=>{{
  const big=document.getElementById('large-ad-image');big.src=button.dataset.image;
  document.querySelectorAll('.thumb button').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
}}));
const frame=document.querySelector('.gallery-main');
if(frame){{
 const show=()=>{{const img=document.getElementById('large-ad-image');const dialog=document.createElement('dialog');dialog.style.cssText='width:100vw;height:100vh;max-width:100vw;max-height:100vh;padding:50px 15px 10px;background:#09170ef5;border:0';const big=document.createElement('img');big.src=img.src;big.alt=img.alt;big.style.cssText='display:block;max-width:96vw;max-height:82vh;margin:auto;object-fit:contain';const close=document.createElement('button');close.textContent='Stäng bild ×';close.onclick=()=>dialog.close();dialog.addEventListener('close',()=>dialog.remove());dialog.append(close,big);document.body.append(dialog);dialog.showModal();}};
 frame.addEventListener('click',show);frame.addEventListener('keydown',e=>{{if(e.key==='Enter'||e.key===' '){{e.preventDefault();show();}}}});
}}
</script></body></html>'''

def main():
    ads = fetch()
    OUTPUT.mkdir(exist_ok=True)
    desired = set()
    # Keep a useful URL in the sitemap even when only test ads (or no ads) exist.
    urls = [BASE + "/annonser.html"]
    for ad in ads:
        if not isinstance(ad.get("title"), str) or not ad["title"].strip(): continue
        if ad.get("status") not in ("sale", "pending"): continue
        # Never expose placeholder test advertisements to search engines.
        if re.match(r"^(test|testannons|test –|test -)(\b|$)", ad["title"].strip(), re.IGNORECASE): continue
        if not re.fullmatch(r"[a-f0-9-]{36}", str(ad["id"])): continue
        name = slugify(ad["title"]) + "-" + ad["id"][:8] + ".html"
        desired.add(name)
        url = f"{BASE}/annonser/{name}"
        (OUTPUT / name).write_text(render(ad,url), encoding="utf-8")
        urls.append(url)
    # Remove only pages created by this generator; leave other files untouched.
    for file in OUTPUT.glob("*.html"):
        if file.name not in desired and MARKER in file.read_text(encoding="utf-8")[:10000]:
            file.unlink()
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += "".join(f"  <url><loc>{xml_escape(url)}</loc></url>\n" for url in urls)
    xml += "</urlset>\n"
    (ROOT / "sitemap-annonser.xml").write_text(xml, encoding="utf-8")
    print(f"SEO_EXPORT_OK={len(urls)}")

if __name__ == "__main__": main()
