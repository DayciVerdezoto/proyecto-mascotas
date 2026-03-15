from __future__ import annotations

from sqlalchemy.orm import Session

from app.models.case import ClinicalCase


def create_case(db: Session, payload: dict) -> ClinicalCase:
    case = ClinicalCase(**payload)
    db.add(case)
    db.commit()
    db.refresh(case)
    return case


def list_cases(db: Session) -> list[ClinicalCase]:
    return db.query(ClinicalCase).order_by(ClinicalCase.created_at.desc()).all()


def get_case(db: Session, case_id: int) -> ClinicalCase | None:
    return db.query(ClinicalCase).filter(ClinicalCase.id == case_id).first()


def update_prediction(db: Session, case: ClinicalCase, probability: float, label: int) -> ClinicalCase:
    case.riesgo_probabilidad = probability
    case.riesgo_etiqueta = label
    db.add(case)
    db.commit()
    db.refresh(case)
    return case
