# Maskinarkivet 3.0 – manualbaserad insamling (pilot)

Datum: 2026-10-30. Detta är ett komplement till befintlig forskningspolicy, inte ett nytt parallellt faktaregister.

## Arbetsflöde
1. Läs senaste main, gemensam policy, källindex och berörda modellregister.
2. Inventera befintliga `sources` innan ny dokumentjakt; jämför dokumentnummer, utgåva, språk och fil/URL, inte bara titel.
3. Sök tillverkarnas originalmanualer först och erbjud användaren samlade nedladdningslänkar. Var tydlig med om länken är verifierad som fungerande PDF, en nedladdningssida eller en äldre registrerad länk.
4. Användaren hämtar manualerna och laddar upp dem i chatten. Spara inte upphovsrättsskyddade PDF:er i det publika repositoriet utan rättighet/grund.
5. Kontrollera dokumentidentitet, modell, produktnummer, marknad, revision och eventuell serienummerintervall **innan** några tekniska slutsatser.
6. Extrahera källbundna uppgifter i satser med sida/figur/tabell och exakt tillämpbar variant; markera `verified`, `needs_verification` eller `rejected`.
7. Spara verifierade tekniska fakta enbart i respektive `research/machines/<slug>.json` (befintligt `sources`/`topics`/`claims`/`gaps`/`scopedRelease`-schema). Vid sidofynd: lägg bara hänvisning i SHARED-KNOWLEDGE-INDEX, inte dubblerade fakta.
8. Behåll `needs_research` och forskningsluckor om grinden inte är uppfylld; ingen automatisk artikelpublicering.
9. Arbeta i separat gren, kontrollera parallella ändringar, kör `scripts/check-research.mjs` för faktiska registerändringar och öppna PR med testresultat.

## Dokumentbeställning – minimifält
- Dokumenttitel, tillverkare, kategori (bruksanvisning / service / delar / sprängskiss)
- Berörd modellfamilj och uttryckliga versions-/serienummergränser eller `ej fastställt`
- Dokumentnummer, revision och språk (om kända)
- Länk och ursprunglig domän
- Länkstatus: `direct_pdf_verified`, `manufacturer_download_page` eller `unverified_legacy_link`
- Match mot befintliga registrerade källor, prioritet och kommentar om variantkontroll

## Pilot: länklista (inte tekniska verifieringsclaims)
| Dokument | Typ | Länkstatus | URL |
| --- | --- | --- | --- |
| Hydro-Gear ZT-2100 / ZT-2200 EZT BLN-52622 | Service- och reparationsmanual | direct_pdf_verified | https://www.hydro-gear.com/wp-content/uploads/2021/09/BLN-52622_ZT2100_ZT2200-1-1.pdf |
| Hydro-Gear manualbibliotek | Nedladdningssida för flera transmissioner | manufacturer_download_page | https://www.hydro-gear.com/service-repair-manuals/ |
| Honda GX160 instruktionsböcker (serienummerstyrda) | Nedladdningssida | manufacturer_download_page | https://engines.honda.com/support-and-service/owners-manuals/gx160 |
| STIGA Villa HST 2011/2012 | Reservdelskatalog, befintlig källa i Villa-register | unverified_legacy_link | https://view.stiga-store.com/files/SSPL2011_20110214_Villa_HST.pdf |
| STIGA Villa HST 2010 | Reservdelskatalog, befintlig källa i Villa-register | unverified_legacy_link | https://view.stiga-store.com/files/SSPL2010_20100208_Villa_HST.pdf |

Listan anger enbart var dokument kan hämtas. Inga tekniska modellpåståenden är verifierade utifrån filerna i denna pilot.
