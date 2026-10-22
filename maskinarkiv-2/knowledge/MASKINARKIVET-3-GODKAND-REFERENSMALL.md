# Maskinarkivet 3.0 – godkänd referensmall för nya modellguider

**Beslut:** Godkänd av webbplatsägaren 2026-10-22.
**Referens:** [STIGA Villa 12 HST](https://skaraborgmaskin.se/maskinarkiv/stiga-villa-12-hst.html).
**Omfattning:** Godkännande av informationsarkitektur, läsbarhet, designriktning och balans mellan gratis modellkunskap och separata digitala guider. Det ersätter inte teknisk källkontroll för nya maskiner.

## Principer som ska återanvändas
1. En riktig kunskapssida: snabb överblick, identifiering, dokumenterade versioner, konstruktion, användning, säkerhet, underhåll, reservdelar, köpråd och relevanta FAQ.
2. Lätt att hitta: tydlig modellrubrik, kort sammanfattning, innehållsförteckning, genomtänkta H2/H3 och responsiva tabeller. Samma webbplatsheader och footer, kanonisk adress och SEO-metadata.
3. Djupet kommer från källor och praktisk förklaring, **inte** från utfyllnad eller fasta ordmål. Översikt för nybörjaren och fördjupning för den vana ägaren.
4. Varje viktig teknisk uppgift binds till **exakt modell-/produktnummer**, originalmanual, sprängskiss eller pålitlig dokumentation. Skilj tillverkarsäkrad information från generella mekaniska förklaringar. Okänt = okänt.
5. Naturligt språk; inga publika forskningsnoteringar, påhittade passformer, osäkra priser eller påståenden om ”vanliga typfel” utan stöd.
6. Bibehåll fri, faktiskt användbar information. Visa **relevant** digital guide där den hjälper, utan att avbryta säkerhetsinstruktioner eller upprepa reklambudskap.
7. Återbruks-/kontaktväg är diskret men lätt att nå.

## Vad som INTE får kopieras från Villa
- Maskinens fem PNC, motorfabrikat/-koder, transmissionstyp K46CJ, rem-/knivnummer eller serviceintervall.
- 85 Combi-referenser, tillbehör, säkerhetskretsar och kompatibilitetsantaganden.
- Villa-specifika Nunjucks-partials (`villa-depth*`, `villa-how-systems-work.njk`) – dessa körs bara för Villa.
- Villa-specifika forskningsclaims, källor, årtal eller produktbeskrivningar.
- Rubriker/kapitel som saknar relevans för den nya maskinen.

## Kapitelmall – välj efter dokumentation
| Kapiteldel | Minsta nyttiga innehåll |
|---|---|
| Översikt | Vad det är, modellens kännetecken, vem sidan hjälper |
| Versioner & identifiering | Produkt-/serienummer, årsvarianter, märkplatser, motoridentifiering |
| Funktion | Motor, kraftöverföring, styrning, reglage, aggregat/redskap efter maskintyp |
| Användning & säkerhet | Modellens arbetssätt, dokumenterade begränsningar, kontroller |
| Underhåll | Exakt manual, intervall/komponent, versionsgränser |
| Reservdelar | Rätt reservdelskatalog, bildposition, delnummer, verifierad passform |
| Felsökning | Symtom → säker första kontroll → nästa system; inga garanterade diagnoser |
| Begagnatköp | Praktisk identifierings- och provkörningskontroll |
| FAQ & källor | Frågor med verkligt värde och spårbara referenser |

## Startmall för maskinens fakta
Fyll i innan publicering. En tom uppgift ska inte fyllas med fakta från en annan modell.

```yaml
model: "[Tillverkare modell]"
slug: "[seo-vanlig-slug]"
category: "[maskintyp]"
identity:
  product_numbers: []
  serial_number_location: "Ej verifierat"
  model_years: "Ej verifierat"
engine:
  variants: []
  service_manual: "Ej verifierat"
drive:
  type: "Ej verifierat"
  variant_source: "Ej verifierat"
equipment:
  confirmed_attachments: []
service:
  manufacturer_intervals: []
parts:
  confirmed_part_numbers: []
safety:
  verified_limits: []
research:
  primary_sources: []
  secondary_sources: []
  open_questions: []
digital_guides:
  placements: []
status: "draft"
```

## Publiceringschecklista
- [ ] Källor och identifierad version stämmer för varje kritisk teknisk uppgift.
- [ ] Alla källänkar och produktlänkar har kontrollerats.
- [ ] Inga dubbletter, platshållare eller tekniska påståenden från Villa har följt med.
- [ ] Innehållsförteckning, ankarlänkar, rubriker, tabeller och bilder fungerar.
- [ ] Mobilvy och datorvy är granskade; användbart även vid smala skärmar.
- [ ] Sidtitel, meta description, canonical och interna länkar är korrekta.
- [ ] Digitala guider länkas bara när relevanta och beskrivs enligt faktisk produkt.
- [ ] Webbplatsens bygg-/testflöde är grönt och genererad HTML verifierad.
- [ ] Ägaren har fått se resultatet och beslutat om publicering.

**Viktig skillnad:** Villa 12 HST är **godkänd referens för arbetsmetod och upplevelse**. De tidigare dokumenterade öppna punkterna kring fullständig mobil-/checkout-verifiering ska inte i efterhand markeras som kontrollerade enbart på grund av referensgodkännandet.
