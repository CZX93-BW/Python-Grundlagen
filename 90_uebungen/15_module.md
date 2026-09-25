# Übung 15 · Ein importierbares Modul

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/15_module.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

Erstelle `greet(name)` mit der Rückgabe `"Hallo NAME"`. Definiere außerdem `main()`, das `greet("Basti")` ausgibt. Beim direkten Start läuft main(), beim Import darf keine Ausgabe entstehen. Der Prüfcode importiert deine Datei.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [15_module.py](15_module.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 15
```

## Ein kleiner Hinweis

Der Startblock vergleicht `__name__` mit `"__main__"`.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
