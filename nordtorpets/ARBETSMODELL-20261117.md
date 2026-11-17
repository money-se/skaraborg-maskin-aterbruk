# Nordtorpets – arbetsmodellen från Skaraborg Maskin & Återbruk
Datum: 2026-11-17
Status: arbetssätt för granskning och pilot, INTE färdig lanseringsplan.

## Befintlig webb
Nordtorpets har en startsida, sju tjänstesidor och kontakt. Separat identitet och CSS är på plats under /nordtorpets/.
Kvar: starkare sökavsikter, tydligare egna kundsituationer och varför välja oss, servicepaket med konkret information, mobilgranskning och verkliga bilder.

## Grundprinciper
1. Sökintention före sidantal. Varje sida ska besvara en specifik kundfråga.
2. Frågan 'Varför ska jag kontakta just Nordtorpets?' ska besvaras med verkliga, verifierbara fördelar. Inga fabricerade kundfall eller bilder.
3. Sida = kundproblem > tydligt erbjudande > process > kostnad och villkor > FAQ > kontakt.
4. Hjo först, sedan andra orter endast med unikt innehåll, verkliga arbetsvillkor och tydlig lokal relevans.
5. Tjänsternas scope ska vara korrekt: ingen mark- och anläggningsentreprenad. Gräsklippare och åkgräsklippare är verkstadsfokus. Svetsning sker endast hos oss.
6. RUT endast där regelverket och arbetsuppgiften medger det. Erbjud inte RUT för gräsklipparreparationer.
7. Nordtorpets och Skaraborg Maskin & Återbruk ska ha separata varumärken och rätt juridisk avtalspart.
8. Samma godkända komponenter, typografi, menyer, kontaktvägar, mobilbeteende och tekniska mall på alla Nordtorpets sidor; inga avvikande designers utan skäl.

## Föreslagen informationsarkitektur
- /nordtorpets/ – nav för service och offert.
- /nordtorpets/grasklipparservice/ – service och felsökning, reparation/renovering efter bedömning.
- /nordtorpets/tradgard-gronytor/ – trädgårdsskötsel / klippning / sly.
- /nordtorpets/rojning-tomning/ – garage, förråd, dödsbo och praktisk utrensning.
- /nordtorpets/fastighetsservice/ – fastighetsservice och vinterarbete.
- /nordtorpets/praktisk-hjalp/ – bära, flytta, vedhantering.
- /nordtorpets/personal-forare/ – extra personal och förartjänster.
- /nordtorpets/svets-reparation/ – mindre svetsning / reparation i egen verkstad.
- /nordtorpets/kontakt/ – direktkontakt, tydliga instruktioner.
Nya URL:er bara när de möter andra verkliga kundbehov; bedöm överlapp först.

## Pilotgranskning
- Pilot: gräsklipparservice, separata noindex-läge under /nordtorpets/forhandsgranskning/grasklipparservice/.
- Pilot exkluderas från sitemap och interna produktionslänkar, ingen canonical.
- Kontrollera mobildesign, innehåll, länkar, H1, kontakt, inskrivna priser, omfattning och FAQ.
- Lägg till riktiga bilder endast när sådana finns och ägaren godkänt dem.
- Ändra ingen befintlig produktionssida förrän pilot och gemensam layout är godkända.

## Vid en senare publicering
- Uppdatera själva tjänstesidan, internlänkar, HTML-head/schema, sitemap och nav i samma PR.
- Testa manuellt och med kodkontroller, läs tillbaka GitHub-filerna.
- Verifiera GitHub Pages-publiceringen och direkt-URL efter merge.
- Följ upp sökfrågor/visningar i Search Console; utvärdera utifrån verklig data.

## Fortsättning efter pilot
1. Förbättra design och innehåll på startsidan så att tjänsterna och de viktiga kundbehoven får rätt prioritet.
2. Fördjupa en tjänstesida i taget med annan kundavsikt, inte kopiera mallen ordagrant.
3. Bygg lokalt först för Hjo, utvärdera sedan Tibro/Skövde/Karlsborg/Tidaholm utifrån belagda arbetsområden.
4. Bilder från verkliga jobb och maskiner, med korrekt bildtext och alt-text.
