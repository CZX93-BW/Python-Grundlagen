# Übung 17 · Nicht leere Zeilen lesen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/17_dateien_pfade.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

`read_nonempty_lines(path)` liest eine UTF-8-Datei. Entferne äußeren Whitespace jeder Zeile und lasse danach leere Zeilen weg. Gib eine Liste zurück. Bei fehlender Datei soll `FileNotFoundError` weitergereicht werden. Eine komplett leere Datei ergibt `[]`.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [17_dateien_pfade.py](17_dateien_pfade.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 17
```

## Ein kleiner Hinweis

Verwende `with path.open(...)` und eine Schleife über die Datei.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
