# 17 · Dateien und Pfade mit pathlib

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](16_fehler.md) · [Nächstes Kapitel](18_json_csv.md)

**Stufe:** Aufbau  
**Suchbegriffe:** Path pathlib open with lesen schreiben UTF-8 exists mkdir glob Dateipfad FileNotFoundError

## Wozu brauche ich das?

Pfade beschreiben, wo Dateien liegen. `pathlib.Path` hilft dabei, Pfade zusammenzusetzen, ohne selbst Windows-Backslashes oder Linux-Schrägstriche zu mischen. Die Beispiele verwenden temporäre Ordner und verändern keine persönlichen Dateien.

## Erst verstehen

Ein **relativer Pfad** bezieht sich auf das aktuelle Arbeitsverzeichnis, nicht automatisch auf den Ordner der Python-Datei. `Path(__file__).resolve().parent` liefert bei einer normalen Skriptdatei deren Ordner. `with` sorgt bei einer geöffneten Datei dafür, dass sie anschließend geschlossen wird.

## Fall 1: Text schreiben und lesen

Du speicherst eine kleine Textnotiz.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "notiz.txt"
    path.write_text("Grüße aus Python\n", encoding="utf-8")
    content = path.read_text(encoding="utf-8")
    print(content.strip())
    print(path.name, path.suffix)
```

**Erwartete Ausgabe:**

```text
Grüße aus Python
notiz.txt .txt
```

**Schritt für Schritt:**

1. `/` setzt bei Path-Objekten Pfadteile zusammen.
2. `write_text()` schreibt den Text; eine vorhandene Datei wird überschrieben.
3. `encoding="utf-8"` macht die Zeichenkodierung ausdrücklich. Der temporäre Ordner verschwindet am Ende.

[Beispieldatei öffnen](../beispiele/17_dateien_pfade/fall_01.py)

```powershell
python ./beispiele/17_dateien_pfade/fall_01.py
```

## Fall 2: Anhängen und zeilenweise lesen

Du ergänzt ein Protokoll, ohne bestehende Zeilen zu ersetzen.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "log.txt"
    with path.open("a", encoding="utf-8") as file:
        file.write("Start\n")
        file.write("Fertig\n")
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip("\n"))
```

**Erwartete Ausgabe:**

```text
Start
Fertig
```

**Schritt für Schritt:**

1. Modus `a` hängt an, `r` liest, `w` überschreibt und `x` erstellt nur eine neue Datei.
2. `write()` ergänzt keinen automatischen Zeilenumbruch.
3. Zeilenweise Verarbeitung muss nicht die gesamte Datei auf einmal in den Speicher laden.

[Beispieldatei öffnen](../beispiele/17_dateien_pfade/fall_02.py)

```powershell
python ./beispiele/17_dateien_pfade/fall_02.py
```

## Fall 3: Ordner anlegen und fehlende Dateien behandeln

Du brauchst einen Datenordner und möchtest passende Dateien finden.

```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    data = Path(folder) / "data"
    data.mkdir(parents=True, exist_ok=True)
    (data / "a.txt").write_text("A", encoding="utf-8")
    print([path.name for path in sorted(data.glob("*.txt"))])
    try:
        (data / "missing.txt").read_text(encoding="utf-8")
    except FileNotFoundError:
        print("Datei fehlt")
```

**Erwartete Ausgabe:**

```text
['a.txt']
Datei fehlt
```

**Schritt für Schritt:**

1. `parents=True` erlaubt fehlende übergeordnete Ordner. `exist_ok=True` akzeptiert einen schon vorhandenen Ordner.
2. `glob()` sucht passende Namen in diesem Ordner; `rglob()` auch in Unterordnern.
3. Die konkrete Leseoperation behandelt den Fehler. Eine vorherige Existenzprüfung allein schützt nicht vor zwischenzeitlichen Änderungen.

[Beispieldatei öffnen](../beispiele/17_dateien_pfade/fall_03.py)

```powershell
python ./beispiele/17_dateien_pfade/fall_03.py
```

## Typische Stolperstellen

`w` überschreibt vorhandene Inhalte. Für Binärdaten nutze `read_bytes()` oder `rb`, nicht eine beliebige Textkodierung. Bei Nutzer-Dateinamen musst du begrenzen, in welchen Ordnern gelesen oder geschrieben werden darf. `exists()` sagt nichts darüber aus, ob die nächste Operation erlaubt oder erfolgreich ist.

## Selbst anwenden

[Übung 17](../90_uebungen/17_dateien_pfade.md) · [Starterdatei](../90_uebungen/17_dateien_pfade.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/pathlib.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
