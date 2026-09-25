"""Tupel, Sets und die passende Sammlung: Doppelte Werte und Mengen vergleichen."""

first = {"Python", "HTML", "Python"}
second = {"Python", "SQL"}
print(sorted(first))
print(sorted(first & second))
print(sorted(first | second))
print(sorted(first - second))
