from tasks import Task, TaskManager

def main():
    tm = TaskManager()
    tm.load_tasks()
    tm.add_task(Task("zbc", "aheuna"))
    tm.print_tasks()
    taskID = int(input("Enter ID: "))
    tm.update_task(taskID)
    taskID = int(input("Enter ID: "))
    tm.mark_task(taskID)
    tm.print_tasks()

    ans = input("Do you want to save changes?: (Y/n)")
    if "n" not in ans:
        tm.save_tasks()

if __name__ == "__main__":
    main()
