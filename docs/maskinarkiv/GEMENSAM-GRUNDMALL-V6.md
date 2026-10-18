# Maskinarkivet v6 – gemensam grundmall

Denna branch innehåller en gemensam CSS-fil: maskinarkiv/maskinarkiv-v6.css.

## Fasta visuella delar
- Hero: gemensam mörkgrön/guldig stil, maxbredd 1180 px.
- Läsinnehåll: 780 px, sticky vänsternavigering 240 px och 54 px mellanrum.
- Typografi: gemensamma storlekar för h1/h2/h3, brödtext, kapitelmarkörer.
- Faktarutor: gemensam styling för .answer, .learn, .hint, .info, .warning, .box.
- Tabeller: gemensamma radavstånd, kanter och header.
- Kontaktblock: gemensam mörkgrön CTA och guldknappar.
- Källor: avslutande öppningsbart details-block (stängt vid sidladdning) med klickbara dokument.
- Mobil: innehållsförteckningen visas som utfällbar details och sidomenyn döljs.
- Nuvarande artiklars faktainnehåll, kapiteltexter och tekniska källor bevaras.

## Omfattning
- STIGA Villa 12 HST
- Husqvarna Rider 13
- Husqvarna LTH151
- STIGA Park 16
- Jonsered LT2115

## För nya artiklar
1. Använd gemensam CSS med <link rel="stylesheet" href="/maskinarkiv/maskinarkiv-v6.css"> EFTER sidans eventuella lokala <style>.
2. Ange <body class="maskinarkiv-v6">.
3. Använd befintliga gemensamma klasser för hero, .wrap.layout, .toc och .article.
4. Använd samma faktarute- och källklasser som v6 förutsätter.
5. Lägg originalmanualer sist i <section id="kallor"> med .source-disclosure och klickbara länkar.
6. Anpassa antalet kapitel efter maskinen, men behåll pedagogisk ordning: översikt -> identifiering -> funktioner -> service/felsökning -> köpråd -> kontakt -> källor.
7. Använd root-absoluta interna href från modellsidor eller gör rebasering av shared partials.
8. Verifiera ankarmål, mobil, länkar och källruta före publicering.

## Granskningsstatus
Statisk kontroll genomförd: alla fem sidor länkar till samma CSS, alla har utfällbara källor och inga interna ankarmål saknas.
Ingen faktisk visuell browser-rendering genomförd. Denna branch bör visas på en riktig preview/staging innan en sammanslagning till main. Vid fel måste ändringar rättas här före merge.
