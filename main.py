from datetime import date

from src.exceptions import TaskNotFoundError
from src.models import Task
from src.services import create_task, get_task


def main() -> None:
    # The storage: task id -> Task
    tasks_by_id: dict[int, Task] = {}

    # Happy path: create a task and read it back by id
    task = create_task(
        tasks_by_id,
        title="Submit homework 1",
        description="Open a pull request for review",
        due_date=date(2026, 10, 22),
    )
    print(get_task(tasks_by_id, task.id))

    # Error path: ask for an id that does not exist
    try:
        get_task(tasks_by_id, 999)
    except TaskNotFoundError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
