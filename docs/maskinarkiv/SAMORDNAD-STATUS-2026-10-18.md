# Maskinarkivet – samordnad statusgranskning 2026-10-18

Repo: money-se/skaraborg-maskin-aterbruk
Status: granskning utan merge/publicering. Samtliga grenar utgår från samma ursprungliga main-SHA men main har avancerat separat.

## Kandidater

| Arbetsgren | Modellsida | Omfattning | Skillnad från aktuell main vid statuskontroll |
|---|---|---|---|
| feature/maskinarkiv-husqvarna-lth151 | maskinarkiv/husqvarna-lth151.html | 14 sections, 34k tecken | 10 commits före, 5 bakom; ytterligare research-v1.md |
| feature/maskinarkiv-stiga-park-16 | maskinarkiv/stiga-park-16.html | 16 sections, 42k tecken | 3 commits före, 5 bakom |
| feature/maskinarkiv-jonsered-lt2115 | maskinarkiv/jonsered-lt2115.html | 22 sections, 42k tecken | 3 commits före, 5 bakom; OVERLAMNING-2026-10-18.md |

Statisk kontroll:
- Alla tre sidor har interna ankarlänkar vars mål finns i respektive HTML.
- STIGA och Jonsered laddar header/footer via ../partials1/ och har egen canonical.
- Inga av dessa modellsidor finns på main enligt branch-jämförelserna.
- Jonsered-chattens överlämningsrapport redovisar uttryckligen kvarstående osäkerhet i produktnummer/tekniska påståenden.
- Dessa kontroller omfattar inte komplett HTML/CSS-validitet, renderad responsivitet, externa länkars funktion eller full sakkontroll.

## Viktiga integrationsspärrar
1. Varje chatt arbetar endast på sin egen gren tills kandidatgranskningen är klar.
2. Ändra inte main, sitemap, maskinarkivet.html, partials1, CSS utanför egna sidor eller andra chattars sidor.
3. Håll isär källbelagda variantuppgifter och generella råd på varje sida.
4. STIGA Park 16: kontrollera HST kontra HST Pro och Kanzaki K110 samt relevanta produktnummer före sammanslagning.
5. Jonsered LT2115: behandla produktnummerkonflikten i original-IPLn 544 46 75-01 som öppen avvikelse, enligt egen överlämning; ingen blind generalisering av hydrostat/aggregat.
6. LTH151: Hydro-Gear T2, Kohler SV470 och däckdimensioner har kontrollerats för produktnummer 96041001903. Andra versioner ej fullständigt avklarade.
7. Main har gått vidare efter att grenar skapades. Integrering kräver ny jämförelse, konfliktanalys och användarens explicita godkännande.
8. Visuellt webbläsartest återstår på alla tre; kalla ingen sida publiceringsklar innan detta och nödvändig källgranskning är utförda.

## Rekommenderad nästa grind
- Hämta aktuell sista commit och mottagen överlämningsrapport per chatt.
- Genomför gemensam kvalitetsmatris för fakta/versioner/källor/nav/mobil.
- När alla är godkända: planera samordnad navigering, arkivlista och sitemap som eget separat integrationsarbete.
- Gör INGEN merge utan användarens godkännande.
