# Maskinarkivet – godkänd referensstandard v1

**Godkänd modell:** STIGA Park 12 HST, 2026-10-20, utkast i PR #19.
**Referensdata:** `src/_data/machines/stiga-park-12-hst.json`.
**Referensförhandsvisning:** `preview/stiga-park-12-hst.html`.

Detta är en **redaktionell och pedagogisk standard**, inte en tillåtelse att kopiera fakta från Park 12 HST till andra maskiner eller automatiskt publicera dem.

## Obligatoriska kvalitetsprinciper

1. **Nybörjaren först.** Börja med frågan besökaren har: Vad är det för maskin? Vilken version? Varför startar den inte? Vilken reservdel passar? Förklara fackord i enkel svenska och låt läsaren fördjupa sig efteråt.
2. **Hitta hjälp snabbt.** Erbjud tydliga genvägar till de vanligaste frågorna och relevant felsökning. Låt fungerande ankarlänkar och mobilnavigering leda till avsnitt som verkligen finns.
3. **Identitet före reservdel.** Dokumentera maskinens produktnummer/serienummer, motorns modell/typ/kod, eventuell transmission och aggregatets egen märkning. Varianter skiljs åt.
4. **Felsök efter symptom.** Använd användarens egna ord (helt tyst, startmotorn går men motorn startar inte, stannar, ingen drivning, klipper dåligt); anpassa symptom till maskintypen. Beskriv säkra första kontroller och när arbetet måste avbrytas.
5. **Dokumentera utan gissningar.** Ange version, dokumenttyp, ursprung, artikelnummer och vilka slutsatser källan stöder. En IPL/sprängskiss bevisar inte servicevärden, användningsinstruktion eller allmän kompatibilitet. Redovisa källkonflikter och osäkra uppgifter öppet.
6. **Praktisk djupnivå.** Ha relevant information om motor, drivning/transmission, styrning, klippaggregat/redskap, elsystem, bromsar, service, reservdelar, begagnatköp och vanliga frågor. Utelämna eller anpassa delar som inte finns på modellen; skapa inga fiktiva mekanismer.
7. **Service och säkerhet.** Skriv inte exakta oljevolymer, intervall, moment, pedal- eller startscheman förrän rätt versions-/motordokument stöder dem. Förklara risker och säkra gränser, särskilt för knivar, remmar, bromsar och rörelse.
8. **Källor som går att använda.** Prioritera tillverkarens originaldokument. Särskilj sekundära register. Undvik identiska källposter bara för högre antal och kontrollera att länk och påstående motsvarar rätt produkt/version.
9. **SEO utan vilseledning.** Unik titel, beskrivning, logisk rubrikstruktur, relevanta frågor, korrekta länkar och tillgängliga tabeller. Undvik upprepningar som gör sidan svårläst.
10. **Säkert arbetsflöde.** Utveckla och förhandsgranska på gren/PR; låt CI verifiera HTML, interna ankare och källor. Ändra inte webbplatsens andra sidor. Utöka publiceringens allow-list först efter uttryckligt godkännande.

## Rekommenderad läsordning (anpassa per maskin)

1. Börja här / snabblänkar
2. Översikt
3. Hitta rätt modell och identifieringsnummer
4. Felsökning efter symptom
5. Reservdelar och rätt dokument
6. Motor
7. Drivning/transmission
8. Klippaggregat eller relevanta redskap
9. Styrning och reglage
10. Elsystem
11. Bromsar
12. Underhåll och service
13. Modellversioner och årgångar
14. Ordlista för nybörjare
15. Begagnatköp
16. Vanliga frågor
17. Källor och manualer

**Observera:** Kapitelnamn och antal är inte låsta. Park 12 HST:s godkända ordning är referens, men exempelvis jordfräsar och andra maskinkategorier behöver andra avsnitt och felsökningsspår.

## Migreringsprincip för äldre Maskinarkivet-sidor

- Inventera befintligt innehåll innan ändring.
- Bevara verifierade fakta och originalkällor.
- Jämför varje sida med checklistan ovan, prioritera nybörjarväg och navigering.
- Bygg en maskin åt gången på separat arbetsgren/PR.
- Förhandsgranska på mobil och dator; kör projektets kontroller.
- Ändra aldrig gemensamma mallar så att redan publicerade modeller oavsiktligt förändras.
- Befintliga sidor är inte automatiskt godkända för omskrivning eller publicering bara för att detta dokument är godkänt.

## Nästa steg

Använd denna standard för att granska de fem befintliga Maskinarkivet-modellerna och ta fram en skillnadslista per sida. Planera förbättringarna innan någon av deras publicerade HTML-filer skrivs över.
