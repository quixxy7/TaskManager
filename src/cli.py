from tasks import TaskManager, Task

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt, Confirm
import sys


class CLI:
    def __init__(self):
        self.console = Console()
        self.tm = TaskManager()

        self.tm.load_tasks()
        self.commands = {
                   1: ("Добавить задачу", self._add_task),
                   2: ("Обновить задачу", self._update_task),
                   3: ("Отметить задачу", self._mark_task),
                   4: ("Удалить задачу", self._remove_task),
                   5: ("Выход", self._exit)
               }

    def _add_task(self):
        self.console.print("[bold]Добавление новой задачи[/]")
        name = Prompt.ask("Введите название задачи")
        description = Prompt.ask("Введите описание задачи")
        new_task = Task(name, description)
        self.tm.add_task(new_task)
        self.console.print("[green]Задача добавлена[/]")

    def _update_task(self):
        task_id = IntPrompt.ask("Введите ID задачи, которую хотите обновить")
        self.tm.update_task(task_id)
        self.console.print("[green]Задача обновлена[/]")

    def _mark_task(self):
        task_id = IntPrompt.ask("Введите ID задачи для смены статуса")
        self.tm.mark_task(task_id)
        self.console.print("[green]Статус изменён[/]")

    def _remove_task(self):
        task_id = IntPrompt.ask("Введите ID задачи, которую хотите удалить")
        self.tm.remove_task(task_id)
        self.console.print("[green]Задача была удалена[/]")

    def clear_screen(self):
        self.console.clear()

    def show_header(self):
        self.console.print("[blue]Task Manager by quixxy7[/]")

    def show_tasks(self):
        table = Table(title="Tasks")
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Description")
        table.add_column("Status")
        table.add_column("Created at")
        table.add_column("Updated at")

        for task_id, task in self.tm.tasks.items():
            table.add_row(
                str(task_id),
                task.name,
                task.description,
                str(task.status),
                str(task.createdAt),
                str(task.updatedAt)
            )

        self.console.print(table)

    def _exit(self):
        if Confirm.ask("Сохранить изменения перед выходом"):
            self.tm.save_tasks()
        self.console.print("[bold blue]До свидания[/]")
        sys.exit(1)


    def run(self):
        self.clear_screen()
        while True:
            self.show_header()
            self.show_tasks()

            options = "\n".join(
                f"[red]{key}.[/] {desc}"
                for key, (desc, _) in self.commands.items()
            )

            self.console.print(Panel(options, title="Выберите действие"))

            choice = IntPrompt.ask(
                "Ваш выбор",
                choices=[str(k) for k in self.commands.keys()],
                show_choices=False
            )

            self.clear_screen()
            self.commands[choice][1]()
            input("\nНажмите любую клавишу, чтобы продолжить...")
            self.clear_screen()
