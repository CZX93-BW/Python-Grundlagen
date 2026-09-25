"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_boundary(self):
        m = MODULE
        self.assertEqual(m.parse_port("1"), 1)
        self.assertEqual(m.parse_port("65535"), 65535)

    def test_range(self):
        m = MODULE
        for value in ["0", "-1", "65536"]:
            with self.assertRaises(ValueError):
                m.parse_port(value)

    def test_text(self):
        m = MODULE
        with self.assertRaises(ValueError):
            m.parse_port("abc")
