# Digitala guider i Maskinarkivet

Alla Shopify-produkter hanteras centralt. Maskinartiklar ska **inte** innehålla handskrivna produktkort.

## Var ändrar vi vad?
- `src/_data/digital-guides.json`: Shopify-produktens titel, pris i SEK, bildadress på Shopify CDN, butikslänk, beskrivning och `active`. Kontrollera mot Shopify när pris, omslag eller publiceringsstatus ändras.
- `src/_data/digital-guide-placements.json`: välj vilket produkt-ID som ska visas efter ett visst kapitel för en viss maskinmodell. Exempel: `{"ny-maskin": [{"chapter": "felsokning", "product": "start"}]}`.
- `scripts/inject-guides.mjs`: gemensam renderare som injicerar ett produktkort i genererad HTML efter kapitelinnehållet.
- `scripts/check.mjs`: kontrollerar central datakälla, alla fyra Rider-korten, bildadresser, länkar samt frånvaro av gamla hårdkodade kort.

## När vi bygger nästa maskin
1. Bygg kapitlen och kontrollera att kapitel-ID:n är stabila.
2. Lägg till en rad för modellens slug i placeringsfilen och välj enbart relevanta produkter.
3. Behåll faktaguiderna gratis. Reklamen ska visa en kompletterande digital PDF och aldrig framstå som tillverkarens officiella manual.
4. Kör `npm run build`, `npm run check`, `npm run audit`; granska mobil- och desktopversion.
5. Publicera först efter granskning och godkännande.

## Pris och butikskoppling
Detta är en **kontrollerad Shopify-snapshot**, inte en levande API-koppling. Priser och omslag ändras inte automatiskt i Maskinarkivet när en Shopify-produkt redigeras. Uppdatera produktregistret efter varje betydande butiksändring, kör bygget och publicera den granskade versionen. Detta undviker beroende av klientnycklar/API på den statiska kunskapssidan.

Produktblocken är märkta med Skaraborg Merch och öppnar Shopify-produktens sida, inte en osäker direktköp-länk. Bilder laddas från de autentiska Shopify-CDN-adresserna.
