"""Musterlösung 21: Ein Zähler als Klasse."""

class Counter:
    """Keep an independent, resettable count per instance."""
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

    def reset(self):
        self.value = 0
