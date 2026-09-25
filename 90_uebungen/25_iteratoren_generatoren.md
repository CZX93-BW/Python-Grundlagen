# Übung 25 · Gerade Zahlen als Generator

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/25_iteratoren_generatoren.md)

**Schwierigkeit:** Anspruchsvoll

## Aufgabe und Anforderungen

`even_numbers(limit)` erzeugt mit yield alle geraden Zahlen ab 0, die kleiner als limit sind. limit ist eine ganze Zahl. Bei limit <= 0 ist die Folge leer. Gib keine vorbereitete Liste zurück.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [25_iteratoren_generatoren.py](25_iteratoren_generatoren.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 25
```

## Ein kleiner Hinweis

range() unterstützt eine Schrittweite.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
