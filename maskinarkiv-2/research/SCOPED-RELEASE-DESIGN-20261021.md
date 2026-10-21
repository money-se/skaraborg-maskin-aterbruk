# Förslag: publiceringsgrind för verifierat och tydligt avgränsat innehåll

**Status:** Designförslag. Ingen befintlig research-kontroll ändrad.

## Problemet
Nuvarande `research:release` kräver A–M samtliga `verified`, noll öppna forskningsluckor, och human review. Det passar en heltäckande verkstadshandbok, men låser en användbar modellartikel om detaljer utanför det som faktiskt publiceras inte går att styrka (t.ex. exakta Briggs Type/Code och varje aggregatkombination).

## Två nivåer med oförändrad sanning
1. **Fullständig teknikrevision** (`ready`): den befintliga hårda grinden gäller fortsatt.
2. **Källavgränsad artikel** (`scoped_ready`, införs endast efter egen kodändring/test): alla **publicerade** tekniska påståenden kontrollerade med sourceId, variant, locator och A/B eller tydlig som osäker markerad C. Osäkra generella motor-/aggregatvärden utesluts, och samtliga existerande forskningsluckor förblir i registret som `out_of_scope`-poster, aldrig förklarade som bekräftade.

### Minimikrav för scoped_ready
- Obligatoriskt A–M-register kvar och minst A/B-grund för varje område som sidan faktiskt avhandlar.
- Whitelist av publicerade tekniska claims, med koppling till exakta textställen.
- Obligatorisk negative-claims-lista för saker som **inte** får stå som verifierade: alla Briggs Model/Type/Code, generell passform för de tre 85 Combi-PNC, transmissionsservice oberoende av monterad enhet.
- Manuell granskning och tydligt ansvarig; reviewer/approvedAt får inte tilldelas automatiskt av AI.
- Automatisk bygg- och sidhänvisningskontroll, HTML-förhandsvisning och uttryckligt beslut om merge/publicering.

## Villa 12 HST – redan byggd innehållskandidat
`research/villa-12-hst-artikelkandidat-20261021.json` innehåller ett fullständigt utkast baserat på befintlig modell-JSON med femte versionen **13-2729-35**, tydligare motor-/deck-källbegränsningar, snabb felsökningshjälp och FAQ. Det är **avsiktligt inte** redigerat i `src/_data/machines` ännu eftersom `check-changed-research` annars ska stoppa den förändringen före godkänd grind.

## Implementeringsordning
1. Skriv testfall som visar att ett sakfel, ett oregistrerat tekniskt påstående eller en osäker generell specifikation stoppar `scoped_ready`.
2. Implementera `scoped_ready` som **ytterligare** giltig status, ej ändring av `ready`-reglerna.
3. Låt ansvarig granska text och källor, registrera faktisk granskning och godkänna negativlistan.
4. Flytta kandidatinnehållet till modell-JSON, kör `research:release`, bygg och granska HTML, publicera först efter uttryckligt beslut.

Detta förslag ger snabbare modellproduktion genom återanvändbar forskning utan att sudda ut okända fakta eller försvaga kravet på att varje publicerat påstående ska vara belagt.
