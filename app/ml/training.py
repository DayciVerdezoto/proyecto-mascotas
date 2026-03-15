from __future__ import annotations

import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from app.config import settings
from app.ml.constants import FEATURE_COLUMNS, NUMERIC_FEATURES, TARGET_COLUMN


def _build_preprocessor(categorical_features: list[str]) -> ColumnTransformer:
    numeric_pipeline = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    return ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, NUMERIC_FEATURES),
            ("cat", categorical_pipeline, categorical_features),
        ]
    )


def _evaluate_model(model: Pipeline, x_test: pd.DataFrame, y_test: pd.Series) -> dict:
    y_pred = model.predict(x_test)
    y_prob = model.predict_proba(x_test)[:, 1]
    return {
        "accuracy": round(float(accuracy_score(y_test, y_pred)), 4),
        "precision": round(float(precision_score(y_test, y_pred, zero_division=0)), 4),
        "recall": round(float(recall_score(y_test, y_pred, zero_division=0)), 4),
        "f1": round(float(f1_score(y_test, y_pred, zero_division=0)), 4),
        "roc_auc": round(float(roc_auc_score(y_test, y_prob)), 4),
    }


def train_models(dataset_path: str) -> dict:
    df = pd.read_csv(dataset_path)
    missing = set(FEATURE_COLUMNS + [TARGET_COLUMN]) - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas en dataset: {missing}")

    x = df[FEATURE_COLUMNS].copy()
    y = df[TARGET_COLUMN].astype(int)

    categorical_features = [c for c in FEATURE_COLUMNS if c not in NUMERIC_FEATURES]
    preprocessor = _build_preprocessor(categorical_features)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    candidates = {
        "logistic_regression": LogisticRegression(max_iter=2000),
        "random_forest": RandomForestClassifier(n_estimators=300, random_state=42, class_weight="balanced"),
    }

    results = {}
    trained = {}
    for name, estimator in candidates.items():
        pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", estimator)])
        pipeline.fit(x_train, y_train)
        cv = cross_val_score(pipeline, x_train, y_train, cv=5, scoring="roc_auc")
        metrics = _evaluate_model(pipeline, x_test, y_test)
        metrics["cv_roc_auc_mean"] = round(float(cv.mean()), 4)
        results[name] = metrics
        trained[name] = pipeline

    selected_model_name = max(results.keys(), key=lambda k: (results[k]["roc_auc"], results[k]["f1"]))
    selected_model = trained[selected_model_name]

    artifact = {
        "model": selected_model,
        "model_name": selected_model_name,
        "feature_columns": FEATURE_COLUMNS,
        "numeric_features": NUMERIC_FEATURES,
        "metrics": results,
    }

    model_path = Path(settings.model_artifact_path)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, model_path)

    metrics_path = Path(settings.metrics_artifact_path)
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text(
        json.dumps(
            {
                "selected_model": selected_model_name,
                "metrics": results,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    return {"selected_model": selected_model_name, "metrics": results, "artifact_path": str(model_path)}
