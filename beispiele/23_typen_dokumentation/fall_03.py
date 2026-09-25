"""Type Hints und verständliche Dokumentation: Verständliche Namen und klare Einheiten."""

MINUTES_PER_HOUR = 60

def hours_to_minutes(hours: int) -> int:
    """Convert non-negative whole hours to minutes.

    Raises:
        ValueError: If hours is negative.
    """
    if hours < 0:
        raise ValueError("hours darf nicht negativ sein")
    return hours * MINUTES_PER_HOUR

print(hours_to_minutes(2))
