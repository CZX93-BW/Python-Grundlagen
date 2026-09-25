# 21 · Klassen, Objekte und Methoden

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](20_standardhelfer.md) · [Nächstes Kapitel](22_dataclasses_komposition.md)

**Stufe:** Aufbau  
**Suchbegriffe:** class self __init__ Objekt Instanz Attribut Methode OOP property

## Wozu brauche ich das?

Eine Klasse beschreibt, welche Daten und welches Verhalten zusammengehören. Ein Objekt ist eine konkrete Instanz dieser Klasse. Du brauchst nicht für jede kleine Funktion eine Klasse; sie ist besonders hilfreich, wenn ein klarer Zustand mit passenden Aktionen zusammengehört.

## Erst verstehen

`__init__()` initialisiert eine neue Instanz. `self` bezeichnet in einer Instanzmethode das gerade verwendete Objekt. **Attribute** sind gespeicherte Eigenschaften. **Methoden** sind Funktionen, die zur Klasse gehören.

## Fall 1: Ein einfaches Objekt bauen

Jede Notiz soll ihren eigenen Titel und Text haben.

```python
class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def summary(self):
        return f"{self.title}: {self.text}"

note = Note("Einkauf", "Milch")
print(note.summary())
note.title = "Wochenende"
print(note.summary())
```

**Erwartete Ausgabe:**

```text
Einkauf: Milch
Wochenende: Milch
```

**Schritt für Schritt:**

1. `Note(...)` erzeugt die Instanz und ruft ihre Initialisierung auf.
2. `self.title` gehört zu dieser konkreten Notiz.
3. Bei `note.summary()` übergibt Python die Instanz automatisch als `self`.

[Beispieldatei öffnen](../beispiele/21_klassen/fall_01.py)

```powershell
python ./beispiele/21_klassen/fall_01.py
```

## Fall 2: Zustände pro Instanz trennen

Zwei Notizbücher dürfen keine gemeinsame Eintragsliste bekommen.

```python
class Notebook:
    def __init__(self):
        self.notes = []

    def add(self, title):
        self.notes.append(title)

first = Notebook()
second = Notebook()
first.add("Python lernen")
print(first.notes)
print(second.notes)
```

**Erwartete Ausgabe:**

```text
['Python lernen']
[]
```

**Schritt für Schritt:**

1. Die Liste entsteht bei jedem `__init__()`-Aufruf neu.
2. Änderungen betreffen damit nur das jeweilige Objekt.
3. Eine veränderbare Liste direkt im Klassenkörper wäre ein Klassenattribut und würde von Instanzen geteilt, solange sie nicht überschattet wird.

[Beispieldatei öffnen](../beispiele/21_klassen/fall_02.py)

```powershell
python ./beispiele/21_klassen/fall_02.py
```

## Fall 3: Eine berechnete Eigenschaft anbieten

Eine Fläche soll immer zu den aktuellen Seitenlängen passen.

```python
class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Seiten müssen positiv sein")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rectangle = Rectangle(4, 3)
print(rectangle.area)
rectangle.width = 5
print(rectangle.area)
```

**Erwartete Ausgabe:**

```text
12
15
```

**Schritt für Schritt:**

1. Der Konstruktor prüft die Anfangswerte.
2. `@property` erlaubt `rectangle.area` ohne Methodenklammern.
3. Die Fläche wird bei jedem Zugriff berechnet und muss nicht separat aktuell gehalten werden.

**Achte darauf:** Die öffentlichen Seitenattribute sind in dieser einfachen Version später frei änderbar. Wenn eine Regel immer gelten muss, brauchst du auch für spätere Änderungen eine geprüfte Schnittstelle.

[Beispieldatei öffnen](../beispiele/21_klassen/fall_03.py)

```powershell
python ./beispiele/21_klassen/fall_03.py
```

## Typische Stolperstellen

`_name` ist eine Konvention für interne Nutzung, kein echter Zugriffsschutz. `__name` verwendet Name Mangling und ist ebenfalls kein Sicherheitsmechanismus. Trenne eine fachliche Klasse von Terminaleingaben und Dateizugriff, damit sie einfacher getestet werden kann.

## Selbst anwenden

[Übung 21](../90_uebungen/21_klassen.md) · [Starterdatei](../90_uebungen/21_klassen.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/tutorial/classes.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
