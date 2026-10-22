# Maskinarkivet 3.0 – gemensamt kunskapsarkiv och återanvändning

**Beslut 2026-10-22:** Vid varje maskinresearch ska relevant ny kunskap dokumenteras i GitHub för kommande modellartiklar, även om den råkar handla om en annan maskin än den aktuella. Detta är en permanent arbetsprincip.

## En enda källa till sanning

**Det befintliga STIGA-systemet är huvudsystemet.** Den kanoniska tekniska forskningen ligger endast i `research/machines/<slug>.json`, i samma schema som `stiga-villa-12-hst.json`: `sources`, `topics` A–M, `claims`, `gaps` och separat `scopedRelease`. Duplicera inte faktapåståenden i löpande separata index eller fristående kunskapsdokument. Ett index ska bara hänvisa till kanonisk post och specifika claim-/source-ID.

`research/SHARED-KNOWLEDGE-INDEX.md` är en **navigationskarta över sidofynd och källrelationer**, inte ett nytt granskningssystem och inte självständigt bevis. Källor som omfattar flera modeller registreras i berörda modellregister med spårbart source-ID. Samma källdokument får återanvändas; en teknisk uppgift får återanvändas endast efter kontroll att den gäller exakt angiven maskin eller komponent.

**Publiceringsgrinden är oförändrad:** `needs_research` ger inte tillåtelse att ändra artikeldata; `scoped_ready` förutsätter kraven i `scripts/check-research.mjs` och bedömd omfattning. Uppgradera aldrig status för att få testerna gröna.

## Arbetsregel
1. Spara varje verifierat relevant källfynd i tillhörande maskins forskningsregister (`research/machines/<slug>.json`) när registret finns. Skapa annars först ett nytt register med `status: needs_research` enligt `scripts/check-research.mjs`. För sidofynd som ännu inte har ett komplett register: skriv en **pekare** i det gemensamma indexet och länka till originalkällan; upphöj inte indexposten till verifierat claim.
2. Om en källa handlar om **flera maskiner**, dokumentera vilka den faktiskt täcker. Registrera uttryckliga variant- och produktnummer separat; återanvänd källan utan att anta universell passform.
3. Gemensamma förklaringar om mekaniska system får delas i kunskapsunderlag. **Motorns faktiska Model/Type/Code, reservdelsnummer, servicevärden och godkända aggregat kräver alltid maskin-/komponentbunden källa.**
4. Varje verifierbart fynd ska åtminstone ha: fakta/påstående, maskin/modell eller komponent, produktnummer/variant (eller "ej identifierad"), dokumentnamn och exakt källa/URL, sid-/figurposition när tillgänglig, källnivå, verifieringsstatus, datum och öppna frågor.
5. Märk information `verified`, `needs_verification` eller `rejected` på fyndnivå i anteckningarna. Forskningens övergripande `status` får **inte** uppgraderas bara för att en enskild uppgift är verifierad.
6. Källor från återförsäljare, annonser och reservdelssidor kan sparas som ledtrådar men får inte förvandlas till tillverkarbekräftade fakta.
7. Spara även **relevanta sidofynd**, t.ex. om Rider 11 eller Rider 16 upptäcks under granskningen av Rider 13. Skriv separata modellidentiteter och ge korsreferens till källan.
8. Radera inte tidigare forskningsluckor utan spårbar upplösning; bevara datum och varför en uppgift ändrades.
9. Publicering är ett **separat steg**: uppgift som finns i kunskapsarkivet ska inte automatiskt publiceras. Artikeländringar måste passera källgrinden, byggtesterna och modellens granskningsregler.

## Exempel på minsta sidofynd
```yaml
machine: "Husqvarna Rider 11 Bio"
product_number: "Ej fastställt"
topic: "Reservdelar"
finding: "Förekommer i samma Husqvarna-originalmanual som Rider 13 Bio"
source: "Husqvarna Rider 11 / Rider 13 / Rider 11 Bio / Rider 13 Bio"
document: "2003-08, pub000021448 / doc000044020"
url: "https://content.tdr.dss.husqvarnagroup.net/pub000021448/doc000044020"
locator: "Manualens omslag/modelllista"
status: "verified"
limitation: "Gemensam manual innebär inte att komponenterna är utbytbara"
```

## Mappstruktur
- `research/machines/*.json`: maskinspecifika belägg, källor, claims, luckor, publiceringsstatus.
- `research/SHARED-KNOWLEDGE-INDEX.md`: index till andra maskiner/komponenter som upptäcks under arbetet.
- `knowledge/`: arbetsmetod, kvalitetskrav och gemensamma pedagogiska förklaringar.
- `src/_data/machines/`: webbpublicerad modelltext; ändras först när artikelns källgrind passerats.

**Mål:** Bygga en sökbar, spårbar maskinkunskapsbank i GitHub som växer med varje researchinsats – inte börja research från noll inför varje ny modell.
