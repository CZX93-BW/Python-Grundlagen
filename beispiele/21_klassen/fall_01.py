"""Klassen, Objekte und Methoden: Ein einfaches Objekt bauen."""

class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def summary(self):
        return f"{self.title}: {self.text}"

note = Note("Einkauf", "Milch")
print(note.summary())
note.title = "Wochenende"
print(note.summary())
