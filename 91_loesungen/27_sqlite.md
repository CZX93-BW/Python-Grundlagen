# Lösung 27 · Einen Kontakt in SQLite anlegen

[Zur Aufgabe](../90_uebungen/27_sqlite.md) · [Zum Kapitel](../kapitel/27_sqlite.md)

## Eine mögliche Lösung

```python
def add_contact(connection, name: str) -> int:
    """Insert one contact; leave transaction and connection to caller."""
    cursor = connection.execute("INSERT INTO contacts (name) VALUES (?)", (name,))
    return cursor.lastrowid
```

## Warum funktioniert das?

Die Werte werden getrennt vom SQL-Befehl übergeben. Dadurch bleiben auch Apostrophe und SQL-ähnlicher Text normale Daten. Der Aufrufer kann mehrere Aktionen in einer Transaktion bündeln.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 27 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
