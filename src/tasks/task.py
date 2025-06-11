from enum import Enum
from datetime import date

class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

    def __str__(self):
        return self.value


class Task:
    def __init__(
        self,
        name: str,
        description: str,
        status: TaskStatus = TaskStatus.TODO,
        createdAt: date = date.today(),
        updatedAt: date = date.today()
    ):
        self.name = name
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def __str__(self):
        return f'''Name: {self.name}
   Description: {self.description}
   Status: {self.status}
   Created: {self.createdAt}
   Updated: {self.updatedAt}'''
