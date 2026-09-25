# 24 · Tests, Fehlersuche und Logging

[Start](../README.md) · [Index](../INDEX.md) · [Vorheriges Kapitel](23_typen_dokumentation.md) · [Nächstes Kapitel](25_iteratoren_generatoren.md)

**Stufe:** Aufbau  
**Suchbegriffe:** unittest Test assertRaises mock logging breakpoint pdb Fehlersuche arrange act assert

## Wozu brauche ich das?

Tests sichern beobachtbares Verhalten: Welche Ausgabe oder welcher Fehler soll bei einer bestimmten Eingabe entstehen? Logging hält während des Betriebs Ereignisse fest. Bei der Fehlersuche hilft oft zuerst ein kleines reproduzierbares Beispiel.

## Erst verstehen

Ein **Unit-Test** prüft einen überschaubaren Baustein. **Arrange–Act–Assert** bedeutet vorbereiten, ausführen, prüfen. Eine Regression ist ein bereits behobener Fehler, der wieder auftaucht. Ein passender Test schützt davor.

## Fall 1: Erfolg und Fehler testen

Du prüfst eine Funktion unabhängig von Terminaleingaben.

```python
import unittest
import io

def positive_double(number):
    if number < 0:
        raise ValueError("number darf nicht negativ sein")
    return number * 2

class DoubleTests(unittest.TestCase):
    def test_normal_value(self):
        self.assertEqual(positive_double(3), 6)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            positive_double(-1)

suite = unittest.defaultTestLoader.loadTestsFromTestCase(DoubleTests)
result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
print(result.testsRun, result.wasSuccessful())
```

**Erwartete Ausgabe:**

```text
2 True
```

**Schritt für Schritt:**

1. Testmethoden beginnen mit `test_`.
2. `assertEqual()` vergleicht Ergebnis und Erwartung. `assertRaises()` prüft einen Fehlerfall.
3. Der Hilfscode führt die Tests aus. In einem Projekt verwendest du meist `python -m unittest discover -s tests -v`.

[Beispieldatei öffnen](../beispiele/24_tests_logging/fall_01.py)

```powershell
python ./beispiele/24_tests_logging/fall_01.py
```

## Fall 2: Ereignisse protokollieren

Ein Programm soll wichtige Schritte und Probleme unterschiedlich kennzeichnen.

```python
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)
logger.debug("Detail nur bei DEBUG")
logger.info("Verarbeitung gestartet")
logger.warning("Ein Datensatz wurde übersprungen")
```

**Erwartete Ausgabe:**

```text
INFO: Verarbeitung gestartet
WARNING: Ein Datensatz wurde übersprungen
```

**Schritt für Schritt:**

1. Die zentrale Konfiguration gehört in den Programmstart.
2. `INFO` zeigt INFO und höhere Stufen, aber kein DEBUG.
3. Ein Logger pro Modul macht die Herkunft von Meldungen nachvollziehbar. In einem except-Block kann `logger.exception()` zusätzlich den Traceback protokollieren.

[Beispieldatei öffnen](../beispiele/24_tests_logging/fall_02.py)

```powershell
python ./beispiele/24_tests_logging/fall_02.py
```

## Fall 3: Einen Fehler eingrenzen

Du möchtest zuerst die Annahme über den Eingangswert prüfen.

```python
def price_per_item(total, quantity):
    if quantity <= 0:
        raise ValueError("quantity muss positiv sein")
    return total / quantity

for quantity in [2, 0]:
    try:
        print(price_per_item(10, quantity))
    except ValueError as error:
        print(f"Eingabe quantity={quantity}: {error}")
```

**Erwartete Ausgabe:**

```text
5.0
Eingabe quantity=0: quantity muss positiv sein
```

**Schritt für Schritt:**

1. Das kleinste Beispiel zeigt einen Normalfall und einen Grenzfall.
2. Die Fehlermeldung nennt den betroffenen Parameter.
3. Für eine interaktive Untersuchung kannst du vor einer verdächtigen Zeile `breakpoint()` setzen und Variablen prüfen. Entferne solche Haltepunkte vor der Weitergabe.

[Beispieldatei öffnen](../beispiele/24_tests_logging/fall_03.py)

```powershell
python ./beispiele/24_tests_logging/fall_03.py
```

## Typische Stolperstellen

Teste nicht nur den glücklichen Weg, sondern auch leere Eingaben, Grenzen und Fehlerfälle. Tests sollen Fachverhalten prüfen, nicht jede interne Zeile nachbauen. Logge keine Passwörter oder Tokens. Für wiederverwendbare Module ist `print()` kein Ersatz für kontrollierbares Logging.

## Selbst anwenden

[Übung 24](../90_uebungen/24_tests_logging.md) · [Starterdatei](../90_uebungen/24_tests_logging.py)

Bearbeite zuerst die Aufgabe. Die Lösung findest du getrennt unter `91_loesungen` mit derselben Nummer.

## Weiterführende offizielle Dokumentation

[Python-Dokumentation](https://docs.python.org/3.12/library/unittest.html)

Die Erklärung und Beispiele dieses Kapitels sind eigenständig für dieses Nachschlagewerk formuliert. Der Link dient der Vertiefung; er ist keine Voraussetzung zum Bearbeiten.
