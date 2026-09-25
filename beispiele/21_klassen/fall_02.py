"""Klassen, Objekte und Methoden: Zustände pro Instanz trennen."""

class Notebook:
    def __init__(self):
        self.notes = []

    def add(self, title):
        self.notes.append(title)

first = Notebook()
second = Notebook()
first.add("Python lernen")
print(first.notes)
print(second.notes)
