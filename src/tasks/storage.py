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

    def save(self, tasks: list[Task]) -> None:
        data = [{"name": task.name,
                 "description": task.description,
                 "done": task.done}
        for task in tasks]

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=2)

    def load(self) -> list[Task]:
        if not self.filename.exists():
            return []

        with open(self.filename) as file:
            data = json.load(file)

        return [Task(task["name"], task["description"], task["done"])
                for task in data]
