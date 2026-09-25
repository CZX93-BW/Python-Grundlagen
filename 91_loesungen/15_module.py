"""Musterlösung 15: Ein importierbares Modul."""

def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hallo {name}"

def main() -> None:
    """Run the terminal demo."""
    print(greet("Basti"))

if __name__ == "__main__":
    main()
