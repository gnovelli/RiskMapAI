# GeoGPT – Copilota dei Dati Territoriali Pubblici

This repository contains a prototype Streamlit application for exploring open geospatial datasets using natural language.

## Setup
Follow `AGENTS.md` for quick setup instructions. Create a Python virtual environment and install dependencies from `requirements.txt`.

Copy `.env.example` to `.env` and replace the placeholders with your own API keys. At minimum you should set `OPENAI_API_KEY`.

## Usage
Launch the application with Streamlit:

```bash
streamlit run app.py
```

The app expects geospatial datasets in the `data/` directory. Download open datasets (e.g. shapefiles or GeoJSON files) from official open data portals such as [dati.gov.it](https://www.dati.gov.it/) or [OpenStreetMap](https://www.openstreetmap.org/). Use symbolic links or small sample files to avoid committing large data. Remember to credit the data source and check its license as noted in `AGENTS.md`:

> Verificare la licenza dei dataset e includere i credit nel README o in una sezione dedicata.

## License
This project is licensed under the MIT License.
