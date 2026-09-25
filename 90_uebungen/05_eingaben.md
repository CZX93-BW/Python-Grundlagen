# Übung 05 · Positive Zahl aus Text lesen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/05_eingaben.md)

**Schwierigkeit:** Leicht

## Aufgabe und Anforderungen

`parse_positive(text)` wandelt Text per `int()` um. Nur ganze Zahlen größer als null sind erlaubt. Für `"abc"`, `"2.5"`, `"0"` und negative Zahlen muss `ValueError` entstehen. Äußere Leerzeichen sind erlaubt. Die Funktion fragt nicht selbst mit `input()` nach.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [05_eingaben.py](05_eingaben.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 05
```

## Ein kleiner Hinweis

`int()` behandelt Leerzeichen bereits und wirft bei ungültigem Zahltext ValueError.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
