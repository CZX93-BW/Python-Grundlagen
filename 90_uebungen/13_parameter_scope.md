# Übung 13 · Tags ohne geteilten Standardwert

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/13_parameter_scope.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

`add_tag(tag, tags=None)` soll ohne zweite Eingabe bei jedem Aufruf eine neue Liste erzeugen. Wird eine Liste übergeben, soll sie ausdrücklich verändert und zurückgegeben werden. Doppelte Tags sind erlaubt.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [13_parameter_scope.py](13_parameter_scope.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 13
```

## Ein kleiner Hinweis

Prüfe `is None`, nicht `if not tags`, damit eine übergebene leere Liste erhalten bleibt.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
