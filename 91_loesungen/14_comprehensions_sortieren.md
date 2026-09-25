# Lösung 14 · Personen filtern und sortieren

[Zur Aufgabe](../90_uebungen/14_comprehensions_sortieren.md) · [Zum Kapitel](../kapitel/14_comprehensions_sortieren.md)

## Eine mögliche Lösung

```python
def adult_names(people: list[dict]) -> list[str]:
    """Return adult names sorted without case-sensitive ordering."""
    names = [person["name"] for person in people if person["age"] >= 18]
    return sorted(names, key=str.casefold)
```

## Warum funktioniert das?

Die Comprehension erzeugt eine neue Liste. Die Sortierfunktion ändert nur das Vergleichskriterium; die Namen im Ergebnis werden nicht kleingeschrieben.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 14 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
