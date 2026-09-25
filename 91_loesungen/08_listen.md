# Lösung 08 · Doppelte Einträge entfernen

[Zur Aufgabe](../90_uebungen/08_listen.md) · [Zum Kapitel](../kapitel/08_listen.md)

## Eine mögliche Lösung

```python
def unique_items(items: list[str]) -> list[str]:
    """Return first occurrences in their original order."""
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
```

## Warum funktioniert das?

Diese bewusst einfache Lösung prüft die bisherige Ergebnisliste. Für große Mengen kann ein zusätzliches Set die Suche beschleunigen. Ein bloßes `list(set(items))` erfüllt die Reihenfolgeanforderung nicht.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 08 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
