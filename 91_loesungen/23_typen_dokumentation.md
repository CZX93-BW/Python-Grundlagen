# Lösung 23 · Eine Funktion dokumentieren

[Zur Aufgabe](../90_uebungen/23_typen_dokumentation.md) · [Zum Kapitel](../kapitel/23_typen_dokumentation.md)

## Eine mögliche Lösung

```python
def find_name(names: list[str], query: str) -> str | None:
    """Return the first case-insensitive exact match, or None if absent."""
    for name in names:
        if name.casefold() == query.casefold():
            return name
    return None
```

## Warum funktioniert das?

Die Funktion sucht einen vollständigen Namen und keinen Teilstring. Die Union-Typangabe und die Docstring erklären denselben Vertrag aus unterschiedlichen Blickwinkeln.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 23 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
