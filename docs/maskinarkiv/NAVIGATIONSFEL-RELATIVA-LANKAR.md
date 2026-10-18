# Integrationsblockerare – relativa länkar i Maskinarkivet
Datum: 2026-10-18
Status: bekräftad statisk felanalys av GitHub-filer, inte en webbläsartest.

## Källan till problemet
Gemensamma partials från main, partials1/header.html och partials1/footer.html, innehåller rotbaserade NAV-mål skrivna som relativa dokumentvägar: index.html, kop-maskiner.html, kontakt.html, sitemap.xml och flera andra.

På en undersida såsom /maskinarkiv/jonsered-lt2115.html resolveras en insprutad länk href="kop-maskiner.html" av webbläsaren till /maskinarkiv/kop-maskiner.html, vilket inte motsvarar avsedd root-sida (/kop-maskiner.html).

## Grenspecifik status
- Husqvarna LTH151, branch feature/maskinarkiv-husqvarna-lth151: ÅTGÄRDAD i commit c66b52c. Injektionen omskriver lokala relativa href/src i header/footer till absolut webbplatsrot. Statiskt kodgranskad men ännu inte körd i browser.
- STIGA Park 16, branch feature/maskinarkiv-stiga-park-16: HAR redan root-rebasering i funktionen insertPartial() på den lästa bloben 09f1a528. Måste browser-verifieras.
- Jonsered LT2115, branch feature/maskinarkiv-jonsered-lt2115: ÖPPEN. Skriptets inject() sätter e.innerHTML direkt, utan att rebasera relativa länkar. Behöver åtgärdas av Jonsered-chatten på dess egen gren; gör inte detta från koordinatorgrenen.

## Säker åtgärd för Jonsered-chatt
Behåll exakt samma layout och gemensamma partialfiler. Efter hämtning av header/footer: parsa fragmentet i en template, iterera över alla element med lokala href/src, gör bara dokumentrelativa värden root-relativa (t.ex. kop-maskiner.html -> /kop-maskiner.html). Bevara absoluta /..., #..., mailto:, tel:, https: samt andra URI-scheman utan modifiering. Kör sedan statisk kontroll och webbläsartest med klick på minst Hem, Vi köper och Kontakt i såväl header som footer.

## Godkännandekriterium
På /maskinarkiv/<modell>.html ska navigationen peka till /index.html eller /, /kop-maskiner.html och /kontakt.html, ALDRIG till /maskinarkiv/index.html, /maskinarkiv/kop-maskiner.html eller /maskinarkiv/kontakt.html. Externa länkar måste vara oförändrade. Detta gäller alla tre sidor före publicering.

## Gränser
Inga ändringar i main, sitemap.xml, maskinarkivet.html, gemensamma partials eller andra chattars gren. Ingen integrering/merge utan användarens uttryckliga godkännande.
