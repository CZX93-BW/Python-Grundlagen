# Lösung 19 · Datumsabstand bestimmen

[Zur Aufgabe](../90_uebungen/19_datum_zufall.md) · [Zum Kapitel](../kapitel/19_datum_zufall.md)

## Eine mögliche Lösung

```python
from datetime import date

def days_between(start: str, end: str) -> int:
    """Return signed calendar days from start to end."""
    return (date.fromisoformat(end) - date.fromisoformat(start)).days
```

## Warum funktioniert das?

Die Datumsbibliothek behandelt Monats- und Jahresgrenzen. Die Reihenfolge der Subtraktion bestimmt das Vorzeichen.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 19 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
