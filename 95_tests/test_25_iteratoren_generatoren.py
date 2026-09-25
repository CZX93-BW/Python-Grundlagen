"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(list(m.even_numbers(7)), [0, 2, 4, 6])

    def test_empty(self):
        m = MODULE
        self.assertEqual(list(m.even_numbers(0)), [])
        self.assertEqual(list(m.even_numbers(-2)), [])

    def test_lazy(self):
        m = MODULE
        from types import GeneratorType
        values = m.even_numbers(4)
        self.assertIsInstance(values, GeneratorType)
        self.assertEqual(next(values), 0)
        self.assertEqual(list(values), [2])
