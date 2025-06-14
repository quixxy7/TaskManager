from tasks import Task, TaskManager

def main():
    tm = TaskManager()
    tm.load_tasks()
    while True:
        choose = int(input("Select action (1 - Add Task | 2 - Update Task | 3 - Mark Task | 4 - Remove Task | 5 - Show Tasks | 6 - Exit): "))
        match choose:
            case 1:
                name = input("Enter name of task: ")
                description = input("Enter description of task: ")
                new_task = Task(name, description)
                tm.add_task(new_task)
            case 2:
                TaskID = int(input("Enter ID of task: "))
                tm.update_task(TaskID)
            case 3:
                TaskID = int(input("Enter ID of task: "))
                tm.mark_task(TaskID)
            case 4:
                TaskID = int(input("Enter ID of task: "))
                tm.remove_task(TaskID)
            case 5:
                tm.print_tasks()
            case 6:
                print("Goodbye!")
                break
            case _:
                print("It's wrong action. Pleast try again")

    ans = input("Do you want to save changes?: (Y/n)")
    if "n" not in ans:
        tm.save_tasks()

if __name__ == "__main__":
    main()
