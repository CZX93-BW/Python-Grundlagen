"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        self.assertEqual(m.divide(10, 2), 5)

    def test_invalid(self):
        m = MODULE
        for count in [0, -1]:
            with self.assertRaises(ValueError):
                m.divide(10, count)

    def test_own_tests(self):
        m = MODULE
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(m.DivideTests)
        self.assertGreaterEqual(suite.countTestCases(), 3)
        result = unittest.TestResult()
        suite.run(result)
        self.assertTrue(result.wasSuccessful(), str(result.errors + result.failures))
