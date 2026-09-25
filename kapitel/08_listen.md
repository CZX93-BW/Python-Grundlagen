# 08 · Listen erstellen, ändern und durchsuchen

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](07_schleifen.md) · [Nächstes Kapitel](09_tupel_sets.md)

**Stufe:** Grundlage  
**Suchbegriffe:** list append extend insert remove pop del index slice in len sort sorted

## Wozu brauche ich das?

Eine Liste speichert mehrere Werte in einer festen Reihenfolge. Sie ist veränderbar und darf doppelte Einträge enthalten. Typische Beispiele sind Aufgaben, Warenkörbe oder deine Notizen.

## Erst verstehen

Die Schreibweise ist `[wert1, wert2]`. Ein Index beginnt bei 0. `len(items)` liefert die Anzahl. Eine Liste enthält Referenzen auf ihre Elemente; das wird bei verschachtelten Daten in Kapitel 11 wichtig.

## Fall 1: Anlegen, ergänzen und ändern

Du pflegst eine Einkaufsliste.

```python
items = ["Brot", "Milch"]
items.append("Eier")
items.extend(["Apfel", "Tee"])
items.insert(1, "Kaffee")
items[0] = "Vollkornbrot"
print(items)
print(items[:2])
```

**Erwartete Ausgabe:**

```text
['Vollkornbrot', 'Kaffee', 'Milch', 'Eier', 'Apfel', 'Tee']
['Vollkornbrot', 'Kaffee']
```

**Schritt für Schritt:**

1. `append()` fügt ein einzelnes Element hinten an.
2. `extend()` fügt mehrere Elemente aus einer anderen Sammlung hinzu. `insert()` fügt an einer Position ein.
3. Über den Index ersetzt du einen Eintrag. Der Slice `[:2]` erzeugt eine neue äußere Liste mit den ersten zwei Elementen.

[Beispieldatei öffnen](../beispiele/08_listen/fall_01.py)

```powershell
python ./beispiele/08_listen/fall_01.py
```

## Fall 2: Löschen nach Wert oder Position

Du möchtest gezielt Einträge entfernen.

```python
items = ["Brot", "Milch", "Milch", "Eier"]
items.remove("Milch")
removed = items.pop(0)
print(removed)
print(items)
del items[-1]
print(items)
```

**Erwartete Ausgabe:**

```text
Brot
['Milch', 'Eier']
['Milch']
```

**Schritt für Schritt:**

1. `remove()` entfernt den ersten passenden Wert.
2. `pop(0)` entfernt die Position 0 und gibt den entfernten Wert zurück.
3. `del` löscht einen Eintrag ohne Rückgabewert. `pop()` ohne Index entfernt das letzte Element.

**Achte darauf:** `remove()` wirft bei einem fehlenden Wert `ValueError`; `pop()` auf einer leeren Liste wirft `IndexError`.

[Beispieldatei öffnen](../beispiele/08_listen/fall_02.py)

```powershell
python ./beispiele/08_listen/fall_02.py
```

## Fall 3: Suchen und sortieren

Du möchtest eine sortierte Ansicht, ohne die ursprüngliche Reihenfolge zu verlieren.

```python
numbers = [5, 2, 5, 1]
print(2 in numbers)
print(numbers.index(5))
print(sorted(numbers))
print(numbers)
result = numbers.sort(reverse=True)
print(numbers)
print(result)
```

**Erwartete Ausgabe:**

```text
True
0
[1, 2, 5, 5]
[5, 2, 5, 1]
[5, 5, 2, 1]
None
```

**Schritt für Schritt:**

1. `in` prüft das Vorkommen; `index()` gibt die erste Fundposition zurück.
2. `sorted()` erstellt eine neue Liste.
3. `sort()` verändert die vorhandene Liste und gibt `None` zurück. Speichere diesen Rückgabewert nicht als neue Liste.

[Beispieldatei öffnen](../beispiele/08_listen/fall_03.py)

```powershell
python ./beispiele/08_listen/fall_03.py
```

## Typische Stolperstellen

`items = items.append(value)` ist ein Fehler: `append()` gibt `None` zurück. Sichere einen möglichen Zugriff auf das erste Element mit `if items:` ab. Suche nach Werten und Löschen am Anfang einer großen Liste können viele Elemente durchlaufen beziehungsweise verschieben.

## Selbst anwenden

[Übung 08](../90_uebungen/08_listen.md) · [Starterdatei](../90_uebungen/08_listen.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/tutorial/datastructures.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
