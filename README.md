# Bilancino

Diario privato di calorie e peso, ispirato a DietAI. Nessun account, nessun server:
i dati restano nel telefono (memoria del browser). Funziona anche offline.

## Cosa fa
- Diario per pasto con obiettivo calorico e macro (calcolo Mifflin-St Jeor + livello di attività + ritmo di dimagrimento)
- Banca dati di ~90 alimenti italiani, i tuoi cibi salvati, recenti
- Codice a barre (foto o cifre) con Open Food Facts
- Stima da foto o descrizione con Claude, usando la tua chiave API Anthropic (facoltativa)
- Peso con grafico, media a 7 giorni, BMI e previsione di arrivo all'obiettivo
- Acqua, calorie degli ultimi 7 giorni, backup/ripristino JSON

## File
- `src/` sorgenti (app.js, app.css, foods.js, sw.js, manifest)
- `dist/` app pronta da pubblicare su un qualsiasi hosting HTTPS statico
- `preview.html` versione per l'anteprima su claude.ai
- `python3 build.py` rigenera `dist/` e `preview.html`

## Installare su Android
Carica il contenuto di `dist/` su un hosting HTTPS (GitHub Pages, Netlify, Cloudflare Pages),
apri l'indirizzo con Chrome e scegli "Installa app" / "Aggiungi a schermata Home".
Il codice è pubblico ma i dati no: restano sul telefono.
