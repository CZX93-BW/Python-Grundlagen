"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_normal(self):
        m = MODULE
        from pathlib import Path
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as folder:
            path = Path(folder) / "data.txt"
            path.write_text("  Grüße  \n\n  Python\n", encoding="utf-8")
            self.assertEqual(m.read_nonempty_lines(path), ["Grüße", "Python"])

    def test_empty(self):
        m = MODULE
        from pathlib import Path
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as folder:
            path = Path(folder) / "empty.txt"
            path.write_text("", encoding="utf-8")
            self.assertEqual(m.read_nonempty_lines(path), [])

    def test_missing(self):
        m = MODULE
        from pathlib import Path
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as folder:
            with self.assertRaises(FileNotFoundError):
                m.read_nonempty_lines(Path(folder) / "missing.txt")
