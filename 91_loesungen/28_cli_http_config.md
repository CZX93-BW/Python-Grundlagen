# Lösung 28 · Boolesche Konfiguration lesen

[Zur Aufgabe](../90_uebungen/28_cli_http_config.md) · [Zum Kapitel](../kapitel/28_cli_http_config.md)

## Eine mögliche Lösung

```python
def parse_bool(text: str) -> bool:
    """Parse an explicit set of true/false configuration strings."""
    normalized = text.strip().casefold()
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    raise ValueError("Unbekannter Wahrheitswert")
```

## Warum funktioniert das?

Die erlaubten Werte sind ausdrücklich festgelegt. Unbekannte Angaben werden nicht stillschweigend als falsch interpretiert; dadurch werden Konfigurationsfehler sichtbar.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 28 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
