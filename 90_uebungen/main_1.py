notes = [
    {"title": "Einkauf", "text": "Milch, Brot, Eier"},
    {"title": "Arbeit", "text": "Backendcall um 11"},
]


def show_notes():
    for note in notes:
        print(f"Title: {note['title']}, Text: {note['text']}")


def add_note():
    new_note = {"title": "Schule", "text": "Hausaufgaben machen"}
    notes.append(new_note)


def delete_note():
    notes.pop(0)


def update_note():
    notes[0]["title"] = "Geändert"
    notes[0]["text"] = "Notiz wurde geändert"


add_note()
delete_note()
update_note()
show_notes()