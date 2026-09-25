"""Dictionaries und Schlüssel-Wert-Paare: Lesen, ergänzen und ändern."""

person = {"name": "Basti", "age": 32}
print(person["name"])
print(person.get("phone", "Nicht hinterlegt"))
person["age"] = 33
person["city"] = "Bottrop"
person.update({"active": True})
print(person)
