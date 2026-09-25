# Übung 27 · Einen Kontakt in SQLite anlegen

[Übungsübersicht](README.md) · [Passendes Kapitel](../kapitel/27_sqlite.md)

**Schwierigkeit:** Anspruchsvoll

## Aufgabe und Anforderungen

`add_contact(connection, name)` erhält eine offene sqlite3-Verbindung. Die Tabelle contacts besitzt `id INTEGER PRIMARY KEY` und `name TEXT NOT NULL`. Speichere name über einen SQL-Platzhalter und gib die neue ID zurück. Die Funktion schließt die Verbindung nicht und führt keinen Commit durch; die aufrufende Stelle verwaltet die Transaktion.

## So gehst du vor

1. Lies die Aufgabe und notiere die Eingaben, Rückgabe und Fehlerfälle.
2. Öffne [27_sqlite.py](27_sqlite.py) und ersetze die Platzhalter.
3. Prüfe zuerst einen normalen Fall, danach leere oder ungültige Eingaben.
4. Starte die zugehörigen Tests aus dem Hauptordner:

```powershell
python ./werkzeuge/uebung_pruefen.py 27
```

## Ein kleiner Hinweis

Das Tupel mit genau einem Element benötigt ein Komma.

## Selbstkontrolle

- Stimmt der Rückgabetyp mit der Aufgabe überein?
- Werden alle genannten Grenz- und Fehlerfälle behandelt?
- Verändert die Funktion Eingaben nur, wenn das ausdrücklich verlangt ist?
- Kannst du jede Zeile deiner Lösung erklären?

Die Tests stehen getrennt unter `95_tests`. Die Musterlösung liegt mit derselben Nummer unter `91_loesungen`. Es gibt oft mehrere richtige Lösungen.
