"""Datum, Zeit und Zufallswerte: Reproduzierbare Zufallswerte."""

import random

first = random.Random(42)
second = random.Random(42)
values = [first.randint(1, 6) for _ in range(3)]
print(values)
print(values == [second.randint(1, 6) for _ in range(3)])
print(first.choice(["Apfel"]))
