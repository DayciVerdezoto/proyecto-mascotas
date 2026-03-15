from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.ml.inference import ModelNotTrainedError, predict
from app.ml.training import train_models
from app.schemas.case import (
    CaseCreate,
    CaseResponse,
    PredictRequest,
    PredictResponse,
    TrainResponse,
)
from app.services.case_service import create_case, get_case, list_cases, update_prediction

router = APIRouter()


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}


@router.post("/cases", response_model=CaseResponse)
def create_case_endpoint(payload: CaseCreate, db: Session = Depends(get_db)) -> CaseResponse:
    case_data = payload.model_dump()
    case_data["cancer_confirmado"] = (
        bool(payload.cancer_confirmado) if payload.cancer_confirmado is not None else None
    )
    case = create_case(db, case_data)
    return case


@router.get("/cases", response_model=list[CaseResponse])
def list_cases_endpoint(db: Session = Depends(get_db)) -> list[CaseResponse]:
    return list_cases(db)


@router.get("/cases/{case_id}", response_model=CaseResponse)
def get_case_endpoint(case_id: int, db: Session = Depends(get_db)) -> CaseResponse:
    case = get_case(db, case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Caso no encontrado")
    return case


@router.post("/predict", response_model=PredictResponse)
def predict_endpoint(payload: PredictRequest, db: Session = Depends(get_db)) -> PredictResponse:
    try:
        result = predict(payload.model_dump(), payload.threshold)
    except ModelNotTrainedError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    case_data = payload.model_dump(exclude={"threshold"})
    case = create_case(db, case_data)
    update_prediction(db, case, result["probability"], result["predicted_label"])
    return result


@router.post("/train", response_model=TrainResponse)
def train_endpoint(dataset_path: str = "data/sample/canine_cancer_dataset.csv") -> TrainResponse:
    try:
        outcome = train_models(dataset_path)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Error entrenando modelo: {exc}") from exc
    return outcome
