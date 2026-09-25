"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(m.normalize_search("  Python  "), "python")

    def test_unicode(self):
        m = MODULE
        self.assertEqual(m.normalize_search("STRASSE"), m.normalize_search("Straße"))

    def test_empty(self):
        m = MODULE
        self.assertEqual(m.normalize_search("   "), "")
        self.assertEqual(m.normalize_search(" A  B "), "a  b")
