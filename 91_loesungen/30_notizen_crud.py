"""Musterlösung 30: Notiz mit stabiler ID ändern."""

def update_note(notes: list[dict], note_id: str, title: str, text: str) -> dict:
    """Validate content, then update the matching note in place."""
    title, text = title.strip(), text.strip()
    if not title or not text:
        raise ValueError("Titel und Text dürfen nicht leer sein")
    for note in notes:
        if note["id"] == note_id:
            note.update({"title": title, "text": text})
            return note
    raise KeyError(note_id)
