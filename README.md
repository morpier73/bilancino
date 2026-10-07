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
- `index.html`, `sw.js`, `manifest.webmanifest`, icone: app pronta (GitHub Pages)
- `preview.html` (non versionato) versione per l'anteprima su claude.ai
- `python3 build.py` rigenera i file dell'app e `preview.html`

## Installare su Android
Apri https://morpier73.github.io/bilancino/ con Chrome e scegli "Installa app",
oppure installa l'APK (sotto).
Il codice è pubblico ma i dati no: restano sul telefono.

## APK Android
Ogni push su `main` compila l'APK (cartella `android-app/`, Capacitor) con GitHub Actions
e lo pubblica nelle Release: https://github.com/morpier73/bilancino/releases/latest
L'APK è firmato con `android-app/debug.keystore` (creata dal primo giro di Actions),
sempre la stessa chiave, così gli aggiornamenti si installano sopra senza perdere i dati.
Il workflow rigenera anche `index.html` e gli altri file della web app da `src/`.
