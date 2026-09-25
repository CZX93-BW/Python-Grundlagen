"""Behavior tests for the public greeting function."""

import unittest

from starter_app.service import make_greeting


class GreetingTests(unittest.TestCase):
    def test_regular_name(self):
        self.assertEqual(make_greeting("Basti"), "Hallo Basti!")

    def test_surrounding_whitespace(self):
        self.assertEqual(make_greeting("  Ada  "), "Hallo Ada!")

    def test_unicode(self):
        self.assertEqual(make_greeting("Jörg"), "Hallo Jörg!")

    def test_empty_name_is_rejected(self):
        for value in ["", "  ", "\n"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                make_greeting(value)
