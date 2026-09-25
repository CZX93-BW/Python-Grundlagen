"""CLI tests without subprocesses or network access."""

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from starter_app.cli import main


class CliTests(unittest.TestCase):
    def test_success_output(self):
        output = io.StringIO()
        with redirect_stdout(output):
            status = main(["Basti"])
        self.assertEqual(status, 0)
        self.assertEqual(output.getvalue(), "Hallo Basti!\n")

    def test_expected_error_uses_stderr(self):
        error_output = io.StringIO()
        with redirect_stderr(error_output):
            status = main([" "])
        self.assertEqual(status, 2)
        self.assertIn("Name", error_output.getvalue())
