# Gemensamt käll- och relationsindex – Maskinarkivet 3.0

**Index – inte faktadatabas.** Allt källbelagt tekniskt innehåll lagras i befintliga forskningsregister enligt STIGA Villa 12 HST-schemat: `research/machines/<slug>.json`. Här finns bara länkar och upptäckta samband, inklusive sådant som behöver egen research. Läs [huvudregeln](../knowledge/GEMENSAM-KUNSKAPSBAS-POLICY.md).

## Aktiva maskinregister
| Maskin | Kanoniskt forskningsregister | Status |
|---|---|---|
| STIGA Villa 12 HST | [stiga-villa-12-hst.json](machines/stiga-villa-12-hst.json) | `scoped_ready`: 53 claims och kvarvarande forskningsluckor |
| Husqvarna Rider 13 | [husqvarna-rider-13.json](machines/husqvarna-rider-13.json) | `needs_research`: påbörjat, inte publiceringsgodkänt för nya ändringar |

| MTD 13BH670F062 | [mtd-13bh670f062.json](machines/mtd-13bh670f062.json) | `needs_research`: 27 källbundna claims; komponent- och revisionskontroll återstår |

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
