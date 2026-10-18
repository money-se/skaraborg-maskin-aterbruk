# Annonsadmin: Supabase version 3 (ej produktionssatt)

Syfte: tre individuella konton (Robin, bror, pappa); publika annonser på skaraborgmaskin.se, privata ändringar via admin. Den godkända lokala prototypen ligger kvar separat tills detta är testat.

## Säker ordning
1. Skapa ett eget Supabase-projekt. Anslut Supabase till ChatGPT om du vill att jag ska kunna verifiera och hantera projektet direkt.
2. Skapa en **public** Storage-bucket `ad-images`. Sätt rimliga filstorleks- och MIME-begränsningar (JPEG, PNG, WebP).
3. Kör `supabase/annonsadmin-schema.sql` i SQL Editor på det valda projektet.
4. Skapa tre Auth-användare med individuella inloggningar. Stäng av öppen självregistrering eller säkra att endast inbjudna kan logga in. Efter identifiering: lägg EXAKT dessa tre Auth-user-UUID:n i `public.ad_editors`. Ge INTE adminbehörighet till alla autentiserade konton.
5. Kontrollera RLS manuellt: anonym kan läsa endast publicerade sale/pending; anonym kan inte skriva; inloggad icke-redaktör kan inte se arkiv, skapa eller ändra; redaktör kan skapa, ändra och arkivera.
6. Testa uppladdning, bildvisning, borttagning och behörigheter. Koppla först därefter adminkod samt publik läsvy.
7. Publicera admin och butikssida först efter test, använd HTTPS. Säkerhetsuppgifter hanteras via Supabase – aldrig i källkod eller chat.

## Datamodell
`ads`: title, description, price_sek, status = sale/pending/sold, published, image_paths, created_by, timestamps.
`ad_editors`: explicit allowlist med auth.uid (endast serveradministratör fyller på).
Sålda annonser är kvar för redaktörer, men osynliga för anonyma besökare.

OBS: Bild-bucket är offentlig och därmed är bildfiler med känd URL offentliga även om annonsen ändras till såld. Lägg aldrig upp kunduppgifter, kvitton eller annan privat information. Om bilder måste bli otillgängliga efter försäljning krävs privat bucket och signerade URL:er eller borttagning. Eventuell lagring av inköpspriser/vinst ska ske i EN ANNAN skyddad tabell, aldrig i `ads`.

## Tekniskt nästa steg
Använd `supabase-js` med **publishable/anon** nyckel i webbläsaren; RLS är den faktiska åtkomstkontrollen. Använd aldrig secret/service_role client-side. Välj kundvy och adminpanel som separata appar, gärna på subdomän för admin. `index.html` och befintliga Tradera/Shopify-sidor påverkas inte i detta steg.

## Kontrollfrågor inför produktion
- Ska offentliga annonser som är Väntande synas med märkning? (nu: ja)
- Ska bilder på Såld ligga kvar offentligt som URL? (nu: ja, annonserna döljs)
- Kontaktväg för köpare (telefon, e-post, formulär) behöver väljas innan publicering.
