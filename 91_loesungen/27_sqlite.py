"""Musterlösung 27: Einen Kontakt in SQLite anlegen."""

def add_contact(connection, name: str) -> int:
    """Insert one contact; leave transaction and connection to caller."""
    cursor = connection.execute("INSERT INTO contacts (name) VALUES (?)", (name,))
    return cursor.lastrowid
