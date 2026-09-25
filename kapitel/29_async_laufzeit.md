# 29 · Asynchroner Code und Laufzeit verstehen

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](28_cli_http_config.md) · [Nächstes Kapitel](30_notizen_crud.md)

**Stufe:** Vertiefung  
**Suchbegriffe:** async await asyncio gather TaskGroup threading GIL performance perf_counter

## Wozu brauche ich das?

Dieses Kapitel ist für später gedacht. Asynchroner Code ist nützlich, wenn ein Programm auf mehrere passende Ein-/Ausgabeoperationen wartet. Er macht eine rechenintensive Schleife nicht automatisch schneller.

## Erst verstehen

`async def` definiert eine Coroutine-Funktion. Ihr Aufruf allein führt den Körper noch nicht vollständig aus. `await` wartet kooperativ auf eine passende Operation. Eine **Ereignisschleife** verwaltet, welcher wartende Ablauf weiterlaufen kann.

## Fall 1: Eine Coroutine ausführen

Du möchtest den kleinsten vollständigen async-Ablauf sehen.

```python
import asyncio

async def greet():
    await asyncio.sleep(0)
    return "Hallo aus async"

print(asyncio.run(greet()))
```

**Erwartete Ausgabe:**

```text
Hallo aus async
```

**Schritt für Schritt:**

1. `greet()` erzeugt eine Coroutine.
2. `asyncio.run()` startet hier die Ereignisschleife und wartet auf das Ergebnis.
3. `sleep(0)` gibt anderen geplanten Aufgaben Gelegenheit weiterzulaufen. In einem schon laufenden Event-Loop, etwa manchen Notebooks, verwendest du stattdessen direkt `await`.

[Beispieldatei öffnen](../beispiele/29_async_laufzeit/fall_01.py)

```powershell
python ./beispiele/29_async_laufzeit/fall_01.py
```

## Fall 2: Mehrere wartende Abläufe starten

Zwei unabhängige Aufgaben sollen gemeinsam geplant werden.

```python
import asyncio

async def load(label):
    await asyncio.sleep(0.01)
    return label.upper()

async def main():
    results = await asyncio.gather(load("eins"), load("zwei"))
    print(results)

asyncio.run(main())
```

**Erwartete Ausgabe:**

```text
['EINS', 'ZWEI']
```

**Schritt für Schritt:**

1. `gather()` plant die beiden Coroutines gemeinsam.
2. Während eine wartet, kann die andere arbeiten. Die Ergebnisliste folgt der Reihenfolge der übergebenen Aufgaben.
3. Das Beispiel simuliert Ein-/Ausgabe. Synchrones `time.sleep()` würde den Event-Loop blockieren.

**Achte darauf:** Bei einem Fehler mit dem Standardverhalten von gather werden andere Aufgaben nicht automatisch sofort abgebrochen. Für zusammengehörige Aufgaben mit strukturiertem Fehlerverhalten ist `TaskGroup` ab Python 3.11 eine Alternative.

[Beispieldatei öffnen](../beispiele/29_async_laufzeit/fall_02.py)

```powershell
python ./beispiele/29_async_laufzeit/fall_02.py
```

## Fall 3: Messen, bevor du optimierst

Du möchtest prüfen, dass eine Messung die richtige Operation umschließt.

```python
from time import perf_counter

start = perf_counter()
result = sum(range(100_000))
elapsed = perf_counter() - start
print(result)
print(elapsed >= 0)
```

**Erwartete Ausgabe:**

```text
4999950000
True
```

**Schritt für Schritt:**

1. `perf_counter()` ist für Laufzeitmessung geeignet.
2. Du bildest die Differenz vor und nach dem relevanten Code.
3. Die tatsächliche Dauer hängt von Umgebung und Last ab. Deshalb zeigt die feste Beispielausgabe nur das Ergebnis und eine Plausibilitätsprüfung.

[Beispieldatei öffnen](../beispiele/29_async_laufzeit/fall_03.py)

```powershell
python ./beispiele/29_async_laufzeit/fall_03.py
```

## Typische Stolperstellen

Async ist kein Ersatz für Prozesse bei aufwendigen CPU-Aufgaben. `asyncio.to_thread()` kann blockierende Ein-/Ausgabe auslagern, benötigt aber ebenfalls eine sinnvolle Abbruch- und Ressourcenstrategie. Optimiere zuerst auffällige Stellen anhand von Messungen, nicht anhand vermuteter Kleinstvorteile.

## Selbst anwenden

[Übung 29](../90_uebungen/29_async_laufzeit.md) · [Starterdatei](../90_uebungen/29_async_laufzeit.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/asyncio-task.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
