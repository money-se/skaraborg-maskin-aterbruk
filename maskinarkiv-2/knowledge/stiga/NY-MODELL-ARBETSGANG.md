# Arbetsgång: bygg en ny STIGA-modell med gemensamt källregister

## Steg 1 – identifiera basmaskinen
Notera fullständigt PNC/artikelnummer, ungefärlig årsmodell, motorns märkning, ev. transaxel-ID och aggregatets eget PNC. Skilj maskin, redskap och motor åt.

## Steg 2 – återanvänd kunskap först
Sök `sources.json` efter modellfamilj, manualnummer, komponent och årsmodell. Sök `claims.json` efter samma `sourceId`. Granska först primärkällorna `tier:1`.

### Snabbsökning med GitHub
Använd GitHubs filsökning eller sök direkt i `sources.json` efter `Villa`, `Park`, `K46CJ`, `85 Combi`, `Briggs` och dokumentnummer. Se `claimRefs` för relevanta tidigare faktauppgifter.

## Steg 3 – återanvänd endast giltig tillämpning
Kontrollera `variant`, `locator`, `grade` och `reusePolicy`. En claim med `model_scoped_requires_compatibility_confirmation` får inte kopieras som ett universellt maskinpåstående. Även generell identifikations- eller säkerhetsinformation ska kopplas till rätt version och manual.

## Steg 4 – komplettera smart
Forska bara där källbiblioteket saknar relevant belägg. Lägg nya dokument med nytt beständigt sourceId; lägg nya variantbundna claims i `claims.json` och spårbara individuella beslut i nya maskinens `research/machines/<slug>.json`. Uppdatera `usedBy` samt `claimRefs`.

## Steg 5 – bygg artikeln
Skriv lättläst innehåll med direkt hjälp för symtom, identifiering och köp, men separera fakta, rekommendationer och olösta kompatibilitetsfrågor. Ingen universaliserad motorservice eller delkompatibilitet.

## Steg 6 – publiceringskontroll
Behåll protokollets fyra separata kontroller (Research/Innehåll/Design/Teknik). Det nya källbiblioteket är ett **tillägg**, inte en genväg genom den befintliga `research:release`-grinden. En framtida ändring till mer praktisk och påståendebaserad publiceringsgrind ska göras i separat PR med verifieringstester.

## Förvaltning
- Kontrollera regelbundet länkstatus, dokumentutgåvor och motsägande reservdelskataloger.
- Ange originaltillverkare, dokumentnummer, giltighet och kapitel/figur vid varje ny upptäckt.
- Bevara historik; korrigera felaktiga claims med Git-ändringar och förklaring.
- Förflytta inte filer till `main` förrän review av registerformat, ursprung och användningsgränser har gjorts.
