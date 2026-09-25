"""Type Hints und verständliche Dokumentation: Einen Funktionsvertrag beschreiben."""

def average(numbers: list[float]) -> float | None:
    """Return the arithmetic mean, or None for an empty list."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

print(average([2.0, 4.0]))
print(average([]))
