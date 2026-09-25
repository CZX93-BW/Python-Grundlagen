"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_default(self):
        m = MODULE
        task = m.Task("Python")
        self.assertEqual(task.title, "Python")
        self.assertFalse(task.done)
        self.assertEqual(task.tags, [])

    def test_independent(self):
        m = MODULE
        first = m.Task("A")
        second = m.Task("B")
        first.tags.append("x")
        self.assertEqual(second.tags, [])

    def test_values(self):
        m = MODULE
        self.assertEqual(m.Task("A", True, ["x"]), m.Task("A", True, ["x"]))
