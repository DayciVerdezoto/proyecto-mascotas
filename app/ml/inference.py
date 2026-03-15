from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd

from app.config import settings
from app.ml.constants import FEATURE_COLUMNS


class ModelNotTrainedError(Exception):
    pass


def load_artifact() -> dict:
    path = Path(settings.model_artifact_path)
    if not path.exists():
        raise ModelNotTrainedError("No hay modelo entrenado. Ejecuta /train primero.")
    return joblib.load(path)


def _top_features(artifact: dict, row: pd.DataFrame, top_n: int = 5) -> list[dict]:
    pipeline = artifact["model"]
    model = pipeline.named_steps["model"]
    preprocessor = pipeline.named_steps["preprocessor"]
    feature_names = preprocessor.get_feature_names_out().tolist()
    transformed = preprocessor.transform(row)
    if hasattr(transformed, "toarray"):
        transformed = transformed.toarray()
    transformed_row = transformed[0]

    if hasattr(model, "coef_"):
        contributions = transformed_row * model.coef_[0]
    else:
        importances = getattr(model, "feature_importances_", None)
        if importances is None:
            return []
        contributions = transformed_row * importances

    pairs = sorted(zip(feature_names, contributions), key=lambda x: abs(x[1]), reverse=True)[:top_n]
    return [{"feature": name, "value": round(float(value), 4)} for name, value in pairs]


def predict(case_payload: dict, threshold: float = 0.5) -> dict:
    artifact = load_artifact()
    model = artifact["model"]

    row_dict = {col: case_payload.get(col) for col in FEATURE_COLUMNS}
    row = pd.DataFrame([row_dict])
    probability = float(model.predict_proba(row)[0][1])
    predicted_label = int(probability >= threshold)
    top_features = _top_features(artifact, row)

    return {
        "probability": round(probability, 4),
        "predicted_label": predicted_label,
        "model_name": artifact["model_name"],
        "top_features": top_features,
    }
