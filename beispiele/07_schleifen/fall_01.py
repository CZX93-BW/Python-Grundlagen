"""Schleifen und Wiederholungen: Elemente und Positionen durchgehen."""

fruits = ["Apfel", "Birne", "Kiwi"]
for number, fruit in enumerate(fruits, start=1):
    print(number, fruit)
print(list(range(2, 8, 2)))
