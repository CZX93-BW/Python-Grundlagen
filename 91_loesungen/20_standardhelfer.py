"""Musterlösung 20: Artikelnummer prüfen."""

import re

def is_article_code(text: str) -> bool:
    """Check the complete ASCII pattern AA-000."""
    return re.fullmatch(r"[A-Z]{2}-[0-9]{3}", text) is not None
