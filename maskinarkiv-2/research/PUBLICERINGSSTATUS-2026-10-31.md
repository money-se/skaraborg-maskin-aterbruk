# Faktisk publiceringsstatus – fem maskinartiklar (2026-10-31)

Detta är en **läsbaserad granskning** av GitHub-grenen `manual-intake-october-30`, inte ett resultat från komplett lokal webbbyggning. Kontrollera om andra alias eller datakällor används innan ett nytt register skapas.

| Artikel | Artikeldata | Kanoniskt register med exakt artikel-slug | Forskningsläge |
|---|---|---|---|
| STIGA Park 16 | ja | hittades inte på `research/machines/stiga-park-16.json` | kontrollera motsvarande befintligt register / annat slug innan åtgärd |
| Husqvarna Rider 13 | ja | ja | `needs_research`, 26 claims, 12 källor, 10 öppna gaps |
| Husqvarna LTH151 | ja | hittades inte på `research/machines/husqvarna-lth151.json` | kontrollera eventuell alternativ slug |
| STIGA Villa 12 HST | ja | ja | `scoped_ready`, 53 claims, 32 källor, 20 öppna gaps, 51 scoped publicerade claim-ID |
| Jonsered LT2115 | ja | **14 separata variantregister finns** under `jonsered-lt2115*` | **inte forskningslöst**; release kräver artikel-till-variantavgränsning |

## Genomfört
- ZT-2200/EZT: forskningsregistrets scope har uppdaterats så att det inte längre felaktigt påstår att kontrollerad oljespecifikation och volym saknas.
- `scripts/audit-article-readiness.mjs` tillagd, **skrivskyddad** och oberoende av GitHub-tester. Jämför artikel-slug, kapitel-ID, existerande forskningsregister, claim/source-referenser och scoped review.
- En motsvarande fristående lokal kontroll har testats med positiva och negativa fixtures (saknat register, strikt spärr, giltig scoped release, felaktigt publicerat claim-ID). Fullständigt lokalt repositorytest är **inte** genomfört.

## Rekommenderat nästa arbete i rätt ordning
1. Jonsered: behåll de 14 separata produktnummer-/variantregistren. Koppla artikelns delpåståenden till rätt variant; ett gemensamt familjenamn får inte räknas som publiceringsgodkännande. STIGA Park 16 och Husqvarna LTH151: ingen motsvarande exakt- eller prefixmatchning i hela GitHub-trädet per 2026-10-31; undersök äldre underlag innan något skapas.
2. För de fem artiklarna: bygg lokalt och kör `npm run check`, `npm run audit`, `npm run research:check`. Slå inte av spärrarna.
3. För Rider 13: arbeta direkt med de 10 dokumenterade forskningsluckorna och belägg berörda artikelsatser med tillverkarkällor; sätt inte `ready` utan stöd.
4. För Villa 12 HST: håll strikt på `scoped_ready` och dess undantag. Ändra inte till universella reservdels- eller motorvärden.
5. Efter grön faktisk lokal webbbyggning: visuell kontroll mobil/desktop och publiceringsbeslut per artikel.

**Viktigt:** Detta är en blockerarrapport, inte ett påstående om att fem sidor nu kan publiceras. Artiklarna är ännu inte kompletta tekniskt granskade mot samtliga originalkällor.

## Korrigering efter fullständig trädkontroll
GitHubs rekursiva träd för arbetsgrenen har kontrollerats (inte enbart kodsökning). Det finns **14** `jonsered-lt2115*`-register (enligt trädets filnamn, inklusive A/CMA-varianter). Den tidigare formuleringen att Jonsered saknar forskningsregister var missvisande och är nu korrigerad. STIGA Park 16 och Husqvarna LTH151 saknar fortfarande exakt/prefixmatchande poster i `research/machines`. Detta bevisar inte att andra artiklar eller historiska källunderlag saknas.
