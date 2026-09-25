# Lösung 29 · Eine Coroutine schreiben

[Zur Aufgabe](../90_uebungen/29_async_laufzeit.md) · [Zum Kapitel](../kapitel/29_async_laufzeit.md)

## Eine mögliche Lösung

```python
import asyncio

async def async_double(number: int) -> int:
    """Yield control once, then return twice the input."""
    await asyncio.sleep(0)
    return number * 2
```

## Warum funktioniert das?

Die Coroutine lässt sich dadurch auch aus einer bereits laufenden Ereignisschleife mit await verwenden. Die künstliche Pause dient nur zum Lernen; diese Rechnung benötigt praktisch kein async.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 29 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
