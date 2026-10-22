# Gemensamt käll- och relationsindex – Maskinarkivet 3.0

**Index – inte faktadatabas.** Allt källbelagt tekniskt innehåll lagras i befintliga forskningsregister enligt STIGA Villa 12 HST-schemat: `research/machines/<slug>.json`. Här finns bara länkar och upptäckta samband, inklusive sådant som behöver egen research. Läs [huvudregeln](../knowledge/GEMENSAM-KUNSKAPSBAS-POLICY.md).

## Aktiva maskinregister
| Maskin | Kanoniskt forskningsregister | Status |
|---|---|---|
| STIGA Villa 12 HST | [stiga-villa-12-hst.json](machines/stiga-villa-12-hst.json) | `scoped_ready`: 53 claims och kvarvarande forskningsluckor |
| Husqvarna Rider 13 | [husqvarna-rider-13.json](machines/husqvarna-rider-13.json) | `needs_research`: påbörjat, inte publiceringsgodkänt för nya ändringar |

## Sidofynd att koppla till egna maskinregister
| Modell/komponent | Källa som upptäckts | Källa eller register | Återstår |
|---|---|---|---|
| Husqvarna Rider 11 | Gemensam Husqvarna-manual för Rider 11/13 med Bio-versioner | [Rider 13-registret](machines/husqvarna-rider-13.json) (claim `rider13-2003-shared-owner-manual`) | Eget produktnummer och variantbundet innehåll |
| Husqvarna Rider 11 Bio | Samma originalmanual | [Rider 13-registret](machines/husqvarna-rider-13.json) (claim `rider13-2003-shared-owner-manual`) | Egen version och komponentkontroll |
| Husqvarna Rider 16 | Verkstadshandbok som omfattar flera Rider-familjer | https://www.manualslib.com/manual/716829/Husqvarna-Rider-13.html | Exakt utförande och vilka avsnitt som avser det |
| K46 i Rider 13 Bio | Versionsspecifik reservdelsritning | [Rider 13-registret](machines/husqvarna-rider-13.json) (claim `bio-2003-k46`) | Inga slutsatser om andra maskiners K46-varianter utan egna belägg |

## När nytt material hittas
1. Sök först i `research/machines/` och återanvänd redan registrerade originaldokument.
2. Registrera claim, relevant produktnummer, source-ID, locator, kvalitetsgrad och osäkerheter i **den berörda maskinens JSON-register**.
3. Lägg hit endast ny relation/pekare som gör andra maskiner lättare att hitta, inte en andra kopia av tekniska påståenden.
4. Sidofynd utan eget register får finnas här som **researchuppslag**, aldrig som verifierat tekniskt underlag eller publiceringsbeslut.
5. Varje ny artikel måste separat uppfylla projektets research-grind och granskningsregler.

## Motorforskning – tillverkaroriginal som väntar på maskinbunden koppling (2026-10-22)

Dessa är **källpekare/identifieringsuppslag**, inte motorpåståenden som får användas i maskinartiklar innan rätt motormärkning och maskinvariant har styrkts.

| Motorfamilj | Originalkälla | Nästa verifieringssteg |
|---|---|---|
| Briggs & Stratton | [Briggs motoridentifiering](https://www.briggsandstratton.com/en-us/support/faqs/engine-codes-model-numbers), [manualer/IPL](https://www.briggsandstratton.com/en-gb/support/manuals) | Utgå från exakt Model/Type/Code för monterad motor; första maskinbundna claim finns i [Rider 13-registret](machines/husqvarna-rider-13.json) (`rider13c-briggs-identification-procedure`) |
| Honda allmänna småmotorer | [Honda Engine Type Identification](https://engines.honda.com/support-and-service/engine-type-identification), [ägarmanualer](https://engines.honda.com/support-and-service/owners-manuals/), [verkstads-/reservdelsmanualer](https://engines.honda.com/support-and-service/shop-manuals) | Honda USA anger att Type Code finns nära motorns serienummer, upp till fyra tecken, samt att serienumret har bokstavsprefix och sju siffror. Identifiera exakt motor och kontrollera europeisk dokumentutgåva innan maskinbundet claim skapas |
| Kohler äldre Magnum/Command | [Kohler Magnum M8–M16 originalverkstadshandbok TP-2203-A](https://resources.kohler.com/power/kohler/enginesUS/pdf/tp_2203_a.pdf), [Kohler Command CV11–CV16 originalverkstadshandbok TP-2339-D](https://resources.kohler.com/power/kohler/enginesUS/pdf/tp_2339_d.pdf) | Identifiera motorns modell, specifikationsnummer och serienummer; jämför relevant manualrevision och maskinkoppling, inte bara hästkraftsnamn |

Originalmanualernas exakta serviceuppgifter läggs i kanoniska maskinregister först när variant/motorpar är verifierat. Kohler-PDF:ernas identifieringsfigurer behöver separat visuell genomgång före detaljerade claims. Briggs kodnyckel (revision 2/06) är visuellt kontrollerad på [originalets PDF-sida 1](https://www.briggsandstratton.com/hubfs/Briggs%20and%20Stratton/EMEA/FAQs/pdfs/Numerical_Designation_System.pdf) och tillhör [Rider 13-registret](machines/husqvarna-rider-13.json), claim `rider13c-briggs-type-code-meaning`.
