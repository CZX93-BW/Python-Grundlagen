"""Musterlösung 05: Positive Zahl aus Text lesen."""

def parse_positive(text: str) -> int:
    """Parse a positive integer, raising ValueError for invalid values."""
    value = int(text)
    if value <= 0:
        raise ValueError("Zahl muss positiv sein")
    return value
