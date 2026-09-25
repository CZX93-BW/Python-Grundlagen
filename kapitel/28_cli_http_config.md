# 28 · Kommandozeile, Konfiguration und HTTP

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](27_sqlite.md) · [Nächstes Kapitel](29_async_laufzeit.md)

**Stufe:** Vertiefung  
**Suchbegriffe:** argparse CLI os environ getenv HTTP API urllib JSON timeout HTTPError URLError

## Wozu brauche ich das?

Programme werden oft über Argumente oder Umgebungsvariablen gesteuert. Bei einer API-Anfrage kommen weitere Fehlerquellen hinzu: Zeitüberschreitungen, HTTP-Fehler, ungültiges JSON und unerwartete Datenformen. Trenne diese Grenzen von deiner eigentlichen Fachlogik.

## Erst verstehen

**CLI** steht für Command Line Interface. Ein **Timeout** begrenzt Wartezeiten einer Operation. **HTTP** ist ein Protokoll für Anfragen und Antworten im Web. Die HTTP-Demo verwendet absichtlich eine simulierte Antwort und benötigt kein Netzwerk.

## Fall 1: Argumente mit argparse lesen

Dein Skript soll einen Namen und eine optionale Anzahl akzeptieren.

```python
import argparse

parser = argparse.ArgumentParser(description="Eine Begrüßung ausgeben")
parser.add_argument("name")
parser.add_argument("--count", type=int, default=1)
args = parser.parse_args(["Basti", "--count", "2"])
for _ in range(args.count):
    print(f"Hallo {args.name}")
```

**Erwartete Ausgabe:**

```text
Hallo Basti
Hallo Basti
```

**Schritt für Schritt:**

1. `name` ist ein positionales Pflichtargument; `--count` ist eine Option.
2. `type=int` übernimmt Umwandlung und Fehlermeldung für keine ganze Zahl. Eine positive Zahl musst du zusätzlich prüfen.
3. Im echten Programm verwendest du `parse_args()` ohne übergebene Liste; dann liest argparse die Terminalargumente. `--help` ist automatisch vorhanden.

[Beispieldatei öffnen](../beispiele/28_cli_http_config/fall_01.py)

```powershell
python ./beispiele/28_cli_http_config/fall_01.py
```

## Fall 2: Konfiguration ausdrücklich umwandeln

Ein Debug-Schalter soll auch den Text "false" richtig behandeln.

```python
import os
from unittest.mock import patch

with patch.dict(os.environ, {"APP_DEBUG": "false", "APP_PORT": "8000"}):
    debug = os.getenv("APP_DEBUG", "false").strip().casefold() == "true"
    port = int(os.getenv("APP_PORT", "8000"))
    print(debug, port)
```

**Erwartete Ausgabe:**

```text
False 8000
```

**Schritt für Schritt:**

1. Umgebungsvariablen sind Strings. `bool("false")` wäre daher die falsche Umwandlung.
2. `int()` wandelt den Port um; danach müsste für eine echte Anwendung der erlaubte Bereich geprüft werden.
3. `patch.dict()` setzt hier nur vorübergehende Beispielwerte. Im echten Programm liest du die bereits gesetzte Umgebung.

**Achte darauf:** Eine `.env`-Datei wird durch Python nicht automatisch geladen. Ohne zusätzliches Werkzeug setzt du Werte beispielsweise in PowerShell mit `$env:APP_PORT = "8000"`.

[Beispieldatei öffnen](../beispiele/28_cli_http_config/fall_02.py)

```powershell
python ./beispiele/28_cli_http_config/fall_02.py
```

## Fall 3: Eine JSON-Antwort mit prüfbarer Grenze laden

Der Netzwerkzugriff soll austauschbar und ohne Internet testbar bleiben.

```python
import json
from urllib.request import urlopen
from io import BytesIO

def fetch_title(url, opener=urlopen):
    with opener(url, timeout=5) as response:
        data = json.load(response)
    if not isinstance(data, dict) or not isinstance(data.get("title"), str):
        raise ValueError("Antwort braucht einen Text in title")
    return data["title"]

def fake_open(url, *, timeout):
    return BytesIO(b'{"title": "Python lernen"}')

print(fetch_title("https://example.invalid/note", opener=fake_open))
```

**Erwartete Ausgabe:**

```text
Python lernen
```

**Schritt für Schritt:**

1. `opener` ist eine übergebene Abhängigkeit. Standardmäßig wäre es die echte Funktion `urlopen`.
2. Der Testersatz liefert lokale Bytes; es findet keine Anfrage statt.
3. JSON wird dekodiert und die erwartete Struktur geprüft. In einer echten Anwendung behandelt die äußere Aufrufstelle passende Netzwerk- und Datenfehler.

**Achte darauf:** `urlopen()` kann unter anderem `HTTPError`, `URLError` und Timeout-Fehler liefern; JSON kann `JSONDecodeError` auslösen. Das Beispiel simuliert nur eine erfolgreiche Antwort und ersetzt keine vollständige HTTP-Client-Implementierung.

[Beispieldatei öffnen](../beispiele/28_cli_http_config/fall_03.py)

```powershell
python ./beispiele/28_cli_http_config/fall_03.py
```

## Typische Stolperstellen

Eine einzelne Timeout-Angabe ist nicht automatisch eine feste Gesamtdauer für alle Phasen und Weiterleitungen. Wiederhole schreibende Anfragen nicht blind, sonst können doppelte Aktionen entstehen. Für produktive Clients plane auch Antwortgrößen, erlaubte Zieladressen und Authentifizierung. Diese Bibliothek führt keine externen API-Aufrufe aus.

## Selbst anwenden

[Übung 28](../90_uebungen/28_cli_http_config.md) · [Starterdatei](../90_uebungen/28_cli_http_config.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/urllib.request.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
