"""Übung 24: Einen Fehler mit Tests absichern. Siehe gleichnamige Markdown-Datei."""

import unittest

def divide(total: float, count: int) -> float:
    raise NotImplementedError("Hier selbst lösen")

class DivideTests(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
