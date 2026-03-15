import axios from 'axios'
import { ClinicalCasePayload, PredictionResult, SavedCase } from '../types/case'

const client = axios.create({
  baseURL: import.meta.env.VITE_API_URL ?? 'http://localhost:8000'
})

export const predictCase = async (payload: ClinicalCasePayload): Promise<PredictionResult> => {
  const { data } = await client.post('/predict', payload)
  return data
}

export const fetchCases = async (): Promise<SavedCase[]> => {
  const { data } = await client.get('/cases')
  return data
}

export const trainModel = async (): Promise<{ selected_model: string; metrics: Record<string, unknown> }> => {
  const { data } = await client.post('/train')
  return data
}
