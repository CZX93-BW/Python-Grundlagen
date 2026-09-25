"""Fehler verstehen und gezielt behandeln: Fachlich ungültige Werte ablehnen."""

def divide(total, count):
    if count == 0:
        raise ValueError("count darf nicht 0 sein")
    return total / count

try:
    print(divide(10, 0))
except ValueError as error:
    print(error)
