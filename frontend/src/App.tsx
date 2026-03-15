import { FormEvent, useEffect, useState } from 'react'
import { fetchCases, predictCase, trainModel } from './services/api'
import { ClinicalCasePayload, PredictionResult, SavedCase } from './types/case'

const initialState: ClinicalCasePayload = { sexo: 'F', estado_reproductivo: 'esterilizado' }

export const App = () => {
  const [form, setForm] = useState<ClinicalCasePayload>(initialState)
  const [result, setResult] = useState<PredictionResult | null>(null)
  const [cases, setCases] = useState<SavedCase[]>([])
  const [loading, setLoading] = useState(false)

  const loadCases = async () => setCases(await fetchCases())
  useEffect(() => {
    void loadCases()
  }, [])

  const onSubmit = async (e: FormEvent) => {
    e.preventDefault()
    setLoading(true)
    try {
      const prediction = await predictCase(form)
      setResult(prediction)
      await loadCases()
    } finally {
      setLoading(false)
    }
  }

  const onTrain = async () => {
    setLoading(true)
    try {
      await trainModel()
      alert('Modelo reentrenado exitosamente')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="container">
      <h1>Plataforma Predictiva de Cáncer Canino</h1>
      <button onClick={onTrain} disabled={loading}>Reentrenar modelo</button>
      <section className="card">
        <h2>Ingreso clínico</h2>
        <form onSubmit={onSubmit} className="grid">
          <input placeholder="Edad" type="number" step="0.1" onChange={(e) => setForm({ ...form, edad: Number(e.target.value) })} />
          <input placeholder="Raza" onChange={(e) => setForm({ ...form, raza: e.target.value })} />
          <input placeholder="Peso" type="number" step="0.1" onChange={(e) => setForm({ ...form, peso: Number(e.target.value) })} />
          <input placeholder="Ubicación anatómica" onChange={(e) => setForm({ ...form, ubicacion_anatomica_tumor: e.target.value })} />
          <input placeholder="Velocidad crecimiento" onChange={(e) => setForm({ ...form, velocidad_crecimiento: e.target.value })} />
          <input placeholder="Diagnóstico citológico" onChange={(e) => setForm({ ...form, diagnostico_citologico: e.target.value })} />
          <input placeholder="Diagnóstico histopatológico" onChange={(e) => setForm({ ...form, diagnostico_histopatologico: e.target.value })} />
          <input placeholder="Índice mitótico" type="number" step="0.1" onChange={(e) => setForm({ ...form, indice_mitotico: Number(e.target.value) })} />
          <button type="submit" disabled={loading}>Predecir riesgo</button>
        </form>
      </section>

      {result && (
        <section className="card">
          <h2>Resultado predictivo</h2>
          <p>Probabilidad: <strong>{(result.probability * 100).toFixed(2)}%</strong></p>
          <p>Etiqueta: <strong>{result.predicted_label === 1 ? 'Alto riesgo' : 'Bajo riesgo'}</strong></p>
          <p>Modelo: {result.model_name}</p>
          <ul>
            {result.top_features.map((f) => <li key={f.feature}>{f.feature}: {f.value}</li>)}
          </ul>
        </section>
      )}

      <section className="card">
        <h2>Historial de casos</h2>
        <table>
          <thead><tr><th>ID</th><th>Raza</th><th>Edad</th><th>Probabilidad</th><th>Riesgo</th></tr></thead>
          <tbody>
            {cases.map((c) => (
              <tr key={c.id}><td>{c.id}</td><td>{c.raza ?? '-'}</td><td>{c.edad ?? '-'}</td><td>{c.riesgo_probabilidad ?? '-'}</td><td>{c.riesgo_etiqueta ?? '-'}</td></tr>
            ))}
          </tbody>
        </table>
      </section>
    </main>
  )
}
