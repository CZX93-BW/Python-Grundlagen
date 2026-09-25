"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(m.split_minutes(135), (2, 15))

    def test_boundary(self):
        m = MODULE
        self.assertEqual(m.split_minutes(0), (0, 0))
        self.assertEqual(m.split_minutes(60), (1, 0))

    def test_invalid(self):
        m = MODULE
        with self.assertRaises(ValueError):
            m.split_minutes(-1)
