# Lösung 03 · Suchtext normalisieren

[Zur Aufgabe](../90_uebungen/03_strings.md) · [Zum Kapitel](../kapitel/03_strings.md)

## Eine mögliche Lösung

```python
def normalize_search(text: str) -> str:
    """Normalize surrounding whitespace and case for text search."""
    return text.strip().casefold()
```

## Warum funktioniert das?

Beide Methoden liefern einen neuen String. `casefold()` behandelt beispielsweise auch ß für einen Vergleich mit SS. Eine Suche ist damit noch nicht automatisch akzentunabhängig.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 03 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
