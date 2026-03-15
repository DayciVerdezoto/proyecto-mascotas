from __future__ import annotations

import logging
import re


class ClinicalExtractor:
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.nlp = self._load_nlp()

    def _load_nlp(self):
        try:
            import spacy

            for model_name in ("es_core_news_md", "es_core_news_sm"):
                try:
                    return spacy.load(model_name)
                except Exception:
                    continue
            return spacy.blank("es")
        except Exception as exc:
            self.logger.warning("spaCy no disponible, usando regex fallback: %s", exc)
            return None

    def extract(self, text: str) -> dict:
        normalized = text or ""
        procedimientos = self._find_keywords(normalized, ["apendicectomia", "colecistectomia", "reseccion", "biopsia"])
        tecnicas = self._find_keywords(normalized, ["sutura", "anastomosis", "coagulacion", "reseccion en bloque"])
        organos = self._find_keywords(normalized, ["apendice", "vesicula", "colon", "higado", "rinon", "pulmon"])
        abordajes = self._find_keywords(normalized, ["abierto", "laparoscopico", "endoscopico"])
        lateralidad = self._extract_laterality(normalized)
        diagnosticos = self._extract_diagnostics(normalized)
        dispositivos = self._find_keywords(normalized, ["stent", "malla", "protesis", "cateter", "clip"])
        hallazgos = self._extract_hallazgos(normalized)

        return {
            "procedimiento": procedimientos[0] if procedimientos else "",
            "tecnica": tecnicas[0] if tecnicas else "",
            "organo": organos[0] if organos else "",
            "lateralidad": lateralidad,
            "abordaje": abordajes[0] if abordajes else "",
            "diagnosticos": diagnosticos,
            "dispositivos": dispositivos,
            "hallazgos": hallazgos,
            "texto_original": text,
        }

    @staticmethod
    def _find_keywords(text: str, keywords: list[str]) -> list[str]:
        found = []
        for k in keywords:
            if re.search(rf"\b{re.escape(k)}\b", text):
                found.append(k)
        return found

    @staticmethod
    def _extract_laterality(text: str) -> str:
        if "bilateral" in text:
            return "bilateral"
        if "derecha" in text or "derecho" in text:
            return "derecha"
        if "izquierda" in text or "izquierdo" in text:
            return "izquierda"
        return ""

    @staticmethod
    def _extract_diagnostics(text: str) -> list[str]:
        diagnostics = []
        patterns = [
            r"diagnostico principal[:\-]\s*([^\.\n]+)",
            r"dx principal[:\-]\s*([^\.\n]+)",
            r"diagnosticos? secundarios?[:\-]\s*([^\.\n]+)",
        ]
        for p in patterns:
            for m in re.findall(p, text):
                diagnostics.append(m.strip())
        seen = set()
        uniq = []
        for d in diagnostics:
            if d not in seen:
                uniq.append(d)
                seen.add(d)
        return uniq

    @staticmethod
    def _extract_hallazgos(text: str) -> str:
        match = re.search(r"hallazgos operatorios?[:\-]\s*([^\n]+)", text)
        return match.group(1).strip() if match else ""
