# Übung 10 · Wörter zählen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/10_dictionaries.md)

**Schwierigkeit:** Leicht

## Aufgabe und Anforderungen

`count_words(text)` trennt an Whitespace und zählt Wörter nach `casefold()`. Satzzeichen bleiben Teil des Wortes. Das Ergebnis ist ein Dictionary. Beispiel: `"Python python SQL"` wird `{"python": 2, "sql": 1}`. Löse es zunächst ohne Counter.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [10_dictionaries.py](10_dictionaries.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 10
```

## Ein kleiner Hinweis

`get(word, 0)` liefert für ein neues Wort den Startwert.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
