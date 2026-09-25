"""Dictionaries und Schlüssel-Wert-Paare: Durch Schlüssel und Werte gehen."""

person = {"name": "Ada", "active": True}
for key, value in person.items():
    print(f"{key}: {value}")
print("name" in person)
print(list(person.keys()))
print(list(person.values()))
