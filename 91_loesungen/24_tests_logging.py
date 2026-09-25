"""Musterlösung 24: Einen Fehler mit Tests absichern."""

import unittest

def divide(total: float, count: int) -> float:
    """Divide by a positive count, raising ValueError otherwise."""
    if count <= 0:
        raise ValueError("count muss positiv sein")
    return total / count

class DivideTests(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            divide(10, -1)

if __name__ == "__main__":
    unittest.main()
