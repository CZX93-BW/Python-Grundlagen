# Lösung 17 · Nicht leere Zeilen lesen

[Zur Aufgabe](../90_uebungen/17_dateien_pfade.md) · [Zum Kapitel](../kapitel/17_dateien_pfade.md)

## Eine mögliche Lösung

```python
from pathlib import Path

def read_nonempty_lines(path: Path) -> list[str]:
    """Return stripped non-empty UTF-8 lines; propagate file errors."""
    result = []
    with path.open(encoding="utf-8") as file:
        for line in file:
            clean = line.strip()
            if clean:
                result.append(clean)
    return result
```

## Warum funktioniert das?

Die Datei wird auch beim Auftreten eines Fehlers geschlossen. Das Weglassen einer leeren Zeile geschieht nach strip(), damit auch eine Zeile nur mit Leerzeichen leer zählt.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 17 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
