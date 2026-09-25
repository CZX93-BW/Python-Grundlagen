# Übung 09 · Gemeinsame Fähigkeiten finden

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/09_tupel_sets.md)

**Schwierigkeit:** Leicht

## Aufgabe und Anforderungen

`common_skills(first, second)` erhält zwei Listen von Strings. Gib gemeinsame Werte genau einmal als alphabetisch sortierte Liste zurück. Groß-/Kleinschreibung bleibt bedeutend. Eingabelisten bleiben unverändert.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [09_tupel_sets.py](09_tupel_sets.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 09
```

## Ein kleiner Hinweis

Sets unterstützen die Schnittmenge mit `&`.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
