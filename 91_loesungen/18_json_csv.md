# Lösung 18 · JSON-Notizen validieren

[Zur Aufgabe](../90_uebungen/18_json_csv.md) · [Zum Kapitel](../kapitel/18_json_csv.md)

## Eine mögliche Lösung

```python
import json

def parse_notes(text: str) -> list[dict[str, str]]:
    """Parse an exact list of title/text string records."""
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("Eine Liste wird erwartet")
    for note in data:
        if not isinstance(note, dict) or set(note) != {"title", "text"}:
            raise ValueError("Jede Notiz braucht genau title und text")
        if not all(isinstance(value, str) for value in note.values()):
            raise ValueError("Notizwerte müssen Strings sein")
    return data
```

## Warum funktioniert das?

Die Prüfung geschieht in einer Reihenfolge, die unzulässige Folgezugriffe vermeidet. `set(note)` betrachtet die Schlüssel. Erst nach der Feldprüfung werden die Werttypen geprüft.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 18 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
