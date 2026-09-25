"""Iteratoren und Generatoren: Einen Iterator schrittweise lesen."""

iterator = iter(["A", "B"])
print(next(iterator))
print(next(iterator))
print(next(iterator, "Ende"))
