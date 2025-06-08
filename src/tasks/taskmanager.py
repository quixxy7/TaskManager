from tasks.task import Task
from tasks.storage import Storage

class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_taks(self, task_name: str) -> None:
        for i, task in enumerate(self.tasks):
            if task.name == task_name:
                self.tasks.pop(i)
                print("Task was removed")
                return
        print("Task wasn't found. Nothing was removed")

    def print_tasks(self) -> None:
        if not self.tasks:
            print("List is empty")
            return

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def save_tasks(self):
        json_file = Storage()
        json_file.save(self.tasks)
        print("Tasks saved")

    def load_tasks(self):
        json_file = Storage()
        self.tasks = json_file.load()
        print("Tasks loaded")
