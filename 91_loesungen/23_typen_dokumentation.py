"""Musterlösung 23: Eine Funktion dokumentieren."""

def find_name(names: list[str], query: str) -> str | None:
    """Return the first case-insensitive exact match, or None if absent."""
    for name in names:
        if name.casefold() == query.casefold():
            return name
    return None
