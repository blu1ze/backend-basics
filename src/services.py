from datetime import date

from src.exceptions import TaskNotFoundError
from src.logger import logger
from src.models import Task


def create_task(
    tasks_by_id: dict[int, Task],
    title: str,
    description: str,
    due_date: date,
) -> Task:
    """Create a task, store it in the dict by its id and return it."""
    # Next id is the biggest existing id plus one (1 for an empty dict)
    task_id = max(tasks_by_id, default=0) + 1

    task = Task(id=task_id, title=title, description=description, due_date=due_date)
    tasks_by_id[task_id] = task

    logger.info("Created task id=%s", task_id)
    return task


def get_task(tasks_by_id: dict[int, Task], task_id: int) -> Task:
    """Return the task with the given id or raise TaskNotFoundError."""
    if task_id not in tasks_by_id:
        logger.warning("Task not found id=%s", task_id)
        raise TaskNotFoundError(f"Task with id {task_id} not found")

    return tasks_by_id[task_id]
