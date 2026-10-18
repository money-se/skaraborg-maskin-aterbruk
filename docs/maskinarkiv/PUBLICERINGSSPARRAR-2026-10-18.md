# Samordning: publiceringsspärrar och åtgärdsuppdrag – 2026-10-18

## Kontrollstatus
Verifierat mot GitHub den 18 oktober 2026, efter separata ändringar i feature-grenarna. Ingen merge eller ändring på main genomförd.

### Husqvarna LTH151
Gren: feature/maskinarkiv-husqvarna-lth151
- Rotrelativa länkar i inlästa header/footer rättade: c66b52c.
- Källfönstret fick z-index 2000 för att ligga över den gemensamma sticky headern (z-index 1000): 884d3ff.
- Statiska interna ankarmål är kompletta. Återstår: faktisk browser-/mobiltest och komplett faktakontroll.

### STIGA Park 16
Gren: feature/maskinarkiv-stiga-park-16
- Inläsning av partials går genom insertPartial som ändrar lokala relativa href till rotbaserade href.
- Statiska interna ankarmål kompletta. Återstår: faktisk browser-/mobiltest och källkontroll av varianter.

### Jonsered LT2115 – öppen blockerare
Gren: feature/maskinarkiv-jonsered-lt2115
- I aktuell blob 15561985073bcfec02818aad68a73fdd36a77046 använder sidan:
  async function inject(id,url){...e.innerHTML=await r.text()...}
- Både partials1/header.html och partials1/footer.html använder relativa länkar såsom href="index.html", href="kop-maskiner.html", href="kontakt.html".
- På /maskinarkiv/jonsered-lt2115.html blir detta felaktigt /maskinarkiv/kop-maskiner.html etc.
- Uppdrag till ägande chatt: ändra endast maskinarkiv/jonsered-lt2115.html på sin egen gren. Läs in partial i template och förvandla webbplatsrotens interna dokumentrelativa href (och relevanta src) till /...; bevara https:, tel:, mailto:, #ankare och redan /-absoluta länkar. Testa även footer. Ingen global partial ska ändras.
- Kontrollera z-index för Jonsereds källmodal mot headerns z-index 1000. Dialogen måste vara över headern.

## Att testa på riktigt före publiceringsgodkännande
- Välj 390px mobil och stor desktop. Verifiera inga horisontella överflöden förutom scrollbara tabeller.
- Testa header/footer från faktisk /maskinarkiv/-URL: Hem, Vi köper, Kontakt.
- Testa källknapp, Escape, tab-fokus, klick på bakgrunden samt placering ovanpå sticky header.
- Testa externa manual-/källänkar; blanda inte ihop källmaterial per produktnummer.
- Granska efter förändringar från main innan någon integration.
- Godkännande krävs innan sitemap, maskinarkivet.html, PR/merge, huvudgrensändring eller publicering.

## Slutsats
Statisk QA ger användbara PASS för ankare och canonical, men inte bevis för full webbläsarfunktion. Jonsereds relativa partial-länkar är ännu blockerande.
