from task import Task
from storage import Storage

class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def print_tasks(self) -> None:
        if not self.tasks:
            print("Empty")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.name} | {task.description}")

    def remove_taks(self, task_name: str) -> None:
        for i, task in enumerate(self.tasks):
            if task.name == task_name:
                self.tasks.pop(i)
                print("task was removed")
                return
        print("task was not found. Nothing removed")

    def save_tasks(self):
        json_file = Storage()
        json_file.save(self.tasks)
        print("Tasks saved")

    def load_tasks(self):
        json_file = Storage()
        self.tasks = json_file.load()
        print("Tasks loaded")

def main():
    task_manager = TaskManager()
    task_manager.load_tasks()
    while True:
            print("\nMenu:")
            print("1. Add new task")
            print("2. View all tasks")
            print("3. Remove task")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                new_task = Task(name, description)
                task_manager.add_task(new_task)
                print("Task added successfully!")
                next = input("|   Press Enter to continue   |")

            elif choice == "2":
                task_manager.print_tasks()
                next = input("|   Press Enter to continue   |")

            elif choice == "3":
                name = input("Enter task name: ")
                task_manager.remove_taks(name)
                next = input("|   Press Enter to continue   |")

            elif choice == "4":
                task_manager.save_tasks()
                print("Exiting application. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
