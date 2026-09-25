# 18 · JSON und CSV lesen und schreiben

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](17_dateien_pfade.md) · [Nächstes Kapitel](19_datum_zufall.md)

**Stufe:** Aufbau  
**Suchbegriffe:** json csv load dump loads dumps serialisieren deserialisieren DictReader DictWriter

## Wozu brauche ich das?

JSON eignet sich für strukturierte Daten wie Listen von Datensätzen. CSV eignet sich für Tabellen mit Zeilen und Spalten. Beide Formate sind Text, benötigen aber eigene Regeln; nutze deshalb ihre Parser statt selbst an Trennzeichen zu schneiden.

## Erst verstehen

**Serialisieren** bedeutet: Python-Werte in ein speicherbares Format umwandeln. **Deserialisieren** macht daraus wieder Python-Werte. `dumps()` und `loads()` arbeiten mit Strings; `dump()` und `load()` arbeiten mit geöffneten Dateien.

## Fall 1: Python-Daten und JSON-Text umwandeln

Du bereitest einen Datensatz für Speicherung oder Übertragung vor.

```python
import json

person = {"name": "Jörg", "active": True, "phone": None}
text = json.dumps(person, ensure_ascii=False, sort_keys=True)
print(text)
restored = json.loads(text)
print(restored["name"])
print(restored["phone"] is None)
```

**Erwartete Ausgabe:**

```text
{"active": true, "name": "Jörg", "phone": null}
Jörg
True
```

**Schritt für Schritt:**

1. `dumps()` erzeugt Text. JSON verwendet `true` und `null`; Python verwendet `True` und `None`.
2. `ensure_ascii=False` lässt Umlaute lesbar. Für die Datei gibst du zusätzlich UTF-8 an.
3. `loads()` stellt Werte wieder her. Eine korrekte JSON-Syntax garantiert aber noch nicht die richtige Datenstruktur.

[Beispieldatei öffnen](../beispiele/18_json_csv/fall_01.py)

```powershell
python ./beispiele/18_json_csv/fall_01.py
```

## Fall 2: Eine JSON-Datei speichern und prüfen

Du speicherst Notizen und kontrollierst beim Laden den äußeren Typ.

```python
import json
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "notes.json"
    notes = [{"title": "Einkauf", "text": "Milch"}]
    with path.open("w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)
    with path.open(encoding="utf-8") as file:
        loaded = json.load(file)
    if not isinstance(loaded, list):
        raise ValueError("Eine Liste wird erwartet")
    print(loaded[0]["title"])
```

**Erwartete Ausgabe:**

```text
Einkauf
```

**Schritt für Schritt:**

1. `indent=2` macht die Datei gut lesbar.
2. Der Kontextmanager schließt jede Datei zuverlässig.
3. Der Typcheck ist nur der Anfang: Bei fremden Daten musst du auch jeden Datensatz und dessen Felder prüfen. Das Notizprojekt zeigt diese vollständige Prüfung.

**Achte darauf:** Ungültiger JSON-Text löst `json.JSONDecodeError` aus. Datumswerte und Sets kann der Standardencoder nicht ohne eigene Umwandlung speichern.

[Beispieldatei öffnen](../beispiele/18_json_csv/fall_02.py)

```powershell
python ./beispiele/18_json_csv/fall_02.py
```

## Fall 3: CSV mit Spaltennamen verarbeiten

Ein Feld darf selbst ein Trennzeichen enthalten.

```python
import csv
from io import StringIO

buffer = StringIO(newline="")
writer = csv.DictWriter(buffer, fieldnames=["name", "quantity"], delimiter=";")
writer.writeheader()
writer.writerow({"name": "Tee; grün", "quantity": 2})
buffer.seek(0)
for row in csv.DictReader(buffer, delimiter=";"):
    print(row["name"])
    print(int(row["quantity"]) + 1)
```

**Erwartete Ausgabe:**

```text
Tee; grün
3
```

**Schritt für Schritt:**

1. `StringIO` ist hier eine Textdatei im Speicher. Bei echten Dateien verwende `open(..., newline="", encoding="utf-8")`.
2. Das CSV-Modul behandelt Anführungszeichen und Trennzeichen innerhalb von Feldern.
3. Geladene CSV-Felder sind Strings. Zahlen müssen geprüft und umgewandelt werden.

[Beispieldatei öffnen](../beispiele/18_json_csv/fall_03.py)

```powershell
python ./beispiele/18_json_csv/fall_03.py
```

## Typische Stolperstellen

JSON-Objektschlüssel sind Strings; numerische Dictionary-Schlüssel bleiben beim JSON-Rundlauf nicht zwangsläufig Zahlen. JSON ist kein Python-Code: Verwende niemals `eval()` zum Laden. CSV-Zellinhalte können beim späteren Öffnen in Tabellenprogrammen als Formeln interpretiert werden; berücksichtige das bei Exporten fremder Inhalte.

## Selbst anwenden

[Übung 18](../90_uebungen/18_json_csv.md) · [Starterdatei](../90_uebungen/18_json_csv.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/json.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
