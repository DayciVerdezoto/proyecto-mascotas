export type ClinicalCasePayload = {
  edad?: number
  raza?: string
  sexo?: string
  estado_reproductivo?: string
  peso?: number
  tamano_corporal?: string
  motivo_consulta?: string
  antecedentes_medicos_previos?: string
  masa_tumoral_previa?: boolean
  tiempo_evolucion_lesion?: number
  tratamientos_previos?: string
  numero_lesiones?: number
  ubicacion_anatomica_tumor?: string
  tamano_lesion?: number
  forma_tumor?: string
  consistencia?: string
  movilidad?: string
  bordes?: string
  velocidad_crecimiento?: string
  ulceracion?: boolean
  invasion_tejidos_cercanos?: boolean
  tipo_estudio_diagnostico?: string
  citologia_realizada?: boolean
  biopsia_realizada?: boolean
  histopatologia_realizada?: boolean
  diagnostico_citologico?: string
  diagnostico_histopatologico?: string
  tipo_tumor?: string
  grado_tumoral?: string
  indice_mitotico?: number
  pleomorfismo_celular?: string
  necrosis_tumoral?: boolean
  metastasis?: boolean
  compromiso_ganglionar?: boolean
  recurrencia_tumoral?: boolean
  progresion_enfermedad?: string
  pronostico_clinico?: string
  tipo_tratamiento?: string
  respuesta_tratamiento?: string
  seguimiento_clinico?: string
}

export type PredictionResult = {
  probability: number
  predicted_label: number
  model_name: string
  top_features: { feature: string; value: number }[]
}

export type SavedCase = ClinicalCasePayload & {
  id: number
  cancer_confirmado?: boolean
  riesgo_probabilidad?: number
  riesgo_etiqueta?: number
  created_at: string
}
