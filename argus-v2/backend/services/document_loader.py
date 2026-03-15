from __future__ import annotations

from pathlib import Path

from fastapi import UploadFile


class DocumentLoaderError(Exception):
    pass


class DocumentLoader:
    SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".png", ".jpg", ".jpeg", ".tiff", ".bmp"}

    async def load(self, file: UploadFile) -> tuple[bytes, str]:
        filename = file.filename or "documento_sin_nombre"
        extension = Path(filename).suffix.lower()
        if extension not in self.SUPPORTED_EXTENSIONS:
            raise DocumentLoaderError(f"Formato no soportado: {extension}")

        content = await file.read()
        if not content:
            raise DocumentLoaderError("Archivo vacío")

        return content, extension
