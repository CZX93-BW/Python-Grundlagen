"""Filtern, umwandeln und sortieren: Nach einem Feld sortieren."""

people = [
    {"name": "Basti", "age": 32},
    {"name": "Ada", "age": 32},
    {"name": "Mira", "age": 25},
]
ordered = sorted(people, key=lambda person: (person["age"], person["name"]))
print([person["name"] for person in ordered])
print(sorted(["Banane", "apfel"], key=str.casefold))
