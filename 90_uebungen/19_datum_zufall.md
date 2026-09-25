# Übung 19 · Datumsabstand bestimmen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/19_datum_zufall.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

`days_between(start, end)` bekommt zwei ISO-Datumsstrings wie `"2026-09-25"`. Gib die Anzahl Tage von start bis end zurück. Ein früheres Enddatum ergibt eine negative Zahl. Ungültige Daten verursachen `ValueError`.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [19_datum_zufall.py](19_datum_zufall.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 19
```

## Ein kleiner Hinweis

Wandle beide Strings mit date.fromisoformat() um.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
