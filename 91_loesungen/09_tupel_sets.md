# Lösung 09 · Gemeinsame Fähigkeiten finden

[Zur Aufgabe](../90_uebungen/09_tupel_sets.md) · [Zum Kapitel](../kapitel/09_tupel_sets.md)

## Eine mögliche Lösung

```python
def common_skills(first: list[str], second: list[str]) -> list[str]:
    """Return sorted, distinct values present in both lists."""
    return sorted(set(first) & set(second))
```

## Warum funktioniert das?

Die Sets entfernen Duplikate und die Schnittmenge beschränkt das Ergebnis auf gemeinsame Werte. `sorted()` liefert die verlangte stabile Reihenfolge als Liste.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 09 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
