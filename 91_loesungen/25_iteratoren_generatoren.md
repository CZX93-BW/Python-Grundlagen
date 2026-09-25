# Lösung 25 · Gerade Zahlen als Generator

[Zur Aufgabe](../90_uebungen/25_iteratoren_generatoren.md) · [Zum Kapitel](../kapitel/25_iteratoren_generatoren.md)

## Eine mögliche Lösung

```python
def even_numbers(limit: int):
    """Yield non-negative even integers below limit."""
    for number in range(0, limit, 2):
        yield number
```

## Warum funktioniert das?

Durch yield wird die Funktion zum Generator. Jeder Abruf produziert nur den nächsten Wert. Die exklusive Obergrenze von range() passt zur Aufgabenstellung.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 25 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
