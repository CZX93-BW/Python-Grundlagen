# 09 · Tupel, Sets und die passende Sammlung

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](08_listen.md) · [Nächstes Kapitel](10_dictionaries.md)

**Stufe:** Grundlage  
**Suchbegriffe:** tuple set frozenset unpacking entpacken Duplikate Schnittmenge Vereinigung hashable

## Wozu brauche ich das?

Nicht jede Sammlung muss eine Liste sein. Ein Tupel hält eine feste Folge zusammen. Ein Set speichert eindeutige, hashbare Werte und eignet sich für Mengenvergleiche. "Hashbar" bedeutet vereinfacht, dass ein Wert als stabiler Schlüssel genutzt werden kann.

## Erst verstehen

Listen sind geordnet und veränderbar. Tupel sind geordnet, ihre direkten Einträge lassen sich nicht ersetzen. Sets garantieren keine Positionsreihenfolge und bieten keine Indexzugriffe. Eine leere Menge schreibst du `set()`; `{}` ist ein Dictionary.

## Fall 1: Zusammengehörige Werte entpacken

Du möchtest ein Koordinatenpaar in sprechende Namen zerlegen.

```python
point = (10, 20)
x, y = point
single = (10,)
print(x, y)
print(single)
first, *middle, last = [1, 2, 3, 4]
print(first, middle, last)
```

**Erwartete Ausgabe:**

```text
10 20
(10,)
1 [2, 3] 4
```

**Schritt für Schritt:**

1. Entpacken verteilt Werte auf mehrere Namen.
2. Das Komma macht `(10,)` zum Tupel mit einem Element; `(10)` wäre nur die Zahl.
3. Ein Stern sammelt die übrigen Werte in einer Liste. Ohne Stern muss die Anzahl genau passen.

[Beispieldatei öffnen](../beispiele/09_tupel_sets/fall_01.py)

```powershell
python ./beispiele/09_tupel_sets/fall_01.py
```

## Fall 2: Doppelte Werte und Mengen vergleichen

Du vergleichst die Fähigkeiten zweier Personen.

```python
first = {"Python", "HTML", "Python"}
second = {"Python", "SQL"}
print(sorted(first))
print(sorted(first & second))
print(sorted(first | second))
print(sorted(first - second))
```

**Erwartete Ausgabe:**

```text
['HTML', 'Python']
['Python']
['HTML', 'Python', 'SQL']
['HTML']
```

**Schritt für Schritt:**

1. Doppelte Set-Einträge verschwinden.
2. `&` ist die Schnittmenge, `|` die Vereinigung, `-` die Differenz.
3. `sorted()` macht die Ausgabe stabil und liefert dafür eine Liste.

[Beispieldatei öffnen](../beispiele/09_tupel_sets/fall_02.py)

```powershell
python ./beispiele/09_tupel_sets/fall_02.py
```

## Fall 3: Ein Set verändern

Du pflegst eine Sammlung bereits bearbeiteter IDs.

```python
processed_ids = set()
processed_ids.add(3)
processed_ids.add(3)
processed_ids.update([4, 5])
processed_ids.discard(99)
processed_ids.remove(4)
print(sorted(processed_ids))
print(3 in processed_ids)
```

**Erwartete Ausgabe:**

```text
[3, 5]
True
```

**Schritt für Schritt:**

1. `add()` ergänzt einen Wert, `update()` mehrere.
2. `discard()` ist auch bei einem fehlenden Wert erlaubt.
3. `remove()` verlangt dagegen, dass der Wert vorhanden ist, sonst entsteht `KeyError`.

[Beispieldatei öffnen](../beispiele/09_tupel_sets/fall_03.py)

```powershell
python ./beispiele/09_tupel_sets/fall_03.py
```

## Typische Stolperstellen

Listen und Dictionaries sind nicht hashbar und können deshalb keine Set-Elemente sein. Ein Tupel ist nur hashbar, wenn seine Elemente hashbar sind. Ein Tupel kann eine veränderbare Liste enthalten; "Tupel unveränderbar" bedeutet nicht, dass automatisch alle enthaltenen Objekte unveränderbar werden.

## Selbst anwenden

[Übung 09](../90_uebungen/09_tupel_sets.md) · [Starterdatei](../90_uebungen/09_tupel_sets.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/stdtypes.html#set-types-set-frozenset)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
