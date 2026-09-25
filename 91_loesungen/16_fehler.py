"""Musterlösung 16: Einen Port validieren."""

def parse_port(text: str) -> int:
    """Parse a port in the inclusive range 1..65535."""
    try:
        port = int(text)
    except ValueError as error:
        raise ValueError("Port muss eine ganze Zahl sein") from error
    if not 1 <= port <= 65535:
        raise ValueError("Port muss zwischen 1 und 65535 liegen")
    return port
