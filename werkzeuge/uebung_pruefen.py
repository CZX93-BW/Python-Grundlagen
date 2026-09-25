"""Run one exercise's behavior tests against a starter or reference solution."""
import argparse
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Modul nicht ladbar: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

def make_suite(number, solution):
    prefix = f"{number:02d}_"
    folder = ROOT / ("91_loesungen" if solution else "90_uebungen")
    matches = sorted(folder.glob(prefix + "*.py"))
    if len(matches) != 1:
        raise ValueError(f"Keine eindeutige Übung für Nummer {number}")
    exercise = load_module(matches[0], f"exercise_{number}")
    tests = load_module(ROOT / "95_tests" / ("test_" + matches[0].name), f"exercise_tests_{number}")
    tests.MODULE = exercise
    return unittest.defaultTestLoader.loadTestsFromModule(tests)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("number", type=int, nargs="?", help="Übungsnummer 1 bis 30")
    parser.add_argument("--loesung", action="store_true", help="Die Musterlösung prüfen")
    parser.add_argument("--alle", action="store_true", help="Alle Übungen prüfen")
    args = parser.parse_args()
    if args.alle and args.number is not None:
        parser.error("Entweder eine Nummer oder --alle verwenden")
    if not args.alle and (args.number is None or not 1 <= args.number <= 30):
        parser.error("Eine Nummer von 1 bis 30 oder --alle angeben")
    numbers = range(1, 31) if args.alle else [args.number]
    suite = unittest.TestSuite(make_suite(number, args.loesung) for number in numbers)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    raise SystemExit(main())
