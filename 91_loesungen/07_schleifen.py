"""Musterlösung 07: Gerade Zahlen summieren."""

def sum_even(numbers: list[int]) -> int:
    """Sum even integers without modifying the input."""
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total
