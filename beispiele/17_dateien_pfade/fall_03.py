"""Dateien und Pfade mit pathlib: Ordner anlegen und fehlende Dateien behandeln."""

from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    data = Path(folder) / "data"
    data.mkdir(parents=True, exist_ok=True)
    (data / "a.txt").write_text("A", encoding="utf-8")
    print([path.name for path in sorted(data.glob("*.txt"))])
    try:
        (data / "missing.txt").read_text(encoding="utf-8")
    except FileNotFoundError:
        print("Datei fehlt")
