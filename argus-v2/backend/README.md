# ARGUS v2 Backend — Sprint 1 (CAN-2 / CAN-3)

Módulo de **Recolección de información clínica** para ingestar documentos y generar JSON clínico estructurado, con persistencia de resultados en PostgreSQL.

## Funcionalidades
- Carga de documentos clínicos (`.txt`, `.pdf`, imágenes).
- OCR y extracción de texto:
  - PDF con texto embebido (`pypdf`).
  - Fallback OCR para PDF/imagen (`pytesseract` + `PyMuPDF`/`Pillow`).
- Normalización de texto clínico.
- Extracción de entidades clínicas (spaCy + reglas regex fallback).
- Endpoint:
  - `POST /clinical/intake`

## Estructura
- `services/document_loader.py`
- `services/ocr_service.py`
- `services/text_normalizer.py`
- `services/clinical_extractor.py`
- `api/routes/clinical_intake.py`
- `main.py`

## Ejecución local
```bash
cd argus-v2/backend
python -m venv .venv
source .venv/bin/activate
pip install -r ../../requirements.txt
uvicorn main:app --reload --port 8010
```

## Ejemplo de uso
```bash
curl -X POST "http://localhost:8010/clinical/intake" \
  -F "file=@./ejemplo_protocolo.txt"
```

## Salida esperada (JSON)
```json
{
  "procedimiento": "",
  "tecnica": "",
  "organo": "",
  "lateralidad": "",
  "abordaje": "",
  "diagnosticos": [],
  "dispositivos": [],
  "hallazgos": "",
  "texto_original": ""
}
```

## Notas
- Este sprint **no codifica CPT**; solo estructura información clínica.
- Requiere binario Tesseract instalado en sistema para OCR por imagen.


## Base de datos
- Motor: PostgreSQL
- Configuración: `DATABASE_URL` en `.env` (ver `.env.example`).
- Tabla creada automáticamente: `clinical_intake_records`.
