from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Plataforma Predictiva de Cáncer Canino"
    database_url: str = "sqlite:///./canine_cancer.db"
    model_artifact_path: str = "app/ml/artifacts/model.joblib"
    metrics_artifact_path: str = "app/ml/artifacts/metrics.json"
    default_threshold: float = 0.5

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
