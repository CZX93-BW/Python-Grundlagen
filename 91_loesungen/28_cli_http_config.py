"""Musterlösung 28: Boolesche Konfiguration lesen."""

def parse_bool(text: str) -> bool:
    """Parse an explicit set of true/false configuration strings."""
    normalized = text.strip().casefold()
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    raise ValueError("Unbekannter Wahrheitswert")
