# Lösung 11 · Eine unabhängige Notizkopie

[Zur Aufgabe](../90_uebungen/11_verschachteln_kopieren.md) · [Zum Kapitel](../kapitel/11_verschachteln_kopieren.md)

## Eine mögliche Lösung

```python
from copy import deepcopy

def copy_notes(notes: list[dict]) -> list[dict]:
    """Return an independent copy of simple nested note data."""
    return deepcopy(notes)
```

## Warum funktioniert das?

Die tiefe Kopie kopiert die verschachtelten Standarddaten mit. Die Aufgabe enthält bewusst keine offenen Dateien oder anderen externen Ressourcen.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 11 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
