# Meddelandesystem – teknisk plan (ej produktionsklart)

## Kundflöde
- Klick på "Skicka meddelande" på en annons.
- Ange namn, e-postadress och fråga, godkänn integritetsinformation.
- Validera Turnstile-token server-side.
- Skapa konversation + första meddelandet genom Edge Function.
- Returnera en slumpgenererad hemlig konversationstoken till kund; lagra endast hash server-side.
- Kunden kan fortsätta tråden med token via en säker konversationslänk. Denna länk är ett hemligt åtkomstbevis och ska inte delas. För borttappade länkar: separat, begränsat e-postbaserat återställningsflöde.

## Adminflöde
- Inbox med olästa trådar, annonsrubrik, datum och senaste meddelande.
- Admins är explicit registrerade i ad_editors och kan läsa/skriva via RLS.
- Svar från admin lagras i ad_messages och syns för kunden med giltig token.
- Stäng konversation, markera spam, blockera/rapportera vid behov.
- Avisering per e-post kräver separat e-postleverantör och säkra serverfunktioner.

## Skydd
- Cloudflare Turnstile verifieras på servern, aldrig endast i frontend.
- Begränsa per IP + ad + e-post, inklusive dagliga tak; fail closed om rate-limit-lagret är nere.
- Begränsa meddelandelängd till 3000 tecken och validera e-postadress.
- Honeypot-fält, svarslatens, anti-spam-logik och loggning utan meddelandetext/PII.
- Håll API-endpointen stängd tills dessa mekanismer är implementerade och testade.
- Förhindra spam i adminsvar: autentisering, medlemskap och RLS.
- GDPR: informera om ändamål, lagringstid, kontaktkanal, rätt till radering. Definiera gallring innan lansering.
- Kör negativa tester med anon, obehörig inloggad, manipulerad trådtoken, ogiltig CAPTCHA och överbelastning.

## Databas
Migration installerad i Supabase: ad_conversations, ad_messages. Inga anonyma policyer. Endast explicit auktoriserade admins får läsa meddelanden. Nästa iteration behöver server-endpoint, rate-limit storage, tokenhashfunktion och säkra transaktioner.

OBS: Publicera aldrig kundkommunikation eller token i GitHub. Den befintliga webbplatsen påverkas inte.
