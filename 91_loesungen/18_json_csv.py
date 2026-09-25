"""Musterlösung 18: JSON-Notizen validieren."""

import json

def parse_notes(text: str) -> list[dict[str, str]]:
    """Parse an exact list of title/text string records."""
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("Eine Liste wird erwartet")
    for note in data:
        if not isinstance(note, dict) or set(note) != {"title", "text"}:
            raise ValueError("Jede Notiz braucht genau title und text")
        if not all(isinstance(value, str) for value in note.values()):
            raise ValueError("Notizwerte müssen Strings sein")
    return data
