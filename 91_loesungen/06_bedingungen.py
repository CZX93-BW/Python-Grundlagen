"""Musterlösung 06: Punktestand einordnen."""

def classify_score(points: int) -> str:
    """Classify a score from zero to one hundred."""
    if not 0 <= points <= 100:
        raise ValueError("Punkte müssen zwischen 0 und 100 liegen")
    if points >= 90:
        return "sehr gut"
    if points >= 60:
        return "bestanden"
    return "weiter üben"
