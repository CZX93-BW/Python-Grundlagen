"""Eine kleine Datenbank mit SQLite: Aktualisieren und löschen."""

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
