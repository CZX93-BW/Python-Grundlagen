# Übung 26 · Einen Rückgabewert dekorieren

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/26_decorators_kontext.md)

**Schwierigkeit:** Anspruchsvoll

## Aufgabe und Anforderungen

Implementiere den Decorator `uppercase_result`. Er soll eine Funktion mit String-Rückgabe umhüllen und deren Ergebnis mit upper() umwandeln. Argumente und Keyword-Argumente werden unverändert weitergeleitet. Der ursprüngliche Funktionsname bleibt durch wraps() erhalten.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [26_decorators_kontext.py](26_decorators_kontext.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 26
```

## Ein kleiner Hinweis

Der äußere Aufruf gibt die Wrapper-Funktion zurück, nicht ihr Ergebnis.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
