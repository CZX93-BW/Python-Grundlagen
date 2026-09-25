"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        import sqlite3
        from contextlib import closing
        with closing(sqlite3.connect(":memory:")) as connection:
            connection.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
            contact_id = m.add_contact(connection, "Ada")
            self.assertEqual(connection.execute("SELECT name FROM contacts WHERE id = ?", (contact_id,)).fetchone(), ("Ada",))

    def test_quotes(self):
        m = MODULE
        import sqlite3
        from contextlib import closing
        with closing(sqlite3.connect(":memory:")) as connection:
            connection.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
            name = "O'Reilly; DROP TABLE contacts;"
            m.add_contact(connection, name)
            self.assertEqual(connection.execute("SELECT name FROM contacts").fetchone()[0], name)

    def test_transaction(self):
        m = MODULE
        import sqlite3
        from contextlib import closing
        with closing(sqlite3.connect(":memory:")) as connection:
            connection.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
            m.add_contact(connection, "Ada")
            connection.rollback()
            self.assertEqual(connection.execute("SELECT COUNT(*) FROM contacts").fetchone()[0], 0)
