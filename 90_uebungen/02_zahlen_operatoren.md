# Übung 02 · Minuten aufteilen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/02_zahlen_operatoren.md)

**Schwierigkeit:** Leicht

## Aufgabe und Anforderungen

`split_minutes(total)` erhält eine ganze Zahl. Gib `(stunden, restminuten)` als Tupel zurück. Beispiel: 135 wird `(2, 15)`. Null ist erlaubt, negative Zahlen verursachen `ValueError`. Du musst andere Datentypen nicht prüfen.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [02_zahlen_operatoren.py](02_zahlen_operatoren.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 02
```

## Ein kleiner Hinweis

Ganzzahldivision und Rest lösen unterschiedliche Teile der Aufgabe.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
