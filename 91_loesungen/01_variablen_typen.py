"""Musterlösung 01: Begrüßung zusammensetzen."""

def greeting(name: str, language: str) -> str:
    """Return a greeting for de or en; reject unsupported languages."""
    if language == "de":
        return f"Hallo {name}"
    if language == "en":
        return f"Hello {name}"
    raise ValueError("Unbekannte Sprache")
