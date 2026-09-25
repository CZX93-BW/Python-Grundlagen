"""Filtern, umwandeln und sortieren: Eine Schleife verkürzen."""

numbers = [1, 2, 3, 4]
result = []
for number in numbers:
    if number % 2 == 0:
        result.append(number ** 2)
print(result)
print([number ** 2 for number in numbers if number % 2 == 0])
