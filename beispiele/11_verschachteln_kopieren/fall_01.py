"""Verschachtelte Daten und Kopien: Einen Datensatz in einer Liste ändern."""

notes = [
    {"title": "Einkauf", "text": "Milch"},
    {"title": "Arbeit", "text": "Anruf"},
]
notes[0]["title"] = "Wocheneinkauf"
for note in notes:
    print(note["title"])
