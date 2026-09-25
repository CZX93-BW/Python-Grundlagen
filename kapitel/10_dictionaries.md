# 10 · Dictionaries und Schlüssel-Wert-Paare

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](09_tupel_sets.md) · [Nächstes Kapitel](11_verschachteln_kopieren.md)

**Stufe:** Grundlage  
**Suchbegriffe:** dict dictionary get keys values items update pop setdefault Schlüssel Objekt

## Wozu brauche ich das?

Ein Dictionary verbindet Schlüssel mit Werten. Du greifst auf Daten über einen Namen zu, etwa `person["email"]`, statt ihre Listenposition zu kennen. Das passt gut zu einzelnen Datensätzen und JSON-Objekten.

## Erst verstehen

Die Schreibweise ist `{"name": "Basti"}`. Schlüssel sind eindeutig und müssen hashbar sein. Werte dürfen beliebige Objekte sein. Dictionaries bewahren die Einfügereihenfolge, sind aber nicht automatisch nach Schlüsseln sortiert.

## Fall 1: Lesen, ergänzen und ändern

Du verwaltest einen kleinen Kontaktdatensatz.

```python
person = {"name": "Basti", "age": 32}
print(person["name"])
print(person.get("phone", "Nicht hinterlegt"))
person["age"] = 33
person["city"] = "Bottrop"
person.update({"active": True})
print(person)
```

**Erwartete Ausgabe:**

```text
Basti
Nicht hinterlegt
{'name': 'Basti', 'age': 33, 'city': 'Bottrop', 'active': True}
```

**Schritt für Schritt:**

1. Eckige Klammern verlangen einen vorhandenen Schlüssel.
2. `get()` liefert bei fehlendem Schlüssel einen Standardwert.
3. Zuweisung ergänzt oder ersetzt einen Wert. `update()` übernimmt Schlüssel-Wert-Paare aus einem anderen Mapping.

[Beispieldatei öffnen](../beispiele/10_dictionaries/fall_01.py)

```powershell
python ./beispiele/10_dictionaries/fall_01.py
```

## Fall 2: Durch Schlüssel und Werte gehen

Du möchtest jeden Eintrag anzeigen.

```python
person = {"name": "Ada", "active": True}
for key, value in person.items():
    print(f"{key}: {value}")
print("name" in person)
print(list(person.keys()))
print(list(person.values()))
```

**Erwartete Ausgabe:**

```text
name: Ada
active: True
True
['name', 'active']
['Ada', True]
```

**Schritt für Schritt:**

1. `items()` liefert Schlüssel und Wert gemeinsam.
2. `in` prüft bei einem Dictionary seine Schlüssel, nicht seine Werte.
3. `keys()` und `values()` liefern Ansichten. `list()` macht für die Anzeige eine konkrete Liste daraus.

[Beispieldatei öffnen](../beispiele/10_dictionaries/fall_02.py)

```powershell
python ./beispiele/10_dictionaries/fall_02.py
```

## Fall 3: Fehlende Werte und Löschen

Du möchtest zwischen einem fehlenden Schlüssel und einem vorhandenen None unterscheiden.

```python
settings = {"theme": None}
print(settings.get("theme", "light"))
print(settings.get("language", "de"))
settings.setdefault("language", "de")
removed = settings.pop("theme", "Nicht vorhanden")
print(removed)
print(settings)
```

**Erwartete Ausgabe:**

```text
None
de
None
{'language': 'de'}
```

**Schritt für Schritt:**

1. Ein vorhandenes `None` wird durch den Standardwert von `get()` nicht ersetzt.
2. `setdefault()` ergänzt nur einen fehlenden Schlüssel.
3. `pop()` entfernt einen Schlüssel und liefert seinen Wert. Ein zweites Argument verhindert `KeyError`, wenn der Schlüssel fehlt.

[Beispieldatei öffnen](../beispiele/10_dictionaries/fall_03.py)

```powershell
python ./beispiele/10_dictionaries/fall_03.py
```

## Typische Stolperstellen

Doppelte Schlüssel in einem Dictionary überschreiben den vorherigen Wert. Ändere die Anzahl der Schlüssel nicht während einer Iteration über dasselbe Dictionary. Ein Tippfehler im Schlüssel führt beim Klammerzugriff zu `KeyError`, bei `get()` möglicherweise nur zu einem unerwarteten Standardwert.

## Selbst anwenden

[Übung 10](../90_uebungen/10_dictionaries.md) · [Starterdatei](../90_uebungen/10_dictionaries.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/stdtypes.html#mapping-types-dict)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
