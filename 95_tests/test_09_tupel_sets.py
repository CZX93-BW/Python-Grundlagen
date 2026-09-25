"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(m.common_skills(["SQL", "Python", "SQL"], ["Python", "SQL"]), ["Python", "SQL"])

    def test_empty(self):
        m = MODULE
        self.assertEqual(m.common_skills([], ["SQL"]), [])

    def test_case(self):
        m = MODULE
        self.assertEqual(m.common_skills(["python"], ["Python"]), [])
