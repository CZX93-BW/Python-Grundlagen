# 12 · Funktionen und Rückgabewerte

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](11_verschachteln_kopieren.md) · [Nächstes Kapitel](13_parameter_scope.md)

**Stufe:** Grundlage  
**Suchbegriffe:** def return Funktion Parameter Argument print None docstring

## Wozu brauche ich das?

Eine Funktion gibt einem wiederverwendbaren Ablauf einen Namen. Statt dieselbe Rechnung an mehreren Stellen zu schreiben, definierst du sie einmal und rufst sie mit passenden Werten auf. Kleine Funktionen lassen sich leichter verstehen und testen.

## Erst verstehen

Ein **Parameter** ist ein Platzhalter in der Definition. Ein **Argument** ist der konkrete Wert beim Aufruf. `return` beendet die Funktion und gibt einen Wert an den Aufrufer zurück. `print()` zeigt nur etwas an.

## Fall 1: Eine Berechnung wiederverwenden

Du möchtest beliebige Rechteckflächen berechnen.

```python
def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height

area = rectangle_area(4, 3)
print(area)
print(rectangle_area(height=5, width=2))
```

**Erwartete Ausgabe:**

```text
12
10
```

**Schritt für Schritt:**

1. `def` definiert die Funktion; der eingerückte Körper läuft erst beim Aufruf.
2. Die Werte 4 und 3 werden den Parametern zugeordnet.
3. Benannte Argumente machen die Bedeutung deutlich und erlauben eine andere Reihenfolge.

[Beispieldatei öffnen](../beispiele/12_funktionen/fall_01.py)

```powershell
python ./beispiele/12_funktionen/fall_01.py
```

## Fall 2: Ausgabe und Ergebnis unterscheiden

Du möchtest einen berechneten Wert weiterverarbeiten.

```python
def show_total(total):
    print(f"Gesamt: {total}")

result = show_total(15)
print(result)

def double(number):
    return number * 2

print(double(15) + 5)
```

**Erwartete Ausgabe:**

```text
Gesamt: 15
None
35
```

**Schritt für Schritt:**

1. `show_total()` zeigt einen Text, gibt aber nicht ausdrücklich einen Wert zurück.
2. Deshalb ist sein Rückgabewert `None`.
3. `double()` liefert eine Zahl, mit der anschließend weitergerechnet werden kann.

[Beispieldatei öffnen](../beispiele/12_funktionen/fall_02.py)

```powershell
python ./beispiele/12_funktionen/fall_02.py
```

## Fall 3: Früh zurückkehren und mehrere Werte liefern

Du möchtest einen Namen prüfen und Min/Max bestimmen.

```python
def greeting(name):
    if not name.strip():
        return "Name fehlt"
    return f"Hallo {name.strip()}"

def limits(numbers):
    if not numbers:
        return None
    return min(numbers), max(numbers)

print(greeting("  "))
smallest, largest = limits([7, 2, 9])
print(smallest, largest)
print(limits([]))
```

**Erwartete Ausgabe:**

```text
Name fehlt
2 9
None
```

**Schritt für Schritt:**

1. Die frühe Rückgabe behandelt zuerst den Sonderfall.
2. Mehrere Rückgabewerte werden als Tupel geliefert und können entpackt werden.
3. Für eine leere Liste gibt es hier bewusst `None`; der Aufrufer muss diesen Fall vor dem Entpacken behandeln.

[Beispieldatei öffnen](../beispiele/12_funktionen/fall_03.py)

```powershell
python ./beispiele/12_funktionen/fall_03.py
```

## Typische Stolperstellen

Code hinter einem unbedingt ausgeführten `return` wird in diesem Funktionsaufruf nicht erreicht. Eine Funktion sollte möglichst einen klaren Zweck erfüllen. Eine starre Zeilenzahl garantiert keine gute Qualität: Verständlichkeit, passende Namen und überschaubare Verantwortung sind wichtiger.

## Selbst anwenden

[Übung 12](../90_uebungen/12_funktionen.md) · [Starterdatei](../90_uebungen/12_funktionen.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/tutorial/controlflow.html#defining-functions)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
