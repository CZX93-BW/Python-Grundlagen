"""Filtern, umwandeln und sortieren: Neue Dictionaries und schnelle Prüfungen."""

numbers = [1, 2, 3]
squares = {number: number ** 2 for number in numbers}
print(squares)
print(sum(numbers))
print(any(number > 2 for number in numbers))
print(all(number > 0 for number in numbers))
print(any([]), all([]))
print(max([], default=0))
