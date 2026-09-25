"""Eine kleine Datenbank mit SQLite: Tabelle anlegen und Datensätze speichern."""

import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as connection:
    with connection:
        connection.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
        connection.execute("INSERT INTO contacts (name) VALUES (?)", ("Ada",))
    rows = connection.execute("SELECT id, name FROM contacts ORDER BY id").fetchall()
    print(rows)
