from tasks import Task, TaskManager

def main():
    tm = TaskManager()
    tm.load_tasks()
    new_task = Task("andrey", "ivandaev")
    tm.add_task(new_task)
    tm.print_tasks()

if __name__ == "__main__":
    main()
