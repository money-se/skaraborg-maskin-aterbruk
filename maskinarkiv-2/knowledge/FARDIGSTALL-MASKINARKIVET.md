# Maskinarkivet – färdigställande före fler verktygsversioner

**Beslut:** Inga fler Manual Research-prototyper som huvudspår. Bygg vidare på existerande webbmallar, artiklar, `research/machines/*.json` och kontroller. Manualimport 1.x är ett **lokalt hjälpmedel**, aldrig en alternativ källa till sanning.

## Vad som redan finns
- Delad 11ty-maskinmall och fem maskinartiklar i förhandsgranskning: STIGA Park 16, Husqvarna Rider 13, Husqvarna LTH151, STIGA Villa 12 HST och Jonsered LT2115. Kontrollera aktuella antal i `scripts/check.mjs` och `scripts/audit-production.mjs`; README innehåller äldre pilotsteg.
- Kanoniska forskningsregister med A–M-områden, källor, fakta, öppna luckor och separata publiceringsgrindar.
- 40 lokala original-PDF:er är inventerade i `research/MANUAL-INBOX-2026-10-30.md`. PDF-bitarna ska inte publiceras i det offentliga repot.

## Blockerare i rätt ordning
1. **Klargör vad som faktiskt ska publiceras nu.** Publicera i första hand säkra befintliga maskinartiklar med tydliga undantag i stället för att vänta på att alla modellvarianter i världen verifieras. Befintlig artikeltext får inte behandlas som ny primärkälla.
2. **Kör lokalt från projektmappen:** `npm install`, `npm run build`, `npm run check`, `npm run audit`, `npm run research:check`. Notera resultat per kommando. GitHub Actions är en sekundär kontroll, inte enda facit.
3. **Åtgärda riktiga röda fel från dessa kontroller** i data, sidmallar och internlänkar. Sänk aldrig säkerhetsspärrar, påhitta källor eller ändra `status` för att få grönt test.
4. **Jämför de fem artiklarnas publicerbara claim-urval med respektive forskningsregister.** Markera tydligt påståenden som bara gäller vissa PNC/BOM/årsmodeller. Detta är viktigare än att importera alla 40 manualer i ett svep.
5. **Använd nya Hydro-Gear-manualer målinriktat för påståenden som blockerar artiklarna.** Matcha först komplett maskin-PNC och transmissionsetikett; slå inte ihop ZT-2200 med ZT-2800e, eller 2018 med 2024 års avtappningsvarianter.
6. **Färdigställ publiceringssidan och slutgranska visuellt** mobil, desktop, källor, navigering, kanonisk URL och gamla sidors omdirigeringar. Kontrollera att inga befintliga publicerade sidor skrivs över av misstag.
7. **Först därefter** utöka artikelutbudet och automatisera bredare manualforskning. Optimeringsmåttet är nya användbara, källsäkrade maskinartiklar, inte antal råträffar.

## Viktiga avgränsningar
- Ett registrerat A-claim bevisar inte en viss OEM-maskins transmission eller reservdel.
- Källsideträff är inte faktaverifiering.
- `needs_research` får inte tyst bli `ready`; `scoped_ready` kräver dokumenterat, begränsat ansvarsområde och godkännande enligt befintlig policy.
- Äldre forsknings-audit för Villa 12 HST är en historisk ögonblicksbild; räkna status från aktuell JSON och senaste checker innan slutsats.
- Pull Request #237 omfattar dokumentinkorg samt riktad ZT-2200-research; den ersätter inte separat releasegranskning av webben.

## När arkivet är redo för nästa steg
En maskinartikel räknas som färdig först när `build`, `check` och `audit` passerar lokalt, alla påståenden som publiceras är avgränsade och källspårade, publiceringsgrinden är uppfylld för det uttryckliga omfånget och en visuell kontroll av genererad artikel är gjord.
