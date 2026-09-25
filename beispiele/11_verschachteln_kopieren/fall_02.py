"""Verschachtelte Daten und Kopien: Zuweisung und flache Kopie unterscheiden."""

original = [{"title": "Alt"}]
alias = original
shallow = original.copy()
alias.append({"title": "Neu"})
shallow[0]["title"] = "Geändert"
print(len(original), len(shallow))
print(original[0]["title"])
print(alias is original)
