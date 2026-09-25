"""Pure application logic without terminal input or output."""


def make_greeting(name: str) -> str:
    """Return a greeting using a stripped name.

    Raises:
        ValueError: If the name contains no non-whitespace characters.
    """
    clean_name = name.strip()
    if not clean_name:
        raise ValueError("Der Name darf nicht leer sein.")
    return f"Hallo {clean_name}!"
