# Maskinarkivet 3.0 – djupguide-standard (förslag)

**Status:** Arbetsstandard, inte automatiskt publiceringsgodkännande.  
**Grund:** Projektets `MASKINARKIVET-HUVUDMALL` v1.0 (2026-08-09), researchämnen A–M och nuvarande Maskinarkivet 2.0. Gäller nya och fördjupade modellguider.

## Målet
Bygg Sveriges mest användbara samlade maskinkunskap, modell för modell. En nybörjare ska hitta ett svar snabbt, medan en van ägare ska kunna gå djupare till dokument, variant, felbild och reservdel.

**Princip:** MYCKET INFORMATION + TYDLIG STRUKTUR + KÄLLKONTROLL + ENKELT SPRÅK.

## 1. Varje sida har två läslägen utan dubbel text
- **Snabbt svar:** tydlig ingress, identifieringssteg, snabbfakta och innehållsförteckning.
- **Fördjupning:** samma artikel med förklaringar, tabeller, källavgränsningar, bilder där de faktiskt lär ut något, och kapitel med stegvis diagnostik.
- På dator behålls sticky navigering; på mobil utfällbar meny, en kolumn och läsbara tabeller.
- Inte många små kort, påträngande kampanjer, upprepningar eller fluff.

## 2. Research A–M – minimum för planering, inte krav att fabricera data
A identitet/versioner; B konstruktion; C motor; D drivlina; E styrning/chassi; F reglage; G säkerhet; H aggregat/redskap; I tillbehör; J underhåll; K reservdelar; L begagnatköp; M vanliga frågor.

För varje område:
1. **Vad vet vi?** Exakta dokumenterade uppgifter, alltid med tillämpbar variant.
2. **Vad betyder det?** Begriplig förklaring och exempel i rätt kontext.
3. **Vad gör ägaren?** Säker kontroll eller åtgärd endast när källorna räcker.
4. **Vad vet vi inte?** Relevant begränsning nära påståendet, inte gömd i källarkivet.

Utelämna irrelevanta delområden med förklaring i arbetsunderlaget.

## 3. Obligatorisk källkedja
Varje teknisk uppgift med betydelse för delar, kompatibilitet eller säkerhet ska kunna spåras:
`artikelavsnitt → claim-ID → produktnummer/variant → dokument → specifik figur/sida/avsnitt → källa`.

Källstatus:
- **A:** tillverkardokument som uttryckligen gäller relevant variant.
- **B:** stark sekundär dokumentation som tydligt märks som sådan.
- **C/D:** publiceras inte som säkert tekniskt faktum; kan redovisas som osäkerhet om detta ger läsaren värde.
- Källregister är inte samma sak som verifierat innehåll; en länk kan vara funnen utan att rätt sida granskats.
- Komponentspecifika data får bara återanvändas när identiteten matchar.

## 4. Modellens fem praktiska kunskapslager
1. **Identifiering:** produkt-/serienummer, modellår, motor Model/Type/Code, aggregat-PNC, transmissionsetikett och dokumenterade variantskillnader.
2. **Förstå konstruktionen:** hur drivning, styrning, PTO, remmar, reglage och knivsystem arbetar tillsammans; pedagogiska begrepp och bilder.
3. **Felsökning efter symtom:** symtom → säker första kontroll → sannolika orsakskategorier (inte fabricerade vanligaste fel) → kontroll → möjliga åtgärder → när verkstad behövs. Skilj startmotor, motorstart, framdrivning och klippfunktion.
4. **Service och reservdelar:** tabeller med intervall, enheter, fullständigt artikelnummer, dokumentrev, variant och uttryckliga undantag. Motor- och transaxelservice blandas aldrig ihop.
5. **Begagnat, ägande och återbruk:** praktiskt provkörningsprotokoll; vanliga felkostnader bara med belägg; återbrukskontakt tydlig men diskret.

## 5. Omfattning och publiceringsbeslut
- Normal ambition för välbelagd djupguide: ungefär **6 000–10 000 faktabärande ord**, men detta är **inte** ett publiceringsvillkor. Kortare om underlaget inte motiverar mer; ingen utfyllnad.
- Research först, disposition sedan, artikel därefter.
- `scoped_ready` innebär enbart att angivet offentligt innehåll kan stödjas; öppna researchluckor är kvar, inte plötsligt lösta.
- Ingen självgodkännande AI-granskning räcker som oberoende slutkontroll.
- Ny information publiceras först när texten, tillhörande claim-ID och variantgräns är granskade.

## 6. Kvalitetsgrind före merge
- Researchregister A–M, samt lista på kvarvarande luckor.
- Faktatabell med källhänvisningar för motor, transmissionsdelar, remmar och säkerhetsvärden.
- Giltig HTML utan block-inbakade `<section>`-taggar; inga brutna ankar-ID, länkar eller rubriknivåer.
- Visuell granskning av desktop och mobil, särskilt navigering, kod-/PNC-strängar och läsbara tabeller.
- Test av samtliga digitala guidelänkar och deras avsnitt; annonser får aldrig störa kunskap.
- Granska faktisk genererad `maskinarkiv/*.html` efter publiceringsflödet; grön PR räcker inte ensam.
- Dokumentera granskare, datum, tydliga undantag och förändring sedan föregående version.

## 7. Skalning och framtida intäkter
- Börja med den kvalitetssäkrade Villa 12 HST och bygg återanvändbara tillverkar- och komponentbibliotek.
- Nya modeller återanvänder **källor**, inte påstådda passformer.
- Mät organisk söktrafik, sökfrågor, läsning, återbesök och relevanta företagskontakter innan annonsbeslut.
- Reklam/affiliatelänkar i framtiden ska vara tydligt märkta och hållas åtskilda från redaktionella rekommendationer. Inga garanterade intäkter eller rankingpåståenden.
- Målet är långsiktigt hög trovärdighet, inte flest genererade sidor på kortast tid.
