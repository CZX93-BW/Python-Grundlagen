"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_value(self):
        m = MODULE
        self.assertEqual(m.copy_notes([{"title": "A"}]), [{"title": "A"}])

    def test_nested(self):
        m = MODULE
        original = [{"title": "A", "tags": ["x"]}]
        result = m.copy_notes(original)
        result[0]["title"] = "B"
        result[0]["tags"].append("y")
        self.assertEqual(original, [{"title": "A", "tags": ["x"]}])

    def test_empty(self):
        m = MODULE
        original = []
        self.assertIsNot(m.copy_notes(original), original)
