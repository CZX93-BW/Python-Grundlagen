"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(m.unique_items(["b", "a", "b", "c"]), ["b", "a", "c"])

    def test_empty(self):
        m = MODULE
        self.assertEqual(m.unique_items([]), [])

    def test_unchanged(self):
        m = MODULE
        values = ["a", "a"]
        result = m.unique_items(values)
        self.assertEqual(values, ["a", "a"])
        self.assertIsNot(result, values)
