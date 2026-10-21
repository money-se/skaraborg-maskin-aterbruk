# Maskinarkivet – obligatoriskt forskningsprotokoll (v2)
Bygger vidare på projektets MASKINARKIVET-HUVUDMALL v1.0 (2026-08-09). Den godkända Villa 12 HST-layouten förblir designreferens men **godkänd layout betyder inte godkänd forskning**.

## Fyra separata godkännanden
1. **Research:** identifierade produktversioner, primärkällor, motor-/transmissions-/aggregatdata, rätt service och reservdelar. Följ ämnesområdena A–M i huvudmallen. Saknas underlag: dokumentera luckan.
2. **Innehåll:** modellen får pedagogiska, versionsbundna förklaringar, symptomguider och köpråd; fakta respektive egna kontrollförslag skiljs åt.
3. **Design:** godkända navigationer, layouter, tillgängliga tabeller, CTA och centrala Shopify-guidekort.
4. **Teknik:** byggning, interna länkar, källreferenser, navigation och mobil förhandsgranskning.

## Faktaklassning (oförändrad från huvudmallen)
A: direkt belagd i primärkälla. B: stark kompletterande källa. C: sannolik men ofullständigt styrkt, får endast visas som osäker. D: okänd, får inte publiceras som fakta.
Varje betydelsefull teknisk siffra eller kompatibilitetsuppgift ska ha käll-ID, modellvariant och källställe (sidnummer eller namngivet avsnitt/figur, där det går att fastställa). **Ange inte påhittade sidnummer.**

## Maskinell forskningsgrind
Forskningsregister ligger i `research/machines/<slug>.json`. Varje register har:
- `status`: `needs_research` eller `ready`
- `topics`: alla A–M, med `verified` eller `gap` samt motivering
- `sources`: käll-ID, nivå, URL och dokumentidentitet
- `claims`: variantbundet faktapåstående, A–D, källa och lokalisering
- `gaps`: öppna frågor

`npm run research:check` kontrollerar att registret är välformat och att en sida **inte felaktigt märks färdig** utan stöd. `npm run research:release -- <slug>` blockerar leverans om forskning inte uppfyller kraven. Det är en **kontroll av spårbarhet och fullständighet**, inte ett bevis att ett påstående i manualen är sant. Manuell källläsning krävs fortfarande.

## Obligatorisk granskningsrutin
1. Research och versionsidentifiering innan ny modell kodas.
2. Registrera källor och påståenden i forskningsregistret.
3. Följ de 13 ämnena A–M; skriv `gap` om belägg saknas, inte ett gissat svar.
4. Manuell primärkällegranskning och teknisk kontroll, samt kontroll av faktatäckning i artikeln.
5. Kör build, check, audit och research:check. Inför publicering måste research:release passera för ändrad modell.
6. Granska HTML visuellt, inklusive mobil och verkliga Shopify-omslag.
7. Användaren godkänner PR/publicering. Automatiska gröna byggtester ensamma är inte ett forskningsgodkännande.

## Befintliga modeller
Äldre sidor granskas successivt; en gammal godkänd design får inte automatiskt status `ready`. Villa 12 HST är nu uttryckligen `needs_research` tills motor-/variantkopplingar, service, kompatibilitet, reservdelsnummer och primärkällornas sidspårning är tillräckligt dokumenterade.
