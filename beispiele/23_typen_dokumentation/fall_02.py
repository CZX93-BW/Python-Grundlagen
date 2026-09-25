"""Type Hints und verständliche Dokumentation: Strukturierte Dictionaries beschreiben."""

from typing import TypedDict

class NoteData(TypedDict):
    title: str
    text: str

def summarize(note: NoteData) -> str:
    return f"{note['title']}: {note['text']}"

print(summarize({"title": "Python", "text": "Üben"}))
