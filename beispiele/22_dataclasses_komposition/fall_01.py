"""Dataclasses, Komposition und Vererbung: Eine Datenklasse mit eigener Liste."""

from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    tags: list[str] = field(default_factory=list)

first = Task("Python")
second = Task("SQL")
first.tags.append("Lernen")
print(first)
print(second.tags)
