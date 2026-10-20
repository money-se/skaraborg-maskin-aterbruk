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

## Steg 2: gemensamma layoutkomponenter (2026-10-20)

Pilotens Nunjucks-mallar återanvänds nu av innehållet i datafilen:

- `src/_includes/partials/hero.njk` – sidhuvud
- `src/_includes/partials/nav.njk` – kapitelmeny
- `src/_includes/partials/mobile-nav.njk` – mobilmeny
- `src/_includes/partials/chapter.njk` – kapitlets rubrik och omslag
- `src/_includes/partials/sources.njk` – utfällbara originalkällor

Maskindatan innehåller titel, ingress, etiketter, kapitelnamn, kapitelinnehåll och källor. Den gamla sidomenyn är inte längre kopierad in i datan.

**Återstår:** att konvertera `bodyHtml` i varje kapitel till helt strukturerade objekt för faktarutor, tekniska tabeller, checklistor och övriga återkommande block. I detta steg är dessa block fortfarande bevarad HTML för att undvika att maskininformation går förlorad. `headHtml` och `footerHtml` är också fortfarande äldre infrastruktur som behöver flyttas till gemensam sidlayout i nästa steg.

GitHub Actions-bygg: https://github.com/money-se/skaraborg-maskin-aterbruk/actions/workflows/maskinarkiv-2-pilot.yml


## Steg 3: återanvändbara innehållsblock (2026-10-20)

STIGA Park 16:s 16 innehållskapitel innehåller nu en ordnad lista av `blocks` i datafilen i stället för en enda `bodyHtml`-sträng per kapitel. Nunjucks använder separata komponentmallar i `src/_includes/blocks/` för:

- `facts` – etikett/värde-rader ur maskinens faktarutor
- `note` och `warning` – notisrubrik och förklaring som separata fält
- `table-scroll`, `check`, `steps`, `answer`, `faq`, `cta` och `tradera-follow`

Tabellceller, listpunkter och andra komplexa underblock ligger ännu som bevarad `innerHtml` inuti respektive komponent. Detta är en medveten, säker mellanform för att behålla uppgifter och länkar under migreringen. Nästa förbättring är att modellera även dem som strukturerade fält.

Tradera-sektionen är nu fristående från kapitlet Återbruk, och källor renderas från sex strukturerade källposter. Kontrollerna omfattar komponentantal, ankarlänkar, unika ID och balanserade HTML-sektioner. Publicerade modellsidor har inte ändrats av denna pilot.
