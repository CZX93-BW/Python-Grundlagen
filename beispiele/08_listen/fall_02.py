"""Listen erstellen, ändern und durchsuchen: Löschen nach Wert oder Position."""

items = ["Brot", "Milch", "Milch", "Eier"]
items.remove("Milch")
removed = items.pop(0)
print(removed)
print(items)
del items[-1]
print(items)
