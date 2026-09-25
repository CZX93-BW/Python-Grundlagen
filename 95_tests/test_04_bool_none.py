"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_missing(self):
        m = MODULE
        self.assertEqual(m.use_default(None, 10), 10)

    def test_falsy(self):
        m = MODULE
        self.assertEqual(m.use_default(0, 10), 0)
        self.assertIs(m.use_default(False, True), False)
        self.assertEqual(m.use_default("", "x"), "")

    def test_identity(self):
        m = MODULE
        items = []
        self.assertIs(m.use_default(items, [1]), items)
