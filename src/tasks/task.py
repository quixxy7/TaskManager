class Task:
    def __init__(self, name: str, description: str, done: bool = False):
        self.name: str = name
        self.description: str = description
        self.status: bool = done

    def __str__(self):
        status: str = "Done" if self.status else "Not done"
        return f"Name: {self.name} | Description: {self.description} | Status: {status}"

    def info(self):
        print(self.name, self.description, self.status, sep = " | ")
