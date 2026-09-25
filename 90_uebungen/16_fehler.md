# Übung 16 · Einen Port validieren

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/16_fehler.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

`parse_port(text)` wandelt Text in eine ganze Zahl von 1 bis 65535 um. Bei ungültigem Text oder außerhalb des Bereichs löst die Funktion `ValueError` mit einer verständlichen Meldung aus. Eine Zahl ist die Rückgabe, keine Fehlermeldung als String.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [16_fehler.py](16_fehler.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 16
```

## Ein kleiner Hinweis

Prüfe zuerst die Umwandlung, danach die fachlichen Grenzen.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
