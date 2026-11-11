# Maskinarkivet – samlat källregister (första inventeringen)

**Inventerat 2026-10-21** från maskinregistren och tidigare forskningsgren i GitHub. Detta index är **inte** en ny faktagranskning av varje extern dokumentlänk.

## Var hittar jag all forskning?

| Tillverkare | Modeller som redan behandlats | Register |
|---|---|---|
| STIGA | Villa 12 HST, Park 16, Park 2000 | [STIGA sources.json](./stiga/sources.json), [claims.json](./stiga/claims.json) |
| Husqvarna | Rider 13, LTH151 | [Andra modeller: sources.json](./other-models-sources.json) |
| Jonsered | LT2115 | [Andra modeller: sources.json](./other-models-sources.json) |

## Inventeringsresultat

- STIGA-delregistret har **43 källposter**: ursprungliga **32** från Villa 12 HST, **6** från Park 16, samt **5** externa länkar från den äldre Park 2000-sidan. Där finns också **53** version-/källbundna claims från Villa-forskningen.
- Övriga befintliga Maskinarkivet 2.0-modellfiler gav **39 extraherade länkhänvisningar** för fyra modeller: **Park 16 (6), Jonsered LT2115 (11), Husqvarna LTH151 (4) och Husqvarna Rider 13 (18)**. Det är **35 unika URL:er** efter att dubbletter identifierats i den exporten.
- Park 16 finns i *både* STIGA-registret och källexporten för de tidigare modellfilerna, avsiktligt för spårbarhet. Därför ska dessa totalsiffror **inte summeras** som ett antal unika kontrollerade dokument.

## Källornas olika kvalitetsnivå

- **STIGA/Villa 12 HST:** separat forskningsregister med ämnen A–M, källklass, påståenden och källposition. Forskningsstatus är `needs_research`; importen till gemensamma biblioteket ändrar inte detta.
- **STIGA Park 16, Husqvarna Rider 13, Husqvarna LTH151, Jonsered LT2115:** hittade i befintliga modell-JSON:s `sources`-fält. Beskrivningar och URL:er är bevarade; deras enskilda källor har **inte** i denna import genomgått samma 13-områdesgranskning som Villa.
- **STIGA Park 2000:** fem externa länkar extraherade ur äldre HTML-artikeln; en länk kan vara företagets allmänna Park-sida, historik eller reservdelssäljare och **inte** ett fullständigt dokumentbevis för maskinens uppgifter.
- Länkar kan vara flyttade eller brutna. Att ett dokument återges av tredje part betyder inte alltid att varje påstående i artikeln är verifierat.

## Använd detta före nästa modell

1. Läs tillverkarens källregister och sök fullständigt maskin-PNC, motor-ID, aggregat-ID eller dokumentnummer.
2. Återanvänd sourceId, dokumentets relevanta avsnitt och **endast** uppgifter som gäller den nya identifierade maskinen.
3. För en ny STIGA-modell: länka till redan lagrad STIGA-källa och lägg till endast de nya källor som behövs. För Husqvarna/Jonsered kan källposterna gradvis delas upp i egna märkesregister.
4. Ange alltid exakt variant, källa och källställe för påståenden om reservdelar, motorkoder, remmar, olja och kompatibilitet.
5. Publiceringsgrinden kontrolleras separat – en existerande källlänk i biblioteket innebär inte att en ny artikel får `ready`.

## Varför ingen automatisk publicering?
Denna förändring sparar och organiserar forskning. Den uppdaterar **inte** själva maskinsidorna och skapar inte ogrundad universell kompatibilitet. Granska registerformatet innan denna PR sammanfogas.
