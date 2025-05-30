import json
from pathlib import Path
from task import Task

class Storage:
    def __init__(self, filename: str = "tasks.json"):
        self.data_dir = Path("../data")
        self.filename = self.data_dir / filename

    def save(self, tasks: list[Task]) -> None:
        data = [{"name": task.name,
                 "description": task.description,
                 "done": task.done}
        for task in tasks]

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self) -> list[Task]:
        if not self.filename.exists():
            return []

        with open(self.filename) as f:
            data = json.load(f)

        return [Task(task["name"], task["description"], task["done"])
                for task in data]
