# Übung 21 · Ein Zähler als Klasse

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/21_klassen.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

Erstelle die Klasse `Counter`. Ihr öffentlicher Wert `value` beginnt bei 0. `increment()` erhöht ihn um 1 und liefert den neuen Wert. `reset()` setzt ihn auf 0 und gibt None zurück. Verschiedene Instanzen sind unabhängig.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [21_klassen.py](21_klassen.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 21
```

## Ein kleiner Hinweis

Der Zustand gehört in `self.value` und wird in __init__ gesetzt.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
