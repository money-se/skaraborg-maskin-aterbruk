# Manualinkorg – 2026-11-01 (9 nya PDF:er)

Lokal användaruppladdning: 9 PDF:er, 552 sidor. **Original-PDF:erna publiceras inte här.** Lokal fullständig CSV-inventering innehåller SHA-256 och exakta sidantal.

| Lokal fil | Verifierad dokumentidentitet | PDF-sidor | Anmärkning |
|---|---|---:|---|
| `72d6a479fe46cbd11de53f0c3c8d712908745b57e81d8ab915ec4c015b77881b.pdf` | Jonsered LT2115A IPL 2006-03, 544 40 90-01 / 96011018200 | 18 | Identisk dokumentfamilj med befintlig LT2115A-forskning; inte en ny variant |
| `33633791.pdf` | STIGA Park 2000–2007 Workshop Manual, edition 2007-03-22 | 187 | Anger uttryckligen att motorreparationer inte omfattas; tabeller identifierar modell/artikelnummer |
| `IPL_Stiga_PARK_PRO_16_13-6216-15_03_SV-EN.pdf` | STIGA Park Pro 16 13-6216-15, Season 2004 | 60 | Ej samma modell som Park 16 HST; filnamnets _03 skiljer från Season 2004 |
| `IPL_Stiga_PARK_16HST_13-1458-15_92_SV-EN.pdf` | STIGA Park 16 HST 13-1458-15, Season 1993 | 47 | Filnamnets _92 ≠ omslagets Season 1993 |
| `IPL_Stiga_PARK_16HST_13-1418-12_89_SV-EN.pdf` | STIGA Park 16 HST 13-1418-12, Season 1990 | 42 | Filnamnets _89 ≠ omslagets Season 1990 |
| `doc000039437.pdf` | Husqvarna Rider 11/13, Rider 11 Bio/13 Bio, Operator's Manual | 52 | Modellöverskridande manual; kontrollera rätt variant |
| `rider-13-2002-02.pdf` | Husqvarna Rider 13 IPL 2002-02 | 37 | TRANSMISSION s. 21: 506 98 64-01 K46 |
| `W0301001.pdf` | Husqvarna Rider 11/13/Bio/16 Workshop Manual | 72 | Technical data PDF s. 6: Rider 13 B&S 286707 och Tuff Torq K46 i tabellen |
| `tracteur_tondeuse_husqvarna_rider_rider-13_vue-eclate-liste-des-pieces_2003-01.pdf` | Husqvarna Rider 13 IPL 2003-01 | 37 | TRANSMISSION s. 33: 506 98 64-01 K46 |

## Integrerat i kanonisk forskning

`research/machines/husqvarna-rider-13.json` har kompletterats med **3 avgränsade faktaposter och 3 dokumentkällor**, knutna till:
- Rider 13 IPL 2002-02, PDF s. 21, K46 med katalognummer 506 98 64-01.
- Rider 13 IPL 2003-01, PDF s. 33, samma modell- och katalogbeteckning.
- Rider 13 verkstadshandbok, PDF s. 6, tabell för motor och växellåda (B&S 286707 respektive K46).

Detta bevisar **inte** att varje Rider 13, Rider 13 Bio, Rider 13C eller eftermonterad transmission har samma utförande. Service- och reservdelsråd måste fortfarande knytas till den faktiska maskinens identitet.

## Nästa högvärdiga forskningsinsats
1. STIGA Park 16 HST 1990 respektive 1993: granska stycklistor och artikelnummervarianter separat, återanvänd inte till Park Pro 16 2004.
2. Rider 13: komplettera källspårningen för 2002/2003 års IPL och verkstadshandbok i artikeln när granskade påståenden kan avgränsas.
3. STIGA Park 2000–2007: matcha `1.6 Technical specifications` mot rätt artikel-/produktnummer innan verkstadsvärden skrivs in.
4. Undvik att skapa ny LT2115A-faktapost för samma 2006-03 katalog utan faktiska nya fynd.
