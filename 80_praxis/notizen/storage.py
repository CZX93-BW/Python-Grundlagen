"""Read validated JSON and replace a file only after complete serialization."""
import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from service import Note, validate_notes

def load_notes(path: Path) -> list[Note]:
    """Load notes; only a missing file is interpreted as a fresh notebook."""
    try:
        with path.open(encoding="utf-8") as file:
            value = json.load(file)
    except FileNotFoundError:
        return []
    return validate_notes(value)

def save_notes(path: Path, notes: list[Note]) -> None:
    """Write via a sibling temporary file; preserve the old file on failure."""
    validated = validate_notes(notes)
    payload = json.dumps(validated, ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, suffix=".tmp", delete=False
        ) as file:
            temporary = Path(file.name)
            file.write(payload)
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
