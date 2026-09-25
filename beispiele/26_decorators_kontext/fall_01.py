"""Decorators und Kontextmanager: Eine Funktion weitergeben."""

def double(number):
    return number * 2

def apply(operation, value):
    return operation(value)

print(apply(double, 4))
