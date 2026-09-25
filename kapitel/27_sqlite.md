# 27 · Eine kleine Datenbank mit SQLite

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](26_decorators_kontext.md) · [Nächstes Kapitel](28_cli_http_config.md)

**Stufe:** Aufbau  
**Suchbegriffe:** sqlite3 SQL CRUD SELECT INSERT UPDATE DELETE commit rollback parameter placeholders

## Wozu brauche ich das?

SQLite speichert Daten in einer Datei und ist für kleine lokale Anwendungen gut geeignet. Für diese Beispiele nutzen wir eine Datenbank im Speicher, damit keine Datei zurückbleibt. SQL ist eine eigene Sprache zum Arbeiten mit Tabellen.

## Erst verstehen

**CRUD** bedeutet Create, Read, Update, Delete: anlegen, lesen, ändern, löschen. Eine **Transaktion** fasst Änderungen zusammen, die gemeinsam gespeichert oder zurückgenommen werden sollen. Verwende Platzhalter für Werte in SQL.

## Fall 1: Tabelle anlegen und Datensätze speichern

Du möchtest einen Namen mit einer stabilen ID speichern.

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as connection:
    with connection:
        connection.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
        connection.execute("INSERT INTO contacts (name) VALUES (?)", ("Ada",))
    rows = connection.execute("SELECT id, name FROM contacts ORDER BY id").fetchall()
    print(rows)
```

**Erwartete Ausgabe:**

```text
[(1, 'Ada')]
```

**Schritt für Schritt:**

1. `:memory:` erstellt eine temporäre Datenbank im Speicher; ein Dateipfad würde eine persistente Datenbank öffnen.
2. `?` ist ein Platzhalter. `("Ada",)` ist das Tupel der Werte.
3. Der innere Kontext speichert die Transaktion bei Erfolg. `closing()` schließt anschließend die Verbindung.

**Achte darauf:** Der Kontextmanager einer sqlite3-Verbindung behandelt Transaktionen, schließt die Verbindung aber nicht automatisch.

[Beispieldatei öffnen](../beispiele/27_sqlite/fall_01.py)

```powershell
python ./beispiele/27_sqlite/fall_01.py
```

## Fall 2: Aktualisieren und löschen

Du möchtest einen ausgewählten Eintrag ändern und anschließend entfernen.

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as connection:
    with connection:
        connection.execute("CREATE TABLE notes (id INTEGER PRIMARY KEY, title TEXT)")
        connection.execute("INSERT INTO notes VALUES (?, ?)", (1, "Alt"))
        connection.execute("UPDATE notes SET title = ? WHERE id = ?", ("Neu", 1))
        print(connection.execute("SELECT title FROM notes WHERE id = ?", (1,)).fetchone())
        cursor = connection.execute("DELETE FROM notes WHERE id = ?", (1,))
        print(cursor.rowcount)
    print(connection.execute("SELECT COUNT(*) FROM notes").fetchone()[0])
```

**Erwartete Ausgabe:**

```text
('Neu',)
1
0
```

**Schritt für Schritt:**

1. `WHERE` beschränkt Änderung und Löschung auf den gewünschten Datensatz.
2. `fetchone()` liefert eine Zeile oder None; `fetchall()` liefert alle übrigen Zeilen als Liste.
3. `rowcount` zeigt hier, wie viele Zeilen gelöscht wurden. Ohne passende ID wären es null.

[Beispieldatei öffnen](../beispiele/27_sqlite/fall_02.py)

```powershell
python ./beispiele/27_sqlite/fall_02.py
```

## Fall 3: Eine fehlgeschlagene Transaktion zurücknehmen

Zwei Änderungen sollen nur gemeinsam gespeichert werden.

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as connection:
    connection.execute("CREATE TABLE tags (name TEXT UNIQUE)")
    try:
        with connection:
            connection.execute("INSERT INTO tags VALUES (?)", ("Python",))
            connection.execute("INSERT INTO tags VALUES (?)", ("Python",))
    except sqlite3.IntegrityError:
        print("Doppelter Wert: Transaktion zurückgenommen")
    print(connection.execute("SELECT COUNT(*) FROM tags").fetchone()[0])
```

**Erwartete Ausgabe:**

```text
Doppelter Wert: Transaktion zurückgenommen
0
```

**Schritt für Schritt:**

1. `UNIQUE` verbietet doppelte Werte in dieser Spalte.
2. Der zweite INSERT löst einen Integritätsfehler aus.
3. Die Transaktion nimmt auch den ersten INSERT zurück. Der Fehler wird außerhalb des Transaktionsblocks behandelt.

[Beispieldatei öffnen](../beispiele/27_sqlite/fall_03.py)

```powershell
python ./beispiele/27_sqlite/fall_03.py
```

## Typische Stolperstellen

Baue fremde Werte nie per f-String in SQL ein. Platzhalter gelten für Werte, nicht für frei wählbare Tabellen- oder Spaltennamen; solche Namen müssen aus festen erlaubten Optionen kommen. Die Beispiele verwenden das Standard-Transaktionsverhalten von Python 3.12; bei anderer autocommit-Konfiguration gelten andere Commit-/Rollback-Abläufe.

## Selbst anwenden

[Übung 27](../90_uebungen/27_sqlite.md) · [Starterdatei](../90_uebungen/27_sqlite.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/sqlite3.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
