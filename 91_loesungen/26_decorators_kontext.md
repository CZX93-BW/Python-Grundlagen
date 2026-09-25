# Lösung 26 · Einen Rückgabewert dekorieren

[Zur Aufgabe](../90_uebungen/26_decorators_kontext.md) · [Zum Kapitel](../kapitel/26_decorators_kontext.md)

## Eine mögliche Lösung

```python
from functools import wraps

def uppercase_result(function):
    """Uppercase a string result while preserving function metadata."""
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return wrapper
```

## Warum funktioniert das?

Die Closure behält Zugriff auf die Originalfunktion. Der Wrapper ruft sie mit den durchgereichten Argumenten auf und verändert ausschließlich ihren String-Rückgabewert.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 26 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
