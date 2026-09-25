"""Dateien und Pfade mit pathlib: Text schreiben und lesen."""

from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "notiz.txt"
    path.write_text("Grüße aus Python\n", encoding="utf-8")
    content = path.read_text(encoding="utf-8")
    print(content.strip())
    print(path.name, path.suffix)
