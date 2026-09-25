# 30 · Deine Notizübung als saubere CRUD-Logik

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](29_async_laufzeit.md) · [Praxisprojekt](../80_praxis/notizen/README.md)

**Stufe:** Praxis  
**Suchbegriffe:** Notizen CRUD hinzufügen anzeigen suchen ändern löschen ID Validierung Funktionen

## Wozu brauche ich das?

Deine ursprüngliche Übung verändert stets die erste Notiz und liest Eingaben direkt in der Funktion. Zum Einstieg ist das nachvollziehbar. Für eine wiederverwendbare Anwendung trennen wir Eingabe, Datenverarbeitung und Speicherung. Eine ID bleibt stabil, auch wenn sich Listenpositionen ändern.

## Erst verstehen

Die folgenden kleinen Fälle zeigen die Bausteine getrennt. Das vollständige ausführbare Projekt liegt unter `80_praxis/notizen/`. Es verwendet ein Terminalmenü, geprüfte JSON-Daten und eine sichere Reihenfolge beim Speichern. Die Originaldatei liegt unverändert im Archiv.

## Fall 1: Eine Notiz übergeben statt versteckt einlesen

Die Funktion soll unabhängig vom Terminal testbar sein.

```python
def create_note(note_id, title, text):
    title = title.strip()
    text = text.strip()
    if not title or not text:
        raise ValueError("Titel und Text dürfen nicht leer sein")
    return {"id": note_id, "title": title, "text": text}

print(create_note("n1", " Einkauf ", " Milch "))
```

**Erwartete Ausgabe:**

```text
{'id': 'n1', 'title': 'Einkauf', 'text': 'Milch'}
```

**Schritt für Schritt:**

1. Alle benötigten Daten kommen über Parameter.
2. Die Funktion säubert die Texte und prüft ihre Pflichtfelder.
3. Sie liefert Daten zurück. Die aufrufende Oberfläche kümmert sich um `input()` und `print()`.

[Beispieldatei öffnen](../beispiele/30_notizen_crud/fall_01.py)

```powershell
python ./beispiele/30_notizen_crud/fall_01.py
```

## Fall 2: Mit einer ID statt einem festen Index suchen

Eine Notiz soll unabhängig von ihrer Listenposition gefunden werden.

```python
def find_note(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None

notes = [{"id": "n1", "title": "Einkauf"}]
print(find_note(notes, "n1"))
print(find_note(notes, "fehlt"))
```

**Erwartete Ausgabe:**

```text
{'id': 'n1', 'title': 'Einkauf'}
None
```

**Schritt für Schritt:**

1. Die Schleife prüft die ID jedes Datensatzes.
2. Eine frühe Rückgabe beendet die Suche bei einem Treffer.
3. `None` ist hier die ausdrücklich vereinbarte Antwort für einen fehlenden Datensatz. Bei wenigen Notizen ist die lineare Suche einfach und ausreichend.

[Beispieldatei öffnen](../beispiele/30_notizen_crud/fall_02.py)

```powershell
python ./beispiele/30_notizen_crud/fall_02.py
```

## Fall 3: Löschen ohne gefährlichen Indexzugriff

Fehlende Notizen und leere Listen sollen klar behandelt werden.

```python
def delete_note(notes, note_id):
    for index, note in enumerate(notes):
        if note["id"] == note_id:
            return notes.pop(index)
    raise KeyError(f"Notiz nicht gefunden: {note_id}")

notes = [{"id": "n1", "title": "Einkauf"}]
print(delete_note(notes, "n1"))
print(notes)
try:
    delete_note(notes, "n1")
except KeyError:
    print("Notiz fehlt")
```

**Erwartete Ausgabe:**

```text
{'id': 'n1', 'title': 'Einkauf'}
[]
Notiz fehlt
```

**Schritt für Schritt:**

1. `enumerate()` liefert Index und Datensatz zusammen.
2. `pop()` entfernt genau den gefundenen Eintrag. Die Funktion kehrt sofort zurück, daher wird nicht mit verschobenen Positionen weiteriteriert.
3. Ein nicht vorhandener Eintrag führt zu einer klaren Fehlermeldung statt eines ungezielten `pop(0)`.

[Beispieldatei öffnen](../beispiele/30_notizen_crud/fall_03.py)

```powershell
python ./beispiele/30_notizen_crud/fall_03.py
```

## Typische Stolperstellen

IDs müssen eindeutig sein. Erst prüfen, dann ändern: Eine ungültige Bearbeitung darf die bisherige Notiz nicht beschädigen. Eine leere Liste ist ein normaler Zustand. Fehler beim Laden vorhandener Daten dürfen nicht stillschweigend zu einer leeren Liste und anschließendem Überschreiben führen.

## Selbst anwenden

[Übung 30](../90_uebungen/30_notizen_crud.md) · [Starterdatei](../90_uebungen/30_notizen_crud.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/tutorial/datastructures.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
