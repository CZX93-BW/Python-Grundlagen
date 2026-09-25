"""Musterlösung 14: Personen filtern und sortieren."""

def adult_names(people: list[dict]) -> list[str]:
    """Return adult names sorted without case-sensitive ordering."""
    names = [person["name"] for person in people if person["age"] >= 18]
    return sorted(names, key=str.casefold)
