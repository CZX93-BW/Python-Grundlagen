"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(m.count_words("Python python SQL"), {"python": 2, "sql": 1})

    def test_whitespace(self):
        m = MODULE
        self.assertEqual(m.count_words(" \n \t"), {})

    def test_punctuation(self):
        m = MODULE
        self.assertEqual(m.count_words("Hi hi!"), {"hi": 1, "hi!": 1})
