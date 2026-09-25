# 11 · Verschachtelte Daten und Kopien

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](10_dictionaries.md) · [Nächstes Kapitel](12_funktionen.md)

**Stufe:** Aufbau  
**Suchbegriffe:** nested verschachtelt Referenz shallow copy deepcopy mutable alias Liste Dictionary

## Wozu brauche ich das?

Eine Liste von Dictionaries ist ein typisches Datenmodell: Die Liste enthält mehrere Datensätze, jedes Dictionary die Eigenschaften eines Datensatzes. Deine ursprüngliche Notizübung verwendet genau diesen Aufbau.

## Erst verstehen

Eine **Referenz** ist ein Verweis auf ein Objekt. Bei `other = notes` entstehen zwei Namen für dieselbe Liste. Eine **flache Kopie** erzeugt eine neue äußere Sammlung. Eine **tiefe Kopie** kopiert geeignete enthaltene Objekte rekursiv mit.

## Fall 1: Einen Datensatz in einer Liste ändern

Du bearbeitest den Titel der ersten Notiz.

```python
notes = [
    {"title": "Einkauf", "text": "Milch"},
    {"title": "Arbeit", "text": "Anruf"},
]
notes[0]["title"] = "Wocheneinkauf"
for note in notes:
    print(note["title"])
```

**Erwartete Ausgabe:**

```text
Wocheneinkauf
Arbeit
```

**Schritt für Schritt:**

1. `notes[0]` liefert das erste Dictionary.
2. `["title"]` greift darin auf den Titel zu.
3. Die Änderung betrifft dieses Dictionary. Bei einer leeren Liste wäre der erste Zugriff nicht möglich.

[Beispieldatei öffnen](../beispiele/11_verschachteln_kopieren/fall_01.py)

```powershell
python ./beispiele/11_verschachteln_kopieren/fall_01.py
```

## Fall 2: Zuweisung und flache Kopie unterscheiden

Du möchtest eine Liste erweitern, ohne die zweite äußere Liste zu erweitern.

```python
original = [{"title": "Alt"}]
alias = original
shallow = original.copy()
alias.append({"title": "Neu"})
shallow[0]["title"] = "Geändert"
print(len(original), len(shallow))
print(original[0]["title"])
print(alias is original)
```

**Erwartete Ausgabe:**

```text
2 1
Geändert
True
```

**Schritt für Schritt:**

1. `alias` und `original` bezeichnen dieselbe Liste; `append()` ist über beide sichtbar.
2. `shallow` ist eine eigene Liste und bekommt den zusätzlichen Eintrag nicht.
3. Das erste Dictionary ist aber geteilt. Deshalb ändert der Zugriff über `shallow` auch den sichtbaren Titel in `original`.

[Beispieldatei öffnen](../beispiele/11_verschachteln_kopieren/fall_02.py)

```powershell
python ./beispiele/11_verschachteln_kopieren/fall_02.py
```

## Fall 3: Unabhängige verschachtelte Daten erzeugen

Du brauchst eine bearbeitbare Kopie einfacher verschachtelter Daten.

```python
from copy import deepcopy

original = [{"title": "Alt"}]
independent = deepcopy(original)
independent[0]["title"] = "Neu"
print(original)
print(independent)
rows = [[0] * 2 for _ in range(2)]
rows[0][0] = 1
print(rows)
```

**Erwartete Ausgabe:**

```text
[{'title': 'Alt'}]
[{'title': 'Neu'}]
[[1, 0], [0, 0]]
```

**Schritt für Schritt:**

1. `deepcopy()` erzeugt hier auch ein neues inneres Dictionary.
2. Änderungen bleiben damit in der Kopie.
3. Die List Comprehension erzeugt für jede Zeile eine eigene Liste. Kapitel 14 erklärt diese Kurzschreibweise.

**Achte darauf:** `[[0] * 2] * 2` würde dieselbe innere Liste zweimal referenzieren; eine Änderung erschiene dann in beiden Zeilen.

[Beispieldatei öffnen](../beispiele/11_verschachteln_kopieren/fall_03.py)

```powershell
python ./beispiele/11_verschachteln_kopieren/fall_03.py
```

## Typische Stolperstellen

`deepcopy()` ist kein pauschales Heilmittel: Große Datenmengen kosten Speicher und Laufzeit, und externe Ressourcen wie offene Dateien lassen sich nicht wie normale Datensätze kopieren. Überlege zuerst, ob eine neue kleine Datenstruktur statt einer vollständigen Kopie genügt.

## Selbst anwenden

[Übung 11](../90_uebungen/11_verschachteln_kopieren.md) · [Starterdatei](../90_uebungen/11_verschachteln_kopieren.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/copy.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
