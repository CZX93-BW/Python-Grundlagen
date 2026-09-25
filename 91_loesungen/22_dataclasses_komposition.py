"""Musterlösung 22: Eine Task-Dataclass."""

from dataclasses import dataclass, field

@dataclass
class Task:
    """Represent a task with independently owned default tags."""
    title: str
    done: bool = False
    tags: list[str] = field(default_factory=list)
