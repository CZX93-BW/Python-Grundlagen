"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_initial(self):
        m = MODULE
        self.assertEqual(m.Counter().value, 0)

    def test_actions(self):
        m = MODULE
        counter = m.Counter()
        self.assertEqual(counter.increment(), 1)
        self.assertEqual(counter.increment(), 2)
        self.assertIsNone(counter.reset())
        self.assertEqual(counter.value, 0)

    def test_independent(self):
        m = MODULE
        first = m.Counter()
        second = m.Counter()
        first.increment()
        self.assertEqual(second.value, 0)
