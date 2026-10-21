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
    summary = " ".join(description.split())[:155] or f"Begagnad {title} i Hjo hos Skaraborg Maskin & Återbruk."
    seo_name = title if "begagnad" in title.lower() else f"{title} begagnad"
    page_title = f"{seo_name} i {str(ad.get('location_name') or 'Hjo').strip()} | Skaraborg Maskin & Återbruk"[:95]
    available = ad["status"] == "sale"
    images = [f"{SUPABASE}/storage/v1/object/public/ad-images/{path}" for path in (ad.get("image_paths") or []) if isinstance(path, str) and not path.startswith("/") and ".." not in path]
    price = int(ad["price_sek"])
    place = str(ad.get("location_name") or "Hjo").strip()
    market_url = str(ad.get("marketplace_url") or "").strip()
    market_link = (f'<p><a class="cta" href="{safe(market_url)}" target="_blank" rel="noopener noreferrer">Visa annonsen på Marketplace ↗</a></p>' if re.match(r"^https://(?:www\\.|m\\.|web\\.)?facebook\\.com/(?:marketplace/|share/)", market_url) else "")
    ld = {
        "@context": "https://schema.org", "@type": "Product", "name": title,
        "description": description or summary,
        "url": url,
        "itemCondition": "https://schema.org/UsedCondition",
        "offers": {"@type": "Offer", "priceCurrency": "SEK", "price": str(price),
                   "availability": "https://schema.org/InStock" if available else "https://schema.org/OutOfStock", "url": url,
                   "seller": {"@type": "Organization", "name": "Skaraborg Maskin & Återbruk"}},
    }
    if images: ld["image"] = images
    ld_json = json.dumps(ld, ensure_ascii=False).replace("<", "\\u003c")
    gallery = ('<div class="gallery"><img id="main-ad-image" class="main-image" src="' + safe(images[0]) + '" alt="' + safe(title) + ' – bild 1"><div class="thumbs">' + "".join(f'<button type="button" class="thumb" data-img="{safe(img)}" aria-label="Visa bild {i+1}"><img src="{safe(img)}" alt="Miniatyr {i+1}" loading="lazy"></button>' for i,img in enumerate(images)) + "</div></div>" if images else "")
    status = "Till salu" if available else "Reserverad / väntande"
    contact = (f'<a class="cta" href="https://www.messenger.com/t/924620407412160/" target="_blank" rel="noopener noreferrer">Skriv till oss på Messenger</a><p>Berätta gärna vilken annons du frågar om: <strong>{safe(title)}</strong>. Messenger öppnas separat.</p>' if available else "<p>Den här maskinen är för närvarande reserverad.</p>")
    return f"""<!doctype html>
<html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{safe(page_title)}</title><meta name="description" content="{safe(summary)}">
<link rel="canonical" href="{safe(url)}">
<meta property="og:type" content="product"><meta property="og:title" content="{safe(title)}">
<meta property="og:description" content="{safe(summary)}"><meta property="og:url" content="{safe(url)}">
<script type="application/ld+json">{ld_json}</script>
<style>
*{{box-sizing:border-box}}body{{margin:0;color:#1d3424;font:16px/1.6 system-ui,sans-serif;background:radial-gradient(ellipse at 5% 10%,#dcebdc,transparent 40%),#edf2e9}}header{{background:#1b3825;color:white;padding:22px 16px}}.wrap{{max-width:1050px;margin:auto;padding:20px}}header a{{color:white}}.box{{background:#fff;border:1px solid #d7e4d7;border-radius:16px;padding:24px;margin:20px 0;box-shadow:0 8px 24px #18352213}}h1{{line-height:1.2}}.price{{font-size:28px;font-weight:800}}.state{{display:inline-block;background:#e5f0e5;padding:6px 12px;border-radius:30px}}.gallery .main-image{{width:100%;max-height:440px;height:350px;object-fit:contain;background:#f0f4ef;border-radius:12px;cursor:zoom-in}}.thumbs{{display:flex;gap:8px;overflow-x:auto;margin-top:10px}}.thumb{{flex:0 0 80px;padding:3px;border:2px solid #c5d6c7;border-radius:8px;background:white;cursor:pointer}}.thumb img{{width:100%;height:65px;object-fit:cover}}.description{{white-space:pre-wrap;overflow-wrap:anywhere}}.cta{{display:inline-block;padding:13px 20px;background:#225436;color:#fff;text-decoration:none;border-radius:9px;font-weight:700}}a{{color:#205735}}@media(max-width:600px){{.wrap{{padding:12px}}.box{{padding:17px}}.gallery .main-image{{height:240px}}}}
</style><script defer src="/statistik-raknare.js" data-page="annons:{safe(ad['id'])}"></script><script>
document.addEventListener('click',function(e){{
 const thumb=e.target.closest('.thumb');if(thumb){{document.getElementById('main-ad-image').src=thumb.dataset.img;return;}}
 const img=e.target.closest('.main-image');if(!img)return;
 const d=document.createElement('dialog');d.style.cssText='width:100vw;height:100vh;max-width:100vw;max-height:100vh;margin:0;padding:50px 15px 10px;background:#09170ef5;border:0';
 const big=document.createElement('img');big.src=img.src;big.alt=img.alt;big.style.cssText='display:block;max-width:96vw;max-height:82vh;margin:auto;object-fit:contain';
 const close=document.createElement('button');close.textContent='Stäng bild ×';close.style.cssText='display:block;margin:0 0 12px auto;padding:10px;font:inherit';close.onclick=()=>d.close();
 d.addEventListener('close',()=>d.remove());d.addEventListener('click',event=>{{if(event.target===d)d.close()}});
 d.append(close,big);document.body.append(d);d.showModal();close.focus();
}});
</script></head><body>{MARKER}<header><div class="wrap"><a href="/annonser.html">← Alla annonser</a><p>Skaraborg Maskin & Återbruk · Hjo</p></div></header>
<main class="wrap"><article class="box"><h1>{safe(title)}</h1><p class="price">{price:,} kr</p><span class="state">{status}</span>{gallery}<h2>Beskrivning</h2><p class="description">{safe(description) if description else 'Kontakta oss för mer information.'}</p><p>Begagnad vara säljs i befintligt skick. Fråga oss gärna om detaljer före köp.</p>{market_link}{contact}</article>
<aside class="box"><h2>Skaraborg Maskin & Återbruk</h2><p>Vi arbetar med begagnade maskiner, redskap och återbruk. Vi finns i Hjo.</p><p><a href="/om-oss.html">Om företaget</a> · <a href="/annonser.html">Fler annonser</a></p></aside></main></body></html>"""

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
