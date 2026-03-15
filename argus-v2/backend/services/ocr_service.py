from __future__ import annotations

import io
import logging
import tempfile
from pathlib import Path


class OCRError(Exception):
    pass


class OCRService:
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)

    def extract_text(self, content: bytes, extension: str) -> str:
        extension = extension.lower()
        if extension == ".txt":
            return content.decode("utf-8", errors="ignore")

        if extension == ".pdf":
            return self._extract_pdf(content)

        if extension in {".png", ".jpg", ".jpeg", ".tiff", ".bmp"}:
            return self._extract_image(content, extension)

        raise OCRError(f"No se puede procesar extensión: {extension}")

    def _extract_pdf(self, content: bytes) -> str:
        text = ""
        try:
            from pypdf import PdfReader

            reader = PdfReader(io.BytesIO(content))
            text = "\n".join((page.extract_text() or "") for page in reader.pages)
        except Exception as exc:
            self.logger.warning("No se pudo extraer texto directo de PDF: %s", exc)

        if text.strip():
            return text

        try:
            import fitz  # PyMuPDF
            from PIL import Image
            import pytesseract

            with tempfile.TemporaryDirectory() as tmp:
                pdf_path = Path(tmp) / "doc.pdf"
                pdf_path.write_bytes(content)
                doc = fitz.open(pdf_path)
                pages = []
                for page in doc:
                    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    pages.append(pytesseract.image_to_string(img, lang="spa+eng"))
                text = "\n".join(pages)
        except Exception as exc:
            raise OCRError(f"Error OCR en PDF: {exc}") from exc

        return text

    def _extract_image(self, content: bytes, extension: str) -> str:
        try:
            from PIL import Image
            import pytesseract

            with tempfile.NamedTemporaryFile(suffix=extension) as tmp:
                tmp.write(content)
                tmp.flush()
                image = Image.open(tmp.name)
                return pytesseract.image_to_string(image, lang="spa+eng")
        except Exception as exc:
            raise OCRError(f"Error OCR en imagen: {exc}") from exc
