"""Zählen, gruppieren und Muster erkennen: Eine Warteschlange verwenden."""

from collections import deque

queue = deque(["Auftrag A", "Auftrag B"])
queue.append("Auftrag C")
print(queue.popleft())
print(list(queue))
