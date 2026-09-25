# Lösung 20 · Artikelnummer prüfen

[Zur Aufgabe](../90_uebungen/20_standardhelfer.md) · [Zum Kapitel](../kapitel/20_standardhelfer.md)

## Eine mögliche Lösung

```python
import re

def is_article_code(text: str) -> bool:
    """Check the complete ASCII pattern AA-000."""
    return re.fullmatch(r"[A-Z]{2}-[0-9]{3}", text) is not None
```

## Warum funktioniert das?

Das Ergebnis einer erfolgreichen Musterprüfung ist ein Match-Objekt. Die Prüfung auf `is not None` liefert den geforderten Boolean. `[0-9]` begrenzt Ziffern ausdrücklich auf ASCII.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 20 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
