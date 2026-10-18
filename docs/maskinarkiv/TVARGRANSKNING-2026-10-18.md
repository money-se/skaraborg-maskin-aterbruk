# Maskinarkivet – tvärgranskning av tre kandidatartiklar
Datum: 2026-10-18
Omfattning: read-only jämförelse av tre aktuella feature-grenar. Inga ändringar på dessa grenar, ingen merge till main.

## Versionslåsta underlag
- Husqvarna LTH151: feature/maskinarkiv-husqvarna-lth151, blob 5850fd54fb045c43ab34c0d13c26e51fe2001d34
- STIGA Park 16: feature/maskinarkiv-stiga-park-16, blob 09f1a528430e2280b6196ae9920ab0939d025e3c
- Jonsered LT2115: feature/maskinarkiv-jonsered-lt2115, blob 15561985073bcfec02818aad68a73fdd36a77046

## Strukturell jämförelse
| Kontroll | LTH151 | Park 16 | LT2115 |
|---|---|---|---|
| HTML-sektioner | 14 | 16 | 22 |
| HTML-tecken (cirka) | 34 619 | 42 171 | 42 768 |
| Dubbeldefinierade id | Inga funna | Inga funna | Inga funna |
| Ankarlänkar utan existerande id-mål | Inga funna | Inga funna | Inga funna |
| Unik canonical under /maskinarkiv/ | Ja | Ja | Ja |
| Relativa partial-sökvägar från undermapp | Ja | Ja | Ja |
| Responsiv CSS finns | Ja | Ja | Ja |
| aria-modal-dialog finns | Ja | Ja | Ja |
| Renderad browser- och mobiltest | Ej utförd | Ej utförd | Ej utförd |

Detta är statiska text-/strukturanalyser och är INTE en fullständig HTML-, Javascript- eller tillgänglighetsvalidering.

## Faktaunderlag och granskningsrisker
**LTH151:** Skiljer versionsberoende Kohler SV470, Hydro-Gear T2, däck och reservdelar för 96041001903 från andra varianter. Den officiella Husqvarna-IPL-portalen är huvudlänk. Andra produktnummer behöver samma versionsspecifika nivå innan man utökar specifikationstabeller.

**STIGA Park 16:** Flera versioner av 16 HST och 16 HST Pro redovisas. Primära IPL-länkar mot view.stiga-store.com finns för 13-1458-15, 13-1458-14, 13-5419-12 samt 13-1441-18. Granska särskilt att K110, motor och styrsystem alltid binds till rätt produktnummer/version och att namnet "Park 16" inte används som universell kompabilitetsgaranti.

**Jonsered LT2115:** Många sekundära manualspegel-länkar utöver IPL-källor. Prioritera en verifierbar ursprunglig tillverkar-IP L framför återförsäljartext för delnummer och tekniska specifikationer. Överlämningen på Jonsered-grenen noterar källkonflikt i IPL 544 46 75-01: 96011018100 jämfört med 96011011800/960 11 01-812. Behåll avvikelsen synlig och försök inte automatiskt 'fixa' numret. Komponentuppgifter för LT2115, LT2115A, LT2115CM och LT2115CMA ska hållas åtskilda.

## Gemensamma publiceringsgrindar
1. Källkontroll per produktnummer, speciellt motor, hydrostat och aggregat.
2. Kontroll av externa originalmanualer, DOI/filförväxlingar och länkar i källfönster.
3. Riktigt webbläsartest av desktop + mobil; intern navigation, källmodal med tangentbord, tabeller, header/footer.
4. Oberoende HTML/JS-validation samt kontroll att inga 404-länkar eller felaktiga canonical finns.
5. Endast efter separat godkännande: integrera genom att föra in modellsidor på en ny integrationsgren, uppdatera maskinarkivet.html och sitemap.xml samordnat, och PR för review. Ingen merge till main utan användarens uttryckliga godkännande.

## Status
Alla tre artiklar existerar i respektive branch, men är ännu inte slutgodkända. Rapporterna innebär inte att externa länkar provnavigerats eller att sidorna fungerar i riktig webbläsare. Ingen huvudgrensändring har gjorts.
