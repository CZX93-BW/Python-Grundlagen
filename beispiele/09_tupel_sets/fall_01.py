"""Tupel, Sets und die passende Sammlung: Zusammengehörige Werte entpacken."""

point = (10, 20)
x, y = point
single = (10,)
print(x, y)
print(single)
first, *middle, last = [1, 2, 3, 4]
print(first, middle, last)
