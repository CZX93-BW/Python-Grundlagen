# Übung 29 · Eine Coroutine schreiben

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/29_async_laufzeit.md)

**Schwierigkeit:** Anspruchsvoll

## Aufgabe und Anforderungen

`async_double(number)` ist eine async-Funktion. Sie soll mit `await asyncio.sleep(0)` kooperativ pausieren und dann die Zahl verdoppelt zurückgeben. Kein asyncio.run() innerhalb der Funktion. Andere Typen als Zahlen müssen nicht geprüft werden.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [29_async_laufzeit.py](29_async_laufzeit.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 29
```

## Ein kleiner Hinweis

asyncio.run() gehört in die äußere Startfunktion beziehungsweise den Test.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
