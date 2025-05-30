class Task:
    def __init__(self, name: str, description: str, done: bool = False):
        self.name: str = name
        self.description: str = description
        self.done: bool = done
    def info(self):
        print(self.name, self.description, self.done, sep = " | ")
