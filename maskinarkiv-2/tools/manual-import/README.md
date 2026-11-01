# Maskinarkivet: manualimport

Kör lokalt (Windows PowerShell):

```powershell
py -m pip install "pymupdf>=1.23,<2"
py manual_import.py "C:\\Manualer" --output "C:\\Manualer\\_index"
```

Verktyget skapar `manuals.csv`, `sections.csv`, `review_candidates.csv` och `report.json`. Dessa är **granskningsunderlag**, inte automatiskt godkända fakta. Det upptäcker binärt identiska filer via SHA-256 och möjliga revisioner genom dokumentnummer på omslag. Bildbaserade PDF-sidor kräver manuell granskning; OCR utförs inte. PDF-sidnummer är 1-baserade och behöver inte motsvara tryckt sidnummer.

Kontrollera alltid exakt modell, BOM, serienummer och tillämplig utgåva innan uppgifter flyttas till `research/machines/*.json`. Käll-PDF:er lagras lokalt och ska inte publiceras i GitHub utan tillstånd. Körs helt utan nätverksanslutning.

För mer omfattande lokal testsvit finns ett separat ZIP-paket med importskript och unittest.