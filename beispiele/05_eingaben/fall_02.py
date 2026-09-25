"""Eingaben lesen und prüfen: Eine Zahl mit Fehlermeldung."""

raw_age = input("Alter: ")
try:
    age = int(raw_age)
except ValueError:
    print("Bitte eine ganze Zahl eingeben.")
else:
    if age < 0:
        print("Das Alter darf nicht negativ sein.")
    else:
        print(f"Gespeichert: {age}")
