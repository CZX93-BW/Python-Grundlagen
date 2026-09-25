"""Musterlösung 17: Nicht leere Zeilen lesen."""

from pathlib import Path

def read_nonempty_lines(path: Path) -> list[str]:
    """Return stripped non-empty UTF-8 lines; propagate file errors."""
    result = []
    with path.open(encoding="utf-8") as file:
        for line in file:
            clean = line.strip()
            if clean:
                result.append(clean)
    return result
