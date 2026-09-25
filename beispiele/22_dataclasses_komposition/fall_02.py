"""Dataclasses, Komposition und Vererbung: Verhalten durch Zusammenarbeit austauschen."""

class ConsolePrinter:
    def write(self, message):
        print(message)

class GreetingService:
    def __init__(self, printer):
        self.printer = printer

    def greet(self, name):
        self.printer.write(f"Hallo {name}")

service = GreetingService(ConsolePrinter())
service.greet("Basti")
