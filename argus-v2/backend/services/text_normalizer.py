from __future__ import annotations

import re
import unicodedata


class TextNormalizer:
    def normalize(self, raw_text: str) -> str:
        text = unicodedata.normalize("NFKC", raw_text or "")
        text = text.replace("\r", "\n")
        text = re.sub(r"\n{2,}", "\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r"[^\S\n]+", " ", text)
        return text.strip().lower()
