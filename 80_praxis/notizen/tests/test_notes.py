"""Check note behavior and persistence using isolated temporary files."""
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from service import add_note, delete_note, find_note, update_note, validate_notes
from storage import load_notes, save_notes

class NoteTests(unittest.TestCase):
    def test_add_trims_and_assigns_unique_ids(self):
        notes = []
        first = add_note(notes, " A ", " B ")
        second = add_note(notes, "A", "B")
        self.assertEqual(first["title"], "A")
        self.assertNotEqual(first["id"], second["id"])

    def test_invalid_add_leaves_list_empty(self):
        notes = []
        with self.assertRaises(ValueError):
            add_note(notes, " ", "Text")
        self.assertEqual(notes, [])

    def test_update_targets_id(self):
        notes = []
        first = add_note(notes, "A", "A")
        second = add_note(notes, "B", "B")
        update_note(notes, second["id"], "C", "D")
        self.assertEqual(first["title"], "A")
        self.assertEqual(second["title"], "C")

    def test_invalid_update_is_not_partial(self):
        notes = []
        note = add_note(notes, "A", "B")
        with self.assertRaises(ValueError):
            update_note(notes, note["id"], "Neu", " ")
        self.assertEqual(note["title"], "A")

    def test_delete_and_missing_id(self):
        notes = []
        note = add_note(notes, "A", "B")
        self.assertIs(delete_note(notes, note["id"]), note)
        with self.assertRaises(KeyError):
            delete_note(notes, note["id"])
        with self.assertRaises(KeyError):
            find_note(notes, "fehlt")

    def test_invalid_structure_and_duplicate_ids(self):
        valid = {"id": "1", "title": "A", "text": "B"}
        for value in [{}, [1], [{"id": "1"}], [valid, valid], [{**valid, "title": None}], [{**valid, "extra": True}]]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_notes(value)

    def test_validation_returns_independent_records(self):
        data = [{"id": "1", "title": "A", "text": "B"}]
        copied = validate_notes(data)
        copied[0]["title"] = "Neu"
        self.assertEqual(data[0]["title"], "A")

    def test_missing_file_starts_empty(self):
        with TemporaryDirectory() as folder:
            self.assertEqual(load_notes(Path(folder) / "missing.json"), [])

    def test_roundtrip_preserves_unicode(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "nested" / "notes.json"
            data = [{"id": "1", "title": "Grüße", "text": "Üben"}]
            save_notes(path, data)
            self.assertEqual(load_notes(path), data)
            self.assertEqual(list(path.parent.glob("*.tmp")), [])

    def test_corrupt_file_is_not_silently_replaced(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "notes.json"
            path.write_text("kaputt", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_notes(path)
            self.assertEqual(path.read_text(encoding="utf-8"), "kaputt")

    def test_failed_replace_preserves_existing_file(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "notes.json"
            old = [{"id": "1", "title": "Alt", "text": "B"}]
            save_notes(path, old)
            with patch("storage.os.replace", side_effect=OSError("simuliert")):
                with self.assertRaises(OSError):
                    save_notes(path, [{**old[0], "title": "Neu"}])
            self.assertEqual(load_notes(path), old)
            self.assertEqual(list(path.parent.glob("*.tmp")), [])

    def test_invalid_save_preserves_existing_file(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "notes.json"
            path.write_text("[]", encoding="utf-8")
            with self.assertRaises(ValueError):
                save_notes(path, [{"bad": True}])
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), [])

if __name__ == "__main__":
    unittest.main()
