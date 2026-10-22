# Villa 12 HST – faktakontroll, etapp 1 (2026-10-22)

## Syfte och metod
Detta är ett internt kontrollprotokoll för den publicerade artikeln, inte extra text för besökaren. Granskat mot `maskinarkiv-2/src/_data/machines/stiga-villa-12-hst.json`, de publicerade Villa-fördjupningarna, befintligt claim-register och dokument på tillverkarnas/tillgängliga originaldokuments webbadresser. Status gäller **enbart de nedanstående uppgifterna**. Denna etapp är inte en fullständig verifiering av samtliga 53 claims, 14 publika källänkar eller hela 12-kapitelartikeln.

| Område | Publicerad uppgift | Underlag och exakt plats | Slutsats |
|---|---|---|---|
| Basmaskin, transmission | Kanzaki K46CJ, STIGA 1134-7766-01 | STIGA VILLA HST 2010, transmissionsfigur 1157G, position 23, PDF-sida 27 (nollbaserad 26), https://view.stiga-store.com/files/SSPL2010_20100208_Villa_HST.pdf | **Styrkt för katalogens specificerade 2727/2729-grupper**, inte automatiskt okända eftermonterade växellådor. Claim `stiga-2010-k46cj`. |
| Transmissionsdrivrem | 1134-9064-01; alternativt 9585-0099-01 | Samma STIGA-katalog, figur 1157G, position 17, PDF-sida 27 | **Styrkt** inom katalogens maskinversioner. Claim `stiga-2010-drivebelt`. |
| Aggregatidentitet | 85 Combi 13-2960-14 för 2011/2012 | STIGA 2011/12 85 Combi originalkatalog, PDF-sida 1: https://view.stiga-store.com/files/SSPL2011_20110214_Mower_deck_Villa_85C-2-.pdf | **Styrkt** som egen aggregatversion; det visar inte universell passform med varje Villa-maskin. Claim `deck-2960-14`. |
| Aggregatknivar och brytdelar | Knivbalk 1134-9116-01; knivsats 1134-9119-01; brytbultsats 1134-9054-01 | Samma STIGA aggregatkatalog, transmissionsfigur 2130A, positioner 6–8, PDF-sida 7 (nollbaserad 6) | **Styrkt för 13-2960-14**. Claim `85combi-2011-independent-blade-parts`. |
| Aggregatremmar | Kuggrem 9585-0161-01; drivrem 1134-9109-01 (= 9585-0160-01) | Samma aggregatkatalog, figur 2130A, positioner 34 och 36, PDF-sida 7 | **Styrkt för 13-2960-14**. Claim `85combi-2011-belt-parts`. |
| Transaxelservice | Tuff Torqs oljeservice omfattar Manufacturing ID K46CJ; normalt anges K46 som underhållsfri vid vanlig drift | Tuff Torq, Tech Tips: https://www.tufftorq.com/tuff-torq-transaxle-oil-service/ , stycket `Models covered` och efterföljande servicetext (kontrollerad 2026-10-22) | **Styrkt för identifierad K46CJ med intern behållare**. Artikelns försiktiga formulering är motiverad; inför inte generella årliga oljebyten. Claim `k46cj-tufftorq-service-primary`. |
| Däcktryck | 0,4 bar fram; 1,2 bar bak | STIGA Villa 12 HST, originalmanual 8211-0038-90 §8.3, återgiven i https://manualzz.com/doc/4520408/stiga-villa-12-hst-ride-on-mower-gebrauchsanweisung | **Textuppgiften stämmer med manualutgåvan**. Kontrollera aktuell maskins manual före tillämpning. Claim `tire-pressure`. |
| Motoroljebyte | Första bytet efter 5 h, sedan var 50:e h eller per säsong, tätare vid hård drift | Samma STIGA 8211-0038-90 §8.4 | **Styrkt för manualens motorutförande**, inte automatiskt för varje Briggs-utrustad Villa. Claim `oil-service`. |
| Styrning | Kontroll efter 5 h och därefter 25 h | Samma STIGA 8211-0038-90 §8.7 | **Styrkt för manualutgåvan**. Claim `steering-check`. |

## Ännu inte godkänt i denna etapp
- PTO-rem 1134-9079-01 för 13-2729-35: endast sekundärkälla i claim-registret; originalbelägg kvarstår.
- Samtliga Briggs Model/Type/Code per maskin-PNC: fortfarande inte fastställt från verkliga motormärkningar.
- Säkra passformsmatriser mellan 13-2960-13/-14/-15 och samtliga fem basmaskin-PNC: ännu inte klarlagda.
- Samtliga serviceintervall i grundartikelns tabell: måste stämmas av rad för rad mot rätt motor- och maskinmanual.
- Externa länkar i det publika källavsnittet: ännu inte samtliga 14 öppnade och testade.
- Bilder, layout, tangentbordsnavigation, mobilvisning, metadata och SEO: ingår i senare acceptansgrind.
- Dokumentens webbsidor gick att läsa som text men PDF-skärmbildsverktyget gav cachefel; ingen fullständig visuell granskning av figurernas layout har därför genomförts i denna etapp.

## Redaktionellt beslut
**Inga ändringar krävs i artikeltexten utifrån de nio kontrollerade raderna ovan.** Numren och värdena stämmer inom uttryckligen angiven variant. Behåll källgränser internt och ge läsaren raka praktiska råd. Nästa faktapass bör prioritera serviceintervallstabellen och de kvarvarande B-källorna, innan slutlig mobil-/SEO-granskning.
