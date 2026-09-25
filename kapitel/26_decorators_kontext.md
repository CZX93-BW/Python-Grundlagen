# 26 · Decorators und Kontextmanager

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](25_iteratoren_generatoren.md) · [Nächstes Kapitel](27_sqlite.md)

**Stufe:** Vertiefung  
**Suchbegriffe:** decorator wraps closure contextmanager with try finally yield Wrapper

## Wozu brauche ich das?

Diese Werkzeuge sind optionales Vertiefungswissen. Ein Decorator erweitert das Verhalten einer Funktion, ohne jeden Aufruf anzupassen. Ein Kontextmanager fasst den geordneten Anfang und Abschluss einer Aktion zusammen.

## Erst verstehen

Ein **Wrapper** ist eine umhüllende Funktion. Eine **Closure** ist eine Funktion, die auf Namen aus einem umschließenden Funktionsbereich zugreift. Ein Kontextmanager wird mit `with` verwendet und kümmert sich beispielsweise um das Schließen einer Datei.

## Fall 1: Eine Funktion weitergeben

Funktionen können wie andere Werte gespeichert und übergeben werden.

```python
def double(number):
    return number * 2

def apply(operation, value):
    return operation(value)

print(apply(double, 4))
```

**Erwartete Ausgabe:**

```text
8
```

**Schritt für Schritt:**

1. `double` ohne Klammern ist das Funktionsobjekt.
2. `apply()` bekommt dieses Objekt als Parameter.
3. Erst `operation(value)` ruft die übergebene Funktion auf. Das ist die Grundlage vieler Decorators.

[Beispieldatei öffnen](../beispiele/26_decorators_kontext/fall_01.py)

```powershell
python ./beispiele/26_decorators_kontext/fall_01.py
```

## Fall 2: Einen Aufruf sichtbar umhüllen

Vor einer Aktion soll eine Meldung erscheinen.

```python
from functools import wraps

def announce(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Aufruf beginnt")
        return function(*args, **kwargs)
    return wrapper

@announce
def greet(name):
    return f"Hallo {name}"

print(greet("Ada"))
print(greet.__name__)
```

**Erwartete Ausgabe:**

```text
Aufruf beginnt
Hallo Ada
greet
```

**Schritt für Schritt:**

1. `@announce` entspricht hier `greet = announce(greet)`.
2. Der Wrapper ergänzt Verhalten und leitet Argumente sowie Rückgabewert weiter.
3. `wraps()` bewahrt wichtige Metadaten wie den Funktionsnamen für Dokumentation und Fehlersuche.

[Beispieldatei öffnen](../beispiele/26_decorators_kontext/fall_02.py)

```powershell
python ./beispiele/26_decorators_kontext/fall_02.py
```

## Fall 3: Aufräumen mit einem Kontextmanager

Ein Abschluss soll auch bei einem Fehler erfolgen.

```python
from contextlib import contextmanager

@contextmanager
def operation():
    print("Start")
    try:
        yield "Arbeitsbereich"
    finally:
        print("Abschluss")

with operation() as name:
    print(name)
```

**Erwartete Ausgabe:**

```text
Start
Arbeitsbereich
Abschluss
```

**Schritt für Schritt:**

1. Code vor `yield` richtet den Bereich ein.
2. Der Wert von `yield` wird hinter `as` verfügbar.
3. Beim Verlassen des with-Blocks läuft der Abschluss im finally-Block. `contextmanager` erwartet genau ein yield pro normalem Durchlauf.

[Beispieldatei öffnen](../beispiele/26_decorators_kontext/fall_03.py)

```powershell
python ./beispiele/26_decorators_kontext/fall_03.py
```

## Typische Stolperstellen

Decorators können Kontrollflüsse verstecken; setze sie gezielt und sparsam ein. Ein `return` im finally-Block kann Ergebnisse oder Fehler überschreiben. Nutze für Dateien und Datenbankverbindungen möglichst die bereits vorhandenen Kontextmanager.

## Selbst anwenden

[Übung 26](../90_uebungen/26_decorators_kontext.md) · [Starterdatei](../90_uebungen/26_decorators_kontext.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/contextlib.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
