# Villa 12 HST – forskningsgrindens blockerare (2026-10-21)

**Resultat:** EJ REDO. Den publicerade maskinartikeln har inte ändrats; detta är en saklig release-audit av forskningens nuvarande register, inte ett frisläppningsbeslut.

## Maskinellt kontrollerad registertäckning
Granskningen är gjord mot `research/machines/stiga-villa-12-hst.json` och `scripts/check-research.mjs` i PR #27. Antal A/B-påståenden per område före denna audits eventuella senare tillägg:

| Område | Tillstånd efter rättelse | Antal A/B | Blockerande arbete |
|---|---|---:|---|
| A Identitet | gap | 4 | Full produkt-/revisionskoppling |
| B Grundkonstruktion | verified | 2 | Ingen maskinell blockerare, men manuell kontroll kvarstår |
| C Motor | gap | 8 | Briggs Model/Type/Code och varianternas specifika service |
| D Transmission | gap | 7 | Hydrostatens riktiga tillverkarservice och revisionsbundenhet |
| E Styrning/chassi | gap | 2 | Identifiera versionsskillnader och kontrollvärden |
| F Reglage | **gap, korrigerad** | **0** | Manualens reglageavsnitt måste källspåras som en eller flera versionsbundna A/B-poster |
| G Säkerhet | verified | 2 | Manuell granskning av påståendena mot artikel |
| H Aggregat | gap | 9 | Faktisk kompatibilitet produktnummer × aggregatnummer |
| I Tillbehör | gap | **0** | Verifiera tillåtna redskap och monteringssatser – annars skriv uttrycklig avgränsning |
| J Underhåll | gap | 1 | Versionsbundna manuella servicevärden; undvik universella Briggs-värden |
| K Reservdelar | gap | 3 | Systematisera produktnummer och remsystem |
| L Köpråd | gap | **0** | Skilj kontrollerad konstruktion från egna kontrollråd |
| M FAQ | gap | **0** | Skapa besvarade, källspårade vanliga frågor för rätt version |

**Viktig upptäckt:** F var markerat `verified` trots att inga grade A/B-påståenden fanns för området. Detta är korrigerat till `gap`. En grön `research:check` betyder inte att ett registrerat område utan påståenden är redo för release.

## Prioriterad nästa arbetsordning
1. **Sluta med små delnummer tills huvudluckorna angrips.** F, I, L och M har helt tom A/B-bevisning och behöver originalmanualanknutna, versionsmärkta påståenden.
2. **C och H är verkliga materiella spärrar.** För C krävs fysisk Briggs-märkskylt eller STIGA/Briggs dokument som kopplar exakt motorkod till produktnummer. För H krävs kompatibilitets-/monteringsanvisning som namnger såväl basmaskin som aggregat, eller tydlig avgränsning i publiceringsprotokollet som inte låtsas täcka en variant.
3. **D och J:** källidentifiera hydrostatens service och skilj från motormanualens service. Ingen oljemängd, oljekvalitet eller intervall får extrapoleras.
4. **E och K:** dokumentera vilka styrlänkar, vajrar, remmar som hör till vilket produkt-ID, och om FR-sidor avviker.
5. **Audit av forskningsjournalen:** 21 öppna lucktexter överlappar delvis, men får inte raderas utan prövning. Varje stängning måste referera till exakt påstående och originalkälla.

## Kriterier före status 'ready'
`check-research.mjs` kräver i ready-läge: (i) noll öppna luckor; (ii) alla A–M = verified; (iii) minst ett A/B-påstående för varje område; (iv) `reviewedBy` och `reviewedAt`. Dessa kriterier får **inte** uppnås genom att markera områden utan faktaunderlag eller ta bort giltiga luckor för att få grönt CI. Värdet av den manuella primärkällegranskningen måste också vara dokumenterat.

Denna audit ger ett mätbart slutmål. Först efter att dessa villkor verkligen uppfylls bör modellens JSON-artikel revideras och publicerings-PR granskas visuellt.
