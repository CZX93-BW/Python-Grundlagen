"""Behavior checks shared by the exercise and its reference solution."""
import unittest

MODULE = None

class ExerciseTests(unittest.TestCase):
    def test_function(self):
        m = MODULE
        self.assertEqual(m.greet("Ada"), "Hallo Ada")

    def test_main(self):
        m = MODULE
        import io
        from contextlib import redirect_stdout
        output = io.StringIO()
        with redirect_stdout(output):
            m.main()
        self.assertEqual(output.getvalue(), "Hallo Basti\n")

    def test_import(self):
        m = MODULE
        import runpy
        import io
        from contextlib import redirect_stdout
        output = io.StringIO()
        with redirect_stdout(output):
            runpy.run_path(m.__file__, run_name="exercise_import")
        self.assertEqual(output.getvalue(), "")
