"""Listen erstellen, ändern und durchsuchen: Anlegen, ergänzen und ändern."""

items = ["Brot", "Milch"]
items.append("Eier")
items.extend(["Apfel", "Tee"])
items.insert(1, "Kaffee")
items[0] = "Vollkornbrot"
print(items)
print(items[:2])
