"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_valid(self):
        m = MODULE
        self.assertEqual(m.parse_notes('[ {"title": "A", "text": "B"} ]'), [{"title": "A", "text": "B"}])
        self.assertEqual(m.parse_notes("[]"), [])

    def test_syntax(self):
        m = MODULE
        with self.assertRaises(ValueError):
            m.parse_notes("kein JSON")

    def test_shape(self):
        m = MODULE
        for text in ['{"title": "A"}', '[1]', '[{"title": 5, "text": "B"}]', '[{"title":"A"}]', '[{"title":"A","text":"B","id":1}]']:
            with self.assertRaises(ValueError):
                m.parse_notes(text)
