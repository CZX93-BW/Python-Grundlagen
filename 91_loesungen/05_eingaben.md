# Lösung 05 · Positive Zahl aus Text lesen

[Zur Aufgabe](../90_uebungen/05_eingaben.md) · [Zum Kapitel](../kapitel/05_eingaben.md)

## Eine mögliche Lösung

```python
def parse_positive(text: str) -> int:
    """Parse a positive integer, raising ValueError for invalid values."""
    value = int(text)
    if value <= 0:
        raise ValueError("Zahl muss positiv sein")
    return value
```

## Warum funktioniert das?

Die Umwandlung und die fachliche Bereichsprüfung sind getrennte Schritte. Die äußere Oberfläche darf den Fehler fangen und eine neue Eingabe anfordern; die Funktion bleibt testbar.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 05 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
