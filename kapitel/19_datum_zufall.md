# 19 · Datum, Zeit und Zufallswerte

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](18_json_csv.md) · [Nächstes Kapitel](20_standardhelfer.md)

**Stufe:** Aufbau  
**Suchbegriffe:** datetime date timedelta timezone UTC random secrets seed Zeit Datum

## Wozu brauche ich das?

Datumswerte solltest du als Datumsobjekte verarbeiten, nicht durch manuelles Aufteilen von Text. Bei Zeitpunkten ist zusätzlich wichtig, in welcher Zeitzone sie gelten. Zufallswerte eignen sich beispielsweise für Spiele oder Testdaten.

## Erst verstehen

`date` enthält ein Datum, `datetime` einen Zeitpunkt mit Uhrzeit und optionaler Zeitzoneninformation. `timedelta` beschreibt eine Zeitspanne. Für Kalenderdaten und Zeitmessung gibt es unterschiedliche Werkzeuge: Eine Laufzeit misst du mit `time.perf_counter()`.

## Fall 1: Datum lesen und Tage addieren

Du berechnest eine Frist von sieben Tagen.

```python
from datetime import date, timedelta

start = date.fromisoformat("2026-09-25")
end = start + timedelta(days=7)
print(end.isoformat())
print((end - start).days)
print(end.strftime("%d.%m.%Y"))
```

**Erwartete Ausgabe:**

```text
2026-10-02
7
02.10.2026
```

**Schritt für Schritt:**

1. ISO-Daten schreiben Jahr, Monat und Tag in dieser Reihenfolge.
2. Die Datumsrechnung berücksichtigt Monatsgrenzen.
3. `strftime()` erzeugt eine Anzeige, hier Tag.Monat.Jahr. Ungültige Daten wie der 31. Februar verursachen `ValueError`.

[Beispieldatei öffnen](../beispiele/19_datum_zufall/fall_01.py)

```powershell
python ./beispiele/19_datum_zufall/fall_01.py
```

## Fall 2: Zeitzonen ausdrücklich angeben

Du speicherst einen eindeutigen UTC-Zeitpunkt.

```python
from datetime import datetime, timezone, timedelta

moment = datetime(2026, 9, 25, 12, 0, tzinfo=timezone.utc)
print(moment.isoformat())
fixed_offset = timezone(timedelta(hours=2))
print(moment.astimezone(fixed_offset).isoformat())
```

**Erwartete Ausgabe:**

```text
2026-09-25T12:00:00+00:00
2026-09-25T14:00:00+02:00
```

**Schritt für Schritt:**

1. Die UTC-Zeitzone macht den Zeitpunkt eindeutig.
2. `astimezone()` ändert die Darstellung, nicht den bezeichneten Moment.
3. Der feste Offset +02:00 ist nur eine Rechenzone. Für Europe/Berlin samt Sommerzeit nutze `zoneinfo.ZoneInfo`; dafür müssen IANA-Zeitzonendaten verfügbar sein.

**Achte darauf:** `datetime.now(timezone.utc)` liefert die aktuelle UTC-Zeit. Naive und zeitzonenbehaftete Datumswerte solltest du nicht unbedacht mischen.

[Beispieldatei öffnen](../beispiele/19_datum_zufall/fall_02.py)

```powershell
python ./beispiele/19_datum_zufall/fall_02.py
```

## Fall 3: Reproduzierbare Zufallswerte

Du möchtest dieselben Testdaten erneut erzeugen.

```python
import random

first = random.Random(42)
second = random.Random(42)
values = [first.randint(1, 6) for _ in range(3)]
print(values)
print(values == [second.randint(1, 6) for _ in range(3)])
print(first.choice(["Apfel"]))
```

**Erwartete Ausgabe:**

```text
[6, 1, 1]
True
Apfel
```

**Schritt für Schritt:**

1. Eine eigene Random-Instanz vermeidet Änderungen am globalen Zufallszustand.
2. Ein gleicher Seed ermöglicht in derselben Umgebung reproduzierbare Abläufe.
3. `randint(1, 6)` schließt beide Grenzen ein; `choice()` wählt ein Element.

**Achte darauf:** Für Sicherheits-Token verwende `secrets.token_urlsafe()`, nicht `random`. Manche Zufallsalgorithmen und Ausgaben können sich zwischen Python-Versionen ändern.

[Beispieldatei öffnen](../beispiele/19_datum_zufall/fall_03.py)

```powershell
python ./beispiele/19_datum_zufall/fall_03.py
```

## Typische Stolperstellen

Ein Monat ist keine feste Anzahl von Tagen. Die Bedeutung einer fachlichen Frist musst du gesondert klären. `replace(tzinfo=...)` setzt eine Zoneninformation und ist keine Umrechnung eines bestehenden Zeitpunkts. `choice([])` schlägt mit `IndexError` fehl.

## Selbst anwenden

[Übung 19](../90_uebungen/19_datum_zufall.md) · [Starterdatei](../90_uebungen/19_datum_zufall.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/datetime.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
