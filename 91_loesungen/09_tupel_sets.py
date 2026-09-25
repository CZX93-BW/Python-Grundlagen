"""Musterlösung 09: Gemeinsame Fähigkeiten finden."""

def common_skills(first: list[str], second: list[str]) -> list[str]:
    """Return sorted, distinct values present in both lists."""
    return sorted(set(first) & set(second))
