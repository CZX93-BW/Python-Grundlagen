# Lösung 04 · Fehlende Werte ergänzen

[Zur Aufgabe](../90_uebungen/04_bool_none.md) · [Zum Kapitel](../kapitel/04_bool_none.md)

## Eine mögliche Lösung

```python
def use_default(value, default):
    """Replace only None, preserving valid falsy values."""
    return default if value is None else value
```

## Warum funktioniert das?

Ein Ersatz mit `value or default` würde alle falschen Wahrheitswerte ersetzen. Die ausdrückliche None-Prüfung erhält die fachlich gültigen Null- und Leerwerte.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 04 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
