"""Decorators und Kontextmanager: Aufräumen mit einem Kontextmanager."""

from contextlib import contextmanager

@contextmanager
def operation():
    print("Start")
    try:
        yield "Arbeitsbereich"
    finally:
        print("Abschluss")

with operation() as name:
    print(name)
