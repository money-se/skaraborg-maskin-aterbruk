# Villa 12 HST – publiceringsrevision och åtgärdskrav
Datum 2026-10-21. Status: redaktionell granskning, **inte publiceringsgodkännande**.

## Kontrollerad publicerad version
https://skaraborgmaskin.se/maskinarkiv/stiga-villa-12-hst.html

### Hög prioritet: versionstabellen
Den nuvarande artikeln anger fyra versioner: 13-2727-13, 13-2727-14, 13-2729-14, 13-2729-15. Originalkatalogen 2011/2012 visar även **13-2729-35 (FR)**. Publicerad tabell måste kompletteras med denna variant. Föreslagna osäkra, exakta Briggs-beteckningar **21R502** respektive **21R602** får inte stå som tillverkarverifierad motoridentitet. Beteckna som sekundärt förväntade modeller och lägg in identifieringshjälp för Model/Type/Code.

### Hög prioritet: aggregatens koppling till maskin
Alla fyra raderna i den publicerade versionstabellen anger **Combi 85**. STIGA-originalkatalogen för 2011/2012 bekräftar **13-2960-14 85 Combi** som självständig aggregatprodukt; den bekräftar därmed *inte automatiskt* komplett kompatibilitet för var och en av alla fem basmaskins-ID:n.

Att två reservdelskataloger är från samma år, eller att en monteringsmanual beskriver Villa/Ready, räcker inte för en generell passformslista. Utan en uttrycklig kompatibilitets-/monteringskälla bör artikeln ersätta tabellens aggregatfält med "Kontrollera aggregatets eget produktnummer och monteringssats". Detta är säkrare än att gissa.

### Hög prioritet: underhåll
Återge inte motoroljans mängd, tändstift, luftfilter eller motorserviceintervall som universella mellan GGP och Briggs. Märk varje värde med sin källmanual och specificerat motorutförande. Håll hydrostatservice separat och lämna den som *ej styrkt* tills riktig serviceinstruktion hittas.

### Hög prioritet: tre skilda drivremssystem
1. Transmission/hydrostatdrift på basmaskinen (exempel STIGA 2010/11: 1134-9064-01)
2. Kraftuttag/PTO mellan maskin och aggregat (versionsspecifikt)
3. Internt kuggrem-/drivremssystem i 85 Combi aggregat 13-2960-14 (exempel 9585-0161-01 och 1134-9109-01)

Artikelns felsökning ska fråga **vilken rem** det gäller före delnummer.

### Medelhög prioritet: FR-marknadsvariant
13-2729-35 har särskilda kaross- och skyddsdetaljer i originalkatalog 2011, figur 2819. Det berättigar en notis i versionskapitlet, inte ett påstående om annan motor/hydrostat.

### Medelhög prioritet: identifieringshjälp
Lägg en lättillgänglig bild-/textbaserad checklista: basmaskinens fullständiga produktnummer; motorns Model/Type/Code; aggregatets produktnummer; bild på eventuell skadad del. Användaren ska veta varför tre olika skyltar kan behövas.

## Släppkriterier
- Research-JSON `status=ready` enligt obligatoriska protokollet, först efter alla verkliga kunskapsluckor är stängda eller kontrollerat avgränsade enligt protokoll.
- Varje faktakänslig siffra och delnummer i artikeln pekar på original- eller robust sekundärkälla och rätt version.
- Ett faktiskt genererat HTML-exemplar granskas visuellt för navigering, mobilvänlighet, tabell och felsökningsflöde.
- Därefter separat kod-PR för artikeln och uttryckligt godkännande före publicering.

## Primärkällor
- STIGA 2011/12 Villa HST: https://view.stiga-store.com/files/SSPL2011_20110214_Villa_HST.pdf
- STIGA 2011/12 85 Combi: https://view.stiga-store.com/files/SSPL2011_20110214_Mower_deck_Villa_85C-2-.pdf
- STIGA 2010 Villa HST: https://view.stiga-store.com/files/SSPL2010_20100208_Villa_HST.pdf
- Briggs motornummer: https://www.briggsandstratton.com/en-us/support/manuals?hl=en_US

Ingen produktversion ska klassas som fullt verifierad enbart på grund av en grön CI-körning.
