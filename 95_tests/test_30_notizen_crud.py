"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        notes = [{"id": "a", "title": "Alt", "text": "Alt"}, {"id": "b", "title": "B", "text": "B"}]
        self.assertIs(m.update_note(notes, "a", " Neu ", " Inhalt "), notes[0])
        self.assertEqual(notes[0], {"id": "a", "title": "Neu", "text": "Inhalt"})
        self.assertEqual(notes[1]["title"], "B")

    def test_invalid(self):
        m = MODULE
        notes = [{"id": "a", "title": "Alt", "text": "Alt"}]
        with self.assertRaises(ValueError):
            m.update_note(notes, "a", "Neu", " ")
        self.assertEqual(notes, [{"id": "a", "title": "Alt", "text": "Alt"}])

    def test_missing(self):
        m = MODULE
        with self.assertRaises(KeyError):
            m.update_note([], "a", "Neu", "Text")
