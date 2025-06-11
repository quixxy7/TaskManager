from tasks import Task, TaskManager

def main():
    tm = TaskManager()
    tm.load_tasks()

    tm.print_tasks()

if __name__ == "__main__":
    main()
