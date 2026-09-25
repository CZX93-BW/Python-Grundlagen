"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_independent(self):
        m = MODULE
        self.assertEqual(m.add_tag("A"), ["A"])
        self.assertEqual(m.add_tag("B"), ["B"])

    def test_identity(self):
        m = MODULE
        tags = []
        self.assertIs(m.add_tag("A", tags), tags)
        self.assertEqual(tags, ["A"])

    def test_duplicates(self):
        m = MODULE
        self.assertEqual(m.add_tag("A", ["A"]), ["A", "A"])
