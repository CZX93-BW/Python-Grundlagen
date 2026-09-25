"""Musterlösung 11: Eine unabhängige Notizkopie."""

from copy import deepcopy

def copy_notes(notes: list[dict]) -> list[dict]:
    """Return an independent copy of simple nested note data."""
    return deepcopy(notes)
