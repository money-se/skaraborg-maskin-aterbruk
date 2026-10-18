# Maskinarkivet – parallellt arbete (planering, 2026-10-18)

## Syfte
Tre oberoende ChatGPT-chattar tar fram en djupgående, källkontrollerad maskinartikel vardera. Arbete sker endast i dedikerade feature-grenar. All integration, gemensam navigation, designförändring, sitemap och publicering avvaktas tills användaren uttryckligen godkänner detta.

## Bas och grenar
Repo: money-se/skaraborg-maskin-aterbruk
Gemensam start-commit: 2b66e2060cc8c472d28f368605e37b6ddc8653a0

- Koordination: feature/webbplats-delprojekt-2026-10-18 (den här filen)
- Arbete A: feature/maskinarkiv-husqvarna-lth151 -> maskinarkiv/husqvarna-lth151.html
- Arbete B: feature/maskinarkiv-stiga-park-16 -> maskinarkiv/stiga-park-16.html
- Arbete C: feature/maskinarkiv-jonsered-lt2115 -> maskinarkiv/jonsered-lt2115.html

Modellerna är preliminära arbetsuppdrag tills användaren bekräftar. Om dokumentationen visar att ett brett modellnamn täcker flera oförenliga versioner, skilj ut versionerna eller föreslå en mer exakt modell innan kodning.

## Absoluta skyddsregler
1. Läs alltid aktuell branch/commit och kontrollera diff mot main före filändringar.
2. Ändra ALDRIG main, merge:a ALDRIG och publicera ALDRIG utan uttryckligt godkännande av användaren.
3. Varje chatt får endast ändra SIN egen nya modellsida samt eventuella temporära forskningsanteckningar inom docs/maskinarkiv/<modell>/ på SIN gren.
4. Ändra inte index.html, maskinarkivet.html, sitemap.xml, robots.txt, partials1/*, gemensam CSS/JS, workflows, andra modellsidor, kataloger eller adminkod. De kommer att samordnas separat efteråt.
5. Ingen annan chatt får committa på någon annans gren. Cross-branch cherry-pick/merge kräver granskning och användarens godkännande.
6. Skapa inga PR till main förrän användaren bett om review. Vid PR: använd draft. Ingen auto-merge.
7. Kontrollera före varje commit att bara tillåtna filer har ändrats. Vid oväntade ändringar STOPPA och redovisa.
8. Ingen automatisk ombasering/reset/force-push; stäm av vid konflikter eller ändrat main.
9. Länkar från ny modellsida får peka mot redan existerande sidor; skapa inte obekräftade URL:er.
10. Om en ny sida får ett framtida canonical ska det vara https://skaraborgmaskin.se/maskinarkiv/<modell>.html. Ingen ändring av sitemap ännu.

## Innehållsstandard
- Projektfilen MASKINARKIVET-HUVUDMALL(1).txt är huvudstandard, särskilt godkända STIGA Villa 12 HST v5.
- Använd befintliga maskinarkiv/stiga-villa-12-hst.html och maskinarkiv/husqvarna-rider-13.html som tekniska förebilder.
- Research FÖRST: originalmanualer, produktnummer, reservdelskataloger, motor- och transmissionsdokumentation. Källstyrkta varianttabeller före HTML.
- Märk under arbetet uppgifter som verifierad primärkälla, stark sekundärkälla, osäker, okänd. Publicera inte gissade tekniska specifikationer, årsmodeller, kompabilitet eller typfel.
- Pedagogiskt språk, rikligt med faktiskt användbart innehåll, enkel orientering, innehållsförteckning (sticky desktop/utfällbar mobil), källknapp/modal, naturlig återbruks-CTA.
- Behåll etablerad grön/guldig design. Ingen global redesign.
- Testa fungerande header/footer från undermappsnivå, interna ankarlänkar, källänkar, mobil/responsivitet, HTML/JS, metadata/canonical och relativa sökvägar.

## Arbetsordning per chatt
1. Bekräfta rätt branch; läs denna plan och referensartiklar.
2. Gör källinventering och faktasammanställning, redovisa osäkra/versionberoende uppgifter.
3. Presentera struktur, kunskapsdjup och källor för användaren innan själva HTML-kodningen.
4. Bygg EN fullständig, fristående modellsida på egen branch när användaren godkänner.
5. Kontrollera ändrade filer och gör egen kvalitetssäkring; dela branchlänk, commit SHA, teststatus och återstående osäkerheter.
6. Låt koordinerande chatt granska kandidaterna och planera samlad integrering först efter att alla är klara.

## Kommunikation
Chattarna har inte en gemensam levande minnes-/arbetsyta. GitHub är den delade källan. Överlämning sker med branch + filväg + commit SHA + kort status. Den här koordinationsfilen uppdateras endast av koordinatorn på koordinatorgrenen.
