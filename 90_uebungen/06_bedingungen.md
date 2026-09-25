# Übung 06 · Punktestand einordnen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/06_bedingungen.md)

**Schwierigkeit:** Leicht

## Aufgabe und Anforderungen

`classify_score(points)` bekommt eine ganze Zahl von 0 bis 100. Ab 90 lautet das Ergebnis `"sehr gut"`, ab 60 `"bestanden"`, darunter `"weiter üben"`. Außerhalb 0–100 muss `ValueError` entstehen.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [06_bedingungen.py](06_bedingungen.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 06
```

## Ein kleiner Hinweis

Prüfe den höchsten Bereich zuerst.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
