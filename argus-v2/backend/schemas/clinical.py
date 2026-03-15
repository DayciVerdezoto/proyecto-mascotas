from pydantic import BaseModel


class ClinicalIntakeResponse(BaseModel):
    procedimiento: str = ""
    tecnica: str = ""
    organo: str = ""
    lateralidad: str = ""
    abordaje: str = ""
    diagnosticos: list[str] = []
    dispositivos: list[str] = []
    hallazgos: str = ""
    texto_original: str = ""
