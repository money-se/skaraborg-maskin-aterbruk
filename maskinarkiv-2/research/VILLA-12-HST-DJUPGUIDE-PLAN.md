# Villa 12 HST – arbetsplan för full djupguide

**Status:** Redaktions- och forskningsplan, **inte** färdig artikel.  
**Utgångsläge:** 12 kapitel, cirka 2 250 ord i artikelns kapitel, fem identifierade maskin-PNC, fyra digitala guider, 14 synliga källposter. Forskningsregister: 53 påståenden, 32 källposter, 20 forskningsluckor.

## Prioriterad ombyggnad
**P0 – måste kvalitetssäkras före större innehållsrevision**
- Fånga varje publicerat numeriskt servicevärde, remnummer, aggregatversion och säkerhetsbegränsning i en granskningsmatris: exakt maskinversion, claim-ID, källa och locator.
- Verifiera att de 14 externa källänkarna leder till rätt dokument. Skilj originaldokument från tredjepartsspegling och reservdelsbutik.
- Granska originalmanualens intervall och motorvariant så Briggs-servicedata aldrig ärvs från GGP/WM.
- Ingen bredare publicering av teknisk fakta förrän varje uppgift klarat denna kontroll.

**P1 – nya kärnfördjupningar**
1. **Identitet och fem versioner:** redovisa varje PNC med dokumenterad produktårgång, källa och belagda skillnader. Bildförklaring för hur etiketter hittas. Saknade Briggs Model/Type/Code skrivs uttryckligen som okända.
2. **Motor:** generell funktionsförklaring och separata, källbundna spår för GGP/WM och Briggs; bränsle/tändning/olja/filter endast enligt relevant motor-ID.
3. **Framdrivning:** pedal, parkeringsbroms, frikoppling, K46CJ och remkedjan; säkra symtomvägar utan generella transmissionsoljeanvisningar.
4. **Styrning och säkerhet:** wire, bakhjulsstyrning, kontrollpunkter, startvillkor och när maskinen måste tas ur bruk.
5. **85 C och 85 Combi:** komponentschema på begriplig nivå, aggregat-PNC, rem-/knivsystem, monteringskontroller och sådan kompatibilitet som går att belägga.
6. **Felsökning:** separata grenar för ingen startmotor, runtdragning utan motorstart, varm/kall drivning, remproblem, ojämnt klippresultat, vibration och sämre klippfunktion.
7. **Service och reservdelar:** intervall- och komponenttabeller med separata manualer, räkna aldrig rem-/transaxeldelar som universella.
8. **Begagnatköp:** kontroll före provkörning, provkörning, varmtest, identitetskontroll, skriftliga reservationer; skilj fakta från praktiska råd.

**P2 – pedagogisk slutredigering**
- Nybörjarvänlig ordförklaring direkt vid första tekniska begreppet; djupare ordlista när den hjälper.
- Samma begripliga navigering som idag; visa djupet via H3, figurer och tabeller snarare än flera stora textväggar.
- Korta sammanfattningar ovanför omfattande underavsnitt och mobilkontroll av alla långa artikelnummer.
- Behåll fyra digitala guider, men låt dem inte bryta kritiska felsökningssteg.

## Ämnesinventering enligt faktiskt forskningsregister

| Område | Innehåll | Forskningsläge | Påståenden |
|---|---|---|---:|
| A | Identitet och produktversioner | Öppna frågor | 5 |
| B | Grundkonstruktion | Verifierad grund | 2 |
| C | Motor | Öppna frågor | 10 |
| D | Transmission och drivlina | Öppna frågor | 8 |
| E | Styrning och chassi | Öppna frågor | 2 |
| F | Reglage | Verifierad grund | 2 |
| G | Säkerhetssystem | Verifierad grund | 2 |
| H | Klippaggregat och redskap | Öppna frågor | 12 |
| I | Tillbehör och användning | Öppna frågor | 2 |
| J | Underhåll | Öppna frågor | 1 |
| K | Reservdelar | Öppna frågor | 4 |
| L | Begagnat och köpråd | Öppna frågor | 1 |
| M | Vanliga frågor | Öppna frågor | 2 |

**Viktigt:** `verified` avser det område som registret granskat; det är inte automatiskt bevis att allt tänkbart inom ämnet är känt. Mängden påståenden mäter inte täckningsgrad.

## Svåra, öppna gränser
1. Koppla exakt produktnummer till motor Model/Type/Code och dess servicevärden.
2. Belägg transmissionsmodell/variant och eventuella nivå- eller oljevärden i primärkälla.
3. Kartlägg varje klippaggregats kompatibilitet och eventuellt monteringskit per produktnummer.
4. Ta fram källposition för varje publicerad teknisk siffra, serviceintervall och reservdelsreferens.
5. Verifikation av tillbehör, säkerhetsvillkor och eventuella varianter av styr-/reglagesystem.
6. Femte reservdelsvarianten 13-2729-35 behöver granskas för motor, drivning och aggregat innan versionskapitlet skrivs om.
7. Motoroljebyte 5/50 timmar, tändstift RC12YC och 0,75 mm finns i maskinmanualen men måste kopplas till korrekt motorvariant innan de presenteras universellt.
8. Kontrollera om transaxel 1134-7766-01 (K46 CJ), styrwire 1134-9154-01 och PTO-rem 1134-9079-01 också förekommer på andra produktnummer; dessa tre uppgifter är endast dokumenterade här för 13-2729-35.
9. Kontrollera exakt vilka Villa 12 HST-produktnummer som godkänner 85 Combi 13-2960-14, utöver att den separata originalkatalogen tillhör READY/VILLA-plattformen.
10. Exakt B&S motorkod för 13-2729-35 kvarstår trots publicerade motor-sprängskisser; fästdelar i motorkapitlet bevisar inte modellkod.
11. Granska skillnader mellan franska 13-2729-35 (FR) och 13-2729-15 mot de enskilda delgrupperna: den märkta marknadsvarianten är inte belägg för samma komponenter.
12. Briggs & Stratton är fabrikatsbekräftat för 13-2729-15 och 13-2729-35 i STIGA-originalkatalog, men uppgifterna 21R602/21R502 har ännu inte originalverifierats på Model/Type/Code-nivå.

Resterande öppna frågor finns i `research/machines/stiga-villa-12-hst.json` och ska behållas tills de har egna källbevis.

## Konkreta acceptanskriterier för nästa artikel-PR
- Fakta som visas i artikeltexten pekar till källa **och relevant variant**.
- Varje P0-fråga är antingen löst eller märkt som tydligt avgränsad.
- Mer innehåll ska bestå av **nya fakta, tydligare felvägar och praktiska förklaringar**, inte omskrivna stycken.
- Researchgrinden går igenom utan att luckor felaktigt avskrivs.
- Bygg/test, genererad HTML samt visuell kontroll på dator/mobil går igenom.
- Publicering görs i egen PR när den nya fullständiga artikeln faktiskt är byggd och verifierad.

## Redaktionellt beslut
Det här dokumentet gör oss inte klara med Villa 12 HST 3.0. Det gör nästa utvecklingssteg granskbart och hindrar att vi råkar kalla en kort översikt för färdig djupguide.
