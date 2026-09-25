"""Eine kleine Datenbank mit SQLite: Eine fehlgeschlagene Transaktion zurücknehmen."""

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
