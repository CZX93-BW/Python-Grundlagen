"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        import asyncio
        self.assertEqual(asyncio.run(m.async_double(3)), 6)

    def test_zero(self):
        m = MODULE
        import asyncio
        self.assertEqual(asyncio.run(m.async_double(0)), 0)

    def test_negative(self):
        m = MODULE
        import asyncio
        self.assertEqual(asyncio.run(m.async_double(-2)), -4)
