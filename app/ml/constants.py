from __future__ import annotations

FEATURE_COLUMNS = [
    "edad",
    "raza",
    "sexo",
    "estado_reproductivo",
    "peso",
    "tamano_corporal",
    "motivo_consulta",
    "antecedentes_medicos_previos",
    "masa_tumoral_previa",
    "tiempo_evolucion_lesion",
    "tratamientos_previos",
    "numero_lesiones",
    "ubicacion_anatomica_tumor",
    "tamano_lesion",
    "forma_tumor",
    "consistencia",
    "movilidad",
    "bordes",
    "velocidad_crecimiento",
    "ulceracion",
    "invasion_tejidos_cercanos",
    "tipo_estudio_diagnostico",
    "citologia_realizada",
    "biopsia_realizada",
    "histopatologia_realizada",
    "diagnostico_citologico",
    "diagnostico_histopatologico",
    "tipo_tumor",
    "grado_tumoral",
    "indice_mitotico",
    "pleomorfismo_celular",
    "necrosis_tumoral",
    "metastasis",
    "compromiso_ganglionar",
    "recurrencia_tumoral",
    "progresion_enfermedad",
    "pronostico_clinico",
    "tipo_tratamiento",
    "respuesta_tratamiento",
    "seguimiento_clinico",
]

NUMERIC_FEATURES = [
    "edad",
    "peso",
    "tiempo_evolucion_lesion",
    "numero_lesiones",
    "tamano_lesion",
    "indice_mitotico",
]

TARGET_COLUMN = "cancer_confirmado"
MODEL_PATH = "app/ml/artifacts/model.joblib"
METRICS_PATH = "app/ml/artifacts/metrics.json"
