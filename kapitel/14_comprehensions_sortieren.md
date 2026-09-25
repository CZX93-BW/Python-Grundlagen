# 14 · Filtern, umwandeln und sortieren

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](13_parameter_scope.md) · [Nächstes Kapitel](15_module.md)

**Stufe:** Aufbau  
**Suchbegriffe:** comprehension lambda sorted key filter map any all sum min max

## Wozu brauche ich das?

Häufig soll eine Sammlung gefiltert oder in eine andere Form gebracht werden. Beginne mit einer normalen Schleife. Wenn der Ablauf kurz und eindeutig bleibt, kannst du eine Comprehension verwenden: eine kompakte Schreibweise zum Erzeugen einer Sammlung.

## Erst verstehen

Die Form `[ausdruck for element in sammlung if bedingung]` beschreibt Ergebnis, Quelle und optionalen Filter. `sorted(..., key=...)` bestimmt, welcher Wert für die Sortierung zählt. `lambda` erzeugt eine kleine unbenannte Funktion für einen Ausdruck.

## Fall 1: Eine Schleife verkürzen

Du möchtest die Quadrate aller geraden Zahlen.

```python
numbers = [1, 2, 3, 4]
result = []
for number in numbers:
    if number % 2 == 0:
        result.append(number ** 2)
print(result)
print([number ** 2 for number in numbers if number % 2 == 0])
```

**Erwartete Ausgabe:**

```text
[4, 16]
[4, 16]
```

**Schritt für Schritt:**

1. Die normale Schleife zeigt alle Schritte ausdrücklich.
2. Die Comprehension führt dieselbe Filterung und Umwandlung aus.
3. Du musst nicht jede Schleife ersetzen. Bei mehreren verschachtelten Entscheidungen ist die lange Form oft verständlicher.

[Beispieldatei öffnen](../beispiele/14_comprehensions_sortieren/fall_01.py)

```powershell
python ./beispiele/14_comprehensions_sortieren/fall_01.py
```

## Fall 2: Nach einem Feld sortieren

Du möchtest Personen nach Alter und bei Gleichstand nach Name ordnen.

```python
people = [
    {"name": "Basti", "age": 32},
    {"name": "Ada", "age": 32},
    {"name": "Mira", "age": 25},
]
ordered = sorted(people, key=lambda person: (person["age"], person["name"]))
print([person["name"] for person in ordered])
print(sorted(["Banane", "apfel"], key=str.casefold))
```

**Erwartete Ausgabe:**

```text
['Mira', 'Ada', 'Basti']
['apfel', 'Banane']
```

**Schritt für Schritt:**

1. `key` bekommt eine Funktion, die zu jedem Element den Vergleichswert liefert.
2. Ein Tupel ermöglicht mehrere Sortierkriterien; zuerst Alter, dann Name.
3. `str.casefold` kann direkt als Funktion übergeben werden. `sorted()` ist stabil: Bei gleichem Schlüssel bleibt die ursprüngliche Reihenfolge erhalten.

[Beispieldatei öffnen](../beispiele/14_comprehensions_sortieren/fall_02.py)

```powershell
python ./beispiele/14_comprehensions_sortieren/fall_02.py
```

## Fall 3: Neue Dictionaries und schnelle Prüfungen

Du möchtest Werte zuordnen und eine Sammlung zusammenfassen.

```python
numbers = [1, 2, 3]
squares = {number: number ** 2 for number in numbers}
print(squares)
print(sum(numbers))
print(any(number > 2 for number in numbers))
print(all(number > 0 for number in numbers))
print(any([]), all([]))
print(max([], default=0))
```

**Erwartete Ausgabe:**

```text
{1: 1, 2: 4, 3: 9}
6
True
True
False True
0
```

**Schritt für Schritt:**

1. `{schlüssel: wert for ...}` erzeugt ein Dictionary.
2. `any()` ist wahr, sobald mindestens eine Bedingung wahr ist; `all()` verlangt alle.
3. Für eine leere Sammlung ist `any()` falsch und `all()` wahr. `default` verhindert bei `max()` einen Fehler für eine leere Eingabe.

[Beispieldatei öffnen](../beispiele/14_comprehensions_sortieren/fall_03.py)

```powershell
python ./beispiele/14_comprehensions_sortieren/fall_03.py
```

## Typische Stolperstellen

Vermeide Comprehensions nur für Seiteneffekte wie `[print(x) for x in items]`; dafür passt eine normale Schleife. Fehlende Sortierschlüssel verursachen beim Klammerzugriff `KeyError`. Ein Standardwert im `key` muss zu den anderen Vergleichswerten passen; `None` und Zahlen sind nicht allgemein sortierbar.

## Selbst anwenden

[Übung 14](../90_uebungen/14_comprehensions_sortieren.md) · [Starterdatei](../90_uebungen/14_comprehensions_sortieren.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/howto/sorting.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
