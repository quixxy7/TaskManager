import json

from pathlib import Path
from tasks.task import Task

class Storage:
    def __init__(self, filename: str = "tasks.json"):
        PROJECT_ROOT = Path(__file__).resolve().parents[2]
        DATA_DIR = PROJECT_ROOT/"data"

        self.data_dir = DATA_DIR
        self.data_dir.mkdir(exist_ok=True)
        self.filename = self.data_dir/filename

    def save_to_json(self, tasks: dict[int, Task], last_task_id: int) -> None:
        data_task = [
            {
                "id": task_id,
                "name": task.name,
                "description": task.description,
                "status": task.status
            }
        for task_id, task in tasks.items()]

        data = {
            "last_task_id": last_task_id,
            "tasks": data_task}

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=2)

    def load_from_json(self) -> tuple[int, dict[int, Task]]:
        if not self.filename.exists():
            return 1, {}

        with open(self.filename) as file:
            data = json.load(file)

        last_task_id: int = data.get("last_task_id") # if isinstance("last_task_id", int) else 1
        tasks: dict[int, Task] = {
            task["id"]: Task(task["name"], task["description"], task["status"])
            for task in data.get("tasks")
        }

        return last_task_id, tasks
