"""Verschachtelte Daten und Kopien: Unabhängige verschachtelte Daten erzeugen."""

from copy import deepcopy

original = [{"title": "Alt"}]
independent = deepcopy(original)
independent[0]["title"] = "Neu"
print(original)
print(independent)
rows = [[0] * 2 for _ in range(2)]
rows[0][0] = 1
print(rows)
