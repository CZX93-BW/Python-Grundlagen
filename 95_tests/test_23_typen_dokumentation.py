"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_match(self):
        m = MODULE
        self.assertEqual(m.find_name(["Ada", "ADA"], "ada"), "Ada")

    def test_absent(self):
        m = MODULE
        self.assertIsNone(m.find_name([], "Ada"))
        self.assertIsNone(m.find_name(["Adaline"], "Ada"))

    def test_docs(self):
        m = MODULE
        self.assertTrue(m.find_name.__doc__)
        self.assertIn("return", m.find_name.__annotations__)
