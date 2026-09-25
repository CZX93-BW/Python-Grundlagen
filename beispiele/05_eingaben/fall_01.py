"""Eingaben lesen und prüfen: Eine einfache Texteingabe."""

name = input("Name: ").strip()
if name:
    print(f"Hallo {name}!")
else:
    print("Bitte einen Namen eingeben.")
