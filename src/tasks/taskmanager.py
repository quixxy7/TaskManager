from tasks.task import Task
from tasks.storage import Storage

class TaskManager:
    def __init__(self):
        self.task_id: int = 1
        self.tasks: dict[int, Task] = {}

    def add_task(self, task: Task) -> None:
        self.tasks[self.task_id] = task
        self.task_id += 1

    def remove_task(self, task_id: int) -> None:
        self.tasks.pop(task_id)

    def update_task(self, task_id: int) -> None:
        pass

    def print_tasks(self) -> None:
        if not self.tasks:
            print("No tasks")
            return

        for task_id, task in self.tasks.items():
            print(f"{task_id}. {task}")

    def save_tasks(self):
        json_file = Storage()
        json_file.save_to_json(self.tasks, self.task_id)
        print("Tasks saved")

    def load_tasks(self):
        json_file = Storage()
        self.task_id, self.tasks = json_file.load_from_json()
        print("Tasks loaded")
