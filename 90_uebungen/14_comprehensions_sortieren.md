# Übung 14 · Personen filtern und sortieren

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/14_comprehensions_sortieren.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

`adult_names(people)` bekommt Dictionaries mit den garantierten Feldern `name` (str) und `age` (int). Gib die Namen aller mindestens 18-Jährigen sortiert nach `casefold()` zurück. Schreibweise und doppelte Namen bleiben erhalten. Die Eingabeliste bleibt unverändert.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [14_comprehensions_sortieren.py](14_comprehensions_sortieren.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 14
```

## Ein kleiner Hinweis

Filtere zuerst nach Alter. Sortiere danach nur die Namen.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
