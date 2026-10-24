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
    url = SUPABASE + "/rest/v1/ads?select=id,title,description,price_sek,status,image_paths,created_at,location_name,marketplace_url&published=eq.true&status=in.(sale,pending,sold)&order=created_at.desc&limit=1000"
    req = urllib.request.Request(url, headers={"apikey": KEY, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)

DETAIL_CSS = "\n:root{--green:#1f3322;--green2:#304936;--gold:#d8a52e;--bg:#f5f7f5;--ink:#142017;--muted:#617064;--line:#dfe7df;--soft:#eaf1ea;--radius:18px}\n*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 system-ui,-apple-system,\"Segoe UI\",Roboto,sans-serif}\na{color:#245c33}button{font:inherit;cursor:pointer}a:focus-visible,button:focus-visible{outline:3px solid var(--gold);outline-offset:3px}\n.wrap{width:min(100% - 36px,1150px);margin:auto}.skip{position:absolute;left:12px;top:-100px;z-index:3000;background:#fff;color:var(--ink);padding:12px;border-radius:10px}.skip:focus{top:12px}\n.ad-hero{padding:40px 0 34px;background:radial-gradient(circle at 86% 14%,#ffffff18,transparent 35%),linear-gradient(135deg,#1f2d1f,#304936);color:#fff}\n.crumb{display:flex;align-items:center;gap:9px;flex-wrap:wrap;font-size:14px;margin-bottom:22px;color:#d6e7d8}.crumb a{color:#eaf2eb;text-underline-offset:4px}\n.kicker{color:#f0cb73;font-size:13px;font-weight:850;letter-spacing:.07em;text-transform:uppercase}.ad-hero h1{font-size:clamp(32px,5vw,53px);line-height:1.13;letter-spacing:-.025em;margin:11px 0 19px;max-width:850px}\n.hero-line{display:flex;gap:14px 24px;flex-wrap:wrap;align-items:center}.hero-price{font-size:clamp(28px,4vw,40px);font-weight:900;letter-spacing:-.02em}.hero-status{border:1px solid #ffffff66;background:#ffffff15;border-radius:999px;padding:8px 15px;font-weight:850;font-size:14px}.hero-status.pending{background:#fff1d6;color:#714e09;border-color:#f2d58a}.hero-status.sold{background:#e4e7e4;color:#3b453e;border-color:#cfd8d0}.hero-place{color:#dae5db;font-weight:650}\n.ad-main{padding:35px 0 65px}.ad-grid{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(285px,.9fr);gap:23px;align-items:start}\n.ad-column{min-width:0}.ad-box{background:#fff;border:1px solid var(--line);border-radius:var(--radius);box-shadow:0 12px 35px #2038260d;overflow:hidden}\n.ad-gallery{padding:20px}.photo-main{border:0;background:var(--soft);width:100%;aspect-ratio:1.42;display:grid;place-items:center;border-radius:14px;overflow:hidden;padding:0;position:relative}\n.photo-main img{width:100%;height:100%;object-fit:contain}.photo-main:hover:after{content:\"Förstora bild\";position:absolute;bottom:14px;right:14px;background:#142017d9;color:#fff;font-weight:800;font-size:13px;padding:7px 12px;border-radius:999px}\n.thumbs{display:flex;gap:10px;padding:15px 0 0;overflow-x:auto}.thumbs button{width:90px;height:73px;flex:none;overflow:hidden;padding:3px;border:2px solid transparent;border-radius:11px;background:#ecf2eb}\n.thumbs button[aria-pressed=\"true\"]{border-color:#296d40}.thumbs img{width:100%;height:100%;object-fit:cover;border-radius:7px}.photo-none{min-height:300px;display:grid;place-items:center;background:#edf1ec;color:#667669;font-weight:700}\n.section-body{padding:25px 27px}.section-body h2{font-size:24px;line-height:1.2;margin:0 0 13px}.description{margin:0;white-space:pre-wrap;overflow-wrap:anywhere;color:#28392b}.smallprint{font-size:14px;color:var(--muted);line-height:1.65;margin-top:22px}\n.offer-panel{padding:27px;position:sticky;top:95px}.offer-panel h2{font-size:24px;line-height:1.2;margin:0 0 10px}.offer-panel p{margin:0 0 17px;color:#4e6252}.offer-panel .panel-price{font-size:35px;line-height:1.2;letter-spacing:-.02em;font-weight:900;color:#214e2f;margin:0 0 12px}\n.panel-status{display:inline-block;background:#e8f2e8;color:#235032;border-radius:999px;font-weight:850;padding:6px 12px;margin-bottom:20px;font-size:13px}.panel-status.pending{background:#fff0d3;color:#80570c}.panel-status.sold{background:#e7eae7;color:#4c5a4f}\n.action{display:flex;justify-content:center;align-items:center;text-align:center;gap:8px;padding:14px 17px;min-height:51px;border-radius:12px;text-decoration:none;font-size:16px;font-weight:850}\n.action-primary{background:var(--green);color:#fff}.action-primary:hover{background:var(--green2)}.action-secondary{border:1px solid #afc8b2;background:var(--soft);color:#1f3e27;margin-top:9px}.action-secondary:hover{background:#d9e8d9}\n.action-disabled{padding:16px;border-radius:12px;background:#fff3d9;color:#6d511c;font-weight:750}.panel-detail{border-top:1px solid var(--line);padding-top:20px;margin-top:22px;color:var(--muted);font-size:14px;line-height:1.75}.panel-detail strong{color:#293d2c}\n.ad-identity{display:flex;align-items:flex-start;gap:12px;border-radius:14px;background:#eaf1ea;padding:18px 20px;margin-top:18px}.ad-identity strong{display:block}.ad-identity p{margin:3px 0 0;color:#516754;font-size:14px}\n.ad-bottom{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-top:26px;font-size:15px}.ad-bottom a{font-weight:800}\n.photo-dialog{border:0;background:#101b13;color:#fff;border-radius:14px;padding:18px;max-width:96vw;max-height:97vh;width:min(1050px,96vw)}.photo-dialog::backdrop{background:#08150de8}.photo-modal-head{display:flex;justify-content:space-between;align-items:center;gap:15px;margin-bottom:12px}.photo-dialog img{display:block;max-width:100%;max-height:76vh;object-fit:contain;margin:auto;border-radius:7px}\n.photo-modal-actions{display:flex;justify-content:space-between;gap:12px;margin-top:11px}.photo-dialog button{border:1px solid #ffffff50;border-radius:9px;background:#eef4eb;color:#17311c;font-weight:800;padding:9px 15px}.photo-dialog button:disabled{opacity:.4}\n@media(max-width:860px){.ad-grid{grid-template-columns:1fr}.offer-panel{position:static}.ad-hero{padding:30px 0}.ad-main{padding-top:18px}.photo-main{aspect-ratio:1.35}}\n@media(max-width:600px){.wrap{width:min(100% - 26px,1150px)}.ad-gallery{padding:12px}.section-body,.offer-panel{padding:19px}.hero-line{gap:10px 16px}.thumbs button{width:70px;height:66px}.photo-dialog{width:100vw;max-width:100vw;max-height:100vh;height:auto;border-radius:0}.photo-dialog img{max-height:67vh}}\n@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}\n"
DETAIL_JS = "\n(() => {\n  const main = document.getElementById('ad-primary-image');\n  const buttons = [...document.querySelectorAll('.thumbs button[data-image]')];\n  const dialog = document.getElementById('photo-dialog');\n  const modal = document.getElementById('photo-modal-image');\n  const count = document.getElementById('photo-count');\n  const prev = document.getElementById('photo-prev');\n  const next = document.getElementById('photo-next');\n  let selected = 0;\n  function choose(index) {\n    if (!main || index < 0 || index >= buttons.length) return;\n    selected = index;\n    const chosen = buttons[index];\n    main.src = chosen.dataset.image;\n    main.alt = chosen.dataset.alt || 'Annonsbild';\n    buttons.forEach((b, i) => b.setAttribute('aria-pressed', String(i === index)));\n    if (modal) { modal.src = main.src; modal.alt = main.alt; }\n    if (count) count.textContent = 'Bild ' + (selected + 1) + ' av ' + buttons.length;\n    if (prev) prev.disabled = selected === 0;\n    if (next) next.disabled = selected === buttons.length - 1;\n  }\n  buttons.forEach((b, i) => b.addEventListener('click', () => choose(i)));\n  const open = document.getElementById('photo-open');\n  if (open && dialog) {\n    open.addEventListener('click', () => { choose(selected); dialog.showModal(); });\n    document.getElementById('photo-close')?.addEventListener('click', () => dialog.close());\n    prev?.addEventListener('click', () => choose(selected - 1));\n    next?.addEventListener('click', () => choose(selected + 1));\n    dialog.addEventListener('keydown', e => {\n      if (e.key === 'ArrowRight') { e.preventDefault(); choose(Math.min(selected + 1, buttons.length - 1)); }\n      if (e.key === 'ArrowLeft') { e.preventDefault(); choose(Math.max(selected - 1, 0)); }\n    });\n  }\n  const copy = document.getElementById('copy-ad-name');\n  copy?.addEventListener('click', async () => {\n    try {\n      await navigator.clipboard.writeText(copy.dataset.name || '');\n      copy.textContent = 'Annonsnamnet kopierat ✓';\n    } catch { copy.textContent = 'Markera och kopiera annonsens rubrik'; }\n  });\n  async function inject(id, url) {\n    const target = document.getElementById(id);\n    if (!target) return;\n    try {\n      const response = await fetch(url, {cache: 'no-cache'});\n      if (!response.ok) return;\n      target.innerHTML = await response.text();\n    } catch (e) { console.warn('Delad navigering kunde inte läsas in', e); }\n  }\n  inject('site-header', '/partials1/header.html');\n  inject('site-footer', '/partials1/footer.html');\n})();\n"


def render(ad, url):
    title = str(ad["title"]).strip()
    description = str(ad.get("description") or "").strip()
    place = str(ad.get("location_name") or "Hjo").strip() or "Hjo"
    summary = " ".join(description.split())[:155] or f"Begagnad {title} i {place} hos Skaraborg Maskin & Återbruk."
    page_title = f"{title} begagnad i {place} | Skaraborg Maskin & Återbruk"[:95]
    status_code = ad["status"]
    available = status_code == "sale"
    status = "Till salu" if available else ("Reserverad" if status_code == "pending" else "Såld")
    state_class = "available" if available else ("pending" if status_code == "pending" else "sold")
    price = int(ad["price_sek"])
    formatted_price = f"{price:,}".replace(",", " ") + " kr"
    images = [f"{SUPABASE}/storage/v1/object/public/ad-images/{path}" for path in (ad.get("image_paths") or []) if isinstance(path, str) and not path.startswith("/") and ".." not in path]
    market_url = str(ad.get("marketplace_url") or "").strip()
    is_facebook_market = re.match(r"^https://(?:www\.|m\.|web\.)?facebook\.com/(?:marketplace/|share/)", market_url)
    market = (f'<a class="action action-secondary" href="{safe(market_url)}" target="_blank" rel="noopener noreferrer">Visa annonsen på Marketplace ↗</a>' if is_facebook_market else "")
    ld = {"@context":"https://schema.org","@type":"Product","name":title,"description":description or summary,"url":url,
          "itemCondition":"https://schema.org/UsedCondition",
          "offers":{"@type":"Offer","priceCurrency":"SEK","price":str(price),
                    "availability":"https://schema.org/InStock" if available else "https://schema.org/OutOfStock",
                    "url":url,"seller":{"@type":"Organization","name":"Skaraborg Maskin & Återbruk"}}}
    if images: ld["image"] = images
    ld_json = json.dumps(ld, ensure_ascii=False).replace("<", "\\u003c")
    seo_index = "noindex,follow" if status_code == "sold" else "index,follow,max-image-preview:large"
    og_image = f'<meta property="og:image" content="{safe(images[0])}">' if images else ""
    thumbnails = "".join(
        f'<button type="button" data-image="{safe(src)}" data-alt="{safe(title)} – bild {i+1}" aria-pressed="{"true" if i == 0 else "false"}" aria-label="Visa bild {i+1} av {len(images)}"><img src="{safe(src)}" alt="" loading="lazy"></button>'
        for i, src in enumerate(images)
    )
    if images:
        gallery = f'''<div class="ad-box ad-gallery">
          <button type="button" id="photo-open" class="photo-main" aria-label="Förstora produktbild">
            <img id="ad-primary-image" src="{safe(images[0])}" alt="{safe(title)} – bild 1" fetchpriority="high">
          </button><div class="thumbs" role="group" aria-label="Välj produktbild">{thumbnails}</div>
        </div>
        <dialog id="photo-dialog" class="photo-dialog" aria-label="Förstorad produktbild">
          <div class="photo-modal-head"><strong id="photo-count">Bild 1 av {len(images)}</strong><button type="button" id="photo-close">Stäng ×</button></div>
          <img id="photo-modal-image" src="{safe(images[0])}" alt="{safe(title)} – bild 1">
          <div class="photo-modal-actions"><button type="button" id="photo-prev" disabled>← Föregående</button><button type="button" id="photo-next" {"disabled" if len(images) == 1 else ""}>Nästa →</button></div>
        </dialog>'''
    else:
        gallery = '<div class="ad-box ad-gallery"><div class="photo-none">Ingen produktbild tillgänglig</div></div>'
    if available:
        actions = '''<a class="action action-primary" href="sms:+46727483256">Skicka SMS om annonsen →</a>
        <a class="action action-secondary" href="https://www.facebook.com/profile.php?id=61588383880828" target="_blank" rel="noopener noreferrer">Kontakta oss via Facebook ↗</a>'''
    else:
        actions = (f'<div class="action-disabled">{"Denna annons är reserverad. Inga nya förfrågningar just nu." if status_code == "pending" else "Objektet är sålt och inte längre tillgängligt."}</div>')
    text_description = safe(description) if description else "Kontakta oss om du vill veta mer om objektet."
    return f'''<!doctype html>
<html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<base href="/"><title>{safe(page_title)}</title>
<meta name="description" content="{safe(summary)}"><meta name="robots" content="{seo_index}">
<link rel="canonical" href="{safe(url)}">
<meta property="og:type" content="product"><meta property="og:title" content="{safe(title)}">
<meta property="og:description" content="{safe(summary)}"><meta property="og:url" content="{safe(url)}">
{og_image}
<script type="application/ld+json">{ld_json}</script>
<style>{DETAIL_CSS}</style>
<script defer src="/statistik-raknare.js" data-page="annons:{safe(ad['id'])}"></script></head>
<body>{MARKER}
<a class="skip" href="#annons-innehall">Hoppa till annonsen</a>
<div id="site-header"></div>
<header class="ad-hero"><div class="wrap">
  <nav class="crumb" aria-label="Brödsmulor"><a href="index.html">Hem</a> <span aria-hidden="true">›</span> <a href="till-salu.html">Till salu</a> <span aria-hidden="true">›</span> <a href="annonser.html">Våra annonser</a></nav>
  <div class="kicker">BEGAGNAT · SKARABORG MASKIN & ÅTERBRUK</div>
  <h1>{safe(title)}</h1>
  <div class="hero-line"><span class="hero-price">{formatted_price}</span><span class="hero-status {state_class}">{status}</span><span class="hero-place">📍 {safe(place)}</span></div>
</div></header>
<main class="ad-main" id="annons-innehall"><div class="wrap"><div class="ad-grid">
  <div class="ad-column">
    {gallery}
    <section class="ad-box section-body" style="margin-top:18px" aria-labelledby="about-object">
      <h2 id="about-object">Om objektet</h2>
      <p class="description">{text_description}</p>
      <p class="smallprint">Begagnade varor säljs i befintligt skick. Fråga gärna om funktion, kända brister och fler bilder före köp.</p>
    </section>
  </div>
  <aside class="ad-box offer-panel" aria-labelledby="seller-heading">
    <h2 id="seller-heading">Intresserad av objektet?</h2>
    <div class="panel-price">{formatted_price}</div>
    <div><span class="panel-status {state_class}">{status}</span></div>
    {actions}
    {market}
    <button type="button" class="action action-secondary" id="copy-ad-name" data-name="{safe(title)}">Kopiera annonsens namn</button>
    <div class="panel-detail">Ange gärna <strong>{safe(title)}</strong> när du kontaktar oss, så vet vi vilket objekt du menar.<p>Visning, betalning och eventuell hämtning eller leverans sker efter överenskommelse.</p></div>
    <div class="ad-identity"><div><strong>Skaraborg Maskin & Återbruk</strong><p>Utgår från Hjo · Skaraborg<br>Vi svarar helst skriftligt.</p></div></div>
  </aside>
</div><div class="ad-bottom"><a href="annonser.html">← Se fler annonser</a><a href="om-oss.html">Läs mer om oss →</a></div></div></main>
<div id="site-footer"></div>
<script>{DETAIL_JS}</script>
</body></html>'''

def main():
    ads = fetch()
    OUTPUT.mkdir(exist_ok=True)
    desired = set()
    # Keep a useful URL in the sitemap even when only test ads (or no ads) exist.
    urls = [BASE + "/annonser.html"]
    for ad in ads:
        if not isinstance(ad.get("title"), str) or not ad["title"].strip(): continue
        if ad.get("status") not in ("sale", "pending", "sold"): continue
        # Never expose placeholder test advertisements to search engines.
        if re.match(r"^(test|testannons|test –|test -)(\b|$)", ad["title"].strip(), re.IGNORECASE): continue
        if not re.fullmatch(r"[a-f0-9-]{36}", str(ad["id"])): continue
        name = slugify(ad["title"]) + "-" + ad["id"][:8] + ".html"
        desired.add(name)
        url = f"{BASE}/annonser/{name}"
        (OUTPUT / name).write_text(render(ad,url), encoding="utf-8")
        if ad["status"] != "sold": urls.append(url)
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
