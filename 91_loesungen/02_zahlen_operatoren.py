"""Musterlösung 02: Minuten aufteilen."""

def split_minutes(total: int) -> tuple[int, int]:
    """Split non-negative minutes into hours and remaining minutes."""
    if total < 0:
        raise ValueError("Minuten dürfen nicht negativ sein")
    return total // 60, total % 60
