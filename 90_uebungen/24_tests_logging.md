# Übung 24 · Einen Fehler mit Tests absichern

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/24_tests_logging.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

Implementiere `divide(total, count)`: count muss größer als 0 sein, sonst entsteht ValueError. Ergänze in der Übungsdatei eine eigene unittest-Testklasse `DivideTests` mit mindestens drei Tests: Normalfall, null und negative Anzahl. Die automatischen Prüffälle ersetzen nicht deine selbst geschriebenen Tests.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [24_tests_logging.py](24_tests_logging.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 24
```

## Ein kleiner Hinweis

Benutze assertEqual() für Ergebnisse und assertRaises() für erwartete Fehler.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
