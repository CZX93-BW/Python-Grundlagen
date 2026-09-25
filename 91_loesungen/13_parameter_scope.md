# Lösung 13 · Tags ohne geteilten Standardwert

[Zur Aufgabe](../90_uebungen/13_parameter_scope.md) · [Zum Kapitel](../kapitel/13_parameter_scope.md)

## Eine mögliche Lösung

```python
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append to the supplied list, or create a fresh list when omitted."""
    if tags is None:
        tags = []
    tags.append(tag)
    return tags
```

## Warum funktioniert das?

Der Standardwert ist unveränderbar. Die neue Liste entsteht erst während des Aufrufs. Eine explizit übergebene Liste wird auch dann verwendet, wenn sie leer ist.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 13 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
