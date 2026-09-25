"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(m.average([2, 4, 6]), 4.0)

    def test_empty(self):
        m = MODULE
        self.assertIsNone(m.average([]))

    def test_mixed(self):
        m = MODULE
        self.assertAlmostEqual(m.average([-1, 2]), 0.5)
