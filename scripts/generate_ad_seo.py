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

DETAIL_CSS = "\n:root{--ink:#13241a;--green:#1f3322;--green2:#304936;--gold:#d8a52e;--paper:#f6f8f4;--pale:#ecf2eb;--muted:#5d7061;--line:#dbe5dc;--radius:20px}\n*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;color:var(--ink);background:var(--paper);font:16px/1.65 system-ui,-apple-system,\"Segoe UI\",Roboto,Arial,sans-serif}\na{color:#205b36}button{font:inherit;cursor:pointer}a:focus-visible,button:focus-visible{outline:3px solid var(--gold);outline-offset:3px}\n.wrap{width:min(100% - 44px,1180px);margin-inline:auto}.skip{position:absolute;top:-120px;left:10px;z-index:3000;padding:12px 16px;color:var(--ink);background:#fff;border-radius:10px}.skip:focus{top:10px}\n.product-intro{background:radial-gradient(circle at 86% 0%,#d8e7d760,transparent 38%),linear-gradient(180deg,#fdfefc,#edf3ee);border-bottom:1px solid #dce7dc;padding:28px 0 40px}\n.crumb{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:0 0 28px;font-size:13px;color:#627165}\n.crumb a{color:#526a55;text-decoration:none;font-weight:700}.crumb a:hover{text-decoration:underline}.crumb .slash{color:#91a194}\n.product-grid{display:grid;grid-template-columns:minmax(0,.94fr) minmax(0,1.06fr);align-items:center;gap:clamp(30px,5vw,74px)}\n.product-copy{position:relative;min-width:0;padding:12px 0 18px}\n.eyebrow{display:inline-flex;align-items:center;gap:9px;text-transform:uppercase;color:#366143;font-size:12px;font-weight:900;letter-spacing:.10em}\n.eyebrow:before{content:\"\";width:27px;height:3px;border-radius:4px;background:var(--gold)}\n.product-copy h1{max-width:690px;font-size:clamp(33px,4.5vw,58px);letter-spacing:-.038em;line-height:1.09;margin:17px 0 23px;text-wrap:balance}\n.title-meta{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:23px}\n.status-pill{display:inline-flex;align-items:center;gap:8px;border-radius:99px;background:#e3f1e5;color:#245633;padding:7px 13px;border:1px solid #cce2cf;font-size:13px;font-weight:850}\n.status-pill:before{content:\"\";width:8px;height:8px;border-radius:50%;background:#31964f}\n.status-pill.pending{background:#fff1d4;border-color:#edd5a1;color:#74550b}.status-pill.pending:before{background:#bd9030}\n.status-pill.sold{background:#e9edeb;border-color:#d2dad4;color:#48574c}.status-pill.sold:before{background:#7e8c80}\n.place{display:inline-flex;align-items:center;gap:6px;font-size:14px;color:#57705d;font-weight:750}\n.hero-price-row{display:flex;flex-wrap:wrap;align-items:end;gap:8px 20px}\n.hero-price{font-size:clamp(32px,4vw,47px);font-weight:950;letter-spacing:-.04em;line-height:1.05;color:#173b23}\n.price-caption{font-size:13px;color:#6d7d70;max-width:245px;line-height:1.5}\n.hero-sub{font-size:15px;max-width:485px;color:#566d5a;margin:21px 0 0}\n.hero-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:27px}\n.primary-link,.quiet-link{min-height:49px;padding:11px 20px;border-radius:12px;display:inline-flex;align-items:center;justify-content:center;text-align:center;text-decoration:none;font-weight:850;font-size:15px}\n.primary-link{background:var(--green);color:#fff;box-shadow:0 9px 24px #1f332222}.primary-link:hover{background:var(--green2)}\n.quiet-link{border:1px solid #b6cabb;background:#fff;color:#28432e}.quiet-link:hover{background:#e5efe5}\n.hero-photo{background:#fff;border:1px solid #d9e5db;box-shadow:0 24px 55px #172d1a18;border-radius:24px;padding:11px;overflow:hidden;min-width:0}\n.photo-main{display:grid;place-items:center;position:relative;width:100%;aspect-ratio:1.37;border:0;background:#e9efe8;border-radius:16px;overflow:hidden;padding:0}\n.photo-main img{width:100%;height:100%;object-fit:contain}.photo-zoom{position:absolute;bottom:12px;right:12px;background:#122a1bdc;color:#fff;font-size:13px;font-weight:850;padding:7px 12px;border-radius:100px}\n.thumbs{display:flex;gap:8px;overflow-x:auto;padding:11px 2px 1px}.thumbs button{width:80px;height:65px;flex:0 0 80px;padding:3px;border:2px solid transparent;border-radius:10px;overflow:hidden;background:#e9efe8}\n.thumbs button[aria-pressed=\"true\"]{border-color:#236e3b}.thumbs button img{width:100%;height:100%;object-fit:cover;border-radius:6px}\n.photo-none{min-height:290px;display:grid;place-items:center;color:#5d7160;font-size:15px;font-weight:750;background:#eaf0ea;border-radius:15px}\n.photo-label{display:flex;justify-content:space-between;gap:8px;align-items:center;padding:6px 7px 1px;color:#728273;font-size:12px}\n.ad-main{padding:37px 0 70px}.ad-grid{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(300px,.86fr);gap:22px;align-items:start}\n.ad-box{min-width:0;background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:30px;box-shadow:0 12px 35px #2038260a}\n.ad-box h2{font-size:clamp(22px,2.3vw,28px);line-height:1.2;letter-spacing:-.018em;margin:0 0 20px}\n.description{white-space:pre-wrap;overflow-wrap:anywhere;margin:0;color:#293b2d;font-size:16px}\n.description-empty{color:#5a6a5d}.detail-meta{padding:18px 0 0;margin-top:24px;border-top:1px solid var(--line);font-size:14px;color:#687c6b}\n.contact{position:sticky;top:98px}.contact h2{margin-bottom:13px}.mini-brand{display:flex;gap:11px;align-items:center;margin-bottom:23px;padding:14px;background:#f0f5ef;border-radius:13px;color:#1e472a;font-weight:850;font-size:14px;line-height:1.4}\n.mini-symbol{width:40px;height:40px;flex:0 0 40px;background:#193b24;color:#f3d388;border-radius:10px;display:grid;place-items:center;font-weight:950;font-size:14px}\n.action{display:flex;align-items:center;justify-content:center;min-height:50px;gap:9px;text-decoration:none;text-align:center;font-weight:850;padding:12px 16px;border-radius:12px;line-height:1.35}\n.action-primary{background:#1f3322;color:#fff}.action-primary:hover{background:#30503a}.action-secondary{color:#24482d;background:#edf4eb;border:1px solid #c5d8c6;margin-top:10px}.action-secondary:hover{background:#deecdf}\n.action-disabled{padding:15px;background:#fff0d6;color:#674b11;border-radius:11px;font-weight:750}\n.contact-hint{font-size:13px;line-height:1.6;color:#657668;margin:17px 0 0}\n.contact-divider{border:0;border-top:1px solid var(--line);margin:22px 0 17px}.seller-detail{font-size:14px;color:#5e7162;line-height:1.7}.seller-detail strong{color:#274d32}\n.buy-info{margin-top:23px;padding:29px 31px;background:#f9fbf8}.buy-info h2{font-size:23px;margin:0 0 10px}.buy-info .info-lead{font-size:14px;color:#637567;margin:0 0 16px}\n.buy-info ul{padding-left:22px;margin:0;display:grid;gap:12px}.buy-info li{font-size:14px;color:#445747}.buy-info li strong{color:#1c3b25}\n.buy-info a{font-weight:750;text-underline-offset:3px}.smallnote{font-size:12px;color:#728173;margin:20px 0 0}\n.ad-bottom{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;margin-top:27px}.ad-bottom a{font-size:14px;font-weight:800}\n.photo-dialog{width:min(1060px,96vw);max-width:96vw;max-height:96vh;background:#0d2014;color:#fff;border:0;border-radius:15px;padding:18px}\n.photo-dialog::backdrop{background:#041209e8}.photo-modal-head,.photo-modal-actions{display:flex;justify-content:space-between;gap:14px;align-items:center}.photo-modal-head{margin-bottom:12px}.photo-dialog img{max-width:100%;max-height:75vh;object-fit:contain;margin:auto;display:block}.photo-modal-actions{margin-top:12px}\n.photo-dialog button{padding:10px 15px;border:0;border-radius:10px;background:#ecf3eb;color:#17351f;font-weight:850}.photo-dialog button:disabled{opacity:.4}\n@media(max-width:900px){.product-grid{grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:24px}.product-copy h1{font-size:clamp(31px,4vw,45px)}.ad-grid{grid-template-columns:1fr}.contact{position:static}.ad-main{padding-top:24px}}\n@media(max-width:660px){.wrap{width:min(100% - 28px,1180px)}.product-intro{padding:21px 0 28px}.crumb{margin-bottom:15px}.product-grid{grid-template-columns:1fr;gap:19px}.product-copy{padding:8px 0 4px}.product-copy h1{font-size:clamp(31px,9vw,44px);margin:12px 0 17px}.title-meta{margin-bottom:19px}.hero-sub{margin-top:15px}.hero-actions{margin-top:20px}.hero-actions a{flex:1 1 140px}.hero-photo{border-radius:18px;padding:8px}.photo-main{aspect-ratio:1.3}.thumbs button{width:70px;flex-basis:70px;height:59px}.ad-box{padding:20px}.buy-info{padding:23px}.photo-dialog{border-radius:0;max-width:100vw;width:100vw;max-height:100vh}.photo-dialog img{max-height:65vh}}\n@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}\n\n.buy-info{margin-top:23px;padding:0;overflow:hidden}.buy-info summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:23px 29px;cursor:pointer;font-size:22px;font-weight:850;line-height:1.25;color:var(--ink)}.buy-info summary::-webkit-details-marker{display:none}.buy-info summary:hover{background:#eaf1ea}.buy-info .expand-icon{display:grid;place-items:center;flex:none;width:33px;height:33px;border-radius:50%;background:#e8f0e7;color:var(--green);font-size:29px;line-height:1;transition:transform .2s}.buy-info[open] .expand-icon{transform:rotate(180deg)}.buy-info[open] summary{border-bottom:1px solid var(--line)}.buy-info-content{padding:23px 29px 27px}.buy-info-content .info-lead{margin-top:0}.buy-info-content ul{margin:0}.buy-info-content .smallnote{margin-bottom:0}@media(max-width:660px){.buy-info summary{padding:18px 20px;font-size:19px}.buy-info-content{padding:20px}}"
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
    market = (f'<a class="action action-secondary" href="{safe(market_url)}" target="_blank" rel="noopener noreferrer">Se annonsen på Marketplace ↗</a>' if is_facebook_market else "")
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
        gallery = f'''<div class="hero-photo">
          <button type="button" id="photo-open" class="photo-main" aria-label="Förstora produktbild">
            <img id="ad-primary-image" src="{safe(images[0])}" alt="{safe(title)} – bild 1" fetchpriority="high">
            <span class="photo-zoom" aria-hidden="true">Förstora bild ↗</span>
          </button>
          <div class="thumbs" role="group" aria-label="Välj produktbild">{thumbnails}</div>
          <div class="photo-label"><span>Faktiska bilder på objektet</span><span>{len(images)} {"bilder" if len(images) != 1 else "bild"}</span></div>
        </div>
        <dialog id="photo-dialog" class="photo-dialog" aria-label="Förstorad produktbild">
          <div class="photo-modal-head"><strong id="photo-count">Bild 1 av {len(images)}</strong><button type="button" id="photo-close">Stäng ×</button></div>
          <img id="photo-modal-image" src="{safe(images[0])}" alt="{safe(title)} – bild 1">
          <div class="photo-modal-actions"><button type="button" id="photo-prev" disabled>← Föregående</button><button type="button" id="photo-next" {"disabled" if len(images) == 1 else ""}>Nästa →</button></div>
        </dialog>'''
    else:
        gallery = '<div class="hero-photo"><div class="photo-none">Ingen produktbild tillgänglig</div></div>'
    if available:
        actions = '''<a class="action action-primary" href="sms:+46727483256">Skicka SMS om annonsen →</a>
        <a class="action action-secondary" href="https://www.facebook.com/profile.php?id=61588383880828" target="_blank" rel="noopener noreferrer">Kontakta oss via Facebook ↗</a>'''
        hero_cta = '<a class="primary-link" href="#kontakt">Fråga om objektet →</a>'
    else:
        actions = (f'<div class="action-disabled">{"Objektet är reserverat och inga nya förfrågningar tas emot just nu." if status_code == "pending" else "Objektet är sålt och inte längre tillgängligt."}</div>')
        hero_cta = ""
    text_description = safe(description) if description else "Kontakta oss om du vill veta mer om objektet."
    return f'''<!doctype html>
<html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<base href="/"><title>{safe(page_title)}</title>
<meta name="description" content="{safe(summary)}"><meta name="robots" content="{seo_index}">
<meta name="theme-color" content="#1f3322">
<link rel="canonical" href="{safe(url)}">
<meta property="og:type" content="product"><meta property="og:title" content="{safe(title)}">
<meta property="og:description" content="{safe(summary)}"><meta property="og:url" content="{safe(url)}">
{og_image}
<script type="application/ld+json">{ld_json}</script>
<style>{DETAIL_CSS}</style>
<script defer src="/statistik-raknare.js" data-page="annons:{safe(ad['id'])}"></script><script defer src="/partials1/site-shell.js" data-shared-site-shell></script>
</head>
<body>{MARKER}
<a class="skip" href="#annons-innehall">Hoppa till annonsen</a><div id="site-header"></div>
<header class="product-intro"><div class="wrap">
  <nav class="crumb" aria-label="Brödsmulor"><a href="index.html">Hem</a><span class="slash">/</span><a href="till-salu.html">Till salu</a><span class="slash">/</span><a href="annonser.html">Våra annonser</a></nav>
  <div class="product-grid">
    <div class="product-copy">
      <div class="eyebrow">Våra begagnade objekt</div>
      <h1>{safe(title)}</h1>
      <div class="title-meta"><span class="status-pill {state_class}">{status}</span><span class="place">📍 {safe(place)}</span></div>
      <div class="hero-price-row"><div class="hero-price">{formatted_price}</div><div class="price-caption">Pris enligt annons. Bekräfta tillgänglighet före köp.</div></div>
      <p class="hero-sub">Se originalbilderna och läs om objektets skick. Vi berättar gärna mer om det du undrar över.</p>
      <div class="hero-actions">{hero_cta}<a class="quiet-link" href="#beskrivning">Läs beskrivningen ↓</a></div>
    </div>
    {gallery}
  </div>
</div></header>
<main class="ad-main" id="annons-innehall"><div class="wrap">
  <div class="ad-grid">
    <div class="ad-details">
      <section class="ad-box" id="beskrivning" aria-labelledby="description-heading">
        <h2 id="description-heading">Beskrivning och känt skick</h2>
        <p class="description">{text_description}</p>
        <p class="detail-meta">Detta är ett begagnat objekt. Bedömningen av skick utgår från annonsens uppgifter och vad vi kommit överens om vid köpet.</p>
      </section>
      <details class="ad-box buy-info" id="kopinformation">
        <summary id="buy-info-heading"><span>Bra att veta före köp</span><span class="expand-icon" aria-hidden="true">⌄</span></summary>
        <div class="buy-info-content">
          <p class="info-lead">Praktisk information om skick, reservation, hämtning och dina rättigheter.</p>
          <ul>
          <li><strong>Skick och funktion:</strong> Läs beskrivningen och fråga gärna om eventuella fel, tester eller sådant som saknas. Begagnade varor kan ha normalt slitage.</li>
          <li><strong>Pris och reservation:</strong> En förfrågan är ingen beställning. Pris, tillgänglighet och eventuella villkor för reservation eller handpenning bekräftas innan ni gör upp affären.</li>
          <li><strong>Hämtning och transport:</strong> Visning, överlämning och eventuell leverans eller frakt ordnas efter överenskommelse.</li>
          <li><strong>Dina rättigheter:</strong> När du köper av oss som konsument gäller konsumentköplagen även för begagnade varor. Vid distansavtal kan du ha ångerrätt enligt lag. <a href="https://www.konsumentverket.se/konsumentratt/handla-begagnat/" target="_blank" rel="noopener noreferrer">Läs mer hos Konsumentverket ↗</a></li>
        </ul>
          <p class="smallnote">Uppgifterna ovan är allmän köpinformation. Det aktuella objektets beskrivning och det ni kommer överens om inför köpet är också viktiga.</p>
        </div>
      </details>
    </div>
    <aside class="ad-box contact" id="kontakt" aria-labelledby="contact-heading">
      <h2 id="contact-heading">Intresserad av objektet?</h2>
      <div class="mini-brand"><span class="mini-symbol" aria-hidden="true">SMÅ</span><span>Skaraborg Maskin &amp; Återbruk<br><small>Företag · Hjo, Skaraborg</small></span></div>
      {actions}
      {market}
      <button type="button" class="action action-secondary" id="copy-ad-name" data-name="{safe(title)}">Kopiera annonsens namn</button>
      <p class="contact-hint">Skriv gärna vilken maskin eller vilket redskap du frågar om, så kan vi hjälpa dig snabbare.</p>
      <hr class="contact-divider">
      <div class="seller-detail"><strong>Skriftlig kontakt föredras.</strong><br>Vi bokar visning och eventuell hämtning efter överenskommelse.<br>Ingen direktbetalning sker på denna annonssida.</div>
    </aside>
  </div>
  <nav class="ad-bottom" aria-label="Fler sidor"><a href="annonser.html">← Tillbaka till annonslistan</a><a href="om-oss.html">Läs mer om företaget →</a></nav>
</div></main>
<div id="site-footer"></div>
<script>{DETAIL_JS}</script></body></html>'''

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
