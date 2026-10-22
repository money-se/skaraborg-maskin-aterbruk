# Utvecklingskarta – Skaraborg Maskin & Återbruk
**Arbetsutkast v1.0 • 2026-10-22 • Planeringsunderlag – inga ändringar av webbplatskod**

## 1. Vad som faktiskt finns
Källa: GitHubs `main`-träd (rekursivt), `sitemap.xml`, `sitemap-annonser.xml`, `sitemap-tavlingar.xml`, `sitemap-veckoblogg.xml`. Jämfört med projektets masterstruktur v1.0 (2026-08-07), webbplatsspecifikation v1.2 och aktuell-status v1.2. **Projektfilerna är äldre än det nuvarande GitHub-läget och får inte användas som automatisk beskrivning av vad som saknas.**

- **330** filer totalt i GitHub-trädet.
- **203 HTML-filer**, varav **69** listas i en av fyra sitemap-filer och **134** inte listas där. Sitemaps är inte ett fullständigt mått på vad som kan vara publikt eller indexerat.
- **27** Nunjucks-mallar, **8** Python-filer och **20** GitHub Actions-workflows.
- Den bifogade filen `SIDINVENTERING-2026-10-22.csv` har en rad för **varje HTML-fil**. Kategorisering och åtgärdsförslag är preliminära; full individuell sidgranskning och Search Console har **inte** utförts för alla 203 sidor.

## 2. Klassificering av HTML-filer
| Område | Filer | I sitemap | Utanför sitemap |
|---|---:|---:|---:|
| Lokala tjänstesidor | 94 | 9 | 85 |
| Förhandsvisning / äldre version | 16 | 0 | 16 |
| Dödsbo & guider | 16 | 15 | 1 |
| Administration / system | 13 | 0 | 13 |
| Ortsnav | 13 | 13 | 0 |
| Köp, återbruk & tjänster | 12 | 4 | 8 |
| Företagslösningar | 9 | 5 | 4 |
| Aktuellt, tävlingar & projekt | 8 | 6 | 2 |
| Maskinarkivet | 7 | 6 | 1 |
| Försäljning & annonser | 6 | 5 | 1 |
| Övergripande / stöd | 5 | 5 | 0 |
| Guider / övrigt | 4 | 1 | 3 |
| **Totalt** | **203** | **69** | **134** |

**Tolkning:** Antalet HTML-filer är inte antalet kvalitetsgranskade SEO-sidor. Äldre lokala tjänstesidor, tekniska administrationssidor och förhandsvisningar ska inte automatiskt in i sitemap.

## 3. Målstruktur – fyra huvudben
Masterstrukturen delar webbplatsen i A. **Sälja/ge/kontakta**, B. **Maskinkunskap**, C. **Till salu**, D. **Levande innehåll och varumärke**. Dessa är besökarvägar, **inte** ett beslut om att alla ska bli synliga huvudmenyposter direkt.

| Besökarbehov | Föreslagen huvudansvarig sida som redan finns | Kompletterande befintliga sidor | Beslut som återstår |
|---|---|---|---|
| Sälja till företaget | `kop-maskiner.html` | `salja-maskin-skaraborg.html`, relevanta lokala sidor, `sa-funkar-det.html` | Bestäm om rubriken ska heta ”Sälj till oss” utan att skapa dublett-URL |
| Ge utan ersättning | `ge-till-aterbruk.html` | `aterbruk.html`, `gratis-aterbrukshamtning-hjo.html` | Skilj mottagande/uppköp från fri bortforsling; godkänn hubbroll |
| Dödsbo och utrensning | `dodsbo-utrensning.html` | Ortssidor och guider | Tydliggör gränsen mot komplett bohagstömning |
| Företagsförfrågningar | `foretag.html` | `foretagsforfragan.html`, `overskottslager-foretag.html`, `maskinavveckling-foretag.html` m.fl. | Avgör vilka icke-sitemap-sidor som ska ingå |
| Maskinkunskap | `maskinarkivet.html` | Modellguider i `maskinarkiv/`, äldre felsöknings-/värderingsguider | En gemensam modellmall, verkliga källor, tydlig ingång till kontakt |
| Till salu | `till-salu.html` | `annonser.html`, `tradera.html`, `shopify.html` | Skilj aktuella maskiner, Tradera och eventuell separat merch |
| Tävlingar | `tavlingar.html` | `tavlingar/`, `skank-maskin-manadens-maskin-hjo.html` | Håll regelverk, aktiva tävlingar och arkiv åtskilda |
| Aktuellt / vi söker | `vi-soker.html` | `veckan-hos-oss.html`, `projekt.html` | Byt generiskt innehåll mot verkligt uppdaterade behov/projekt |
| Lokal närvaro | `hjo.html` och 12 andra ortsnav | 11 etablerade Hjo-sidor; äldre tjänstesidor i fler orter | Följ Hjo som kvalitetsreferens, men skapa inte ortskopior |
| Förtroende & stöd | `om-oss.html`, `faq.html`, `kontakt.html` | `sa-funkar-det.html` | Behåll konsekventa uppgifter och tydliga CTA |
| Startsida | `index.html` | Alla hubbar | **Vänta med ombyggnad** tills ansvar, navigation och innehållskällor är beslutade |

**URL-princip:** Nuvarande fungerande adresser behålls som utgångspunkt. Masterdokumentets skisser som `/salj-till-oss/` eller `/maskinarkiv/` är **framtida förslag**, inte anledning att skapa dubletter eller flytta kanoniska sidor utan analys.

