"""Musterlösung 12: Durchschnitt berechnen."""

def average(numbers: list[float]) -> float | None:
    """Return the mean, or None if no values were supplied."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
