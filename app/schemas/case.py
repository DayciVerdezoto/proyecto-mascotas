from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CaseBase(BaseModel):
    edad: Optional[float] = Field(default=None, ge=0, le=30)
    raza: Optional[str] = None
    sexo: Optional[str] = None
    estado_reproductivo: Optional[str] = None
    peso: Optional[float] = Field(default=None, ge=0)
    tamano_corporal: Optional[str] = None
    motivo_consulta: Optional[str] = None
    antecedentes_medicos_previos: Optional[str] = None
    masa_tumoral_previa: Optional[bool] = None
    tiempo_evolucion_lesion: Optional[float] = Field(default=None, ge=0)
    tratamientos_previos: Optional[str] = None
    numero_lesiones: Optional[int] = Field(default=None, ge=0)
    ubicacion_anatomica_tumor: Optional[str] = None
    tamano_lesion: Optional[float] = Field(default=None, ge=0)
    forma_tumor: Optional[str] = None
    consistencia: Optional[str] = None
    movilidad: Optional[str] = None
    bordes: Optional[str] = None
    velocidad_crecimiento: Optional[str] = None
    ulceracion: Optional[bool] = None
    invasion_tejidos_cercanos: Optional[bool] = None
    tipo_estudio_diagnostico: Optional[str] = None
    citologia_realizada: Optional[bool] = None
    biopsia_realizada: Optional[bool] = None
    histopatologia_realizada: Optional[bool] = None
    diagnostico_citologico: Optional[str] = None
    diagnostico_histopatologico: Optional[str] = None
    tipo_tumor: Optional[str] = None
    grado_tumoral: Optional[str] = None
    indice_mitotico: Optional[float] = Field(default=None, ge=0)
    pleomorfismo_celular: Optional[str] = None
    necrosis_tumoral: Optional[bool] = None
    metastasis: Optional[bool] = None
    compromiso_ganglionar: Optional[bool] = None
    recurrencia_tumoral: Optional[bool] = None
    progresion_enfermedad: Optional[str] = None
    pronostico_clinico: Optional[str] = None
    tipo_tratamiento: Optional[str] = None
    respuesta_tratamiento: Optional[str] = None
    seguimiento_clinico: Optional[str] = None


class CaseCreate(CaseBase):
    cancer_confirmado: Optional[int] = Field(default=None, ge=0, le=1)


class CaseResponse(CaseBase):
    id: int
    cancer_confirmado: Optional[bool]
    riesgo_probabilidad: Optional[float]
    riesgo_etiqueta: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True


class PredictRequest(CaseBase):
    threshold: float = Field(default=0.5, ge=0, le=1)


class FeatureContribution(BaseModel):
    feature: str
    value: float


class PredictResponse(BaseModel):
    probability: float
    predicted_label: int
    model_name: str
    top_features: list[FeatureContribution]


class TrainResponse(BaseModel):
    selected_model: str
    metrics: dict
    artifact_path: str
