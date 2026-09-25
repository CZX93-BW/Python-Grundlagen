# Lösung 30 · Notiz mit stabiler ID ändern

[Zur Aufgabe](../90_uebungen/30_notizen_crud.md) · [Zum Kapitel](../kapitel/30_notizen_crud.md)

## Eine mögliche Lösung

```python
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
```

## Warum funktioniert das?

Die Validierung vor der Änderung verhindert einen halbfertigen Zustand. Die stabile ID wählt den Datensatz unabhängig von seiner Position. Das vollständige Praxisprojekt ergänzt Speicherung und Oberfläche.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 30 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
