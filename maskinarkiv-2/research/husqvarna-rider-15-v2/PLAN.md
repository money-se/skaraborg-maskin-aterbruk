# Maskinarkivet 2.0 – forskningsuppdrag: Husqvarna Rider 15 V2

Status: FAS 1 PÅBÖRJAD – endast modellval och källinventering, ingen genererad artikel.
Startbas: main @ b92413bb2bdcd50bb788fc0343b6e76c0af155f1
Arbetsgren: feature/maskinarkiv-2-husqvarna-rider-15-v2
Planerad slug: husqvarna-rider-15-v2

## Modellval
Vald modell: **Husqvarna Rider 15 V2** (inte den breda, otydliga beteckningen Rider 15).
Syftet är en djup pedagogisk kunskapssida som kompletterar Rider 13 och återanvänder gemensamma Eleventy/Nunjucks-mallar.

Viktigt: **Rider 15 V2**, **Rider 15 V2 AWD**, **Rider 15 V2s AWD** och **Rider 15 T / 15 T AWD** får inte behandlas som samma tekniska utförande. Skillnader i drivning, utrustning och produktnummer kräver dokumentation per variant.

## Första källinventering (2026-10-20)
**Primärkälla A – Husqvarna originalreservdelsportal:**
- RIDER 15V2; visade separata IPL-avsnitt för bland annat transmission, engine, steering, electrical samt klippaggregat i olika mått.
- https://shop-pa-v9.husqvarna.com/webapp/wcs/stores/servlet/us/EPCProductView?catalogId=13051&epcBrandName=Husqvarna&epcProduct=RIDER+15V2&langId=-1&modelId=Husqvarna-Riders_RIDER+15V2&storeId=11251
- Specifik identifierad katalogpost: **RIDER 15V2, 953 53 37-01, 2006-01**. Datum är dokument-/katalogdatum, INTE verifierat tillverkningsår.
- https://shop-pa-v9.husqvarna.com/EPCProductView?catalogId=13051&epcBrandName=Husqvarna&epcCategory=Riders&epcProduct=RIDER+15V2&epcVariantName=RIDER+15V2%2C+953+53+37-01%2C+2006-01&langId=-1&modelId=Husqvarna-Riders_RIDER+15V2&storeId=11251

**Primärkälla A – Husqvarna originalförarmanual:**
- OM, Rider 15 V2, Rider 15 V2 AWD, Rider 15 V2 s AWD, 2008-11.
- https://content.tdr.dss.husqvarnagroup.net/pub000038634/doc000071096
- Manualen beskriver identifikationsskylt fram till vänster under sätet och att motor respektive hydrostat har separata identitetsuppgifter. Kontrollera manualrevision mot maskinens produktnummer.

**Jämförelsekällor, inte automatiskt kompatibilitetsbevis:**
- RIDER 15V2 AWD i Husqvarnas IPL-portal:
  https://shop-pa-v9.husqvarna.com/us/EPCProductView?catalogId=13051&epcBrandName=Husqvarna&epcProduct=RIDER+15V2+AWD&langId=-1&modelId=Husqvarna-Riders_RIDER+15V2+AWD&storeId=11251
- RIDER 15 T AWD i tillverkarens IPL-portal:
  https://shop-pa-v9.husqvarna.com/us/EPCProductView?catalogId=13051&epcBrandName=Husqvarna&epcProduct=RIDER+15+T+AWD&langId=-1&modelId=Husqvarna-Riders_RIDER+15+T+AWD&storeId=11251

## Sakuppgifter och bevisnivå
- Verifierat i tillverkarens portal: RIDER 15V2 har ett eget IPL-register och flera revisionsbundna dokument.
- Verifierat i tillverkarens manual: modell-/tillverkartyp-/serienummer på identifikationsskylt samt separata märkningar på motor/transmission.
- Ej verifierat för samtliga revisioner: motorfamilj, exakt hydrostattyp, effekt, drivning, aggregatkompatibilitet, däckstorlek, kapacitet, årsmodell, serviceintervall och specifika reservdelsnummer.
- Inga generella 'typfel' eller utbytbara reservdelar ska påstås utan primärkälla.

## Artikelplan för granskning
1. Enkel modellöversikt – maskinens funktion och användning.
2. Identifiering: märkplåt, serienummer, motormärkning, transmissions-ID.
3. V2-modellrevisioner: produktnummer och dokumentdatum med källstöd.
4. Vad som skiljer vanlig Rider 15 V2 från AWD och senare 15 T-varianter.
5. Motor och drivning – grundprinciper + verifierade variantuppgifter.
6. Styrning och reglage; säker körning.
7. Klippaggregat, klippteknik, versionsberoende kompatibilitet.
8. Underhåll enligt rätt manual.
9. Felsökningsguide: observationsbaserade kontroller, inga påstådda typfel.
10. Reservdelskataloger, hur man hittar rätt del.
11. Kontrollpunkter före begagnatköp.
12. Frågor och svar, gemensam återbruk-/Tradera-del, källor.

## Arbetsgång / gränser
1. Fullständig faktainventering av Rider 15 V2-produktrevisioner i Husqvarnas IPL och förarmanualer.
2. Källklassificerat faktaunderlag och granskning av variantmatris.
3. Skriv JSON i maskinarkiv-2/src/_data/machines/husqvarna-rider-15-v2.json och 11ty-entry med befintlig machine.njk; återanvänd block/partials och STIGA Park 16-designen.
4. Utöka berörda hårdkodade modellregister i scripts/check.mjs, scripts/audit-production.mjs, scripts/stage-production.mjs, scripts/audit-content-parity.mjs, src/index.njk samt uttryckliga allowlist i .github/workflows/maskinarkiv-2-pilot.yml inför en senare godkänd publicering.
5. Kör npm run build, npm run check och npm run audit samt faktagranskning och mobil/desktop-preview.
6. INGEN merge, publicering, main-ändring eller ändring utanför Maskinarkivet utan uttryckligt godkännande.
7. Denna forskningsfil är en arbetsregistrering och **ingen publiceringsklar modellsida**.

## Nuvarande status
Modellval och första primärkällor registrerade. Teknisk artikelkodning och publiceringskoppling ej påbörjade.
