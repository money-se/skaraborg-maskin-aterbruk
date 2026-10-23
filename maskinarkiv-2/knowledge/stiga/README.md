# STIGA – gemensamt källregister för Maskinarkivet

Detta är det **återanvändbara källbiblioteket** som ska öppnas **innan forskning om en ny STIGA-modell**. Biblioteket ligger fristående från modellartiklarna. Det är en kunskapsbas, **inte** en lista över delar som säkert passar alla modeller.

## Filer

- [sources.json](./sources.json) – källförteckning med ID, titel, dokumentnummer, källa, URL, kategori, hänvisning till tidigare påståenden och vilka maskiner källan redan använts till.
- [claims.json](./claims.json) – 53 fakta-/kontrolluppgifter från Villa 12 HST, med grade A–D, variant, sourceId, locator och explicit återanvändningsregel.
- [NY-MODELL-ARBETSGANG.md](./NY-MODELL-ARBETSGANG.md) – sök-, gransknings- och publiceringsrutin.
- Ursprunglig forskningsfil i PR #27: `maskinarkiv-2/research/machines/stiga-villa-12-hst.json`.

**Startläge 2026-10-21:** 43 källposter och 53 källkopplade påståenden, importerade från Villa 12 HST-forskningen. Biblioteket är **inte** en systematisk inventering av alla STIGA-manualer eller maskinserier. Vi utökar löpande till Villa, Park, Ready, Estate, Tornado, motorsågar och andra produktfamiljer först när de undersöks. Varje ny maskin ska kunna tillföra nya källor och återanvända befintliga käll-ID.

## Vad betyder registrerade källor?

Källorna har `tier`: **1** primärkälla (tillverkaroriginal, även om den nås via tredje part), **2** kompletterande reservdelshandlare/sekundärkälla, **3** svagare underlag. Faktapåståenden har `grade`: A direkt originalbelägg, B stark komplettering, C obekräftat, D okänt. Att en källa är nivå 1 betyder inte att varje variant eller monteringskombination är verifierad.

`state: seeded_from_villa_12_hst_research` innebär att registret är överfört från en befintlig forskningsgren; det påstår **inte** att varje extern URL har öppnats och omprövats i denna separata import.

## Hård regel: ursprung kontra kompatibilitet

**Återanvänd gärna:** originalmanual som täcker samma maskinfamilj, identifieringsmetod, dokumentets käll-ID och sektioner, typgemensam teori, säkerhetsprinciper med tillämpningskontroll.

**Kräv alltid nytt modellbelägg:** exakta motorvarianter, oljemängder, remnummer, PTO, drag-/drivdelar, klippaggregat som passar, årsmodeller och individuella serviceintervall. Ett delnummer kan förekomma i flera kataloger men **passform måste ändå visas per produktnummer och revision**.

## Rekommenderad källstruktur för framtida utveckling

```text
maskinarkiv-2/
  knowledge/
    stiga/
      README.md
      sources.json        # återanvändbart källindex
      claims.json         # spårbara uppgifter, alltid tillämpningsbundna
      NY-MODELL-ARBETSGANG.md
  research/
    machines/
      <modell>.json       # modellens egen relevans- och publiceringskontroll
```

Nästa naturliga utbyggnad är fler tillverkargrupper (`briggs/`, `tufftorq/`), delade komponent-ID samt verktyg som kan koppla `usedBy` automatiskt till modellregistren. Flytta inte på befintliga maskinregister eller ändra release-grinden utan separat migration och tester.

## Så hittar du information snabbt i GitHub

1. Öppna `sources.json` och sök exempelvis `8211-3401-10`, `85 Combi` eller `K46CJ`.
2. Notera `id` för källan och sök samma ID i `claims.json`.
3. Läs `locator`, `variant` och `reusePolicy`; kontrollera källan och den nya maskinens PNC.
4. Lägg sedan det verifierade påståendet i nya maskinens forskningsregister. Märk inte A om belägget bara är sekundärt eller fel variant.
5. Låt modellens egen forsknings-, innehålls-, design- och teknikgrind avgöra publicering.

**GitHub är en lagringsplats för våra strukturerade hänvisningar och analyser, inte en garanti för att tredjepartslänkar lever för alltid.** Vill vi långtidssäkra PDF:er måste licensvillkor och rättigheterna till kopiering granskas innan originalfiler checkas in.

## Utökning med tidigare byggda STIGA-modeller

Källbiblioteket innehåller nu även 6 katalog-/manualhänvisningar från den befintliga sidan **STIGA Park 16** och 5 externa länkar från den äldre **STIGA Park 2000**-artikeln. Park 2000-länkarna är indexerade som historiska artikelexterna länkar, **inte** som manuellt omverifierade tekniska källor. Kopplingen finns i `usedBy`.

Källorna från andra tillverkare (Husqvarna och Jonsered) finns i `../other-models-sources.json`. Se även `../README.md` för en samlad inventering.
