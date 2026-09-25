# 25 · Iteratoren und Generatoren

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](24_tests_logging.md) · [Nächstes Kapitel](26_decorators_kontext.md)

**Stufe:** Vertiefung  
**Suchbegriffe:** iter next yield generator iterable StopIteration lazy range Generatorausdruck

## Wozu brauche ich das?

Eine Liste hält ihre Elemente bereits bereit. Ein Generator erzeugt Werte erst nach Bedarf. Das ist hilfreich, wenn sehr viele Werte nacheinander verarbeitet werden sollen und nicht gleichzeitig im Speicher liegen müssen.

## Erst verstehen

Ein **Iterable** lässt sich durchlaufen. Ein **Iterator** merkt sich dabei seine aktuelle Position. `iter()` liefert einen Iterator; `next()` holt den nächsten Wert. Eine Funktion mit `yield` erzeugt beim Aufruf einen Generator.

## Fall 1: Einen Iterator schrittweise lesen

Du möchtest Werte einzeln abholen.

```python
iterator = iter(["A", "B"])
print(next(iterator))
print(next(iterator))
print(next(iterator, "Ende"))
```

**Erwartete Ausgabe:**

```text
A
B
Ende
```

**Schritt für Schritt:**

1. `iter()` erzeugt einen zustandsbehafteten Durchläufer.
2. Jeder next-Aufruf bewegt ihn weiter.
3. Ein Standardwert verhindert hier `StopIteration`, sobald keine Werte mehr da sind.

[Beispieldatei öffnen](../beispiele/25_iteratoren_generatoren/fall_01.py)

```powershell
python ./beispiele/25_iteratoren_generatoren/fall_01.py
```

## Fall 2: Werte mit yield erzeugen

Du möchtest einen Countdown ohne vorbereitete Liste.

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

values = countdown(3)
print(next(values))
print(list(values))
print(list(values))
```

**Erwartete Ausgabe:**

```text
3
[2, 1]
[]
```

**Schritt für Schritt:**

1. Beim Funktionsaufruf wird zunächst nur der Generator erzeugt.
2. `yield` liefert einen Wert und pausiert die Funktion. Beim nächsten Abruf läuft sie danach weiter.
3. Nach dem Verbrauch ist derselbe Generator leer. Für einen neuen Durchlauf brauchst du einen neuen Aufruf.

[Beispieldatei öffnen](../beispiele/25_iteratoren_generatoren/fall_02.py)

```powershell
python ./beispiele/25_iteratoren_generatoren/fall_02.py
```

## Fall 3: Einen Generatorausdruck verwenden

Du willst nur die Summe und keine zusätzliche Ergebnisliste.

```python
numbers = [1, 2, 3, 4]
squares = (number ** 2 for number in numbers)
print(sum(squares))
print(list(squares))
```

**Erwartete Ausgabe:**

```text
30
[]
```

**Schritt für Schritt:**

1. Runde statt eckiger Klammern erzeugen hier einen Generatorausdruck.
2. `sum()` ruft seine Werte nacheinander ab.
3. Danach ist der Generator erschöpft. Das spart eine Zwischenliste, garantiert aber nicht automatisch kürzere Laufzeit.

[Beispieldatei öffnen](../beispiele/25_iteratoren_generatoren/fall_03.py)

```powershell
python ./beispiele/25_iteratoren_generatoren/fall_03.py
```

## Typische Stolperstellen

Ein Generator ist nicht wie eine Liste beliebig oft durchlaufbar und unterstützt normalerweise kein `len()` oder Indexieren. Werden bei seiner Erzeugung oder Verarbeitung Ressourcen geöffnet, muss auch bei vorzeitigem Abbruch ihre Lebensdauer bedacht werden.

## Selbst anwenden

[Übung 25](../90_uebungen/25_iteratoren_generatoren.md) · [Starterdatei](../90_uebungen/25_iteratoren_generatoren.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/tutorial/classes.html#generators)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
