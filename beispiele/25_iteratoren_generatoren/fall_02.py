"""Iteratoren und Generatoren: Werte mit yield erzeugen."""

def countdown(start):
    while start > 0:
        yield start
        start -= 1

values = countdown(3)
print(next(values))
print(list(values))
print(list(values))
