# Übung 11 · Eine unabhängige Notizkopie

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/11_verschachteln_kopieren.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

`copy_notes(notes)` kopiert eine Liste von Dictionaries vollständig für einfache verschachtelte Daten. Wenn nachher ein Titel oder eine innere Tag-Liste in der Kopie geändert wird, bleibt das Original unverändert.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [11_verschachteln_kopieren.py](11_verschachteln_kopieren.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 11
```

## Ein kleiner Hinweis

Eine flache Listenkopie genügt für innere Dictionaries und Listen nicht.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
