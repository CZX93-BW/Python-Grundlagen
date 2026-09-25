# 23 · Type Hints und verständliche Dokumentation

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](22_dataclasses_komposition.md) · [Nächstes Kapitel](24_tests_logging.md)

**Stufe:** Aufbau  
**Suchbegriffe:** typing annotation hint Optional union list dict TypedDict docstring PEP8 Clean Code

## Wozu brauche ich das?

Type Hints beschreiben, welche Werte eine Funktion erwartet und zurückgibt. Sie helfen dir, deinem Editor und einer statischen Typprüfung. Eine Docstring erklärt zusätzlich Bedeutung, Sonderfälle und mögliche Fehler.

## Erst verstehen

**Statisch** bedeutet hier: Ein Werkzeug untersucht den Code, ohne alle Fälle auszuführen. Python erzwingt normale Typannotationen zur Laufzeit nicht. Nutze englische Namen im Code und verständliche Erklärungen daneben; das passt zu Dokumentation und Fehlermeldungen der Sprache.

## Fall 1: Einen Funktionsvertrag beschreiben

Ein Durchschnitt ist für eine leere Liste nicht definiert.

```python
def average(numbers: list[float]) -> float | None:
    """Return the arithmetic mean, or None for an empty list."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

print(average([2.0, 4.0]))
print(average([]))
```

**Erwartete Ausgabe:**

```text
3.0
None
```

**Schritt für Schritt:**

1. `list[float]` beschreibt eine Liste von Gleitkommazahlen.
2. `float | None` nennt die beiden möglichen Rückgabetypen.
3. Die Docstring erläutert, wann None entsteht. Der Aufrufer muss diesen Fall behandeln.

[Beispieldatei öffnen](../beispiele/23_typen_dokumentation/fall_01.py)

```powershell
python ./beispiele/23_typen_dokumentation/fall_01.py
```

## Fall 2: Strukturierte Dictionaries beschreiben

Deine Notiz-Dictionaries sollen für den Editor eine klare Form haben.

```python
from typing import TypedDict

class NoteData(TypedDict):
    title: str
    text: str

def summarize(note: NoteData) -> str:
    return f"{note['title']}: {note['text']}"

print(summarize({"title": "Python", "text": "Üben"}))
```

**Erwartete Ausgabe:**

```text
Python: Üben
```

**Schritt für Schritt:**

1. `TypedDict` beschreibt erwartete Schlüssel und Werttypen.
2. Die tatsächlichen Werte bleiben normale Dictionaries.
3. JSON-Daten werden durch diese Beschreibung nicht automatisch geprüft. Für fremde Eingaben brauchst du weiterhin Laufzeitvalidierung.

[Beispieldatei öffnen](../beispiele/23_typen_dokumentation/fall_02.py)

```powershell
python ./beispiele/23_typen_dokumentation/fall_02.py
```

## Fall 3: Verständliche Namen und klare Einheiten

Eine Funktion soll ihre Bedeutung ohne Ratespiel vermitteln.

```python
MINUTES_PER_HOUR = 60

def hours_to_minutes(hours: int) -> int:
    """Convert non-negative whole hours to minutes.

    Raises:
        ValueError: If hours is negative.
    """
    if hours < 0:
        raise ValueError("hours darf nicht negativ sein")
    return hours * MINUTES_PER_HOUR

print(hours_to_minutes(2))
```

**Erwartete Ausgabe:**

```text
120
```

**Schritt für Schritt:**

1. Namen nennen die fachliche Größe und die Einheit.
2. Der konstante Faktor hat einen erklärenden Namen. Großschreibung ist eine Konvention.
3. Die Docstring dokumentiert die Voraussetzung und den Fehlerfall, statt nur jede Codezeile zu wiederholen.

[Beispieldatei öffnen](../beispiele/23_typen_dokumentation/fall_03.py)

```powershell
python ./beispiele/23_typen_dokumentation/fall_03.py
```

## Typische Stolperstellen

Vermeide `Any` als Standardlösung für unklare Datenmodelle. Eine kurze Funktion ist nicht automatisch gut, wenn ihr Name und Vertrag unklar sind. Kommentare sollten vor allem Gründe erklären; Namen, Typen und klare Kontrollflüsse erklären bereits einen großen Teil des Ablaufs.

## Selbst anwenden

[Übung 23](../90_uebungen/23_typen_dokumentation.md) · [Starterdatei](../90_uebungen/23_typen_dokumentation.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/typing.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
