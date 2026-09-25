# 15 · Module, Pakete und Imports

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](14_comprehensions_sortieren.md) · [Nächstes Kapitel](16_fehler.md)

**Stufe:** Aufbau  
**Suchbegriffe:** import from Modul Paket __name__ __main__ __init__ venv pip sys.path ModuleNotFoundError

## Wozu brauche ich das?

Ein Modul ist üblicherweise eine Python-Datei. Du kannst Funktionen daraus in anderen Dateien nutzen. Ein reguläres Paket ist ein Ordner mit einer `__init__.py`, in dem zusammengehörige Module liegen. Installation und Import sind zwei verschiedene Schritte.

## Erst verstehen

`import math` macht das Modul unter seinem Namen verfügbar. `from math import sqrt` importiert gezielt einen Namen. `pip` installiert zusätzliche Pakete in eine Python-Umgebung; `import` lädt ein verfügbares Modul in dein laufendes Programm.

## Fall 1: Die Standardbibliothek importieren

Du möchtest vorhandene Mathematikfunktionen verwenden.

```python
import math
from statistics import mean

print(math.sqrt(16))
print(mean([2, 4, 6]))
```

**Erwartete Ausgabe:**

```text
4.0
4
```

**Schritt für Schritt:**

1. `math` und `statistics` sind Teil der Python-Standardbibliothek. Dafür ist keine zusätzliche Installation nötig.
2. Mit dem Modulnamen bleibt die Herkunft von `sqrt()` sichtbar.
3. Beim gezielten Import kann `mean()` direkt aufgerufen werden.

[Beispieldatei öffnen](../beispiele/15_module/fall_01.py)

```powershell
python ./beispiele/15_module/fall_01.py
```

## Fall 2: Den Programmstart schützen

Eine Datei soll beim Import keine Demo starten.

```python
def greet(name):
    return f"Hallo {name}"

def main():
    print(greet("Basti"))

if __name__ == "__main__":
    main()
```

**Erwartete Ausgabe:**

```text
Hallo Basti
```

**Schritt für Schritt:**

1. Beim direkten Start trägt `__name__` den Wert `"__main__"`.
2. Beim Import trägt es den Modulnamen. Deshalb läuft die Demo nur beim direkten Start.
3. Funktionsdefinitionen bleiben trotzdem importierbar. Lege wiederverwendbare Logik oberhalb dieses Startblocks ab.

[Beispieldatei öffnen](../beispiele/15_module/fall_02.py)

```powershell
python ./beispiele/15_module/fall_02.py
```

## Fall 3: Ein eigenes Modul laden

Du möchtest sehen, wie Dateien zusammenarbeiten.

```python
from greetings import greet

print(greet("Ada"))
```

**Erwartete Ausgabe:**

```text
Hallo Ada
```

**Schritt für Schritt:**

1. Öffne auch die Datei `greetings.py` im selben Beispielordner. Sie definiert `greet(name)` und gibt einen Begrüßungstext zurück.
2. `from greetings import greet` übernimmt diese Funktion. Du schreibst beim Import keine Dateiendung.
3. Die letzte Zeile ruft sie auf. Starte diese Beispieldatei aus dem Projektordner mit dem darunter angegebenen Befehl.

**Achte darauf:** Eine Datei enthält die wiederverwendbare Funktion, die andere deren Aufruf. Das ist bereits eine kleine Trennung von Logik und Verwendung.

[Beispieldatei öffnen](../beispiele/15_module/fall_03.py)

```powershell
python ./beispiele/15_module/fall_03.py
```

## Typische Stolperstellen

Benenne eigene Dateien nicht `json.py`, `typing.py` oder `random.py`, wenn du die gleichnamigen Standardmodule nutzen möchtest. Vermeide `from modul import *`. Bei `ModuleNotFoundError` zuerst den ausgewählten Interpreter, den Installationsort und den Startordner prüfen; nicht pauschal `sys.path` verändern.

## Selbst anwenden

[Übung 15](../90_uebungen/15_module.md) · [Starterdatei](../90_uebungen/15_module.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/tutorial/modules.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
