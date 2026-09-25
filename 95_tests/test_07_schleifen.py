"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(m.sum_even([1, 2, 3, 4]), 6)

    def test_negative(self):
        m = MODULE
        self.assertEqual(m.sum_even([-4, -3, 2]), -2)
        self.assertEqual(m.sum_even([]), 0)

    def test_unchanged(self):
        m = MODULE
        values = [2, 1]
        m.sum_even(values)
        self.assertEqual(values, [2, 1])
