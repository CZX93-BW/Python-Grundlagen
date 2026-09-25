# Lösung 01 · Begrüßung zusammensetzen

[Zur Aufgabe](../90_uebungen/01_variablen_typen.md) · [Zum Kapitel](../kapitel/01_variablen_typen.md)

## Eine mögliche Lösung

```python
def greeting(name: str, language: str) -> str:
    """Return a greeting for de or en; reject unsupported languages."""
    if language == "de":
        return f"Hallo {name}"
    if language == "en":
        return f"Hello {name}"
    raise ValueError("Unbekannte Sprache")
```

## Warum funktioniert das?

Jeder unterstützte Sprachcode bekommt einen eindeutigen Rückgabewert. Ein unbekannter Code ist ein Eingabefehler und wird ausdrücklich gemeldet. `return` erlaubt dem Aufrufer, den Text weiterzuverwenden.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 01 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
