"""Listen erstellen, ändern und durchsuchen: Suchen und sortieren."""

numbers = [5, 2, 5, 1]
print(2 in numbers)
print(numbers.index(5))
print(sorted(numbers))
print(numbers)
result = numbers.sort(reverse=True)
print(numbers)
print(result)
