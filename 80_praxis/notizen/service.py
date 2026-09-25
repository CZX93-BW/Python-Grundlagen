"""Validate and manipulate notes without terminal or filesystem access."""
from uuid import uuid4

Note = dict[str, str]

def validate_notes(value: object) -> list[Note]:
    """Validate exact note fields and unique IDs; return independent records."""
    if not isinstance(value, list):
        raise ValueError("Die Notizdatei muss eine Liste enthalten.")
    result = []
    seen_ids = set()
    for note in value:
        if not isinstance(note, dict) or set(note) != {"id", "title", "text"}:
            raise ValueError("Jede Notiz braucht genau id, title und text.")
        if not all(isinstance(item, str) and item.strip() for item in note.values()):
            raise ValueError("Notizfelder müssen nicht leere Texte sein.")
        if note["id"] in seen_ids:
            raise ValueError("Die Notizdatei enthält doppelte IDs.")
        seen_ids.add(note["id"])
        result.append(note.copy())
    return result

def clean_content(title: str, text: str) -> tuple[str, str]:
    """Strip text fields and reject empty content."""
    title, text = title.strip(), text.strip()
    if not title or not text:
        raise ValueError("Titel und Text dürfen nicht leer sein.")
    return title, text

def add_note(notes: list[Note], title: str, text: str) -> Note:
    """Append a validated note with a unique ID; return that note."""
    title, text = clean_content(title, text)
    existing_ids = {note["id"] for note in notes}
    note_id = uuid4().hex
    while note_id in existing_ids:
        note_id = uuid4().hex
    note = {"id": note_id, "title": title, "text": text}
    notes.append(note)
    return note

def find_note(notes: list[Note], note_id: str) -> Note:
    """Return a matching record, or raise KeyError if it is missing."""
    for note in notes:
        if note["id"] == note_id:
            return note
    raise KeyError(f"Notiz nicht gefunden: {note_id}")

def update_note(notes: list[Note], note_id: str, title: str, text: str) -> Note:
    """Validate both fields before modifying the selected record."""
    title, text = clean_content(title, text)
    note = find_note(notes, note_id)
    note.update({"title": title, "text": text})
    return note

def delete_note(notes: list[Note], note_id: str) -> Note:
    """Remove the record with a stable ID, or raise KeyError."""
    for index, note in enumerate(notes):
        if note["id"] == note_id:
            return notes.pop(index)
    raise KeyError(f"Notiz nicht gefunden: {note_id}")
