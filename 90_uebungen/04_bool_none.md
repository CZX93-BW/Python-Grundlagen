# Übung 04 · Fehlende Werte ergänzen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/04_bool_none.md)

**Schwierigkeit:** Leicht

## Aufgabe und Anforderungen

`use_default(value, default)` ersetzt ausschließlich `None`. Die Werte `0`, `False`, `""` und eine leere Liste müssen unverändert zurückgegeben werden. Prüfe nicht nur den Wahrheitswert.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [04_bool_none.py](04_bool_none.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 04
```

## Ein kleiner Hinweis

Der passende Vergleich lautet `is None`.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
