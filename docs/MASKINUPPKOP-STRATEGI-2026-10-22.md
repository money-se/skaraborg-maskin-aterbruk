# Strategisk granskning – undersidor för maskinuppköp
**2026-10-22 | Arbetsutkast för PR #53 | Inga publika sidändringar**

## Slutsats
Skaraborg Maskin & Återbruk bör inte skapa ytterligare ort × maskintyp-sidor förrän vi har fastställt **sökintention, unik nytta, sidhierarki och indexeringsbeslut**. Vi bör skilja tydligt på (a) att sälja till företaget, (b) ge utan ersättning, (c) skrot/bortforsling och (d) att läsa guider. Hjo-sidorna är kvalitetsreferens, inte krav på lika många sidor i varje ort.

Den regionala affärsingången för **få ett bud** bör fortsätta vara `kop-maskiner.html`. `ge-till-aterbruk.html` ansvarar för förfrågningar utan ersättning (se separat draft-PR #56). `aterbruk.html` är bredare för partier/gårdar/verkstäder. Försäljning, donation och betald bortforsling ska inte utlovas som samma tjänst.

## Inventering – sex uppköpsnära sidfamiljer
I inventeringsfilen `docs/MASKINUPPKOP-UNDERSSIDOR-2026-10-22.csv` listas varje familjemedlem individuellt med preliminär rekommendation. Siffror från GitHubs `main`-träd och fyra sitemap-filer.

| Sidfamilj | Antal filer | Finns i sitemap | Strategiskt beslut |
|---|---:|---:|---|
| Sälja maskin | 11 | 1 | Regional tjänst/översikt; ortspilot snarare än masskopior |
| Sälja åkgräsklippare | 11 | 1 | Specialisering möjlig; kräv faktisk modellerfarenhet/unikt innehåll |
| Sälja gräsklippare | 11 | 1 | Specialisering möjlig; kräv unik vägledning |
| Sälja trädgårdsmaskiner | 11 | 0 | Starkt överlapp; pröva konsolidering mot regional/ortshubb |
| Bli av med maskiner | 11 | 0 | Vägval köp/gåva/skrot, men svag kandidat som många ortskopior |
| Maskinskrot | 11 | 0 | Eget ämne skrot; ägarskap under skrothämtning, ej direkt uppköp |
| **Totalt** | **66** | **3** | **Ingen massindexering** |

Detta är **sex familjer om 11 filer = 66 HTML-filer**, inte 66 kvalitetssäkrade indexeringsmål. Utöver dem finns `kop-maskiner.html`, `kop-trasiga-maskiner-skaraborg.html`, värderings-/felsökningsguider och relaterade verkstads-/skrot-/återbrukssidor.

### Belagda observationer
1. **Hög dupliceringsgrad mellan vissa äldre ortsvarianter.** Huvudtexten i `salja-maskin-skovde.html`, `salja-maskin-falkoping.html`, `salja-maskin-skara.html`, `salja-maskin-toreboda.html` och `salja-maskin-habo.html` är ordagrant lika när ortsnamnen normaliseras (i jämförelsen exkluderas HTML-element, script, style och navigation). Samma i granskade `salja-akgrasklippare-falkoping/mariestad/karlsborg.html`. Exemplen är *källverifierade*, men inte alla 66 filer har full textjämförts.
2. **Skillnad i textdjup.** `kop-maskiner.html` har cirka 4 968 tecken synlig huvudtext och `salja-maskin-skaraborg.html` cirka 4 269. Granskade äldre lokala `salja-maskin-tibro/karlsborg/skovde.html` innehåller ungefär 750–900 tecken. Godkända Hjo-varianter har cirka 3 800 tecken, egna maskinbilder och tydliga förfrågningsflöden. Sidlängd är inget kvalitetsmått i sig.
3. **Flera regionala äldre sidor anger fel domän i canonical.** Bekräftade: `salja-akgrasklippare-skaraborg.html`, `salja-grasklippare-skaraborg.html`, `salja-tradgardsmaskiner-skaraborg.html`, `kop-trasiga-maskiner-skaraborg.html`, `bli-av-med-maskiner-skaraborg.html` och `maskinskrot-skaraborg.html` pekar på `money-se.github.io/skaraborg-maskin-aterbruk/`. Om en sådan sida ska vara självständig sida för `skaraborgmaskin.se` bör canonical peka på den valda kanoniska adressen där; välj mål och kontrollera internlänkar/sitemap tillsammans.
4. **Gammalt Hjo-material har redan konsoliderats.** `bli-av-med-maskiner-hjo.html` och `salja-tradgardsmaskiner-hjo.html` leder till `salja-maskin-hjo.html`; `maskinskrot-hjo.html` leder till `skrot-hamtning-hjo.html`. Bevara dessa befintliga besökarvägar.
5. **Frånvaro i sitemap är inte samma sak som noindex.** Regionala äldre sidor och många lokala undersidor är inte med i sitemap, men saknar samtidigt uttrycklig noindex. Vi kan inte fastställa faktisk Google-indexering, kanonisering eller trafik utan Search Console.
6. **Automatik måste hållas under kontroll.** `scripts/phase1_local_seo.py` har familjelista och en förväntad scope om **105 existerande lokala HTML-filer**. `.github/workflows/phase1-local-seo.yml` går vid ändring av skriptet eller manuellt (`workflow_dispatch`), inte enligt timschema. Skriptet *lägger till* canonical när den saknas, men rättar inte redan befintliga canonicals med fel domän. Kör inte det arbetsflödet slentrianmässigt under omstrukturering.

## Rekommenderad sidhierarki
### Steg 1: Primär konverteringssida
**`/kop-maskiner.html` – Sälj till oss.** Huvuduppgiften är att få en intressant maskinförfrågan: 1–3 bilder, ort, märke/modell, skick, saknade delar, ungefärligt prisönskemål. Inget automatiskt köplöfte. PR #56 (draft) förtydligar väg till `ge-till-aterbruk.html`.

### Steg 2: Regionala guide- och specialistintentioner
| URL / ämne | Beslut nu | Villkor för egen sida |
|---|---|---|
| `salja-maskin-skaraborg.html` | **Utred som informationsguide**, inte andra identisk tjänsteingången | Skilj från `kop-maskiner.html` genom verklig värderingsmetodik, dokumenterade exempel och tydlig guidefunktion. Annars slå ihop senare efter data. |
| `salja-akgrasklippare-skaraborg.html` | **Möjlig specialistguide** | Modellspecifika detaljer om åkgräsklippare, hydrostat, aggregat, motor och vilka foton/uppgifter som spelar roll. |
| `salja-grasklippare-skaraborg.html` | **Möjlig specialistguide** | Eget användbart innehåll för handklippare: motor, drivning, däck/uppsamlare, skick och värderingsfaktorer. |
| `kop-trasiga-maskiner-skaraborg.html` | **Möjlig specialistguide** | Faktisk vägledning om defekter, reservdelsvärde, identifiering och vilka objekt som passar uppköp. |
| `salja-tradgardsmaskiner-skaraborg.html` | **Låg prioritet som egen URL** | Överlapp med huvudköp, åkgräsklippare, handklippare och övriga maskiner; pröva konsolidering. |
| `bli-av-med-maskiner-skaraborg.html` | **Vägvalsfråga snarare än extra generisk landningssida** | Skilj bud, gåva, återbruk och eventuell betald tjänst; troligen bättre som stödtext på befintlig hubb. |
| `maskinskrot-skaraborg.html` | **Flytta ämnesansvar till skrotspåret** | Se `skrot-hamtning.html` och faktiska villkor; separera skrot från maskinuppköp. |
| `trasig-grasklippare-varde.html` och `akgrasklippare-startar-inte.html` | **Nuvarande tunna kunskapsingångar – möjliga att bygga ut** | Måste få substantiell vägledning, sakliga källor och verkligt värde utöver ”skicka bilder”. |
| `tomma-verkstad-maskiner.html` | **Flytta ämnesansvar till större partier/företag** | Knyt till `aterbruk.html` och `foretag.html`, med tydlig avgränsning mot avfallshämtning. |

**Viktigt:** ovan är strategiska förslag, inte beslut om att noindexa, 301-omdirigera eller radera sidor. Särskilt två likartade URL:er kan ha olika trafik och historik.

### Steg 3: Lokala sidor efter pilot
- **Hjo**: håll de tre godkända uppköpssidorna (`salja-maskin-hjo.html`, `salja-akgrasklippare-hjo.html`, `salja-grasklippare-hjo.html`) orörda. Befintliga Hjo-vidarebefordringar bevaras.
- **Tibro som testort**: starta med *en* övergripande lokal uppköpssida `salja-maskin-tibro.html`, och jämför kvalitet och syfte med `tibro.html`. Bestäm därefter om egen åkgräsklipparsida ger tillräckligt unikt värde. Undvik att genast lyfta alla befintliga `*-tibro.html` till sitemap.
- **Skövde och övriga orter**: vänta med stora förändringar tills Tibro-piloten och Search Console visar vad som får relevanta besök och förfrågningar.

## Föreslagna beslutspunkter innan kod
1. Bekräfta att `kop-maskiner.html` är regional affärshubb och att `salja-maskin-skaraborg.html` endast behålls som självständig guide om den utvecklas till något tydligt annat.
2. Godkänn pilotort **Tibro**, med målet en kvalitativ lokal uppköpssida först.
3. Godkänn att äldre regionala undersidor **inte** indexeras/en-masse; gör i stället en URL-plan per sida, med eventuell GSC-data om visningar, sökord och Google-vald canonical.
4. När detta är beslutat: skapa en isolerad PR för pilot + länkar + kvalitetskontroller. Lämna startsida, header/footer och godkända Hjo-sidor orörda.

## Datagränser
- Jämförelserna bygger på GitHub-kod och urval; inte live-skärmbilder, full Lighthouse-mätning eller Search Console. Läs inte frånvaro i sitemap som bevis på ”ej indexerad”.
- Lokalt/tekniskt namn i filen betyder inte att företaget har en fysisk filial eller dokumenterat arbete på orten. Undvik sådana påståenden utan underlag.
- Ingen befintlig URL har ändrats eller avpublicerats i denna granskning.

## Referenser och beslutsunderlag
- [Google Search Central – canonicalisering](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google Search Central – dubbelt innehåll](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google Search Central – doorway abuse](https://developers.google.com/search/docs/essentials/spam-policies)
- GitHub: `main`, `scripts/phase1_local_seo.py`, `.github/workflows/phase1-local-seo.yml` och angivna HTML-filer.
- Övergripande karta: `docs/UTVECKLINGSKARTA-2026-10-22.md` (utkast i PR #53).
