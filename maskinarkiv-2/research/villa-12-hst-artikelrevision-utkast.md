# Villa 12 HST – planerad artikelrevision (arbetsutkast, inte för publicering)
Datum: 2026-10-21. Forskningsstatus: `needs_research`. Materialet nedan är ett redaktionellt förslag och får inte förväxlas med en genomförd teknisk godkännandegranskning.

## 1. Ny ingång: Hitta rätt Villa på tre minuter
**Föreslagen ingress:** ”STIGA Villa 12 HST är inte en enda oförändrad maskin. Innan du beställer motor-, transmissions- eller klippaggregatdelar behöver du veta exakt vilken maskinversion du har. Börja med produktnumret på maskinens skylt, fotografera motorns Model/Type/Code och leta efter klippaggregatets egen beteckning.”

**Interaktivt upplägg i framtida artikel:** tre enkla ingångar – *Jag vill identifiera min maskin*, *Min maskin fungerar inte*, *Jag funderar på att köpa en begagnad*. All teknisk information finns kvar i kapitel längre ned; ingångarna är enbart genvägar.

## 2. Versionsöversikt – ersätt nuvarande fyra poster
Den befintliga artikeln listar fyra maskinversioner. Forskningsjournalen listar fem, inklusive den franska versionen. Föreslagen tabell nedan ska publiceras först när forskningsgrinden tillåter redaktionella modelländringar:

| Produktnummer | Modellår enligt katalog | Motor enligt underlag | Transaxel enligt reservdelslista | Förväxla inte med |
|---|---|---|---|---|
| 13-2727-13 | 2009 | GGP WM 12,5, A | Ännu inte individuellt fastställd | 85 Combi-aggregatets separata nummer |
| 13-2727-14 | 2010 | GGP WM 12,5, B | Ytterligare individuell kontroll behövs | Motorns egna serienummer |
| 13-2729-14 | 2010 | Briggs 21R502, C (preliminärt) | K46 CJ 1134-7766-01, B | Fullständigt Briggs Type/Code saknas |
| 13-2729-15 | 2011–2012 | Briggs-fabrikat A; 21R602 endast C | K46 CJ 1134-7766-01, B | 13-2729-35 |
| 13-2729-35 | 2011–2012 | B&S-motoravsnitt, A | K46 CJ 1134-7766-01, B | Märkt FR i originalkatalog |

A betyder identifierad i STIGA:s originalkatalog; B betyder separat kompletterande reservdelsbelägg; C anger att uppgiften endast är preliminär. Utan motsvarande motoridentitet på just maskinen gäller inte C-uppgiften som reservdelsinstruktion.

## 3. Motoravsnitt – dela upp på maskin och motor
- **Maskinen:** produktnummer avgör vilken maskinversion tillverkarens lista avser.
- **Motorn:** motorns egna Model/Type/Code avgör rätt motorhandbok, filter, tändstift och komponenter. Att en reservdelssida anger 21R502 eller 21R602 som *förväntad* motor är inte tillräckligt för universella servicevärden.
- **Felsökning:** beskriv skillnaden mellan startmotorn reagerar inte, motorn drar runt men startar inte och motorn startar men stannar. Kontrollera normala säkerhetsvillkor, bryt strömmen innan arbete vid skärande eller roterande delar och koppla aldrig bort skydd för provning.

Fördjupad felträdsgrafik och motorspecifika värden byggs först när motorvarianterna och tillhörande instruktioner är dokumenterade.

## 4. Service – särskilj maskinmanualens värden och motorvarianter
Källan 8211-0038-90 anger bland annat däcktryck 0,4 bar fram och 1,2 bar bak (8.3), motoroljebyte efter första 5 timmarna och sedan normalt var 50:e timme eller säsongsvis (8.4) samt kontroll av styrning efter 5 timmar och var 25:e timme (8.7). Vid kraftig belastning eller värme anger manualen tätare oljebyten.

**Varning i tabellen:** `Motorolja ≠ hydrostatolja`. Angivna motorvärden är **inte automatiskt tillämpliga på alla Briggs-utföranden**. Lägg aldrig in ”K46 CJ ska fyllas med X liter Y-olja” utan anvisning från rätt originalkälla. Särskilj maskinmanual och motorns servicemanual.

## 5. Klippaggregat – separat identitet
De originaldokumenterade **85 Combi**-katalogerna `13-2960-13` respektive `13-2960-14` representerar aggregatversioner, inte maskinernas identitetsnummer. Dokumentet `8211-7000-10` är en aggregatmanual. Ingen generell kompatibilitetslista får visas innan den jämförts med maskinens produktnummer, redskapsfäste och eventuella remvarianter.

## 6. Reservdelar – tre-fotoprincipen
För bästa möjliga matchning: 1) maskinens skylt, 2) motorns märkning, 3) klippaggregatets märkning och skadade delens foto. De tre reservdelsnumren för FR-versionen som kartlagts i research-journalen ska inte presenteras som universella. Vid beställning måste även revisionsnummer och mått kontrolleras.

## 7. Källor och källställen
- STIGA Villa-manual 8211-0038-90: främst avsnitt 2.3, 8.3, 8.4, 8.7, 8.9–8.12.
- STIGA 2009 parts catalogue 8211-3401-09: översikt F-3.
- STIGA 2011/2012 Villa HST parts catalogue: modellförteckning och MOTOR/ENGINE (B&S).
- STIGA 85 Combi 13-2960-14 parts catalogue: aggregatidentitet.
- Sekundära reservdelsscheman till 13-2729-14, 13-2729-15 och 13-2729-35: K46 CJ.
- Briggs & Strattons identifierings- och manualsökning: motorns Model/Type/Code.
Se `stiga-villa-12-hst-review-20261021.md`, `villa-12-hst-versionsmatris.md` och `research/machines/stiga-villa-12-hst.json` för käll-ID och öppna begränsningar.

## 8. Publiceringsvillkor
Artikeln **ändras inte i PR #27**, eftersom den strikta forskningsgrinden ännu ska blockera ändrat modellinnehåll. Först när alla obligatoriska forskningsområden är ordentligt dokumenterade och manuellt granskade får `needs_research` ändras till `ready`. Arbetsutkastet är inte ett sätt att kringgå grinden.
