"""Parse CLI arguments and translate expected errors into exit codes."""

import argparse
import sys
from collections.abc import Sequence

from starter_app.service import make_greeting


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI and return zero on success or two for invalid input."""
    parser = argparse.ArgumentParser(description="Ein kleines Python-Projekt")
    parser.add_argument("name", help="Name für die Begrüßung")
    args = parser.parse_args(argv)
    try:
        message = make_greeting(args.name)
    except ValueError as error:
        print(f"Fehler: {error}", file=sys.stderr)
        return 2
    print(message)
    return 0
