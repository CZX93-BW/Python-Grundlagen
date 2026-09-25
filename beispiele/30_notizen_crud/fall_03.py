"""Deine Notizübung als saubere CRUD-Logik: Löschen ohne gefährlichen Indexzugriff."""

def delete_note(notes, note_id):
    for index, note in enumerate(notes):
        if note["id"] == note_id:
            return notes.pop(index)
    raise KeyError(f"Notiz nicht gefunden: {note_id}")

notes = [{"id": "n1", "title": "Einkauf"}]
print(delete_note(notes, "n1"))
print(notes)
try:
    delete_note(notes, "n1")
except KeyError:
    print("Notiz fehlt")
