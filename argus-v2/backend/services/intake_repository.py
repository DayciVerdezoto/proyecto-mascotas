from __future__ import annotations

import json

from sqlalchemy.orm import Session

from models.intake import ClinicalIntakeRecord


def save_intake(db: Session, filename: str, normalized_text: str, extracted_payload: dict) -> ClinicalIntakeRecord:
    record = ClinicalIntakeRecord(
        filename=filename,
        normalized_text=normalized_text,
        extracted_json=json.dumps(extracted_payload, ensure_ascii=False),
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
