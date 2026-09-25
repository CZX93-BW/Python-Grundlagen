"""Musterlösung 13: Tags ohne geteilten Standardwert."""

def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append to the supplied list, or create a fresh list when omitted."""
    if tags is None:
        tags = []
    tags.append(tag)
    return tags
