"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_month(self):
        m = MODULE
        self.assertEqual(m.days_between("2026-09-25", "2026-10-02"), 7)

    def test_reverse(self):
        m = MODULE
        self.assertEqual(m.days_between("2026-10-02", "2026-09-25"), -7)
        self.assertEqual(m.days_between("2026-01-01", "2026-01-01"), 0)

    def test_invalid(self):
        m = MODULE
        with self.assertRaises(ValueError):
            m.days_between("2026-02-30", "2026-03-01")
