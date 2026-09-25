# 16 · Fehler verstehen und gezielt behandeln

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](15_module.md) · [Nächstes Kapitel](17_dateien_pfade.md)

**Stufe:** Grundlage  
**Suchbegriffe:** try except else finally raise Exception ValueError TypeError traceback Fehler

## Wozu brauche ich das?

Ein Fehler bedeutet nicht automatisch, dass du schlecht programmiert hast. Manche Eingaben sind ungültig, Dateien können fehlen und Netzwerke ausfallen. Gute Fehlerbehandlung unterscheidet erwartbare Probleme von eigenen Programmierfehlern.

## Erst verstehen

Eine **Exception** unterbricht den normalen Ablauf. `try` markiert den überwachten Bereich, `except` behandelt passende Fehlertypen. `raise` löst einen Fehler bewusst aus. Im **Traceback** findest du die Aufrufkette; die letzte Zeile nennt meist Typ und Meldung.

## Fall 1: Genau den erwarteten Fehler fangen

Du wandelst mehrere mögliche Eingaben um.

```python
for raw_value in ["12", "abc"]:
    try:
        number = int(raw_value)
    except ValueError as error:
        print(f"Ungültige Zahl: {raw_value}")
    else:
        print(number * 2)
    finally:
        print("Versuch abgeschlossen")
```

**Erwartete Ausgabe:**

```text
24
Versuch abgeschlossen
Ungültige Zahl: abc
Versuch abgeschlossen
```

**Schritt für Schritt:**

1. Der kleine try-Block enthält nur den riskanten Schritt.
2. `else` läuft bei Erfolg. `finally` wird beim Verlassen des try-Ablaufs normalerweise unabhängig vom Ergebnis ausgeführt.
3. Der Fehler kann mit `as error` benannt werden, wenn Details gebraucht werden.

[Beispieldatei öffnen](../beispiele/16_fehler/fall_01.py)

```powershell
python ./beispiele/16_fehler/fall_01.py
```

## Fall 2: Fachlich ungültige Werte ablehnen

Eine Division soll den Nullfall klar melden.

```python
def divide(total, count):
    if count == 0:
        raise ValueError("count darf nicht 0 sein")
    return total / count

try:
    print(divide(10, 0))
except ValueError as error:
    print(error)
```

**Erwartete Ausgabe:**

```text
count darf nicht 0 sein
```

**Schritt für Schritt:**

1. Die Funktion formuliert ihren Vertrag ausdrücklich.
2. Die aufrufende Stelle entscheidet, wie die Fehlermeldung angezeigt wird.
3. Ein Rückgabewert wie -1 wäre hier unklar, weil er auch ein gültiges Rechenergebnis sein könnte.

[Beispieldatei öffnen](../beispiele/16_fehler/fall_02.py)

```powershell
python ./beispiele/16_fehler/fall_02.py
```

## Fall 3: Eigene Fehler mit Ursache

Du möchtest technische Details in einen verständlichen Fachfehler einordnen.

```python
class ConfigurationError(Exception):
    """Signal invalid application configuration."""

def read_port(raw_value):
    try:
        return int(raw_value)
    except ValueError as error:
        raise ConfigurationError("Port muss eine ganze Zahl sein") from error

try:
    read_port("abc")
except ConfigurationError as error:
    print(error)
    print(type(error.__cause__).__name__)
```

**Erwartete Ausgabe:**

```text
Port muss eine ganze Zahl sein
ValueError
```

**Schritt für Schritt:**

1. Der eigene Fehlertyp bezeichnet die Bedeutung für dein Programm.
2. `raise ... from error` behält die ursprüngliche Ursache.
3. Ein Aufrufer kann gezielt Konfigurationsprobleme behandeln. Klassen werden in Kapitel 21 erklärt.

[Beispieldatei öffnen](../beispiele/16_fehler/fall_03.py)

```powershell
python ./beispiele/16_fehler/fall_03.py
```

## Typische Stolperstellen

Ein nacktes `except:` fängt zu viel, sogar normale Abbrüche wie `KeyboardInterrupt`. `except Exception: pass` verschluckt wichtige Informationen. Verwende `assert` nicht zur Prüfung fremder Eingaben: Python kann Assertions im optimierten Modus deaktivieren. Behandle Fehler dort, wo du sinnvoll darauf reagieren kannst.

## Selbst anwenden

[Übung 16](../90_uebungen/16_fehler.md) · [Starterdatei](../90_uebungen/16_fehler.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/tutorial/errors.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
