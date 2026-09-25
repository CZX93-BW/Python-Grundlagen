"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(m.adult_names([{"name": "basti", "age": 32}, {"name": "Ada", "age": 18}, {"name": "Mira", "age": 17}]), ["Ada", "basti"])

    def test_empty(self):
        m = MODULE
        self.assertEqual(m.adult_names([]), [])

    def test_duplicates(self):
        m = MODULE
        self.assertEqual(m.adult_names([{"name": "Ada", "age": 20}, {"name": "Ada", "age": 22}]), ["Ada", "Ada"])
