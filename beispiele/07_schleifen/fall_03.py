"""Schleifen und Wiederholungen: Suchen und zusammengehörige Listen verbinden."""

for number in [1, 3, 5]:
    if number % 2 == 0:
        print("Gerade Zahl gefunden")
        break
else:
    print("Keine gerade Zahl gefunden")

for name, score in zip(["Ada", "Basti"], [9, 8], strict=True):
    print(name, score)
