# Plataforma Predictiva de Cáncer Canino (MVP)

## Objetivo
MVP funcional para estimar riesgo de cáncer canino con variables clínicas veterinarias estructuradas.
**Importante:** herramienta de apoyo clínico/investigación. No sustituye diagnóstico veterinario.

## Arquitectura
- `app/`: backend FastAPI modular (API, DB, schemas, servicios, ML).
- `data/sample/`: dataset sintético inicial.
- `scripts/`: utilidades (generación de dataset).
- `frontend/`: React + TypeScript (dashboard, formulario, resultados, historial).
- `docs/`: documentación técnica.
- `tests/`: pruebas básicas API.

## Stack
- Backend: FastAPI, SQLAlchemy, Pydantic, scikit-learn, pandas, joblib.
- DB: SQLite (MVP local).
- Frontend: React + TypeScript + Vite.

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Ejecución backend
```bash
uvicorn app.main:app --reload --port 8000
```

## Entrenamiento de modelo
1) Generar/re-generar dataset sintético:
```bash
python scripts/generate_synthetic_dataset.py
```
2) Entrenar:
```bash
curl -X POST "http://localhost:8000/train"
```

Se persiste en `app/ml/artifacts/model.joblib` y `metrics.json`.

## Ejecución frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend en `http://localhost:5173`.

## Uso API rápido
- Salud: `GET /health`
- Crear caso: `POST /cases`
- Listar casos: `GET /cases`
- Obtener caso: `GET /cases/{id}`
- Predicción: `POST /predict`
- Reentrenar: `POST /train`

Más detalle en `docs/api.md`.

## Tests
```bash
pytest -q
```

## Decisiones metodológicas
Implementadas en `docs/modeling.md`.

## ARGUS Sprint 1 (Recolección de información clínica)
Se incorporó un módulo nuevo en `argus-v2/backend` para ingesta de documentos clínicos, OCR, normalización de texto y extracción estructurada vía `POST /clinical/intake`. Ver `argus-v2/backend/README.md`.
