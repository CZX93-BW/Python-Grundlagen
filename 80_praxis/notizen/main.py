"""Run a small interactive notebook. Start with python main.py."""
import argparse
from pathlib import Path
from service import add_note, delete_note, update_note
from storage import load_notes, save_notes

def show_notes(notes):
    """Print records without changing them."""
    if not notes:
        print("Noch keine Notizen vorhanden.")
    for note in notes:
        print(f"[{note['id']}] {note['title']}: {note['text']}")

def apply_action(command, notes):
    """Ask for action-specific input and modify a candidate list."""
    if command == "2":
        add_note(notes, input("Titel: "), input("Text: "))
    elif command == "3":
        note_id = input("Vollständige ID: ").strip()
        update_note(notes, note_id, input("Neuer Titel: "), input("Neuer Text: "))
    elif command == "4":
        delete_note(notes, input("Vollständige ID: ").strip())

def run_menu(path, notes):
    """Keep accepted state unchanged until a candidate has been saved."""
    while True:
        command = input("\n1 Anzeigen | 2 Hinzufügen | 3 Ändern | 4 Löschen | q Ende: ").strip().casefold()
        if command == "q":
            return 0
        if command == "1":
            show_notes(notes)
            continue
        if command not in {"2", "3", "4"}:
            print("Unbekannter Befehl.")
            continue
        candidate = [note.copy() for note in notes]
        try:
            apply_action(command, candidate)
            save_notes(path, candidate)
        except (ValueError, KeyError, OSError) as error:
            print(f"Nicht gespeichert: {error}")
        else:
            notes = candidate
            print("Gespeichert.")

def main():
    parser = argparse.ArgumentParser(description="Persönliche Notizen im Terminal")
    parser.add_argument("--file", type=Path, default=Path(__file__).resolve().parent / "data" / "notes.json")
    args = parser.parse_args()
    try:
        notes = load_notes(args.file)
    except (OSError, ValueError) as error:
        print(f"Notizen konnten nicht geladen werden: {error}")
        print("Die vorhandene Datei wird nicht überschrieben. Inhalt prüfen oder einen anderen Pfad wählen.")
        return 1
    try:
        return run_menu(args.file, notes)
    except (EOFError, KeyboardInterrupt):
        print("\nBeendet. Bereits bestätigte Änderungen sind gespeichert.")
        return 0

if __name__ == "__main__":
    raise SystemExit(main())
