# API del MVP

Base URL local: `http://localhost:8000`

## GET /health
Verifica disponibilidad.

## POST /cases
Registra caso clínico.

Ejemplo:
```json
{
  "edad": 10,
  "raza": "Labrador",
  "peso": 27.5,
  "velocidad_crecimiento": "rapido",
  "diagnostico_citologico": "sospechoso"
}
```

## GET /cases
Lista historial de casos.

## GET /cases/{id}
Obtiene detalle de caso.

## POST /predict
Predice riesgo y guarda caso.

Ejemplo:
```json
{
  "edad": 12,
  "raza": "Boxer",
  "peso": 31,
  "diagnostico_citologico": "maligno",
  "indice_mitotico": 10,
  "threshold": 0.5
}
```

Respuesta:
```json
{
  "probability": 0.86,
  "predicted_label": 1,
  "model_name": "random_forest",
  "top_features": [
    {"feature": "cat__diagnostico_citologico_maligno", "value": 0.04}
  ]
}
```

## POST /train
Entrena/reentrena modelos desde `data/sample/canine_cancer_dataset.csv`.
Parámetro opcional query: `dataset_path`.