## 4. Strategiska observationer
1. **Hjo är färdig referens för 11 sidor.** Utforma sidkategorierna därifrån, inte genom att mekaniskt göra 11 sidor i varje ort.
2. **85 äldre lokala tjänstefiler ligger utanför sitemap.** Utred publiceringsstatus, unik nytta, innehållslikhet, länkar och canonical **innan** någon sådan sida indexeras, tas bort eller omdirigeras.
3. **Hubbkandidater finns redan men ligger utanför sitemap:** `ge-till-aterbruk.html`, `vi-soker.html`, `projekt.html`. `projekt.html` beskriver ännu framtida projekt; publicera inte påstådda case utan verkligt material.
4. **Teknisk särskiljning behövs:** HTML för admin/test, förhandsvisningar och `maskinarkiv-2/preview/` är **inte** vanliga besökarsidor. Kontrollera åtkomst och `noindex` där relevant, men ändra inte osedda autentiseringsflöden.
5. **Automatiskt genererade sidor har egna källor.** `.github/workflows/competition-seo.yml` kör schemalagt varje timme och regenererar `tavlingar/` med `scripts/generate_competition_seo.py`. Därför kan manuella rättningar av de tre tävlingsartiklarna från fas A **skrivas över**. Ändringar måste in i generatorn, och genererad HTML ska testas efter körning. Annons- och veckobloggarkiv genereras också.
6. **Ytterligare canonical-avvikelse:** `dodsbo-glom-inte-garaget.html` finns faktiskt men pekar på obefintliga `e-garaget.html`. Detta är inte samma fil som de tre länkarna som rättades i fas A. Avgör om guiden ska användas och korrigera canonical till avsedd existerande URL.
7. **Header/footer:** `partials1/header.html` och `partials1/footer.html` finns. Godkända Hjo-sidor har identiska inbäddade kopior efter tidigare visningsfix. Framtida lösning bör byggas och testas samlat, inte tillbaka till skör JS-injektion utan fallback.
8. **Ingen bred SEO-masspublicering** av de 134 filerna utanför sitemap. Det krävs per-sida-beslut om värde, ägarskap och mål.

## 5. Föreslagen arbetsordning och stoppunkter
**Etapp 0 – Nu: besluta arkitekturen (enbart dokument).**
- Godkänn fyra huvudben, sida som ansvarar för varje avsikt och val av befintliga hubbar.
- Besluta status för överlappande URL:er: behåll / förbättra / slå ihop efter kontroll / redirect efter kontroll / internt.
- Välj mått: relevanta förfrågningar per besökarväg, inte rått sidantal.

**Etapp 1 – Säkra innehållskällorna.**
- Reparera tävlingsgeneratorn i källfil i stället för att rätta genererad HTML gång på gång.
- Utred och rätta canonical för `dodsbo-glom-inte-garaget.html` efter beslut om dess URL.
- Inventera genererade lokala tjänstesidor och beslut om versionsägarskap.

**Etapp 2 – Kärnflödet för relevanta förfrågningar.**
- Gör `kop-maskiner.html`, `ge-till-aterbruk.html`, `aterbruk.html` och `foretag.html` till tydligt avgränsade hubbar.
- Lägg in verkliga villkor och konsekvent underlag: bilder, ort, skick, modell, mängd och åtkomlighet.
- Länka naturligt mellan de relevanta delarna, men rör inte startsidans större design ännu.

**Etapp 3 – Lokal modell och utbyggnad.**
- Pilotgranska en ort utöver Hjo (t.ex. Tibro): befintligt ortsnav, äldre undersidor och verkliga lokala sökbehov.
- Först därefter bestäm unika tjänstesidor, internlänkar, canonical och sitemap.

**Etapp 4 – Kunskap och återkommande innehåll.**
- En gemensam publiceringsprocess för Maskinarkivet med källgranskning och relaterade värderings-/felsökningsguider.
- `vi-soker.html`, `projekt.html`, tävlingar och annonser får faktiska uppdateringsansvariga och innehållskällor.

**Etapp 5 – Huvudnavigation och sist ny startsida.**
- När hubbarna fungerar, gör ändringar i navigation och header/footer med regressionstester för Hjo och arkivet.
- Designa sedan startsidan som ingång till de färdiga flödena.

**SEO-kontroll genom hela arbetet:** Sökintention, unik användarnytta, CTA, canonical, internlänkar, sitemap, robots, mobil och Search Console. **Detta planeringsdokument verifierar inte Google-indexering eller konverteringsutfall.**

## 6. Vad som uttryckligen inte görs nu
- Ingen kod på publika sidor ändras i denna planerings-PR.
- Ingen förhandsvisning eller adminfil läggs automatiskt i sitemap.
- Inga nya orts-/modellsidor skapas nu.
- Ingen redirect, flytt eller radering av befintliga URL:er beslutas utan individuell genomgång.
- Ingen ombyggnad av startsidan, headern eller footern ännu.

## 7. Beslut att få godkända före genomförande
1. **Föreslagen hubbstruktur:** `kop-maskiner.html` (sälj), `ge-till-aterbruk.html` (ge bort), `maskinarkivet.html` (kunskap), `till-salu.html` (säljsidan), `tavlingar.html` och `vi-soker.html` (aktuellt).
2. **Konsekvent prioritet:** fler relevanta affärsförfrågningar före fler SEO-URL:er.
3. **Fortsättning:** börja med generatorberoenden och de viktigaste hubbarna, inte med startsidan.

---
*Förhandsklassificeringen av 203 HTML-filer finns i `docs/SIDINVENTERING-2026-10-22.csv`. Den är ett beslutsunderlag, inte ett beslut att publicera, ta bort eller omdirigera någon sida.*
