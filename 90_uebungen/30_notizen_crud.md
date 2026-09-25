# Übung 30 · Notiz mit stabiler ID ändern

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/30_notizen_crud.md)

**Schwierigkeit:** Mittel

## Aufgabe und Anforderungen

`update_note(notes, note_id, title, text)` sucht die ID in einer Liste gültiger Notizen. Bei Treffer werden Titel und Text nach strip() im vorhandenen Dictionary ersetzt, und genau dieses Dictionary wird zurückgegeben. Beide Texte müssen gefüllt sein; sonst ValueError und keine Änderung. Prüfe die Texte vor der Suche. Bei fehlender ID entsteht KeyError. Andere Notizen bleiben unverändert.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [30_notizen_crud.py](30_notizen_crud.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 30
```

## Ein kleiner Hinweis

Erst beide neuen Werte prüfen, dann überhaupt Daten verändern.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
