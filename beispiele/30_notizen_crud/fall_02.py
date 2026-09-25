"""Deine Notizübung als saubere CRUD-Logik: Mit einer ID statt einem festen Index suchen."""

def find_note(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None

notes = [{"id": "n1", "title": "Einkauf"}]
print(find_note(notes, "n1"))
print(find_note(notes, "fehlt"))
