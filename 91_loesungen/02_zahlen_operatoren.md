# Lösung 02 · Minuten aufteilen

[Zur Aufgabe](../90_uebungen/02_zahlen_operatoren.md) · [Zum Kapitel](../kapitel/02_zahlen_operatoren.md)

## Eine mögliche Lösung

```python
def split_minutes(total: int) -> tuple[int, int]:
    """Split non-negative minutes into hours and remaining minutes."""
    if total < 0:
        raise ValueError("Minuten dürfen nicht negativ sein")
    return total // 60, total % 60
```

## Warum funktioniert das?

`// 60` zählt vollständige Stunden, `% 60` den Rest. Die Prüfung vor der Berechnung macht den erlaubten Wertebereich deutlich.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 02 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
