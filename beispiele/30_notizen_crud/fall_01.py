"""Deine Notizübung als saubere CRUD-Logik: Eine Notiz übergeben statt versteckt einlesen."""

def create_note(note_id, title, text):
    title = title.strip()
    text = text.strip()
    if not title or not text:
        raise ValueError("Titel und Text dürfen nicht leer sein")
    return {"id": note_id, "title": title, "text": text}

print(create_note("n1", " Einkauf ", " Milch "))
