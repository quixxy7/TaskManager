class Task:
    def __init__(self, name: str, description: str, done: bool = False):
        self.name: str = name
        self.description: str = description
        self.done: bool = done

    def __str__(self):
        status: str = "Done" if self.done else "Not done"
        return f"Name: {self.name} | Description: {self.description} | Status: {status}"

    def info(self):
        print(self.name, self.description, self.done, sep = " | ")
