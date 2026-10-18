# Husqvarna LTH151 – researchunderlag v1
Datum: 2026-10-18
Gren: feature/maskinarkiv-husqvarna-lth151
Status: RESEARCH PÅGÅR – ännu inte publiceringsklar HTML

## Kontrollerade primärkällor

1. Husqvarnas officiella LTH151 reservdelsportal:
https://shop-pa-v9.husqvarna.com/us/EPCProductView?catalogId=13051&epcBrandName=Husqvarna&epcCategory=Tractors%2Fride+Mowers&epcOverrideCategory=&epcProduct=LTH151&epcVariantName=LTH151&langId=-1&modelId=Husqvarna-Tractors%2Fride+Mowers_LTH151&storeId=11251

Officiell versionlista innehåller bland annat:
- HELTH151A / HELTH151B / HELTH151C (2004-dokument)
- 96011000200 (2005-01)
- 96011011200 och 96011011300 (2006)
- 96041001900, 01901, 01902, 01903, 01905, 01906, 01907 (2007–2010)
- 96041002000, 02001, 02002, 02003, 02004, 02005, 02006 (2007–2010)
- 96041020100, 96041020101 (2010–2011)
- 96041020700 (2010)
Dessa datum är katalogversioner och får INTE likställas med exakta produktionsår.

2. Husqvarnas originalmanual (LTH151), dokumentkod 532 43 41-78 Rev. 2:
https://content.tdr.dss.husqvarnagroup.net/pub000046231/doc000082753
80 sidor, flera språk. Originalmanual behöver kapitelgenomgång innan detaljer om motor/service/etc publiceras.

3. Reservdelskatalog (IPL), LTH151 96041001903, 2008-01:
https://www.xn--grsklipparbutiken-rqb.se/dokument/bibliotek/Image/Akgrasklippare/LTH151/IPL%2C-LTH151%2C-96041001903%2C-2008-01_wm.pdf
18 sidor. Källmaterial för just 96041001903, inte för samtliga LTH151.

4. Husqvarna Sverige support:
https://www.husqvarna.com/se/support/

## Faktagradering
A (primärkälla):
- Modellnamn LTH151 existerar som egen produktfamilj i Husqvarnas officiella reservdelsportal.
- Det finns många olika produktnummer/versioner.
- Husqvarna tillhandahåller flera separata originalmanualer kopplade till dessa produktnummer.
- Delgrupper i katalogen är bland annat chassi, drivlina, elsystem, motor, klippaggregat, lyft, säte, styrning, hjul.

Ej fastställda / ännu inte publicerbara:
- En enda motormodell/effekt för samtliga LTH151
- Ett enda klippmått
- Exakt transmissionsfabrikat för alla varianter
- Oljemängd och tändstift för samtliga versioner
- Reservdelar som påstås passa alla varianter
- Start- och slutår för produktionen

## Plan för maskinartikeln
1. Snabbsvar och modellöversikt
2. Identifiering: modellnamn vs produktnummer vs seriemärkning
3. Dokumenterade versioner (separerade 960110…, 960410019…, 960410020…, 960410201…)
4. Grundkonstruktion och vad reglagen gör
5. Motor och motormärkning per version
6. Drivlina/hydrostat per version
7. Klippaggregat, knivdrift och höjdjustering
8. Säkerhet och startvillkor
9. Service: motor, remmar, styrning, däck, batteri
10. Felsökning (praktiska kontrollpunkter utan obelagda typfel)
11. Reservdelar: praktiskt arbetssätt från typskylt till sprängskiss
12. Begagnatkontroll, köpråd
13. Vanliga frågor
14. Naturlig återbruks-CTA
15. Källmodal med primärkällor

## Nästa kvalitetsspärr
Verifiera delspecifikationer med rätt versionskopplade originalmanualer och IPL innan dessa anges i HTML. Behåll sticky innehållsförteckning, mobilanpassning och källmodal enligt maskinarkivets huvudmall. Ändra bara maskinarkiv/husqvarna-lth151.html och docs/maskinarkiv/husqvarna-lth151/ på denna gren. Ingen sitemap, huvudarkiv, partial, startsida eller main.

## Bekräftade detaljuppgifter för just produktnummer 96041001903

Källa: IPL LTH151 96041001903, 2008-01, sidorna 9–12 i PDF (tryckta sidorna 9–12):
https://www.xn--grsklipparbutiken-rqb.se/dokument/bibliotek/Image/Akgrasklippare/LTH151/IPL%2C-LTH151%2C-96041001903%2C-2008-01_wm.pdf

A för denna variant, INTE alla LTH151:
- Motor: Kohler SV470, enligt sprängskissens motorlista (tryckt sida 11).
- Transmission: Hydro-Gear T2, enligt "Transaxle, Hydro GR T2" (tryckt sida 9).
- Drivrem: Husqvarna 532 12 59-07, enligt samma drivlineförteckning (tryckt sida 9). Verifiera ny ersättningskod mot aktuell Husqvarna-katalog före beställning.
- Frikopplingsstång: 532 40 84-18 ("Rod Bypass", sida 9).
- Styrningens främre axelenhet: 532 19 56-73 (sida 13).

Tolkningsnotering: Katalogen visar reservdelsnummer för en historisk produktvariant; artikelnumren kan ha ersatts. En tryckt reservdelspost utgör inte bevis för passning på övriga LTH151-versioner.

## Säkerhetsunderlag i originalmanualen

Manual 532 43 41-78 Rev. 2, engelska säkerhetskapitlet, tryckt sida 3:
- Kör inte på lutning över 15 grader (gäller denna manualutgåva; kontrollera rätt maskins manual).
- Motorn ska inte köras i stängt utrymme på grund av kolmonoxid.
- Innan start: koppla ur knivdriften och lägg växeln/drivningen i neutralt.
- Ingen körning med borttagna eller defekta skydd/säkerhetsanordningar.

Ingen instruktion om förbikoppling av säkerhetsbrytare ska publiceras.

## Öppna researchfrågor före HTML
1. Jämför teknisk motor-/transmissionsdata mellan produktnummer 960410019xx och 960410020xx.
2. Kontrollera om och hur klippaggregatens bredd/uppbyggnad varierar mellan versioner.
3. Kontrollera instruktioner för däcktryck, oljemängd och service mot versionsspecifik manual.
4. Spåra svensk operatörsmanual från Husqvarnas officiella dokumentbibliotek.
5. Validera aktuella reservdelsersättningar separat från historisk IPL.

