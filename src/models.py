from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A single task: what to do, details and the deadline."""

    id: int
    title: str
    description: str
    due_date: date
