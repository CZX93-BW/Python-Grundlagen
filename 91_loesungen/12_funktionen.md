# Lösung 12 · Durchschnitt berechnen

[Zur Aufgabe](../90_uebungen/12_funktionen.md) · [Zum Kapitel](../kapitel/12_funktionen.md)

## Eine mögliche Lösung

```python
def average(numbers: list[float]) -> float | None:
    """Return the mean, or None if no values were supplied."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
```

## Warum funktioniert das?

Die frühe Rückgabe verhindert Division durch null. Der Rückgabetyp dokumentiert, dass der Aufrufer ein fehlendes Ergebnis berücksichtigen muss.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 12 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
