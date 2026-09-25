# Übung 03 · Suchtext normalisieren

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/03_strings.md)

**Schwierigkeit:** Leicht

## Aufgabe und Anforderungen

`normalize_search(text)` entfernt äußere Leerzeichen und normalisiert Groß-/Kleinschreibung mit `casefold()`. Innere Leerzeichen bleiben unverändert. Nur aus Leerzeichen bestehender Text ergibt `""`.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [03_strings.py](03_strings.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 03
```

## Ein kleiner Hinweis

Du kannst Methoden nacheinander auf dem jeweiligen Ergebnis aufrufen.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
