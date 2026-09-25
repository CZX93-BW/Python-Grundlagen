"""Run all recorded examples and compare their actual standard output."""
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def main():
    cases = json.loads((ROOT / "95_tests" / "beispiele.json").read_text(encoding="utf-8"))
    failures = []
    for case in cases:
        try:
            result = subprocess.run(
                [sys.executable, "-X", "utf8", str(ROOT / case["path"])],
                input=case["stdin"], capture_output=True, text=True, encoding="utf-8",
                timeout=10, cwd=ROOT,
                env={**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"},
            )
            if result.returncode or result.stderr or result.stdout != case["stdout"]:
                failures.append((case["path"], result.stderr or f"Erwartet: {case['stdout']!r}; erhalten: {result.stdout!r}"))
        except subprocess.TimeoutExpired:
            failures.append((case["path"], "Zeitlimit überschritten"))
    for path, reason in failures:
        print(f"FEHLER {path}: {reason}")
    print(f"{len(cases) - len(failures)}/{len(cases)} Beispiele stimmen mit der dokumentierten Ausgabe überein.")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
