# Übung 20 · Artikelnummer prüfen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/20_standardhelfer.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

`is_article_code(text)` gibt einen Boolean zurück. Gültig sind genau zwei ASCII-Großbuchstaben, ein Bindestrich und drei ASCII-Ziffern: `AB-123`. Kein vorangestellter oder nachfolgender Text, auch kein Zeilenumbruch, ist erlaubt.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [20_standardhelfer.py](20_standardhelfer.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 20
```

## Ein kleiner Hinweis

fullmatch() ist hier geeigneter als search().

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
