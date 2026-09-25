# Lösung 16 · Einen Port validieren

[Zur Aufgabe](../90_uebungen/16_fehler.md) · [Zum Kapitel](../kapitel/16_fehler.md)

## Eine mögliche Lösung

```python
def parse_port(text: str) -> int:
    """Parse a port in the inclusive range 1..65535."""
    try:
        port = int(text)
    except ValueError as error:
        raise ValueError("Port muss eine ganze Zahl sein") from error
    if not 1 <= port <= 65535:
        raise ValueError("Port muss zwischen 1 und 65535 liegen")
    return port
```

## Warum funktioniert das?

Die Fehlerursache bleibt mit `from error` erhalten. Für gültige Werte gibt es immer denselben Rückgabetyp. Unterschiedliche Fehlerbedingungen erhalten passende Meldungen.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 16 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
