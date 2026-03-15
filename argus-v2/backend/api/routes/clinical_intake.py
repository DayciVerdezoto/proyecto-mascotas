from __future__ import annotations

import logging

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.clinical import ClinicalIntakeResponse
from services.clinical_extractor import ClinicalExtractor
from services.document_loader import DocumentLoader, DocumentLoaderError
from services.intake_repository import save_intake
from services.ocr_service import OCRError, OCRService
from services.text_normalizer import TextNormalizer

logger = logging.getLogger("clinical_intake")
router = APIRouter(prefix="/clinical", tags=["clinical"])

_loader = DocumentLoader()
_ocr = OCRService()
_normalizer = TextNormalizer()
_extractor = ClinicalExtractor()


@router.post("/intake", response_model=ClinicalIntakeResponse)
async def clinical_intake(file: UploadFile = File(...), db: Session = Depends(get_db)) -> ClinicalIntakeResponse:
    try:
        content, extension = await _loader.load(file)
        raw_text = _ocr.extract_text(content, extension)
        clean_text = _normalizer.normalize(raw_text)
        extracted = _extractor.extract(clean_text)
        save_intake(db, file.filename or "documento_sin_nombre", clean_text, extracted)
        logger.info("Documento procesado: %s", file.filename)
        return ClinicalIntakeResponse(**extracted)
    except DocumentLoaderError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except OCRError as exc:
        logger.exception("Error OCR")
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:  # noqa: BLE001
        logger.exception("Error procesando intake clínico")
        raise HTTPException(status_code=500, detail=f"Error interno: {exc}") from exc
