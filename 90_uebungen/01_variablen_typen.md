# Übung 01 · Begrüßung zusammensetzen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/01_variablen_typen.md)

**Schwierigkeit:** Leicht

## Aufgabe und Anforderungen

Schreibe `greeting(name, language)`. Bei `language == "de"` lautet das Ergebnis `"Hallo Basti"`, bei `"en"` `"Hello Basti"`, wenn der Name Basti ist. Andere Sprachcodes sollen `ValueError` auslösen. Der Name ist garantiert ein String und wird unverändert übernommen. Gib den Text zurück, statt ihn zu drucken.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [01_variablen_typen.py](01_variablen_typen.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 01
```

## Ein kleiner Hinweis

Nutze einen f-String und zwei Vergleiche. Die benötigten Bedingungen findest du in Kapitel 6.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
