"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_de(self):
        m = MODULE
        self.assertEqual(m.greeting("Basti", "de"), "Hallo Basti")

    def test_en(self):
        m = MODULE
        self.assertEqual(m.greeting("Ada", "en"), "Hello Ada")

    def test_invalid(self):
        m = MODULE
        with self.assertRaises(ValueError):
            m.greeting("Ada", "fr")
