# Lösung 07 · Gerade Zahlen summieren

[Zur Aufgabe](../90_uebungen/07_schleifen.md) · [Zum Kapitel](../kapitel/07_schleifen.md)

## Eine mögliche Lösung

```python
def sum_even(numbers: list[int]) -> int:
    """Sum even integers without modifying the input."""
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total
```

## Warum funktioniert das?

Der Anfangswert 0 passt auch zu einer leeren Liste. Jede passende Zahl wird addiert; Lesen und Summieren ändern die ursprüngliche Sammlung nicht.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 07 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
