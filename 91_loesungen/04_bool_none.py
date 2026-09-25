"""Musterlösung 04: Fehlende Werte ergänzen."""

def use_default(value, default):
    """Replace only None, preserving valid falsy values."""
    return default if value is None else value
