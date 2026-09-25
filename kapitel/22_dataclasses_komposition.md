# 22 · Dataclasses, Komposition und Vererbung

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](21_klassen.md) · [Nächstes Kapitel](23_typen_dokumentation.md)

**Stufe:** Vertiefung  
**Suchbegriffe:** dataclass field default_factory frozen inheritance super Komposition Vererbung

## Wozu brauche ich das?

Wenn eine Klasse vor allem Daten zusammenhält, kann `dataclass` wiederkehrenden Code erzeugen. Für die Zusammenarbeit mehrerer Klassen ist Komposition oft einfach: Ein Objekt benutzt ein anderes. Vererbung passt, wenn eine Unterklasse die Bedeutung und Erwartungen einer Oberklasse tatsächlich erfüllt.

## Erst verstehen

Ein **Decorator** wie `@dataclass` verarbeitet eine Klasse oder Funktion nach ihrer Definition. Dataclasses können unter anderem Initialisierung, Darstellung und Vergleich erzeugen. Komposition bedeutet "hat ein", Vererbung bedeutet fachlich "ist ein".

## Fall 1: Eine Datenklasse mit eigener Liste

Jede Aufgabe bekommt eigene Tags.

```python
from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    tags: list[str] = field(default_factory=list)

first = Task("Python")
second = Task("SQL")
first.tags.append("Lernen")
print(first)
print(second.tags)
```

**Erwartete Ausgabe:**

```text
Task(title='Python', tags=['Lernen'])
[]
```

**Schritt für Schritt:**

1. Die Typangaben beschreiben die beabsichtigten Felder.
2. `dataclass` erzeugt hier `__init__()` und eine lesbare Darstellung.
3. `default_factory=list` erzeugt für jedes Objekt eine neue Liste. Eine Typangabe validiert Eingaben nicht automatisch.

[Beispieldatei öffnen](../beispiele/22_dataclasses_komposition/fall_01.py)

```powershell
python ./beispiele/22_dataclasses_komposition/fall_01.py
```

## Fall 2: Verhalten durch Zusammenarbeit austauschen

Ein Dienst soll eine Begrüßung erzeugen, aber nicht selbst die Ausgabe bestimmen.

```python
class ConsolePrinter:
    def write(self, message):
        print(message)

class GreetingService:
    def __init__(self, printer):
        self.printer = printer

    def greet(self, name):
        self.printer.write(f"Hallo {name}")

service = GreetingService(ConsolePrinter())
service.greet("Basti")
```

**Erwartete Ausgabe:**

```text
Hallo Basti
```

**Schritt für Schritt:**

1. Der Dienst erhält sein Ausgabewerkzeug von außen.
2. Dadurch könnte im Test ein anderes Objekt mit einer `write()`-Methode eingesetzt werden.
3. Diese einfache Form der Abhängigkeitsübergabe benötigt kein zusätzliches Framework.

[Beispieldatei öffnen](../beispiele/22_dataclasses_komposition/fall_02.py)

```powershell
python ./beispiele/22_dataclasses_komposition/fall_02.py
```

## Fall 3: Eine Klasse gezielt erweitern

Ein spezieller Bericht ergänzt die Grundbeschreibung.

```python
class Report:
    def describe(self):
        return "Bericht"

class WeeklyReport(Report):
    def describe(self):
        return super().describe() + " für eine Woche"

print(WeeklyReport().describe())
```

**Erwartete Ausgabe:**

```text
Bericht für eine Woche
```

**Schritt für Schritt:**

1. Die Klammern hinter dem Klassennamen nennen die Oberklasse.
2. Die Unterklasse überschreibt `describe()`.
3. `super()` ruft die nächste passende Implementierung gemäß Methodenauflösung auf; bei dieser einfachen Hierarchie ist das die Oberklasse.

[Beispieldatei öffnen](../beispiele/22_dataclasses_komposition/fall_03.py)

```powershell
python ./beispiele/22_dataclasses_komposition/fall_03.py
```

## Typische Stolperstellen

Baue keine tiefen Vererbungsketten nur zur Wiederverwendung weniger Zeilen. `frozen=True` verhindert bei Dataclasses gewöhnliche Feldzuweisungen, macht aber enthaltene Listen nicht unveränderbar. Automatisch erzeugte Methoden ersetzen keine fachliche Validierung.

## Selbst anwenden

[Übung 22](../90_uebungen/22_dataclasses_komposition.md) · [Starterdatei](../90_uebungen/22_dataclasses_komposition.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/dataclasses.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
