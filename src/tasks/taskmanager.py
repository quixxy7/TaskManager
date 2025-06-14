from tasks.task import Task, TaskStatus
from tasks.storage import Storage
from datetime import date

class TaskManager:
    def __init__(self):
        self.task_id: int = 1
        self.tasks: dict[int, Task] = {}

    def clear(self) -> None:
        self.task_id = 1
        self.tasks = {}

    def add_task(self, task: Task) -> None:
        self.tasks[self.task_id] = task
        self.task_id += 1

    def remove_task(self, task_id: int) -> None:
        self.tasks.pop(task_id)

    def update_task(self, task_id: int) -> None:
        updated = False

        print("| Leave the field blank if you want to leave it unchanged |")
        u_name = input("Enter new name: ")
        u_description = input("Enter new description: ")

        if u_name:
            self.tasks[task_id].name = u_name
            updated = True
        if u_description:
            self.tasks[task_id].description = u_description
            updated =True

        if updated:
            self.tasks[task_id].updatedAt = date.today()

    def mark_task(self, task_id: int) -> None:
        new_status = int(input("Enter new status (1 - todo, 2 - in-progress, 3 - done): "))
        match new_status:
            case 1:
                self.tasks[task_id].status = TaskStatus.TODO
            case 2:
                self.tasks[task_id].status = TaskStatus.IN_PROGRESS
            case 3:
                self.tasks[task_id].status = TaskStatus.DONE
            case _:
                print("Wrong status")


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
