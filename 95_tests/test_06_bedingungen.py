"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_high(self):
        m = MODULE
        self.assertEqual(m.classify_score(90), "sehr gut")
        self.assertEqual(m.classify_score(100), "sehr gut")

    def test_boundary(self):
        m = MODULE
        self.assertEqual(m.classify_score(60), "bestanden")
        self.assertEqual(m.classify_score(59), "weiter üben")
        self.assertEqual(m.classify_score(0), "weiter üben")

    def test_invalid(self):
        m = MODULE
        for value in [-1, 101]:
            with self.assertRaises(ValueError):
                m.classify_score(value)
