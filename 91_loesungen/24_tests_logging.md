# Lösung 24 · Einen Fehler mit Tests absichern

[Zur Aufgabe](../90_uebungen/24_tests_logging.md) · [Zum Kapitel](../kapitel/24_tests_logging.md)

## Eine mögliche Lösung

```python
import unittest

def divide(total: float, count: int) -> float:
    """Divide by a positive count, raising ValueError otherwise."""
    if count <= 0:
        raise ValueError("count muss positiv sein")
    return total / count

class DivideTests(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            divide(10, -1)

if __name__ == "__main__":
    unittest.main()
```

## Warum funktioniert das?

Die Tests prüfen den Vertrag an seinen wichtigen Grenzen. Die Fachfunktion enthält weder Testcode noch Ausgabe. unittest.main() steht im geschützten Startblock.

## Prüfen

```powershell
python ./werkzeuge/uebung_pruefen.py 24 --loesung
```

Dieser Befehl prüft die Musterlösung. Ohne `--loesung` prüfst du deine eigene Starterdatei. Vergleiche erst nach deinem eigenen Versuch. Die Tests sind dieselben; ihre Erwartungen werden nicht aus der Lösung abgeleitet.
