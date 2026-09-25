# Übung 08 · Doppelte Einträge entfernen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/08_listen.md)

**Schwierigkeit:** Leicht

## Aufgabe und Anforderungen

`unique_items(items)` bekommt eine Liste von Strings. Liefere eine neue Liste mit jedem Text nur einmal; die Reihenfolge des ersten Auftretens muss bleiben. Die Eingabeliste bleibt unverändert. Eine leere Liste ergibt eine neue leere Liste.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [08_listen.py](08_listen.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 08
```

## Ein kleiner Hinweis

Beginne mit einer leeren Ergebnisliste und prüfe vor jedem append().

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
