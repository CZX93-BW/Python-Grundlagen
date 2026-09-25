"""JSON und CSV lesen und schreiben: Eine JSON-Datei speichern und prüfen."""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "notes.json"
    notes = [{"title": "Einkauf", "text": "Milch"}]
    with path.open("w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)
    with path.open(encoding="utf-8") as file:
        loaded = json.load(file)
    if not isinstance(loaded, list):
        raise ValueError("Eine Liste wird erwartet")
    print(loaded[0]["title"])
