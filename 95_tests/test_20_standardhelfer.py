"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_valid(self):
        m = MODULE
        self.assertIs(m.is_article_code("AB-123"), True)

    def test_invalid(self):
        m = MODULE
        for text in ["ab-123", "A-123", "AB-12", " AB-123", "AB-123\n", "AB-１２３"]:
            self.assertIs(m.is_article_code(text), False)

    def test_empty(self):
        m = MODULE
        self.assertIs(m.is_article_code(""), False)
