# Lösung 21 · Ein Zähler als Klasse

[Zur Aufgabe](../90_uebungen/21_klassen.md) · [Zum Kapitel](../kapitel/21_klassen.md)

## Eine mögliche Lösung

```python
class Counter:
    """Keep an independent, resettable count per instance."""
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

    def reset(self):
        self.value = 0
```

## Warum funktioniert das?

Jeder Konstruktoraufruf initialisiert die eigene Instanz. `reset()` braucht kein ausdrückliches return, wenn None die gewünschte Rückgabe ist.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 21 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
