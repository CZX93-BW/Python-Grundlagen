"""Tests, Fehlersuche und Logging: Erfolg und Fehler testen."""

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
