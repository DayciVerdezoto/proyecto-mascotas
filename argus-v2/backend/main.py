from fastapi import FastAPI

from api.routes.clinical_intake import router as clinical_router
from core.logging_config import configure_logging
from db.session import Base, engine

configure_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ARGUS - Recolección de información clínica", version="0.1.0")
app.include_router(clinical_router)


@app.get('/health')
def health() -> dict:
    return {'status': 'ok'}
