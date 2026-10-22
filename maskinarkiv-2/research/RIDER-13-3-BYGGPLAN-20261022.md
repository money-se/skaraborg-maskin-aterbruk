# Husqvarna Rider 13 – Maskinarkivet 3.0, research- och byggstart

**Datum:** 2026-10-22
**Status:** Påbörjad. Befintlig Rider 13-sida är en arbetad guide, inte ett tomt skelett. Den godkända Villa 12 HST-mallen styr arbetssätt och läsupplevelse, inte modellfakta.

## Inventering av befintlig sida
- Artikeldatakälla: `src/_data/machines/husqvarna-rider-13.json`
- 17 kapitel från snabbhjälp, identifiering och felsökning till motor, transmission, aggregat, service, varianter, köpråd och FAQ.
- 18 poster i nuvarande källista, med bland annat Husqvarnas originalmanualer, IPL och kompletterande reservdelskataloger.
- Sidan har redan fyra kontextuella digitala guider genom `digital-guide-placements.json` och samma gemensamma tema som Villa.
- **Ändra inte** produktversioner, motor-/remnummer eller servicevärden genom att kopiera från STIGA Villa.

## Första källkontroll och klassning

| Område | Belagt stöd | Begränsning/följd |
|---|---|---|
| Rider 13-familjen har flera versioner | Husqvarna originalmanual `pub000021448/doc000044020` (Rider 11 / 13 / 11 Bio / 13 Bio) och originalmanualer för Rider 13C i artikelns källregister | Betrakta inte 13, 13 H, 13 Bio, 13 R och 13C som identiska maskiner |
| K55 mot K46 | Återförsäljaren Gräsklipparbutiken listar K55 och K46 för Rider 13 och årsspecifika sprängskisser: https://www.xn--grsklipparbutiken-rqb.se/sv/gb/reservdelar-grasklippare/reservdelar-husqvarna-rider/reservdelar-rider-13 | **Sekundärkälla.** Husqvarna original-IPL för respektive produktnummer behövs innan en specifik variant får låst transmissionstyp |
| Tidig Rider 13 H | Husqvarna workshop manual med 2000-06-version för Rider 11 / 13 H / 11 Bio / 13 H Bio / 14 Pro / 16 H; exempel: https://mymowerparts.com/pdf/Husqvarna-Service-Repair-Manuals/W0001005.pdf | Den verkstadshandbokens K55-uppgifter kan inte ärvas av varje efterföljande Rider 13C |
| Rider 13C | Husqvarna original-IPL för produktnummer 965094301 (samt 966830601), 2010-07, https://www-static-nw.husqvarna.com/hbd/tdrdownload/v2/pub000045662/doc000081903/IPL/C9SKnqTaHbnAcqc819IE6aMI2Xo?httproute=True | Denna källa är relevant för dessa produktnummer; komponentpassning till äldre 13-varianter är inte visad |
| Köp-/reservdelsmetod | Modellbeteckning → produktnummer → motormärkning → transaxelns märkning → aggregatets identitet → sprängskiss | Metoden är generell, men delar, knivar, remmar och olja måste beläggas separat |

## Arbetsordning för Rider 13
1. **Identifieringsmatris:** kartlägg alla dokumenterade produktnummer för 13, 13 H, Bio/BioClip, R/R Special och 13C. Ange källa och år för varje rad.
2. **Motor och transmission:** använd endast originalmanual/IPL för aktuell produktvariant; dokumentera märkplatser och Model/Type/Code där motorfabrikatet kräver det.
3. **Klippaggregat:** koppla bredd, infästning, rem och knivsystem till identifierat redskap och maskinutförande – aldrig modellnamnet ensamt.
4. **Service- och säkerhetsmatris:** radvis kontroll av tryck, smörjning, laddning, motorservice och hydrostat endast med angiven modell/manual.
5. **Felsökning och köpråd:** bevara gratis modellunik kunskap; undvik upprepning av generella PDF-guider.
6. **Visuell slutkontroll:** ankarlänkar, tabeller på mobil, källor, köpflöde, SEO och genererad HTML.

## Hårda stopp före slutgodkännande
- Okänd motor-/transmissionsidentitet får inte ersättas av gissad specifikation.
- Inga universella serviceintervall eller remkompatibiliteter för hela Rider 13-familjen.
- Tillverkardokument som avser 13C, 13 H och 13 Bio måste hållas isär.
- Befintligt material granskas innan nya textavsnitt tillkommer, så att artikeln inte blir repetitiv.

## Resultat av denna etapp
Projektet har **påbörjats**, med dokumenterad källhierarki och prioriterad plan. Nästa PR får lägga till sakligt innehåll först när varje uppgift och tillhörande maskinversion är verifierad.
