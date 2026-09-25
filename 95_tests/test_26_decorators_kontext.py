"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_result(self):
        m = MODULE
        @m.uppercase_result
        def greet(name):
            return f"Hallo {name}"
        self.assertEqual(greet("Ada"), "HALLO ADA")

    def test_keyword(self):
        m = MODULE
        @m.uppercase_result
        def greet(*, name):
            return name
        self.assertEqual(greet(name="Basti"), "BASTI")

    def test_metadata(self):
        m = MODULE
        @m.uppercase_result
        def original():
            return "x"
        self.assertEqual(original.__name__, "original")
