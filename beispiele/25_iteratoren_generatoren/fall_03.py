"""Iteratoren und Generatoren: Einen Generatorausdruck verwenden."""

numbers = [1, 2, 3, 4]
squares = (number ** 2 for number in numbers)
print(sum(squares))
print(list(squares))
