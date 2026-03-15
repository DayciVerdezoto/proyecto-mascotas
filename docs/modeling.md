# Modeling del MVP

## Objetivo
Predecir `cancer_confirmado` (1 cáncer confirmado, 0 lesión benigna/no cáncer).

## Variables
Se usan 40 variables clínicas veterinarias estructuradas (edad, raza, sexo, estado reproductivo, peso, características de lesión, estudios diagnósticos, hallazgos oncológicos, tratamiento y seguimiento).

## Pipeline
- Clasificación binaria.
- Split train/test estratificado (80/20).
- Imputación:
  - numéricas: mediana
  - categóricas: moda
- Escalado para numéricas (StandardScaler).
- One-Hot Encoding para categóricas.
- Modelos: Logistic Regression (baseline) y Random Forest.
- Validación cruzada de entrenamiento: 5 folds con ROC-AUC.
- Selección final: mayor ROC-AUC en test (desempate por F1).

## Métricas reportadas
- Accuracy
- Precision
- Recall
- F1
- ROC-AUC
- CV ROC-AUC (media)

## Explicabilidad MVP
- Si el modelo final es Logistic Regression: contribuciones por coeficientes.
- Si es Random Forest: aproximación de contribución por `feature_importances_` ponderada por valor transformado.

## Limitaciones
- Dataset sintético, no clínicamente validado.
- El output es soporte investigativo, no diagnóstico médico.
- Requiere validación externa con datos reales, control de sesgos y protocolo ético.
