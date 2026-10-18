# Jonsered LT2115 – delprojektets överlämningsrapport (2026-10-18)

## Omfattning och skyddsregler
Repo: money-se/skaraborg-maskin-aterbruk
Arbetsgren: feature/maskinarkiv-jonsered-lt2115
Modellsida: maskinarkiv/jonsered-lt2115.html
Startpunkt: 2b66e2060cc8c472d28f368605e37b6ddc8653a0
Inget ska mergas till main, ombaseras eller publiceras utan uttryckligt godkännande.

## Arbete genomfört
- Befintlig Jonsered-modellsida vidareutvecklad, inte ersatt med en grundare sida.
- Utökad variantmatris: LT2115 96011018100, LT2115A 96011018200, LT2115CM 96061008101 och LT2115CMA 96061008301.
- Separata avsnitt för Kohler SV470-service och manual-/säkerhetsfrågor.
- Reservdelsvarningar för remmar, standardknivar/cross blades och hydrostatvariationer.
- Källmodal utökad med IPL-nummer och externa dokumentlänkar.
- Mobil-TOC rättad till samma 21 länkar som desktop.
- CSS-alias för tidigare felrefererade färgvariabler rättade.

## Kontroller
PASS (statisk HTML-/källtextkontroll):
- Alla refererade interna ankare finns; inga dubbla id identifierade.
- 22 sections och 22 sluttaggar; 9 details och 9 sluttaggar.
- Desktop och mobil-TOC har 21 länkar vardera.
- Canonical till https://skaraborgmaskin.se/maskinarkiv/jonsered-lt2115.html finns.
- Header och footer har relativa sökvägar ../partials1/header.html och ../partials1/footer.html.
- Endast Jonsered-filens HTML har ändrats i kandidatens tidigare commits.

PARTIELLT (källverifiering):
- LT2115A 96011018200 Hydro-Gear 322-0510 bekräftad i original-IPLs text (544 40 90-01).
- LT2115CMA 96061008301 Hydro-Gear 321-0510 bekräftad i original-IPLs text (544 88 89-01).
- Kohler SV470-SV620 handbok 20 690 01 Rev. J kontrollerad för normalt 100h/årligt olja+filter och särskilt villkorat 300h PRO-intervall.
- Bruksanvisningar för LT2115 och LT2115CM återfunna, men inte entydigt kopplade till alla produktnummer.

EJ TESTAT / EJ GODKÄNT:
- Riktig renderings- och responsivitetstestning i webbläsare på desktop/mobil; ingen publik feature-preview fanns att navigera.
- Källornas PDF-sidor kunde läsas som extraherad text, men screenshot/bildvisning av PDF:er misslyckades; sprängskisser behöver manuell bildgranskning.
- Samtliga externa länkar testade inte som webbläsarnavigering från modellsidan; ett urval öppnades via webbkällor.
- Detaljerad fullständig sakkontroll av alla äldre stycken och äldre reservdelsnummer på sidan.
- Användbarhet med tangentbord/skärmläsare för källmodal.
- Validering av HTML/CSS i riktig webbläsare och faktisk laddning av header/footer från staging.

## Publiceringsspärrar
1. Produktnummerkonflikt i LT2115 IPL 544 46 75-01: 96011018100 kontra 96011011800 / 960 11 01-812. Presentera som källavvikelse, inte som korrigerat faktum.
2. Ingen reservdelskompatibilitet får härledas enbart ur liknande modellnamn.
3. Kohler-service anges bara för rätt motorfamilj/specifikation; 300h inte generellt.
4. LT2115CM/LT2115CMA och LT2115/LT2115A har olika dokumenterade drivlinor och aggregat.
5. De äldre påståendena om LT2115 / 954130210 och andra historiska versioner behöver källgranskas på detaljnivå innan publicering.

## Integrering
Den samordnande chatten ska granska kandidatsidan och denna rapport. Ändra inte gemensam navigation, sitemap, CSS eller main här. Inget PR, merge eller deploy initierat från denna chatt.
