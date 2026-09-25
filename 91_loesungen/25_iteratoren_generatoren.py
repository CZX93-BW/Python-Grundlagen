"""Musterlösung 25: Gerade Zahlen als Generator."""

def even_numbers(limit: int):
    """Yield non-negative even integers below limit."""
    for number in range(0, limit, 2):
        yield number
