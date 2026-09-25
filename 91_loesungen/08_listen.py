"""Musterlösung 08: Doppelte Einträge entfernen."""

def unique_items(items: list[str]) -> list[str]:
    """Return first occurrences in their original order."""
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
