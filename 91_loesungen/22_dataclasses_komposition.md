# Lösung 22 · Eine Task-Dataclass

[Zur Aufgabe](../90_uebungen/22_dataclasses_komposition.md) · [Zum Kapitel](../kapitel/22_dataclasses_komposition.md)

## Eine mögliche Lösung

```python
from dataclasses import dataclass, field

@dataclass
class Task:
    """Represent a task with independently owned default tags."""
    title: str
    done: bool = False
    tags: list[str] = field(default_factory=list)
```

## Warum funktioniert das?

Die Factory wird je Instanz aufgerufen. Die Dataclass erzeugt den Konstruktor und den inhaltlichen Vergleich; die Typangaben allein erzwingen keine Laufzeitvalidierung.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 22 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
