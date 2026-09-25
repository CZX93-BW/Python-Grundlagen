"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(m.parse_positive(" 7 "), 7)

    def test_text(self):
        m = MODULE
        for value in ["abc", "2.5", ""]:
            with self.assertRaises(ValueError):
                m.parse_positive(value)

    def test_range(self):
        m = MODULE
        for value in ["0", "-2"]:
            with self.assertRaises(ValueError):
                m.parse_positive(value)
