# Übung 07 · Gerade Zahlen summieren

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/07_schleifen.md)

**Schwierigkeit:** Leicht

## Aufgabe und Anforderungen

`sum_even(numbers)` summiert alle geraden ganzen Zahlen einer Liste. Negative gerade Zahlen zählen ebenfalls. Eine leere Liste ergibt 0. Löse es zuerst mit einer for-Schleife; verändere die Eingabeliste nicht.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [07_schleifen.py](07_schleifen.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 07
```

## Ein kleiner Hinweis

Der Rest bei Division durch 2 ist für gerade Zahlen 0.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
