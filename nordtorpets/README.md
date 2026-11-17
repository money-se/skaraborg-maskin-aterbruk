# Nordtorpets Allservice AB – separat webbplats i undermapp

Detta är en första fristående, statisk webbplats under `https://skaraborgmaskin.se/nordtorpets/`.

## Separat från huvudwebbplatsen
- All ny webbdesign, HTML och CSS ligger i `nordtorpets/`.
- Endast interna länkar med prefix `/nordtorpets/`; Skaraborg Maskin & Återbruk har ingen gemensam header eller design här.
- Huvudwebbplatsens sidor, annonser, script och övriga tjänster är inte ändrade.

## Före lansering
1. Ersätt monogrammet N i sidhuvudet med Nordtorpets valda original-logotyp, optimera bilden till WebP/PNG, använd `alt`-text och sätt rätt bildstorlek.
2. Lägg in verifierad direktlänk till Nordtorpets Facebooksida i `kontakt/index.html` (just nu finns en tydlig uppmaning att söka efter sidan, ingen påhittad länk).
3. Kontrollera företagets RUT- och tillståndshantering för respektive uppdrag och aktuella formuleringar om behörigheter.
4. När sidan ska publiceras: lägg till sitemap i huvuddomänens `robots.txt` och/eller `sitemap.xml`; länka gärna mellan de två företagssidorna i relevant kontext.
5. Testa mobillägen, kontrollera text och länkar, begär indexering i Search Console efter publicering.

## SEO
Egen sidtitel, description, canonical, Open Graph och strukturerade data per sida. Undvik tunna ortssidor eller duplicerat innehåll; bygg lokala landningssidor först när unikt innehåll finns.

## Drift
GitHub Pages kan servera statiska HTML-filer direkt från undermappen med nuvarande CNAME. Ingen extra domän krävs. Inga bundlers eller tredjepartsbibliotek används i denna version.
