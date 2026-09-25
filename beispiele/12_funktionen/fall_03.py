"""Funktionen und Rückgabewerte: Früh zurückkehren und mehrere Werte liefern."""

def greeting(name):
    if not name.strip():
        return "Name fehlt"
    return f"Hallo {name.strip()}"

def limits(numbers):
    if not numbers:
        return None
    return min(numbers), max(numbers)

print(greeting("  "))
smallest, largest = limits([7, 2, 9])
print(smallest, largest)
print(limits([]))
