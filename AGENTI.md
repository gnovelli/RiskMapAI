# AGENTI.md

## Project Overview
**GeoGPT – Copilota dei Dati Territoriali Pubblici**  
Un prototipo per esplorare dataset geografici open (shapefile, GeoJSON, CSV geolocalizzati) tramite un’interfaccia in linguaggio naturale.  
Il progetto usa Python (≥3.10) con Streamlit o Jupyter/Gradio per la UI e sfrutta LLM locali o API per generare insight e filtri geospaziali.

## Setup rapido
1. Creare un ambiente virtuale:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Installare i pacchetti richiesti (da definire in `requirements.txt`, es. `streamlit`, `geopandas`, `folium`, `shapely`).
3. Opzionale: configurare chiavi/API per l’LLM (es. variabile `OPENAI_API_KEY` o equivalente).
4. Avviare l’app:
   ```bash
   streamlit run app.py
   ```
   oppure eseguire un notebook Jupyter/Gradio se previsto.

## Struttura consigliata
```
RiskMapAI/
├── app.py                # Entry point Streamlit
├── notebooks/            # Notebook esplorativi (opzionali)
├── data/                 # Link simbolici o README con i dataset usati (non commitare file di grandi dimensioni)
├── requirements.txt      # Pacchetti Python
└── AGENTI.md             # (questo file)
```

## Contribuire
- Usare branch con nome descrittivo (es. `feature/map-interface`).
- Commit in inglese, stile imperativo: "Add map layer filtering".
- Descrivere in ogni PR i dataset o le fonti open dati utilizzate.
- Mantenere il codice documentato e con docstring.
- Se si aggiungono script di test, utilizzare `pytest` e assicurarsi che i test passino prima di aprire una PR.

## Best practice
- Verificare la licenza dei dataset e includere i credit nel README o in una sezione dedicata.
- Non inserire direttamente file di grandi dimensioni (>50 MB) nel repository: usare link a fonti ufficiali o Git LFS.
- Utilizzare `.env` (non versionato) per credenziali e chiavi API.

