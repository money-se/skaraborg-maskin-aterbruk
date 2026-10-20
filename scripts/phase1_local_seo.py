#!/usr/bin/env python3
"""Phase 1: conservative, repeatable technical changes to LOCAL SEO landing pages only.
Does not delete pages, rewrite substantive content, change statuses or redirect URLs.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FAMILIES = (
    "salja-maskin", "salja-grasklippare", "salja-akgrasklippare",
    "salja-tradgardsmaskiner", "bli-av-med-maskiner", "verkstad-maskiner",
    "maskinskrot", "skrot-hamtning", "aterbruk", "dodsbo-utrensning",
)
PLACES = ("hjo", "tibro", "skovde", "mariestad", "karlsborg", "falkoping",
          "skara", "toreboda", "tidaholm", "habo", "skaraborg")
CONTACT = "https://www.messenger.com/t/924620407412160/"
MARKER = "Fler sätt att kontakta oss och läsa vidare"

def relevant_service(name):
    if name.startswith("dodsbo-"): return "dodsbo-utrensning.html"
    if name.startswith(("skrot-hamtning-", "maskinskrot-")): return "skrot-hamtning.html"
    if name.startswith("aterbruk-"): return "aterbruk.html"
    return "kop-maskiner.html"

def edit(name, original):
    result = original
    if not re.search(r'<link\b[^>]*\brel=["\']canonical["\']', result, re.I):
        if not re.search(r'</head>', result, re.I):
            raise ValueError(f"No head closing tag: {name}")
        canonical = f'<link rel="canonical" href="https://skaraborgmaskin.se/{name}">\n'
        result = re.sub(r'</head>', lambda m: canonical + m.group(), result, count=1, flags=re.I)
    # Replace ONLY phone-button links, keeping telephone number in prose untouched.
    def text_cta(m):
        attrs, label = m.group(1), m.group(2)
        attrs = re.sub(r'href=["\']tel:[^"\']+["\']',
                       f'href="{CONTACT}" target="_blank" rel="noopener noreferrer"', attrs, flags=re.I)
        if re.search(r'\bRing\b|📞|072[\s-]*748', label, re.I):
            label = "✉ Skriv på Messenger"
        return "<a" + attrs + ">" + label + "</a>"
    result = re.sub(r'<a(\s[^>]*\bhref=["\']tel:[^"\']+["\'][^>]*)>([^<]*)</a>',
                    text_cta, result, flags=re.I)
    if MARKER not in result:
        service = relevant_service(name)
        links = f'''\n<nav aria-label="{MARKER}" style="max-width:1080px;margin:22px auto;padding:15px 20px;background:#f0f5ef;border-radius:12px">
<strong>Mer information:</strong> <a href="/{service}">Läs om tjänsten</a> · <a href="/foretag.html">För företag</a> · <a href="/kontakt.html">Kontakt</a>.
<p>Vi föredrar skriftliga förfrågningar. Skicka gärna bilder, ort och en kort beskrivning via <a href="{CONTACT}" target="_blank" rel="noopener noreferrer">Messenger</a>.</p>
</nav>\n'''
        if not re.search(r'</main>', result, re.I):
            raise ValueError(f"No main closing tag: {name}")
        result = re.sub(r'</main>', lambda m: links + m.group(), result, count=1, flags=re.I)
    # Normalize existing trailing spaces too, so git diff --check stays clean.\n    result = re.sub(r"[ \\t]+(?=\\r?$)", "", result, flags=re.M)\n    return result\n\ndef main():
    changed = []
    for family in FAMILIES:
        for place in PLACES:
            name = f"{family}-{place}.html"
            path = ROOT / name
            if not path.is_file(): continue
            original = path.read_text(encoding="utf-8")
            revised = edit(name, original)
            if revised != original:
                path.write_text(revised, encoding="utf-8")
                changed.append(name)
    # 105 currently existing pages; fail closed if directory layout changes unexpectedly.
    existing = [f"{f}-{place}.html" for f in FAMILIES for place in PLACES
                if (ROOT / f"{f}-{place}.html").exists()]
    if len(existing) != 105:
        raise RuntimeError(f"Unexpected local page scope: {len(existing)}")
    print("LOCAL_SEO_SCOPE=" + str(len(existing)))
    print("LOCAL_SEO_UPDATED=" + str(len(changed)))
    for name in changed: print("UPDATED " + name)

if __name__ == "__main__":
    main()
