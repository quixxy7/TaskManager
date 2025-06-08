from tasks import Task, TaskManager
import time

def main():
    task_manager = TaskManager()
    task_manager.load_tasks()
    while True:
        time.sleep(1)
        print("\n1. Add task | 2. Remove task | 3. Show tasks | 4. Exit")
        print("_______________________________________________________")
        choose = input("What you want to do?: ")

        match choose:
            case "1":
                name: str = input("Enter task's name: ")
                description: str = input("Enter tasks description: ")
                task = Task(name, description)
                task_manager.add_task(task)
            case "2":
                task_name: str = input("Enter task's name: ")
                task_manager.remove_taks(task_name)
            case "3":
                task_manager.print_tasks()
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Please choose in diaposon 1-4")
    task_manager.save_tasks()

if __name__ == "__main__":
    main()
