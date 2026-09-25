"""Decorators und Kontextmanager: Einen Aufruf sichtbar umhüllen."""

from functools import wraps

def announce(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Aufruf beginnt")
        return function(*args, **kwargs)
    return wrapper

@announce
def greet(name):
    return f"Hallo {name}"

print(greet("Ada"))
print(greet.__name__)
