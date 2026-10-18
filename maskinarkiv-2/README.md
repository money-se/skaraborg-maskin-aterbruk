# Maskinarkivet 2.0 – 11ty-pilot

Detta är en **separat testbyggnad**; ingen publicerad HTML-fil skrivs över.

## Kör lokalt

```bash
cd maskinarkiv-2
npm install
npm run build
npm run check
```

Byggutdata skrivs till `_maskinarkiv-preview/maskinarkiv/stiga-park-16.html` i projektroten. Öppna gärna via en lokal HTTP-server från projektroten så att befintlig CSS, header och footer går att hämta. Den här piloten migrerar STIGA Park 16 **utan redaktionella innehållsändringar**.

## Hur det fungerar

- `src/stiga-park-16.njk`: sidmall som monterar ihop kapitel
- `src/_data/machines/stiga-park-16.json`: maskinspecifika kapitel med id, rubrik och befintlig källkontrollerad HTML
- `src/_data/machines.js`: läser innehållsfilen
- `scripts/check.mjs`: verifierar att kapitel och vitala element återfinns i den genererade filen

**Begränsning i första piloten:** sidhuvud, meny och befintliga kapitelmarkup följer med som oförändrade HTML-delar. Nästa steg är att bryta ut gemensamma komponenter (faktaruta, steg, källor, navigering) till separata Nunjucks-mallar och omvandla innehållet till fält i JSON. Först då blir komponenternas form helt styrd av en enda mall. Denna pilot bevisar byggkedjan och gör migreringen reversibel.

Den publika CSS-sökvägen är `/maskinarkiv/maskinarkiv-v6.css`. För att förhandsgranska behöver man antingen leverera CSS från webbplatsen eller kopiera in den i en lokal webbserver. Inget byggsteg körs automatiskt av GitHub Pages ännu.
