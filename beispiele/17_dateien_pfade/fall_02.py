"""Dateien und Pfade mit pathlib: Anhängen und zeilenweise lesen."""

from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "log.txt"
    with path.open("a", encoding="utf-8") as file:
        file.write("Start\n")
        file.write("Fertig\n")
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip("\n"))
