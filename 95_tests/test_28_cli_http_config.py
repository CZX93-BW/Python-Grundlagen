"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_true(self):
        m = MODULE
        for text in ["true", "1", " YES "]:
            self.assertIs(m.parse_bool(text), True)

    def test_false(self):
        m = MODULE
        for text in ["false", "0", " NO "]:
            self.assertIs(m.parse_bool(text), False)

    def test_invalid(self):
        m = MODULE
        for text in ["", "vielleicht", "2"]:
            with self.assertRaises(ValueError):
                m.parse_bool(text)
