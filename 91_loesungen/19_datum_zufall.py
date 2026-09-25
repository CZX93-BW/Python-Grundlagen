"""Musterlösung 19: Datumsabstand bestimmen."""

from datetime import date

def days_between(start: str, end: str) -> int:
    """Return signed calendar days from start to end."""
    return (date.fromisoformat(end) - date.fromisoformat(start)).days
