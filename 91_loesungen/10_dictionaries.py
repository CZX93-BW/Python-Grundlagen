"""Musterlösung 10: Wörter zählen."""

def count_words(text: str) -> dict[str, int]:
    """Count casefolded whitespace-separated words."""
    counts = {}
    for word in text.casefold().split():
        counts[word] = counts.get(word, 0) + 1
    return counts
