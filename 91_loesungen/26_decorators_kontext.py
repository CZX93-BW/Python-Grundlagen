"""Musterlösung 26: Einen Rückgabewert dekorieren."""

from functools import wraps

def uppercase_result(function):
    """Uppercase a string result while preserving function metadata."""
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return wrapper
