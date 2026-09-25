"""Musterlösung 03: Suchtext normalisieren."""

def normalize_search(text: str) -> str:
    """Normalize surrounding whitespace and case for text search."""
    return text.strip().casefold()
